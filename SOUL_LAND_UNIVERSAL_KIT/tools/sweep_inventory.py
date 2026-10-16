#!/usr/bin/env python3
"""Public sweep discovery: paginate, clone completely, record exact Git heads.

No credentials are used. An empty inventory, malformed page, unexpected owner,
existing destination or failed clone is an infrastructure error, never a clean
scan. Successful clones and the failure receipt remain available for diagnosis.
This does NOT detect private repositories or keep a full Git-history backup.
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path


def fetch_json(url):
    request = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'public-account-sweep',
    })
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def discover(owner, fetch=fetch_json):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', owner):
        raise ValueError('invalid GitHub owner')
    repos = []
    seen = set()
    for page in range(1, 1001):
        data = fetch(f'https://api.github.com/users/{owner}/repos'
                     f'?per_page=100&type=owner&sort=full_name&page={page}')
        if not isinstance(data, list):
            raise ValueError('repository API did not return a list')
        for item in data:
            name = item.get('name', '')
            if not re.fullmatch(r'[A-Za-z0-9_.-]+', name) or name in ('.', '..'):
                raise ValueError('unsafe repository name')
            if item.get('owner', {}).get('login', '').lower() != owner.lower():
                raise ValueError(f'unexpected owner: {name}')
            if item.get('private') is not False:
                raise ValueError(f'non-public repository in public inventory: {name}')
            if name.lower() in seen:
                raise ValueError(f'duplicate repository across API pages: {name}')
            seen.add(name.lower())
            repos.append({'name': name, 'archived': bool(item.get('archived')),
                          'default_branch': item.get('default_branch')})
        if len(data) < 100:
            break
    else:
        raise ValueError('pagination safety limit exceeded')
    if not repos:
        raise ValueError('empty public inventory; refusing to report health')
    return sorted(repos, key=lambda r: r['name'].lower())


def clone_all(owner, repos, root, receipt, run=subprocess.run):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    for repo in repos:
        dest = root / repo['name']
        try:
            if dest.exists():
                raise ValueError('destination already exists; refusing a stale scan')
            run(['git', '-c', 'credential.helper=', 'clone', '-q', '--depth', '1',
                 f"https://github.com/{owner}/{repo['name']}.git", str(dest)],
                check=True, timeout=180)
            result = run(['git', '-C', str(dest), 'rev-parse', 'HEAD'],
                         check=True, capture_output=True, text=True, timeout=30)
            head = result.stdout.strip()
            if not re.fullmatch(r'[0-9a-f]{40}', head):
                raise ValueError('clone has no valid Git HEAD')
            repo.update(status='cloned', head=head)
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            repo.update(status='failed', error=str(error))
        Path(receipt).write_text(json.dumps(repos, indent=2) + '\n', encoding='utf-8')
    failures = [r['name'] for r in repos if r.get('status') != 'cloned']
    if failures:
        raise RuntimeError('incomplete inventory: ' + ', '.join(failures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--owner', default='gm5206663-bit')
    parser.add_argument('--root', required=True)
    parser.add_argument('--out-prefix', default='sweep-inventory')
    args = parser.parse_args()
    prefix = Path(args.out_prefix)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    status = {'owner': args.owner, 'public_only': True, 'complete': False,
              'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    code = 0
    try:
        repos = discover(args.owner)
        status['expected'] = len(repos)
        prefix.with_suffix('.txt').write_text(
            ''.join(r['name'] + '\n' for r in repos), encoding='utf-8')
        clone_all(args.owner, repos, args.root, str(prefix) + '-heads.json')
        status.update(complete=True, cloned=len(repos),
                      archived=sum(r['archived'] for r in repos))
        print(f'INVENTORY COMPLETE: {len(repos)} public repositories cloned')
    except Exception as error:
        status['error'] = str(error)
        print(f'INVENTORY INCOMPLETE: {error}', file=sys.stderr)
        code = 2
    prefix.with_suffix('.json').write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
    return code


if __name__ == '__main__':
    sys.exit(main())

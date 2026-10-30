#!/usr/bin/env python3
"""Check the kit itself — the gate the largest repository on the account did not have.

WHY THIS EXISTS
    On 2026-10-29 the account audit found the kit to be the only repository of
    comparable size with no check of its own: 2,392 tracked files, 67 MB, every
    Soul Land serial, and `tools/` holding a writer and nothing else. Every
    chapter-bearing tree was checked from the outside, by a tool living in
    another repository. This file is the inside check.

WHAT IT CHECKS — and what it deliberately does not
    links      Local links in the kit's governing documents resolve. Scoped to
               the spine, not to all 2,002 markdown files: a serial's own
               manuscript may cite a source it does not ship, and a gate that
               cannot tell a citation from a link is noise. The chapter-bearing
               trees have their own panels (`check_panels.py` in two of them).
    spine      Every governing document exists and is non-empty.
    manifest   MANIFEST.sha256 matches the files that govern the kit. Drift is a
               WARNING by default — this repository is pushed most days, and a
               permanently red badge over a regenerable file is a badge people
               learn to ignore. `--strict` promotes drift to an error, which is
               what a release cut should run.
    structure  Committed archives and empty tracked files. Both WARN: the desk
               carries an open author ruling on archives, and an empty file may
               be a deliberate placeholder or may be a lost file. The gate
               reports; the author rules.
    dupes      Identical content in more than one tracked file (>= 20 KB).
               WARN, for the same reason: the house rule is one copy of one
               thing, but *which* copy survives is a consolidation decision.

USAGE
    python3 tools/check.py                 # report; exit 1 only on hard errors
    python3 tools/check.py --strict        # release mode: manifest drift fails
    python3 tools/check.py --write         # re-stamp MANIFEST.sha256
    python3 tools/check.py --selftest      # prove the door locks (fixtures)
    python3 tools/check.py --verbose       # name every duplicate group in full

    Exit codes: 0 clean · 1 findings (in the current mode) · 2 selftest failed.
"""
from __future__ import annotations

import hashlib
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'MANIFEST.sha256'

SPINE = [
    'README.md', 'AGENTS.md', 'PROJECTS.md', 'REGISTER.md', 'STATE.md',
    'HISTORY.md', 'SARA.md', 'NOTICE.md', 'THE_GOLDEN_LION.md',
]

# The files that govern the kit: if one of these changes, it changed on purpose.
GOVERNING_GLOBS = [
    '*.md',
    'tools/*.py',
    '.github/workflows/*.yml',
    'tools/ci/*.yml',
    'docs/index.html',
]

LINK = re.compile(r'\]\(([^)\s]+)\)|(?:href|src)="([^"]+)"')
SCHEME = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*:')
ARCHIVE = re.compile(r'\.(zip|tar|tar\.gz|tgz|7z|rar|gz)$', re.I)
SKIP_ARCHIVE_NAMES = {'.gitignore', '.gitkeep'}


def governing_files(root: Path) -> list[Path]:
    found: list[Path] = []
    for pattern in GOVERNING_GLOBS:
        for path in sorted(root.glob(pattern)):
            if path.is_file() and path.name != MANIFEST:
                found.append(path)
    return found


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(65536), b''):
            digest.update(block)
    return digest.hexdigest()


def read_manifest(root: Path) -> dict[str, str]:
    path = root / MANIFEST
    if not path.exists():
        return {}
    entries: dict[str, str] = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(None, 1)
        if len(parts) == 2:
            entries[parts[1].strip().lstrip('*')] = parts[0]
    return entries


def write_manifest(root: Path) -> int:
    lines = ['# MANIFEST.sha256 — the governing files of the kit, hashed.',
             '# Regenerate with: python3 tools/check.py --write',
             '# Verified by: python3 tools/check.py --strict (warning in normal mode).']
    for path in governing_files(root):
        lines.append(f'{sha256(path)}  {path.relative_to(root).as_posix()}')
    (root / MANIFEST).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return len(lines) - 3


def check_links(root: Path, errors: list[str]) -> int:
    checked = 0
    for name in SPINE:
        path = root / name
        if not path.exists():
            errors.append(f'spine: {name} is missing')
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for match in LINK.finditer(text):
            target = match.group(1) or match.group(2)
            if not target or SCHEME.match(target) or target.startswith(('#', '//', 'mailto:')):
                continue
            local = target.split('#', 1)[0].split('?', 1)[0]
            if not local:
                continue
            checked += 1
            if not (path.parent / local).exists():
                errors.append(f'links: {name} -> missing local target {target}')
    return checked


def check_spine(root: Path, errors: list[str]) -> None:
    for name in SPINE:
        path = root / name
        if path.exists() and path.stat().st_size == 0:
            errors.append(f'spine: {name} is empty')


def check_manifest(root: Path, warnings: list[str], strict: bool) -> int:
    recorded = read_manifest(root)
    if not recorded:
        warnings.append(f'manifest: {MANIFEST} is missing — run --write')
        return 0
    current = {p.relative_to(root).as_posix(): sha256(p) for p in governing_files(root)}
    bucket = warnings if not strict else None
    drift = 0
    for name in sorted(set(recorded) | set(current)):
        old, new = recorded.get(name), current.get(name)
        if old == new:
            continue
        drift += 1
        if old is None:
            message = f'manifest: {name} is new and unstamped'
        elif new is None:
            message = f'manifest: {name} is stamped but gone'
        else:
            message = f'manifest: {name} changed since the last stamp'
        if bucket is None:
            # strict: announced through the same channel as errors
            raise_manifest_error(message)
        else:
            bucket.append(message)
    return drift


class ManifestDrift(Exception):
    pass


def raise_manifest_error(message: str) -> None:
    raise ManifestDrift(message)


def check_structure(root: Path, warnings: list[str], files: list[Path]) -> None:
    for path in files:
        relative = path.relative_to(root)
        if ARCHIVE.search(path.name) and path.name not in SKIP_ARCHIVE_NAMES:
            warnings.append(f'structure: committed archive {relative} '
                            f'({path.stat().st_size / 1024:.0f} KB) — desk item 6 is still open')
        elif path.stat().st_size == 0 and path.name not in {'.gitkeep', '.nojekyll'}:
            warnings.append(f'structure: empty tracked file {relative}')


def check_dupes(root: Path, warnings: list[str], verbose: bool = False) -> int:
    by_hash: dict[str, list[Path]] = {}
    for path in root.rglob('*'):
        if not path.is_file() or '.git' in path.parts:
            continue
        try:
            if path.stat().st_size < 20000:
                continue
        except OSError:
            continue
        by_hash.setdefault(sha256(path), []).append(path.relative_to(root))
    groups = [sorted(str(p) for p in g) for g in by_hash.values() if len(g) > 1]
    if groups:
        largest = max(groups, key=len)
        warnings.append(f'dupes: {len(groups)} identical-content group(s) across '
                        f'{sum(len(g) for g in groups)} files — one copy of one thing '
                        f'is still an open consolidation; write it with --verbose')
        if verbose:
            for group in groups:
                warnings.append('dupes: identical content in ' + ', '.join(group))
        else:
            warnings.append('dupes: largest group is ' + ', '.join(largest))
    return len(groups)


def run(root: Path = ROOT, strict: bool = False, verbose: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    links = check_links(root, errors)
    check_spine(root, errors)
    try:
        drift = check_manifest(root, warnings, strict)
    except ManifestDrift as exc:
        errors.append(str(exc))
        drift = 1

    files = sorted(p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts)
    check_structure(root, warnings, files)
    check_dupes(root, warnings, verbose)

    for line in errors:
        print(f'FAIL: {line}')
    for line in warnings:
        print(f'WARN: {line}')

    print(f'KIT-CHECK: {len(errors)} error(s), {len(warnings)} warning(s) · '
          f'{len(files)} tracked files · {links} spine links · '
          f'{len(governing_files(root))} governing files · manifest drift {drift}')
    if errors:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS' + (' (strict)' if strict else ''))
    return 0


def selftest() -> int:
    """A gate that has never failed is a gate nobody has tested."""
    failures = 0

    def expect(label: str, cond: bool) -> None:
        nonlocal failures
        if not cond:
            failures += 1
            print(f'SELFTEST FAIL: {label}')
        else:
            print(f'SELFTEST ok:   {label}')

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / 'README.md').write_text('# kit\n\n[a](AGENTS.md)\n', encoding='utf-8')
        (root / 'AGENTS.md').write_text('# agents\n', encoding='utf-8')
        for name in SPINE:
            target = root / name
            if not target.exists():
                target.write_text(f'# {name}\n', encoding='utf-8')
        (root / 'tools').mkdir()
        (root / 'tools' / 'x.py').write_text('print(1)\n', encoding='utf-8')
        (root / '.github' / 'workflows').mkdir(parents=True)
        (root / '.github' / 'workflows' / 'w.yml').write_text('name: w\n', encoding='utf-8')

        expect('clean tree passes', run(root) == 0)
        write_manifest(root)
        expect('after --write, strict passes', run(root, strict=True) == 0)

        (root / 'AGENTS.md').write_text('# agents changed\n', encoding='utf-8')
        expect('drift warns but does not fail', run(root) == 0)
        expect('drift fails in strict', run(root, strict=True) == 1)

        write_manifest(root)
        (root / 'README.md').write_text('# kit\n\n[a](NOWHERE.md)\n', encoding='utf-8')
        expect('a broken link fails', run(root) == 1)

        (root / 'README.md').write_text('# kit\n\n[a](AGENTS.md)\n', encoding='utf-8')
        (root / 'old.zip').write_bytes(b'PK\x03\x04' + b'0' * 64)
        expect('an archive warns', run(root) == 0)
        expect('an archive is not silently ignored',
               any('archive' in line for line in _capture_warnings(root)))

    print(f'SELFTEST: {failures} failure(s)')
    return 0 if failures == 0 else 2


def _capture_warnings(root: Path) -> list[str]:
    import contextlib
    import io
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        run(root)
    return [line for line in buffer.getvalue().splitlines() if line.startswith('WARN')]


def main(argv: list[str]) -> int:
    if '--selftest' in argv:
        return selftest()
    if '--write' in argv:
        count = write_manifest(ROOT)
        print(f'MANIFEST: {count} governing files stamped into {MANIFEST}')
        return 0
    return run(ROOT, strict='--strict' in argv, verbose='--verbose' in argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

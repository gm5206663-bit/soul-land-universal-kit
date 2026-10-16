#!/usr/bin/env python3
"""Distinguish measured findings (exit 1) from an interrupted/crashed checker.

The sweep is reporting-only for findings, NOT for missing evidence. Validate
completion markers, report schema, coverage and exit-code consistency before
calling a reporting run successful. No checker output is reinterpreted here.
"""
import argparse
import json
from pathlib import Path
import sys


def validate_gate(path, code):
    text = Path(path).read_text(encoding='utf-8')
    lines = text.strip().splitlines()
    if code not in (0, 1) or not lines or lines[-1] not in ('PASS', 'FAIL'):
        raise ValueError('gate did not finish with a valid verdict')
    if not any(line.startswith('COVERAGE: ') for line in lines):
        raise ValueError('gate coverage missing')
    if (lines[-1] == 'PASS') != (code == 0):
        raise ValueError('gate verdict and exit code disagree')


def validate_report(prefix, code):
    prefix = str(prefix)
    for ext in ('.json', '.md', '.html'):
        if not Path(prefix + ext).is_file() or not Path(prefix + ext).stat().st_size:
            raise ValueError('missing report artifact: ' + prefix + ext)
    report = json.loads(Path(prefix + '.json').read_text(encoding='utf-8'))
    if report.get('tool') != 'account-control-centre':
        raise ValueError('wrong report tool')
    if not report.get('books') or not report.get('facts'):
        raise ValueError('report examined no chapters')
    required = {'gate', 'dupes', 'two-homes', 'receipts', 'publication',
                'housekeeping', 'links', 'generated', 'enforcement',
                'stale-claims', 'sightings'}
    detectors = {row['detector'] for row in report.get('coverage', [])}
    if not required.issubset(detectors):
        raise ValueError('incomplete detector coverage: ' + ', '.join(sorted(required - detectors)))
    hard = sum(f['severity'] == 'hard' for f in report['findings'])
    if report['summary']['hard'] != hard:
        raise ValueError('report summary does not match findings')
    if code != (1 if hard else 0):
        raise ValueError('report findings and exit code disagree')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=('gate', 'report'))
    parser.add_argument('path')
    parser.add_argument('exit_code', type=int)
    args = parser.parse_args()
    try:
        (validate_gate if args.kind == 'gate' else validate_report)(args.path, args.exit_code)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'SWEEP EVIDENCE INCOMPLETE: {error}', file=sys.stderr)
        return 2
    print('SWEEP EVIDENCE COMPLETE: findings are reported, not suppressed')
    return 0


if __name__ == '__main__':
    sys.exit(main())

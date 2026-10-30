#!/usr/bin/env python3
"""tools/register_drift.py — is the committed REGISTER still what the tree says?

    python3 tools/register_drift.py            # verify: regenerate, compare, exit 0/1
    python3 tools/register_drift.py --write    # refresh REGISTER.md from the tree
    python3 tools/register_drift.py --selftest # prove the comparison can fail

WHY THIS EXISTS
  `REGISTER.md` says, in its own second line, *"Generated … Regenerate it; never edit it."*
  Nothing checked that. A generated file with no drift check is a hand-written file that
  happens to have been generated once — and the guide's whole fourth big idea is that state
  must be rebuilt in the same turn, because a memory that nobody re-derives drifts silently
  and then gets quoted as fact.

  This is the same class of defect as the manifest: the claim is fine, the proof was missing.

WHAT IS COMPARED
  Everything except the "Generated <date> by … over …" line, which changes every run by
  design. Comparing it would make the check fail on a clock tick and train people to ignore
  it — which is how a gate dies.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / 'REGISTER.md'
TOOL = ROOT / 'SOUL_LAND_UNIVERSAL_KIT' / 'tools' / 'register.py'
STAMP_RX = re.compile(r'^\*Generated .*\*$', re.M)

# Registers that are NOT rebuilt from this checkout, with the reason. An entry here is a
# declared exemption, not a pass: the guide's rule is that a claim which cannot be checked
# is stated, never assumed. Each of these is a whole-account snapshot produced from a full
# clone set, which this repository does not contain — so it cannot be verified here, and
# pretending otherwise is exactly the "generated file nobody checks" defect this tool exists
# to end. The author's decision (regenerate, or delete as a duplicate) is recorded in
# docs/METHOD_CONFORMANCE.md §8.
# An exemption that says "it is a copy of X" must BE a copy of X. A reason in a comment is
# a claim like any other; these are checked, not trusted.
COPY_OF = {
    'SOUL_LAND_WORKSPACE/kit/REGISTER.md': 'SOUL_LAND_UNIVERSAL_KIT/REGISTER.md',
}

EXEMPT = {
    'SOUL_LAND_UNIVERSAL_KIT/REGISTER.md':
        'whole-account snapshot, scope "a full clone set" — not reproducible from this checkout',
    'SOUL_LAND_WORKSPACE/kit/REGISTER.md':
        'byte-identical copy of the file above (verified 2026-10-30) — one copy of one thing',
}


def body(text: str) -> str:
    return STAMP_RX.sub('*Generated …*', text)


def regenerate(root: Path) -> str:
    with tempfile.NamedTemporaryFile('r', suffix='.md', delete=False) as tf:
        tmp = tf.name
    try:
        subprocess.run([sys.executable, str(TOOL), '--root', str(root), '--out', tmp],
                       cwd=ROOT, check=True, capture_output=True)
        return Path(tmp).read_text(encoding='utf-8')
    finally:
        os.unlink(tmp)


def compare(root: Path, committed: Path) -> tuple[bool, str]:
    if not committed.exists():
        return False, f'{committed.name} does not exist — the register was never generated'
    fresh = body(regenerate(root))
    on_disk = body(committed.read_text(encoding='utf-8'))
    if fresh == on_disk:
        return True, f'{committed.name} matches the tree'
    fresh_lines, disk_lines = fresh.splitlines(), on_disk.splitlines()
    for i, (a, b) in enumerate(zip(fresh_lines, disk_lines), 1):
        if a != b:
            return False, (f'{committed.name} is stale at line {i}\n'
                           f'    tree says:      {a[:120]}\n'
                           f'    register says:  {b[:120]}')
    if len(fresh_lines) != len(disk_lines):
        return False, (f'{committed.name} is stale: the tree produces {len(fresh_lines)} '
                       f'line(s), the file has {len(disk_lines)}')
    return False, f'{committed.name} is stale'


def selftest() -> int:
    fails = 0

    def check(name: str, ok: bool) -> None:
        nonlocal fails
        print(f'SELFTEST {"ok:  " if ok else "FAIL:"} {name}')
        fails += 0 if ok else 1

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        # a minimal book the register can see
        (root / 'repo').mkdir()
        (root / 'repo' / '.git').mkdir()
        book = root / 'repo' / 'Book_One' / 'chapters'
        book.mkdir(parents=True)
        (book / 'Chapter_01.md').write_text(
            '# Chapter 1\n\n' + ('The boy walked east and counted stones. ' * 40) + '\n',
            encoding='utf-8')

        reg = root / 'REGISTER.md'
        reg.write_text(regenerate(root), encoding='utf-8')
        ok, why = compare(root, reg)
        check('a fresh register matches the tree', ok)

        # the clock tick must not count as drift
        reg.write_text(body(reg.read_text(encoding='utf-8')).replace(
            '*Generated …*', '*Generated 1999-01-01 00:00 by `tools/register.py` over `x`. '
            'Regenerate it; never edit it.*'), encoding='utf-8')
        ok, why = compare(root, reg)
        check('the timestamp line alone is not drift', ok)

        # a new chapter is exactly the drift that matters
        (book / 'Chapter_02.md').write_text(
            '# Chapter 2\n\n' + ('She ran west and counted nothing. ' * 40) + '\n',
            encoding='utf-8')
        ok, why = compare(root, reg)
        check('a chapter added since the register is caught', not ok)
        check('and the message names the stale line', 'stale' in why)

        # hand-editing the totals is the same lie as never regenerating
        reg.write_text(regenerate(root), encoding='utf-8')
        # the fixture used to replace '16 books', which does not exist in a one-book tree —
        # so it compared an unmodified file and called the check broken. A fixture that edits
        # nothing proves nothing; find the number that is actually there.
        text = reg.read_text(encoding='utf-8')
        edited, n = re.subn(r'\b\d+(?= registered books)', '999', text, count=1)
        assert n == 1, f'fixture could not find a book count to edit in:\n{text[:400]}'
        reg.write_text(edited, encoding='utf-8')
        ok, why = compare(root, reg)
        check('a hand-edited register is caught', not ok)

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / 'deep' / 'kit').mkdir(parents=True)
        (root / 'REGISTER.md').write_text('the root one\n', encoding='utf-8')
        (root / 'deep' / 'REGISTER.md').write_text('a copy nobody declared\n', encoding='utf-8')
        found = [p.relative_to(root).as_posix() for p in all_registers(root)]
        check('every REGISTER.md is found, not just the root one',
              found == ['REGISTER.md', 'deep/REGISTER.md'])
        check('an undeclared second register would be caught',
              'deep/REGISTER.md' not in EXEMPT)

    print(f'SELFTEST: {fails} failure(s)')
    return 1 if fails else 0


def all_registers(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob('REGISTER.md')
                  if '.git' not in p.parts and '_archive' not in p.parts)


def main(argv: list[str]) -> int:
    if '--selftest' in argv:
        return selftest()
    if '--write' in argv:
        REGISTER.write_text(regenerate(ROOT), encoding='utf-8')
        print(f'REGISTER: regenerated from the tree ({REGISTER.name})')
        return 0

    ok, why = compare(ROOT, REGISTER)
    print(f'REGISTER: {"PASS" if ok else "FAIL"} — {why}')

    # Every OTHER file claiming to be a generated register must either be checkable or be a
    # declared exemption. Silence here is how a 17-day-old snapshot keeps being quoted as today.
    unlisted = []
    for p in all_registers(ROOT):
        rel = p.relative_to(ROOT).as_posix()
        if rel == REGISTER.name:
            continue
        if rel not in EXEMPT:
            unlisted.append(rel)
        else:
            print(f'REGISTER: EXEMPT — {rel}: {EXEMPT[rel]}')
            twin = COPY_OF.get(rel)
            if twin:
                a, b = ROOT / rel, ROOT / twin
                same = a.exists() and b.exists() and a.read_bytes() == b.read_bytes()
                print(f'REGISTER: {"PASS" if same else "FAIL"} — {rel} is '
                      f'{"still" if same else "NO LONGER"} a byte copy of {twin}')
                if not same:
                    unlisted.append(f'{rel} (no longer a copy of {twin})')
    for rel in unlisted:
        print(f'REGISTER: UNVERIFIED — {rel} declares itself generated, is not the root '
              f'register, and has no declared exemption')
    if unlisted:
        print(f'REGISTER: FAIL — {len(unlisted)} unverified register(s); regenerate it, delete '
              f'it, or declare why it cannot be checked')
        return 1
    print(f'REGISTER: PASS — 1 regenerated here, {len(EXEMPT)} declared exempt, '
          f'{len(COPY_OF)} copy claim(s) checked')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

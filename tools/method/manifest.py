#!/usr/bin/env python3
"""tools/method/manifest.py — independent proof that the tree is the tree.

    python3 tools/manifest.py --write    # record the current tree (the author is accepting it)
    python3 tools/manifest.py            # verify: every hash still matches, no file unlisted
    python3 tools/manifest.py --selftest # prove the check can fail

WHY THIS EXISTS
  The guide's third rule: "Never trust only the project's own checker." A repository that cannot
  prove its own files are the files it checked cannot prove anything downstream. The gate and the
  thing gated can be wrong together; a hash manifest cannot be wrong with them, it can only be
  stale — and stale is exactly what this detects.

  Written as a portable drop-in because six repositories on this account have no manifest at all,
  and the guide's own `check_manifest.py` assumes its own layout. Stdlib only, no imports from the
  repository it checks.

THE ONE LAW OF --write
  Never run `--write` to make a red build green. The manifest records what the author accepted.
  Re-stamping an unaccepted change forges an acceptance receipt. If the tree changed and nobody
  accepted the change, the correct state is RED, and the correct fix is a decision, not a re-run.

FORMAT
  sha256<two spaces>path, sorted by path, LF endings, no timestamps — so the file itself is
  diffable and does not churn when nothing changed.
"""
from __future__ import annotations

import hashlib
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / 'MANIFEST.sha256'

SKIP_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'build', 'dist', '.mypy_cache',
             '.pytest_cache', '.ruff_cache', '.idea', '.vscode'}
SKIP_FILES = {'MANIFEST.sha256'}          # a manifest cannot list itself
SKIP_SUFFIX = {'.pyc', '.pyo'}


def walk(root: Path) -> list[Path]:
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            p = Path(dirpath) / name
            if name in SKIP_FILES or p.suffix in SKIP_SUFFIX:
                continue
            out.append(p)
    return out


def digest(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def read_manifest(root: Path) -> dict[str, str]:
    m = {}
    if not (root / 'MANIFEST.sha256').exists():
        return m
    for line in (root / 'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        h, _, rel = line.partition('  ')
        if rel:
            m[rel] = h
    return m


def verify(root: Path) -> tuple[list[str], list[str], list[str]]:
    """-> (changed, missing, unlisted)"""
    recorded = read_manifest(root)
    if not recorded:
        return [], [], []
    changed, missing = [], []
    for rel, want in sorted(recorded.items()):
        p = root / rel
        if not p.exists():
            missing.append(rel)
            continue
        if digest(p) != want:
            changed.append(rel)
    unlisted = sorted(str(p.relative_to(root)) for p in walk(root)
                      if str(p.relative_to(root)) not in recorded)
    return changed, missing, unlisted


def write(root: Path) -> int:
    files = walk(root)
    lines = [f'{digest(p)}  {p.relative_to(root).as_posix()}' for p in files]
    lines.sort(key=lambda l: l.split('  ', 1)[1])
    tmp = root / 'MANIFEST.sha256.tmp'
    tmp.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    tmp.replace(root / 'MANIFEST.sha256')
    print(f'MANIFEST: wrote {len(lines)} file(s)')
    print('MANIFEST: this records an ACCEPTANCE. If nobody accepted this tree, revert it.')
    return 0


def selftest() -> int:
    fails = 0

    def check(name: str, ok: bool) -> None:
        nonlocal fails
        print(f'SELFTEST {"ok:  " if ok else "FAIL:"} {name}')
        fails += 0 if ok else 1

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / 'a.txt').write_text('one', encoding='utf-8')
        (root / 'sub').mkdir()
        (root / 'sub' / 'b.txt').write_text('two', encoding='utf-8')
        write(root)
        check('a clean tree verifies', verify(root) == ([], [], []))

        (root / 'a.txt').write_text('one!', encoding='utf-8')
        check('a changed byte is caught', verify(root)[0] == ['a.txt'])

        write(root)
        (root / 'sub' / 'b.txt').unlink()
        check('a deleted file is caught', verify(root)[1] == ['sub/b.txt'])

        write(root)
        (root / 'c.txt').write_text('three', encoding='utf-8')
        check('an unlisted file is caught', verify(root)[2] == ['c.txt'])

        # a manifest that lists itself would change its own hash forever
        (root / 'MANIFEST.sha256.tmp').unlink(missing_ok=True)
        write(root)
        check('the manifest never lists itself',
              'MANIFEST.sha256' not in read_manifest(root))

        # a stale-but-matching manifest must not hide a rewritten file of the same size
        (root / 'c.txt').write_text('thr33', encoding='utf-8')
        check('a same-length edit is still caught', 'c.txt' in verify(root)[0])

        # __pycache__ churn must not create noise that trains people to ignore red
        (root / '__pycache__').mkdir()
        (root / '__pycache__' / 'x.pyc').write_bytes(b'\x00')
        check('build noise is ignored', verify(root)[2] == [])

    print(f'SELFTEST: {fails} failure(s)')
    return 1 if fails else 0


def main(argv: list[str]) -> int:
    if '--selftest' in argv:
        return selftest()
    if '--write' in argv:
        return write(ROOT)
    changed, missing, unlisted = verify(ROOT)
    if not (ROOT / 'MANIFEST.sha256').exists():
        print('MANIFEST: no MANIFEST.sha256 — this repository cannot prove its own files')
        return 1
    for rel in changed:
        print(f'CHANGED  {rel}')
    for rel in missing:
        print(f'MISSING  {rel}')
    for rel in unlisted:
        print(f'UNLISTED {rel}')
    total = len(read_manifest(ROOT))
    if changed or missing or unlisted:
        print(f'MANIFEST: FAIL — {len(changed)} changed, {len(missing)} missing, '
              f'{len(unlisted)} unlisted of {total}')
        return 1
    print(f'MANIFEST: PASS — {total} file(s) match')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

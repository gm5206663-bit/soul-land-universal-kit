#!/usr/bin/env python3
"""tools/record_links.py — every file path the serial's records cite, resolved.

WHY THIS EXISTS
    On 2026-10-30 the audit found **31 file paths cited across 33 record files that do not
    exist where they are cited**. Almost none of them were lost. They had moved:

      chapters/Chapter_05_The_Better_Version.md   -> the V1 epoch, archived 2026-09-23
      SOUL_LAND_NEW/foundation/METHOD.md          -> the pre-consolidation repo name
      reference/sl3_lin_hao/...                   -> adaptive_prodigy/, after the one-home pass
      canon_028.txt                               -> a canon extract that was never imported

    A record that cites a path which no longer resolves is not automatically wrong — but a
    reader cannot tell "moved" from "never existed" without doing what this tool does, and
    neither can a future gate. So the citation is checked, and classified.

THE FIVE ANSWERS
    OK         the cited path exists, from the citing document's own directory or the project
    MOVED      not there, but a file with the same name exists elsewhere in the kit — prints where
    ARCHIVED   not on disk, but present in the one-home archive in history (2026-10-12) —
               recoverable with `git show 9379d40^:<path>`
    PLANNED    names a chapter the serial has not written yet (ch9+ of the current epoch) —
               a plan, not a citation. Not a defect.
    EXTERNAL   names another repository on the account (storyos-site, soul-library, ...) —
               a pointer across repos, not a local path. Not a defect either.
    DELETED    was in this repository and has been removed; recoverable from history.
    MISSING    nowhere: not on disk, not in this history, not in a sibling repo, not planned.
               **The only hard failure.**

WHY HISTORY MATTERS, AND WHY THIS FILE SHOUTS WHEN IT IS ABSENT
    Every `git show 9379d40^:...` recovery instruction in this repository is TRUE — verified
    2026-10-30, 478 files — and every one of them is FALSE on a shallow clone, where `9379d40`
    is simply an unknown object. Arena sessions and most CI checkouts are shallow by default.
    A resolver that reads "no history" as "no file" would mark 478 recoverable files as lost.
    So when history is unavailable this tool says so and refuses to classify ARCHIVED at all.

USAGE
    python3 tools/record_links.py            # report
    python3 tools/record_links.py --strict   # MOVED and ARCHIVED also fail
    python3 tools/record_links.py --selftest # prove the classifier separates the five cases
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT.parent
ARCHIVE_COMMIT = '9379d40^'
# The account's other repositories. A citation beginning with one of these names is not a
# path in this project — it is a pointer across repositories, and it resolves there or not.
SIBLING_REPOS = {
    'the-authors-desk', 'soul-library', 'storyos-site', 'sara', 'adaptation-talent',
    'how-to-write-fanfiction', 'the-universal-storyline-creation', 'stark_heir',
    'mcu_eternal_fanfic', 'supergirl-adrian-vale', 'pokemon-adaptation', 'gm5206663-bit',
}
CITE = re.compile(r'`([A-Za-z0-9_./-]+\.(?:md|py|json|txt|html))(?::\d+)?`')
# a range (`canon_001..018_excerpt.txt`) or a placeholder (`canon_0XX_...`) is notation, not a path
NOT_A_PATH = re.compile(r'\.\.|XX|xx\b|\bNN\b|\.\.\.')


def record_files(root: Path = ROOT) -> list[Path]:
    found = sorted((root / 'foundation').glob('*.md'))
    found += sorted((root / 'codex').glob('*.md'))
    for name in ('HANDOFF.md', 'AGENTS.md', 'README.md'):
        p = root / name
        if p.exists():
            found.append(p)
    return found


def kit_index() -> dict[str, list[str]]:
    """basename -> every path in the kit that carries it."""
    index: dict[str, list[str]] = {}
    for p in KIT.rglob('*'):
        if p.is_file() and '.git' not in p.parts:
            index.setdefault(p.name, []).append(str(p.relative_to(KIT)))
    return index


def archive_index() -> dict[str, list[str]] | None:
    """basename -> paths inside the one-home archive, or None when history is unavailable."""
    try:
        out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', ARCHIVE_COMMIT,
                              '--', '_archive/2026-10-12_one-home/'],
                             cwd=KIT, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    index: dict[str, list[str]] = {}
    for line in out.stdout.splitlines():
        index.setdefault(Path(line).name, []).append(line)
    return index


def shipped_chapters(root: Path = ROOT) -> set[int]:
    nums = set()
    for p in (root / 'chapters').glob('Chapter_*.md'):
        m = re.match(r'Chapter_(\d+)', p.name)
        if m:
            nums.add(int(m.group(1)))
    return nums


def classify(cite: str, doc: Path, index, archive, shipped,
             root: Path | None = None) -> tuple[str, str]:
    root = root or ROOT
    for base in (doc.parent, root, root / 'foundation', root / 'codex', root.parent):
        if (base / cite).exists():
            return 'OK', ''
    name = Path(cite).name
    if index and name in index:
        where = sorted(index[name])[0]
        return 'MOVED', where
    m = re.search(r'Chapter_(\d+)', name)
    if m and int(m.group(1)) not in shipped and 'chapters/' in cite:
        return 'PLANNED', f'ch{int(m.group(1))} not yet written (edge ch{max(shipped)})'
    if cite.split('/')[0] in SIBLING_REPOS:
        return 'EXTERNAL', f'{cite.split("/")[0]} is another repository on the account'
    if archive is None:
        return 'UNVERIFIABLE', 'history unavailable (shallow clone) — cannot rule archived'
    if name in archive:
        return 'ARCHIVED', archive[name][0]
    if in_history(name):
        return 'DELETED', f'deleted from this repository; recover with `git log --all -- {name}`'
    return 'MISSING', 'not on disk, not in history, not in a sibling repo'


def in_history(name: str) -> bool:
    try:
        out = subprocess.run(['git', 'log', '--all', '--format=%h', '--', f'*{name}'],
                             cwd=KIT, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return False
    return out.returncode == 0 and bool(out.stdout.strip())


def run(strict: bool = False, root: Path = ROOT, quiet: bool = False) -> int:
    index, archive, shipped = kit_index(), archive_index(), shipped_chapters(root)
    tally = {'OK': 0, 'MOVED': 0, 'ARCHIVED': 0, 'PLANNED': 0, 'MISSING': 0,
             'UNVERIFIABLE': 0, 'EXTERNAL': 0, 'DELETED': 0}
    rows = []
    for doc in record_files(root):
        text = doc.read_text(encoding='utf-8', errors='replace')
        for m in CITE.finditer(text):
            cite = m.group(1)
            if cite.startswith(('http', '/')) or NOT_A_PATH.search(cite):
                continue
            verdict, detail = classify(cite, doc, index, archive, shipped, root)
            tally[verdict] += 1
            if verdict not in ('OK', 'PLANNED', 'EXTERNAL'):
                rows.append((verdict, cite, doc.name, detail))

    if archive is None and not quiet:
        print('⚠  HISTORY UNAVAILABLE — this is a shallow clone, so no archived file can be')
        print('   confirmed. Every recovery instruction in this repository (`git show')
        print(f'   {ARCHIVE_COMMIT}:...`) does not resolve here. Run `git fetch --unshallow`.')
        print()

    if not quiet:
        for verdict, cite, doc, detail in sorted(rows):
            tail = f'  ->  {detail}' if detail else ''
            print(f'{verdict:13s} {cite}{tail}')
            print(f'{"":13s} cited by {doc}')
        print()
        print(f'{tally["OK"]} ok · {tally["EXTERNAL"]} in another repo · '
              f'{tally["MOVED"]} moved · {tally["ARCHIVED"]} archived · '
              f'{tally["DELETED"]} deleted · {tally["PLANNED"]} planned · '
              f'{tally["MISSING"]} missing · {tally["UNVERIFIABLE"]} unverifiable')

    failed = tally['MISSING'] > 0
    if strict:
        failed = failed or tally['MOVED'] > 0 or tally['ARCHIVED'] > 0 or tally['DELETED'] > 0
    if not quiet:
        print('RESULT:', 'FAIL' if failed else 'PASS')
    return 1 if failed else 0


def selftest() -> int:
    failures = 0

    def expect(label, cond):
        nonlocal failures
        print(f'SELFTEST {"ok:  " if cond else "FAIL:"} {label}')
        failures += 0 if cond else 1

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / 'lan_shen'
        (root / 'foundation').mkdir(parents=True)
        (root / 'codex').mkdir()
        (root / 'chapters').mkdir()
        (root / 'chapters' / 'Chapter_01_Real.md').write_text('x', encoding='utf-8')
        (root / 'tools').mkdir()
        (root / 'tools' / 'here.py').write_text('x', encoding='utf-8')
        index = {'here.py': ['lan_shen/tools/here.py'], 'old.md': ['_archive/x/old.md']}
        archive = {'ghost.md': ['_archive/2026-10-12_one-home/x/ghost.md']}
        shipped = {1}
        doc = root / 'foundation' / 'Doc.md'

        v, _ = classify('tools/here.py', doc, index, archive, shipped, root)
        expect('a real path is OK', v == 'OK')
        v, where = classify('here.py', doc, index, archive, shipped, root)
        expect('an unqualified name resolves by basename (MOVED)', v == 'MOVED' and where)
        v, _ = classify('chapters/Chapter_05_Old.md', doc, index, archive, shipped, root)
        expect('a future chapter is PLANNED, not missing', v == 'PLANNED')
        v, _ = classify('ghost.md', doc, index, archive, shipped, root)
        expect('a file only in the one-home archive is ARCHIVED', v == 'ARCHIVED')
        v, _ = classify('nowhere_at_all.md', doc, index, archive, shipped, root)
        expect('a file in neither place is MISSING', v == 'MISSING')
        v, detail = classify('nowhere_at_all.md', doc, index, None, shipped, root)
        expect('no history => UNVERIFIABLE, never MISSING', v == 'UNVERIFIABLE')

        (root / 'foundation' / 'Doc.md').write_text(
            '`tools/here.py` and `nowhere_at_all.md`\n', encoding='utf-8')
        expect('run() fails on a MISSING citation', run(root=root, quiet=True) == 1)

        (root / 'foundation' / 'Doc.md').write_text('`tools/here.py`\n', encoding='utf-8')
        expect('run() passes when every citation resolves', run(root=root, quiet=True) == 0)

        (root / 'foundation' / 'Doc.md').write_text('`canon_001..018_excerpt.txt`\n', encoding='utf-8')
        expect('a range notation is not a path', run(root=root, quiet=True) == 0)

    print(f'SELFTEST: {failures} failure(s)')
    return 0 if failures == 0 else 2


def main(argv):
    if '--selftest' in argv:
        return selftest()
    return run(strict='--strict' in argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

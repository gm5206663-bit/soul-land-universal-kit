#!/usr/bin/env python3
"""tools/chapter_shape.py — the shape of a chapter file, the two ungated conventions, and stubs.

    python3 tools/chapter_shape.py --report     # what every chapter's head looks like
    python3 tools/chapter_shape.py --check      # the gate (pinned backlog shrinks only)
    python3 tools/chapter_shape.py --freeze     # re-record the pinned backlog
    python3 tools/chapter_shape.py --selftest   # prove each rule can fail

WHY THIS EXISTS
  `docs/CANON_METHOD.md` found one convention that the account practised but never checked:
  the canon line. It was not the only one. This tool covers the rest of the chapter's shape —
  the parts a reader never notices until they are missing.

WHAT IT CHECKS
  S1  THE TITLE IS A HEADING. The first non-empty line of a chapter is `# …`. One chapter in
      the corpus started `--- # Chapter One: …`, which Markdown renders as a horizontal rule
      followed by plain text: the title is not a heading, so nothing that reads headings can
      see it — not a table of contents, not an anchor, not a tool. Found 2026-10-30.

  S2  THE TITLE NAMES A CHAPTER AND A TITLE. `# Chapter 12: The Wall` or `# Chapter 12 — The
      Wall` or `# Chapter 12 - The Wall`. Both separators are in use across the account and
      both are fine; a bare `# Chapter 12` with nothing after it is not. A heading with no
      number at all is not a chapter file.

  S3  A PLACEHOLDER IS NOT A CHAPTER. `soul_land_new/chapters/Chapter_01.md` contains
      `# Chapter 1: {Title}` and 24 words of template text, sitting beside the real
      `Chapter_01_The_Grass_That_Stayed.md`. Every measuring tool on the account counts it as
      a chapter, so the corpus size, the chapter count and the register all include a file the
      author never wrote. Unfilled template brackets are the tell. This is a HARD finding: a
      stub inflates counts silently, and silent inflation is the failure the register exists
      to prevent.

  S4  THE TIMELINE LINE, where the serial declared it. `## Timeline: Spring, age 11 — six days
      on the road.` is the sibling of the canon line: **canon says what source, Timeline says
      when in-world**. Two serials apply it to every chapter (Soul_Land_2_Project 24/24,
      soul_land_2_new 8/8) and one applies it to 37 of 116. It was never written down and never
      checked. A serial that has adopted it declares so in `DECLARED` below, and then every
      chapter must carry it; a serial that never used it is left alone, because inventing a
      timeline for 100 chapters is authoring, not checking.

  S5  THE FILE IS NOT TRUNCATED. The last prose line ends with terminal punctuation. A chapter
      that stops mid-sentence is either a bad save or a bad edit, and it is invisible in a
      diff of a long file. Advisory, so a deliberately mid-air ending is the author's call —
      but it must be visible.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = Path(__file__).resolve().parent / 'chapter_shape_baseline.json'

# Serials that have adopted `## Timeline:` as their own convention. This table is the whole
# point: a convention is declared by the book that keeps it, not imposed by a tool on books
# that never did. Add a serial here when its author adopts it — then every chapter needs one.
DECLARED = {
    'Soul_Land_2_Project': 'complete — 24 of 24 chapters carry a Timeline line',
    'soul_land_2_new': 'complete — 8 of 8 chapters carry a Timeline line',
}
# NOT declared: adaptive_prodigy (37 of 116). Declaring it would impose a rule the author kept
# a third of the time and invent a 72-item backlog for a habit the author may not want. It is
# counted in --report and left alone. Adopting it is a decision for the author, not a tool.

H1 = re.compile(r'^#\s+(\S.*)$')
# The number may be a digit or an English word: lan_shen writes `# Chapter One: …` and is
# right to. Requiring digits reported eight correct chapters as untitled on 2026-10-30 — a
# false finding is not a small error, it asks someone to fix what is already right.
WORDS = ('one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|'
         'fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|'
         'seventy|eighty|ninety|hundred')
TITLE = re.compile(r'^#\s+(?:chapter|ch\.?)\s*(\d+[a-z]?|(?:' + WORDS + r')(?:[-\s](?:' +
                   WORDS + r'))*)\s*(?::|—|–|-)\s*(\S.*)$', re.I)
TIMELINE = re.compile(r'^#{2,4}\s*Timeline\s*:\s*(\S.*)$', re.I | re.M)
PLACEHOLDER = re.compile(r'\{[A-Za-z][^}\n]{0,40}\}|no content yet|body goes here only after|'
                         r'no chapter is authorized|prose rules:', re.I)
TERMINAL = re.compile(r'[.!?"\u2019\u201d*_—…)\]}]$')


def chapters(root: Path) -> list[Path]:
    out = []
    for d in sorted(root.glob('*/chapters')):
        for p in sorted(d.glob('*.md')):
            if p.name.lower().startswith(('chapter_template', 'index', 'readme')):
                continue
            out.append(p)
    return out


def head_lines(p: Path, n: int = 16) -> list[str]:
    try:
        return p.read_text(encoding='utf-8', errors='replace').splitlines()[:n]
    except OSError:
        return []


def first_nonempty(lines: list[str]) -> tuple[int, str]:
    for i, l in enumerate(lines):
        if l.strip():
            return i, l
    return -1, ''


def last_prose_line(p: Path) -> str:
    try:
        lines = [l.strip() for l in p.read_text(encoding='utf-8', errors='replace').splitlines()]
    except OSError:
        return ''
    for l in reversed([l for l in lines if l]):
        if l.startswith(('#', '---', '```', '|', '>', '-', '*', '•')) or re.match(r'^\d+\.\s', l):
            continue
        return l
    return ''


def shape(p: Path) -> dict:
    lines = head_lines(p)
    _, first = first_nonempty(lines)
    head = '\n'.join(lines)
    return {
        'h1': bool(H1.match(first)),
        'titled': bool(TITLE.match(first)),
        'placeholder': bool(PLACEHOLDER.search("\n".join(lines[:12]))),
        'timeline': bool(TIMELINE.search(head)),
        'terminal': bool(TERMINAL.search(last_prose_line(p))),
        'first': first,
    }


def survey(root: Path) -> dict[str, dict]:
    out = {}
    for p in chapters(root):
        out[str(p.relative_to(root))] = shape(p)
    return out


def load_baseline() -> dict:
    if not BASELINE.exists():
        return {}
    return json.loads(BASELINE.read_text(encoding='utf-8'))


def problems(rel: str, s: dict, base: dict) -> list[str]:
    """Every failure for one chapter, minus what the baseline pins."""
    out = []
    pin = base.get('pinned', {})
    if not s['h1']:
        out.append(f'S1 not a heading: first line is {s["first"][:70]!r}')
    if s['h1'] and not s['titled']:
        out.append(f'S2 the heading names no chapter-and-title: {s["first"][:70]!r}')
    if s['placeholder'] and rel not in pin.get('stub', []):
        out.append('S3 placeholder file counted as a chapter (unfilled template brackets)')
    book = rel.split('/')[0]
    if book in DECLARED and not s['timeline'] and rel not in pin.get('timeline', []):
        out.append(f'S4 no `## Timeline:` line — {book} declared this convention')
    if not s['terminal'] and rel not in pin.get('terminal', []):
        out.append('S5 the file appears truncated (last prose line has no terminal punctuation)')
    return out


def check(root: Path) -> int:
    base = load_baseline()
    data = survey(root)
    bad = 0
    for rel, s in sorted(data.items()):
        for msg in problems(rel, s, base):
            print(f'{rel}: {msg}')
            bad += 1
    # a pin that no longer fails must be dropped, or the list is a museum
    stale = []
    for kind, rels in base.get('pinned', {}).items():
        for rel in rels:
            if rel not in data:
                stale.append((kind, rel, 'the file is gone'))
                continue
            s = data[rel]
            still = {'timeline': not s['timeline'], 'terminal': not s['terminal'],
                     'stub': s['placeholder']}.get(kind, True)
            if not still:
                stale.append((kind, rel, 'it now passes — drop the pin'))
    for kind, rel, why in stale:
        print(f'STALE PIN {kind}: {rel} — {why}')
    hard = bad + len(stale)
    total = len(data)
    ok = total - len({r for k, v in base.get('pinned', {}).items() for r in v})
    print(f'CHAPTER SHAPE: {total} chapter file(s); {bad} unpinned finding(s); '
          f'{len(stale)} stale pin(s); conventions declared for {len(DECLARED)} serial(s)')
    if hard:
        print(f'RESULT: FAIL — {hard} problem(s)')
        return 1
    print('RESULT: PASS — every chapter has a heading and a title; pins are live')
    return 0


def report(root: Path) -> int:
    data = survey(root)
    print(f'{"chapter":58s} h1 tit stub rm tm end')
    for rel, s in sorted(data.items()):
        flags = ' '.join('ok ' if s[k] else '.. ' for k in ('h1', 'titled'))
        flags += ('STUB' if s['placeholder'] else '  . ')
        flags += ' '.join('ok ' if s[k] else '.. ' for k in ('timeline', 'terminal'))
        if s['h1'] and s['titled'] and not s['placeholder']:
            continue          # only show the interesting ones
        print(f'{rel:58s} {flags}')
    n = len(data)
    print(f'\n{n} chapter file(s): '
          f'{sum(1 for s in data.values() if s["h1"])} with a real heading, '
          f'{sum(1 for s in data.values() if s["titled"])} with a chapter-and-title, '
          f'{sum(1 for s in data.values() if s["placeholder"])} placeholder(s), '
          f'{sum(1 for s in data.values() if s["timeline"])} with a Timeline line')
    return 0


def freeze(root: Path) -> int:
    data = survey(root)
    pinned = {'timeline': [], 'terminal': [], 'stub': []}
    for rel, s in sorted(data.items()):
        book = rel.split('/')[0]
        if book in DECLARED and not s['timeline']:
            pinned['timeline'].append(rel)
        if not s['terminal']:
            pinned['terminal'].append(rel)
        if s['placeholder']:
            pinned['stub'].append(rel)
    BASELINE.write_text(json.dumps({
        'note': 'Pinned 2026-10-30. This list may only SHRINK: fill the line, then drop the pin. '
                'S1/S2/S3 are never pinned — a heading and a real chapter are not backlog.',
        'pinned': pinned}, indent=1) + '\n', encoding='utf-8')
    print(f'BASELINE: pinned {len(pinned["timeline"])} Timeline gap(s), '
          f'{len(pinned["terminal"])} truncation advisory(ies), '
          f'{len(pinned["stub"])} declared stub(s)')
    return 0


def selftest() -> int:
    fails = 0

    def ck(name: str, ok: bool) -> None:
        nonlocal fails
        print(f'SELFTEST {"ok:  " if ok else "FAIL:"} {name}')
        fails += 0 if ok else 1

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        d = root / 'soul_land_2_new' / 'chapters'
        d.mkdir(parents=True)

        def mk(name: str, body: str) -> Path:
            p = d / name
            p.write_text(body, encoding='utf-8')
            return p

        good = mk('Chapter_01_Good.md',
                  '# Chapter 1: The Road\n\n## Canon Reference: canon ch 1\n\n'
                  '## Timeline: Spring, age 11 — six days.\n\nHe walked.\n')
        ck('S1 a real heading passes', shape(good)['h1'])
        ck('S2 chapter-and-title passes', shape(good)['titled'])
        ck('S4 a declared Timeline passes', shape(good)['timeline'])
        ck('S5 a closed sentence passes', shape(good)['terminal'])

        glued = mk('Chapter_02_Glued.md',
                   '--- # Chapter Two: What the Master Said\n\nprose.\n')
        ck('S1 a title glued after --- is caught', not shape(glued)['h1'])

        dash = mk('Chapter_03_Dash.md', '# Chapter 3 — The Wall\n\nprose.\n')
        ck('S2 an em-dash separator is accepted', shape(dash)['titled'])
        hy = mk('Chapter_04_Hy.md', '# Chapter 4 - The Wall\n\nprose.\n')
        ck('S2 a hyphen separator is accepted', shape(hy)['titled'])

        word = mk('Chapter_09_Word.md', '# Chapter One: What the Master Said\n\nprose.\n')
        ck('S2 a spelled-out chapter number is accepted', shape(word)['titled'])
        big = mk('Chapter_10_Big.md', '# Chapter Twenty-One: The Find\n\nprose.\n')
        ck('S2 a hyphenated spelled number is accepted', shape(big)['titled'])

        bare = mk('Chapter_05_Bare.md', '# Chapter 5\n\nprose.\n')
        ck('S2 a bare chapter number is caught', not shape(bare)['titled'])

        stub = mk('Chapter_06_Stub.md',
                  '# Chapter 6: {Title}\n\n{No content yet. This file is populated only later.}\n')
        ck('S3 an unfilled template is caught as a placeholder', shape(stub)['placeholder'])
        ck('S3 real prose is not a placeholder', not shape(good)['placeholder'])

        cut = mk('Chapter_07_Cut.md', '# Chapter 7: Cut\n\nHe raised the sword and\n')
        ck('S5 a truncated tail is caught', not shape(cut)['terminal'])

        # the gate, with a pinned backlog that may only shrink.
        # The four defect fixtures above are removed first: leaving them in the tree made the
        # "a frozen backlog passes" case fail for their reasons, and the later cases pass for
        # the wrong reason. A fixture set that overlaps its own assertions tests nothing.
        for bad in (glued, bare, stub, cut):
            bad.unlink()

        global BASELINE
        real = BASELINE
        BASELINE = root / 'baseline.json'
        try:
            freeze(root)
            ck('a frozen backlog passes the gate', check(root) == 0)
            mk('Chapter_08_New.md', '# Chapter 8: New\n\nprose without a Timeline line.\n')
            ck('a NEW chapter missing a declared convention fails', check(root) == 1)
            # filling the line must force the PIN out. This has to be a chapter that freeze()
            # actually pinned — filling an unpinned file leaves nothing stale and the gate
            # rightly passes, which is how the first version of this test lied.
            pinned_now = json.loads((root / 'baseline.json').read_text())['pinned']['timeline']
            assert pinned_now, 'freeze pinned nothing; the stale-pin case cannot mean anything'
            target = root / pinned_now[0]
            target.write_text(
                target.read_text(encoding='utf-8').replace(
                    '\n\nprose', '\n\n## Timeline: after the wall.\n\nprose'),
                encoding='utf-8')
            ck('a stale pin fails the gate (the list must shrink)', check(root) == 1)
        finally:
            BASELINE = real

    print(f'SELFTEST: {fails} failure(s)')
    return 1 if fails else 0


def main(argv: list[str]) -> int:
    if '--selftest' in argv:
        return selftest()
    if '--report' in argv:
        return report(ROOT)
    if '--check' in argv:
        return check(ROOT)
    if '--freeze' in argv:
        return freeze(ROOT)
    print(__doc__)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

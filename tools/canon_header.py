#!/usr/bin/env python3
"""tools/canon_header.py — the canon line at the head of every chapter.

    python3 tools/canon_header.py --report      # coverage: which chapters say what they adapt
    python3 tools/canon_header.py --check       # gate: no chapter may go quiet (see BASELINE)
    python3 tools/canon_header.py --backfill    # fill from the author's own coverage receipts
    python3 tools/canon_header.py --freeze      # record today's backlog (shrinks only)
    python3 tools/canon_header.py --selftest    # prove the gate can fail

THE METHOD THIS ENFORCES
  The author's rule, in their words: at the start of every chapter, say **which canon chapter
  or episode that chapter is built on**. The reason is not tidiness. Canon is ore, not
  transcript — the chapter is ours — but a reader (and the next agent) must be able to see
  *which ore* without reading the whole book. A chapter that does not say what it adapts
  cannot be checked against canon at all; it can only be admired.

  Three shapes are already in use in this corpus, and all three are accepted:

    1. novel form      `## Canon Reference: canon ch 286 "Dreams of Battle Armor" AS ORE (…)`
                       — adaptive_prodigy (116 of 116), Soul_Land_2_Project, soul_land_2_new
    2. short form      `## Canon: SL3 ch 1–2 — the awakening · the walk home`
    3. episode form    `**[canon: S1 slot 1 — Stormy Weather (production N° 101)]**`
                       — Miraculous_Project: an animated source numbers episodes, not chapters

  The detector insists on a **source locator** — a chapter number, an episode, a slot, a
  production number. A line that says "canon-inspired" and stops is not a reference; it is a
  mood. The guide's rule is that a claim must be checkable, and this is the smallest claim a
  chapter makes.

WHY THE BACKLOG IS PINNED RATHER THAN RED
  On 2026-10-30, 151 of 286 chapter files carried no canon line. Turning that red on day one
  would red the whole workspace and teach everyone to ignore it — the failure mode the method
  calls out by name. Instead the backlog is written down in `canon_header_baseline.json` and
  may only ever SHRINK: a chapter not in it must carry a canon line, and a baseline entry that
  has since gained a line must be removed or the gate fails. A pinned-pending set that can grow
  is not a gate; it is a historian.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = Path(__file__).resolve().parent / 'canon_header_baseline.json'

# Where each book keeps its own receipts, and how to read a span out of them. Adding a book
# here is how its backfill becomes possible; the receipt is always named in the header we
# write, so a wrong number is traceable to the document that asserted it.
RECEIPTS = {
    'soul_land_3_oc': ('canon_coverage/INDEX.md',),
    'soul_land_1_fire_dragon_lizard': ('canon_coverage/CANON_COVERAGE_INDEX.md',),
    'soul_land_4_fire_phoenix': ('canon_coverage/CANON_COVERAGE_INDEX.md',),
}

# A canon line: a marker word plus a locator that names which canon unit it is.
MARKER = re.compile(r'\bcanon\b', re.I)
LOCATOR = re.compile(
    r'(?:\bch(?:apter)?s?\.?\s*\d+'
    r'|\bnovel\s+(?:prologue|ch)'
    r'|\bepisode\b|\bep\.?\s*\d+'
    r'|\bS\d+\s*[·\s]*E\d+'
    r'|\bslot\s*\d+'
    r"|\bN[°o]\s*\d+"
    r'|\bprologue\b'
    # the house shorthand: "canon 286", "canon 247-248". It names a canon unit as precisely
    # as "ch 286" does, and it is the form adaptive_prodigy actually writes.
    r'|\bcanon\s*\d+)', re.I)
HEADER_ZONE = 20          # the canon line belongs in the head of the file, not the footer


def chapter_files(book: Path) -> list[Path]:
    d = book / 'chapters'
    if not d.is_dir():
        return []
    out = []
    for p in sorted(d.glob('*.md')):
        if p.name.lower().startswith(('chapter_template', 'index', 'readme')):
            continue
        out.append(p)
    return out


EXPLICIT = re.compile(r'^\s{0,3}#{1,6}\s*(canon\s*(reference)?)\s*[:—-]|^\s*\*\*\[canon\b', re.I)
# A canon header may legitimately say "there is no canon chapter here": an interstitial, a
# walked skip, a series-level trait. That is a declaration, not a mood, and it counts.
NO_SPAN = re.compile(r'\b(interstitial|numberless|no canon chapter|walked skip|series-level|'
                     r'canon-silent|prologue to the canon)\b', re.I)


def canon_line(path: Path) -> str | None:
    """The line in the head of the file that names its canon relationship — or None.

    Three ways a chapter may qualify:

      1. an explicit header — `## Canon Reference: …`, `## Canon: …`, `**[canon: …]**` — whose
         text is substantial and names either a canon unit or an explicit "no span here";
      2. an incidental line that carries both the word canon and a locator;
      3. the same, when the author hard-wrapped the header across several `##` lines — which
         is how adaptive_prodigy writes it, and which a single-line scan reported as silence
         on four of its chapters on 2026-10-30.
    """
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return None
    lines = text.splitlines()[:HEADER_ZONE]
    for i, line in enumerate(lines):
        if EXPLICIT.match(line):
            block = [line]
            for nxt in lines[i + 1:i + 9]:
                if nxt.lstrip().startswith('#') or nxt.strip():
                    block.append(nxt)
                else:
                    break
            body = ' '.join(b.strip(' #*') for b in block)
            if len(body) > 60 and (LOCATOR.search(body) or NO_SPAN.search(body)):
                return line.strip()
        if MARKER.search(line) and LOCATOR.search(line):
            return line.strip()
    return None


def books(root: Path) -> list[Path]:
    return sorted(d.parent for d in root.glob('*/chapters') if d.is_dir())


def survey(root: Path) -> dict[str, dict]:
    out = {}
    for book in books(root):
        files = chapter_files(book)
        if not files:
            continue
        rows = [{'file': str(f.relative_to(root)), 'has': canon_line(f) is not None} for f in files]
        out[book.name] = {'total': len(files),
                          'have': sum(1 for r in rows if r['has']),
                          'missing': [r['file'] for r in rows if not r['has']]}
    return out


def load_baseline() -> dict[str, list[str]]:
    if not BASELINE.exists():
        return {}
    return json.loads(BASELINE.read_text(encoding='utf-8')).get('backlog', {})


def check(root: Path) -> int:
    data = survey(root)
    pinned = load_baseline()
    grew, stale = [], []
    for book, d in sorted(data.items()):
        allowed = set(pinned.get(book, []))
        for f in d['missing']:
            if f not in allowed:
                grew.append(f)
        for f in allowed:
            if not (root / f).exists():
                stale.append((book, f, 'the file is gone — drop the baseline entry'))
            elif f not in d['missing']:
                stale.append((book, f, 'it now carries a canon line — drop the baseline entry'))
    for f in grew:
        print(f'NO CANON LINE  {f}')
    for book, f, why in stale:
        print(f'STALE PIN      {book}: {f} — {why}')
    total = sum(d['total'] for d in data.values())
    have = sum(d['have'] for d in data.values())
    print(f'CANON HEADERS: {have} of {total} chapter(s) name their canon source; '
          f'{total - have} in the pinned backlog')
    if grew or stale:
        print(f'RESULT: FAIL — {len(grew)} unpinned chapter(s) with no canon line, '
              f'{len(stale)} stale pin(s)')
        return 1
    print('RESULT: PASS — the backlog did not grow and no pin is stale')
    return 0


def report(root: Path) -> int:
    data = survey(root)
    print(f'{"book":36s} {"have":>5s} {"total":>6s}  first chapters still silent')
    for book, d in sorted(data.items(), key=lambda kv: kv[1]['have'] - kv[1]['total']):
        gap = d['total'] - d['have']
        sample = ', '.join(Path(m).name for m in d['missing'][:4])
        print(f'{book:36s} {d["have"]:5d} {d["total"]:6d}  {sample}')
    total = sum(d['total'] for d in data.values())
    have = sum(d['have'] for d in data.values())
    print(f'\n{have} of {total} chapter(s) name their canon source '
          f'({100 * have // max(total, 1)}%)')
    return 0


def freeze(root: Path) -> int:
    data = survey(root)
    backlog = {b: d['missing'] for b, d in sorted(data.items()) if d['missing']}
    BASELINE.write_text(json.dumps(
        {'note': 'Chapters that predate the canon-header rule (frozen 2026-10-30). '
                 'This list may only shrink: fill the line, then drop the entry.',
         'backlog': backlog}, indent=1) + '\n', encoding='utf-8')
    print(f'BASELINE: pinned {sum(len(v) for v in backlog.values())} chapter(s) '
          f'in {len(backlog)} book(s) → {BASELINE.name}')
    return 0


# --------------------------------------------------------------------------
# Backfill: the author's coverage receipts, quoted, never guessed.
# --------------------------------------------------------------------------
# `Chapters?` alone matched only 'chapter'/'chapters' — never the bare `ch` every receipt
# actually writes. A span guard that cannot see the commonest spelling rejects every real row.
CONSUMED = re.compile(r'((?:SL\d\s*)?(?:Ch(?:apter)?s?\.?)\s*\d+[^.;|]{0,90})', re.I)
FIC_NUM = re.compile(r'^\**\s*(?:Ch(?:apter)?[\s_]*)?(\d+)\b', re.I)
FILE_CELL = re.compile(r'\.md\b|`')


def _trim(span: str, limit: int = 110) -> str:
    span = re.sub(r'\s+', ' ', span).strip(' *`')
    if len(span) <= limit:
        return span
    cut = span[:limit].rsplit(' ', 1)[0].rstrip(' ·—-:;,')
    return cut + ' …'


def receipt_spans(receipt: Path) -> dict[int, str]:
    """chapter number -> the span phrase that receipt states, verbatim and trimmed.

    Three layouts are in use in this corpus and none of them is the "obvious" one:
      · soul_land_3_oc      | **Ch 1 — The Reading** | SL3 ch1–ch2 (…) | …
      · fire_dragon_lizard  | 1 | `Canon_Coverage_Chapter_01.md` | Village opening era … |
      · fire_phoenix        | Chapter_46.md | Canon_Coverage_Chapter_46.md | Anchor/valid | Chapters169-170 consumed; … |
    Reading cells instead of columns is what makes one parser serve all three. The fire
    phoenix notes are the awkward case: the span sits in a free-text column after two
    bookkeeping columns, so the cell is searched, not indexed.
    """
    out: dict[int, str] = {}
    if not receipt.exists():
        return out
    for line in receipt.read_text(encoding='utf-8', errors='replace').splitlines():
        if '|' in line and not set(line.strip()) <= set('|-: '):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            n, num_cell = None, -1
            for i, c in enumerate(cells):
                m = FIC_NUM.match(c)
                if m:
                    n, num_cell = int(m.group(1)), i
                    break
            if n is None:
                continue
            for i, c in enumerate(cells):
                # the cell the chapter number came from is a TITLE, not a span. Reading it as
                # one produced `Canon Reference: Ch 1 — The Reading` for all seven of 3-OC's
                # chapters: a header that names the chapter it is the header of.
                if i == num_cell or FILE_CELL.search(c):
                    continue
                if not CONSUMED.search(c):
                    continue
                m = CONSUMED.search(c)
                start = max(0, m.start())
                span = c[start:]
                # keep the clause around the span, not the whole paragraph of notes
                span = re.split(r'(?<=[.;])\s', span)[0] if len(span) > 120 else span
                out.setdefault(n, _trim(span))
                break
        else:
            # bullet form: - **Chapter_03 — Three Months**: novel ch2–3 span (…)
            m = re.match(r'\s*[-*]\s*\**\s*Chapter[_ ]?(\d+)', line, re.I)
            if not m:
                continue
            c = line[m.end():]
            cm = CONSUMED.search(c)
            if cm:
                out.setdefault(int(m.group(1)), _trim(c[cm.start():]))
    return out


def backfill(root: Path, dry: bool) -> int:
    wrote, skipped = 0, []
    for book in books(root):
        srcs = RECEIPTS.get(book.name)
        if not srcs:
            continue
        spans: dict[int, str] = {}
        used: dict[int, str] = {}
        for rel in srcs:
            r = book / rel
            for n, span in receipt_spans(r).items():
                spans.setdefault(n, span)
                used.setdefault(n, rel)
        for f in chapter_files(book):
            if canon_line(f):
                continue
            m = re.search(r'(?:chapter|ch)[\s_-]*(\d+)', f.name, re.I)
            if not m:
                skipped.append((f, 'no chapter number in the filename'))
                continue
            n = int(m.group(1))
            span = spans.get(n)
            if not span:
                skipped.append((f, f'no span recorded for ch{n}'))
                continue
            span = span.rstrip(' ;,·—-')
            header = (f'## Canon Reference: {span}\n'
                      f'> Span taken from `{used[n]}` — the receipt, not a memory. '
                      f'Canon is ore, not transcript; this chapter is ours.\n')
            text = f.read_text(encoding='utf-8', errors='replace')
            lines = text.splitlines(keepends=True)
            # after the H1 title, before any existing rule or prose
            at = 1
            while at < len(lines) and (lines[at].strip() == '' or lines[at].startswith(('>', '**'))):
                at += 1
            head = ''.join(lines[:at]).rstrip('\n')
            tail = ''.join(lines[at:]).lstrip('\n')
            new = head + '\n\n' + header + '\n' + tail
            if dry:
                print(f'WOULD WRITE {f.relative_to(root)}: {span[:70]}')
            else:
                f.write_text(new, encoding='utf-8')
                print(f'WROTE       {f.relative_to(root)}: {span[:70]}')
            wrote += 1
    for f, why in skipped[:40]:
        print(f'  skip  {f.relative_to(root)} — {why}')
    if len(skipped) > 40:
        print(f'  … {len(skipped) - 40} more skipped')
    print(f'{"WOULD WRITE" if dry else "WROTE"}: {wrote} chapter(s); '
          f'{len(skipped)} left for the author')
    return 0


STRONG = re.compile(r'canon\s+(span|source|block|reference|covers?|chapters?)|'
                    r'(span|source)\s+touched|adapts\s+canon|canon\s+consumed', re.I)
PIPE = '\\|'


def todo(root: Path) -> int:
    """Write the backlog as work, not as a number.

    Most of the 119 unpinned chapters already say somewhere in the file what canon they carry
    — in a record block at the foot, which is exactly where the header rule says it must NOT
    be. Those are cheap to fix: promote the line. This lists them with the line to promote,
    and separately lists the chapters where no span exists anywhere, which need a decision
    rather than a copy-paste.
    """
    strong, weak = [], []
    for b in books(root):
        for f in chapter_files(b):
            if canon_line(f):
                continue
            text = f.read_text(encoding='utf-8', errors='replace')
            cands = [(i + 1, ln.strip()) for i, ln in enumerate(text.splitlines())
                     if MARKER.search(ln) and LOCATOR.search(ln)]
            rel = str(f.relative_to(root))
            good = [(n, ln) for n, ln in cands if STRONG.search(ln)]
            if good:
                strong.append((rel, good[0]))
            else:
                weak.append((rel, cands[0] if cands else None))

    nothing = [r for r, c in weak if c is None]
    L = []
    L.append('# CANON HEADERS — the open backlog')
    L.append('')
    L.append(f'*Generated 2026-10-30 by `tools/canon_header.py --todo` over '
             f'{len(strong) + len(weak)} chapter(s). Regenerate it; never edit it.*')
    L.append('')
    L.append('The rule and its reasons: [`docs/CANON_METHOD.md`](../docs/CANON_METHOD.md). '
             'A header is one line under `## Canon Reference:` at the head of the chapter, '
             'naming the canon chapter or episode the chapter is built on, and the receipt '
             'it came from.')
    L.append('')
    L.append(f'**{len(strong)} chapter(s) already name their canon source somewhere in the '
             f'file — promote the line.**')
    L.append('')
    L.append('| chapter | line to promote |')
    L.append('|---|---|')
    for rel, (n, ln) in strong:
        L.append('| `%s` | line %d: %s |' % (rel, n, ln[:180].replace('|', PIPE)))
    L.append('')
    L.append(f'**{len(nothing)} chapter(s) say nothing about canon anywhere — these need a '
             f'span, not a copy-paste.**')
    L.append('')
    for rel in nothing:
        L.append('- `%s`' % rel)
    L.append('')
    L.append('## Nearest mentions that are not spans (do not promote these blindly)')
    L.append('')
    L.append('| chapter | mention |')
    L.append('|---|---|')
    for rel, c in weak:
        if c is not None:
            L.append('| `%s` | line %d: %s |' % (rel, c[0], c[1][:140].replace('|', PIPE)))
    dest = root / 'reports' / 'CANON-HEADERS-TODO.md'
    dest.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'TODO: {len(strong)} promotable · {len(nothing)} with nothing at all · '
          f'written to {dest.relative_to(root)}')
    return 0


LEAD_TEXT = re.compile(r'[-*]?\s*\**\s*(canon\s+(?:span|source)[^:]*|'
                       r'span\s+touched|source\s+used)\s*:?\s*\**\s*', re.I)


def promote(root: Path, dry: bool) -> int:
    """Move a canon span that already exists in a chapter's own record block up to the head.

    Nothing is invented and nothing is deleted: the span is the author's sentence, quoted,
    and the original line stays where it is as the receipt. The head gains a pointer with a
    line number, so anyone can check the promotion against the block it came from.
    """
    wrote, skipped = 0, 0
    for b in books(root):
        for f in chapter_files(b):
            if canon_line(f):
                continue
            lines = f.read_text(encoding='utf-8', errors='replace').splitlines()
            hit = None
            for i, ln in enumerate(lines):
                if not (MARKER.search(ln) and LOCATOR.search(ln) and STRONG.search(ln)):
                    continue
                m = LEAD_TEXT.search(ln)
                span = (ln[m.end():] if m else ln).strip(' *-')
                span = re.sub(r'\s+', ' ', span)
                if len(span) < 12:
                    continue
                hit = (i + 1, span[:150].rstrip(' ,;·—-'))
                break
            if not hit:
                skipped += 1
                continue
            n_line, span = hit
            header = (f'## Canon Reference: {span}\n'
                      f'> Promoted from this chapter\'s own record block, line {n_line} — '
                      f'the span is the author\'s sentence, not a summary. Canon is ore, '
                      f'not transcript; this chapter is ours.\n')
            head = '\n'.join(lines[:1]).rstrip('\n')
            tail = '\n'.join(lines[1:]).lstrip('\n')
            new = head + '\n\n' + header + '\n' + tail
            if dry:
                print(f'WOULD PROMOTE {f.relative_to(root)}: {span[:90]}')
            else:
                f.write_text(new, encoding='utf-8')
                print(f'PROMOTED      {f.relative_to(root)}: {span[:90]}')
            wrote += 1
    print(f'{"WOULD PROMOTE" if dry else "PROMOTED"}: {wrote} chapter(s); '
          f'{skipped} had no promotable span')
    return 0


def selftest() -> int:
    fails = 0

    def check_(name: str, ok: bool) -> None:
        nonlocal fails
        print(f'SELFTEST {"ok:  " if ok else "FAIL:"} {name}')
        fails += 0 if ok else 1

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        book = root / 'a_book' / 'chapters'
        book.mkdir(parents=True)

        def make(name: str, body: str) -> Path:
            p = book / name
            p.write_text(body, encoding='utf-8')
            return p

        novel = make('Chapter_01.md', '# Chapter 1: A\n\n## Canon Reference: canon ch 286 "X" AS ORE\n\n---\n\nprose\n')
        short = make('Chapter_02.md', '# Chapter 2: B\n\n## Canon: SL3 ch 1–2 — the awakening\n\nprose\n')
        epi = make('Chapter_03.md', '# Chapter 3: C\n\n**[canon: S1 slot 1 — Stormy Weather (production N° 101)]**\n\nprose\n')
        mood = make('Chapter_04.md', '# Chapter 4: D\n\nThis chapter is canon-inspired and follows the original.\n\nprose\n')
        none = make('Chapter_05.md', '# Chapter 5: E\n\nprose with no header at all\n')
        footer = make('Chapter_06.md',
                      '# Chapter 6: F\n\n' + ('prose\n\n' * 30) +
                      '\n## Canon Reference: canon ch 12\n')

        # the house shorthand "canon 247" — no 'ch', and it is how adaptive_prodigy writes
        bare = make('Chapter_08.md',
                    '# Chapter 8: H\n\n## Canon Reference: THE BIRTHDAY — canon 247 (Ready) and canon 248\n\nprose\n')
        check_('the bare "canon 247" shorthand counts', canon_line(bare) is not None)

        # a header hard-wrapped across several ## lines: four adaptive_prodigy chapters were
        # reported as silent on 2026-10-30 purely because a one-line scan could not see them
        wrapped = make('Chapter_09.md',
                       '# Chapter 9: I\n\n## Canon Reference: THE ARRIVAL — canon 244\'s held tail (the\n'
                       '## announcement, the Pagoda tower) + canon 245 (The Legendary Shrek City)\n'
                       '## — all fetched in full and mined here.\n\nprose\n')
        check_('a hard-wrapped header counts', canon_line(wrapped) is not None)

        # an interstitial legitimately adapts no canon chapter, and says so
        inter = make('Chapter_10.md',
                     '# Chapter 10: J\n\n## Canon Reference: interstitial — the walked skip, weeks\n'
                     '## three to four; no canon chapter is adapted, the confession is user-directed.\n\nprose\n')
        check_('a declared interstitial counts', canon_line(inter) is not None)

        check_('the novel form counts', canon_line(novel) is not None)
        check_('the short form counts', canon_line(short) is not None)
        check_('the episode form counts', canon_line(epi) is not None)
        check_('"canon-inspired" with no locator does NOT count',
               canon_line(mood) is None)
        check_('a chapter with no line is caught', canon_line(none) is None)
        check_('a canon line in the footer does not count', canon_line(footer) is None)

        data = survey(root)['a_book']
        # nine files now: novel, short, episode, bare, wrapped, interstitial count; the mood
        # line, the silent chapter and the footer-only line do not.
        check_('the survey counts 6 of 9', (data['have'], data['total']) == (6, 9))

        # the pinned baseline: may only shrink
        global BASELINE
        real = BASELINE
        BASELINE = root / 'baseline.json'
        try:
            BASELINE.write_text(json.dumps({'backlog': {'a_book': [
                str(p.relative_to(root)) for p in (mood, none, footer)]}}), encoding='utf-8')
            import io
            from contextlib import redirect_stdout
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc_pinned = check(root)
            check_('a pinned backlog passes', rc_pinned == 0)

            make('Chapter_07.md', '# Chapter 7: G\n\nprose, no canon line\n')
            with redirect_stdout(io.StringIO()):
                rc_new = check(root)
            check_('a NEW chapter with no canon line fails the gate', rc_new == 1)

            # filling a line must force the pin out, not leave it rotting
            short.write_text('# Chapter 2: B\n\n## Canon: SL3 ch 1–2\n', encoding='utf-8')
            with redirect_stdout(io.StringIO()):
                rc_stale = check(root)
            check_('a stale pin fails the gate (the list must shrink)', rc_stale == 1)
        finally:
            BASELINE = real

        # backfill reads a receipt and writes nothing it did not read
        b2 = root / 'b_book'
        (b2 / 'chapters').mkdir(parents=True)
        (b2 / 'chapters' / 'Chapter_01.md').write_text('# Chapter 1: Z\n\nprose\n', encoding='utf-8')
        (b2 / 'canon_coverage').mkdir()
        (b2 / 'canon_coverage' / 'INDEX.md').write_text(
            '| Ch 1 — Z | SL3 ch1–ch2 (the awakening · the walk home) | `x.md` | audit | shipped |\n',
            encoding='utf-8')
        global RECEIPTS
        saved = RECEIPTS
        RECEIPTS = dict(RECEIPTS, b_book=('canon_coverage/INDEX.md',))
        try:
            import io
            from contextlib import redirect_stdout
            with redirect_stdout(io.StringIO()):
                backfill(root, dry=False)
            got = canon_line(b2 / 'chapters' / 'Chapter_01.md')
            check_('backfill writes the span it read', got is not None and 'SL3 ch1' in got)
            body = (b2 / 'chapters' / 'Chapter_01.md').read_text(encoding='utf-8')
            check_('backfill names the receipt it came from', 'canon_coverage/INDEX.md' in body)
            check_('backfill keeps the prose intact', body.rstrip().endswith('prose'))
            check_('backfill puts the line in the head, not the foot',
                   body.index('Canon Reference') < 200)
        finally:
            RECEIPTS = saved

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
    if '--promote' in argv:
        return promote(ROOT, dry='--dry-run' in argv)
    if '--todo' in argv:
        return todo(ROOT)
    if '--backfill' in argv:
        return backfill(ROOT, dry='--dry-run' in argv)
    print(__doc__)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

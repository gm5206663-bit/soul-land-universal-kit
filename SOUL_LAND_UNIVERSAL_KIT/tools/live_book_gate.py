#!/usr/bin/env python3
"""LIVE BOOK GATE — the house-wide gate for a book's live text.

WHY THIS EXISTS (2026-10-11)

A whole-account sweep found the same defect in five places: a check that
reported success while covering less than it claimed. The worst of them was
Blue Silver, whose live Book One sits in `chapters_rebuilt/` while `chapters/`
holds the first draft the author rejected as "nonsense" — so a gate written
the obvious way, "sweep chapters/", sweeps the rejected draft and never sees
the book. Nothing gated either one.

This gate refuses to make that mistake. It finds the chapter directories by
CONTENT, decides which one is live by reading the project's own status files,
and when it cannot tell it FAILS and says so rather than guessing. Then it
checks the live text for the one thing every book in this house must have:
speech, and no sentence over sixty words.

The three questions of the Scope Law, asked of every run:
  1. did it cover what ships?      → the live directory, chosen and named
  2. does it say how much?         → a COVERAGE line
  3. does it fail on nothing?      → 0 chapters is a hard failure

Run:  python3 tools/live_book_gate.py PROJECT_DIR
      python3 tools/live_book_gate.py --all --root /path/to/workspace
      python3 tools/live_book_gate.py --selftest
"""
import os, re, sys, glob, statistics

DIALOGUE_FLOOR = 3      # hard — house law
DIALOGUE_BAR = 8.0      # per 1,000 words, advisory
WORD_BAND = (2400, 3400)
CHAPTER_RX = re.compile(r'^chapter[\s_-]*\d+', re.I)
# Not every file called Chapter_<n> is a chapter. Audit reports, validation
# dumps and review notes live beside the prose and match the same pattern —
# counting them as chapters is how the first version of this gate refused
# eleven directories in fire-phoenix-workshop/sources on one run.
NON_CHAPTER_RX = re.compile(r'(audit|validation|review|report|notes|ledger|summary|'
                            r'index|readme|check|status|predraft|alternate|_r\d\b)', re.I)
DERIVED = ('manuscript',)                  # reader editions, generated from the author's
# Tested against the whole relative path, not the basename: the dead copies
# live at _archive/…, sources/…, …/superseded/… — the directory at the end has
# an innocent name.
DEAD_PATH_RX = re.compile(r'(^|/)(_archive|archive|archives|_attic|attic|audit|audits|'
                          r'old|_old|drafts?|planning|notes|history|rejected|stale|'
                          r'quarantine|snapshot|sources|parked|backup|backups)(/|$)|'
                          r'(archive_|_archive|superseded|rejected|stale|unshipped|'
                          r'unreceipted|_alt_drafts)', re.I)
# Lines that look like sentences but are planning furniture: beats, spines and
# status dumps use "·" as a separator and "LABEL:" openings. Measuring them as
# prose invents sixty-word sentences that nobody wrote.
PLAN_LINE_RX = re.compile(r'·|^[A-Z][A-Za-z /()\-]{2,24}:\s|^\s*\||^\s*[-*]\s?')

#: Paths that are never the live book: historical snapshots, promotion staging,
#: reference copies kept beside the work. ONE definition — the gate and the
#: control centre both call is_out_of_scope(), because two copies of a scope
#: rule drift exactly like two copies of a text.
OUT_OF_SCOPE_RX = re.compile(r'(/reference/|promotion_proposal|staging|_kit_reference'
                             r'|sources/)', re.I)


def is_out_of_scope(rel):
    return bool(DEAD_PATH_RX.search(rel) or OUT_OF_SCOPE_RX.search(rel))
DEAD_MARK = re.compile(r'(superseded|do not use|rejected|first draft|historical|'
                       r'archived|not authoritative|never read it as current)', re.I)
STATUS_FILES = ('HANDOFF.md', 'README.md', 'STATUS.md', 'STATE.md', 'NEXT.md')


def chapter_files(d):
    out = []
    for f in sorted(os.listdir(d)):
        if (f.endswith('.md') and CHAPTER_RX.match(f)
                and not NON_CHAPTER_RX.search(f)):
            out.append(os.path.join(d, f))
    return out


def chapter_dirs(project):
    """Every directory under the project that holds chapter-numbered files."""
    found = {}
    for dirpath, dirnames, filenames in os.walk(project):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        rel = os.path.relpath(dirpath, project)
        if rel == '.':
            continue
        if any(CH_RX_match(f) for f in filenames):
            found[rel] = dirpath
    return found


def CH_RX_match(f):
    return (f.endswith('.md') and CHAPTER_RX.match(f)
            and not NON_CHAPTER_RX.search(f))


def status_text(project):
    for f in STATUS_FILES:
        p = os.path.join(project, f)
        if os.path.exists(p):
            return open(p, encoding='utf-8', errors='replace').read(), f
    return '', ''


def choose_live(project, dirs):
    """Return (live_dir, dead_dirs, why) or (None, [], refusal)."""
    candidates = {r: p for r, p in dirs.items()
                  if os.path.basename(r) not in DERIVED and not DEAD_PATH_RX.search(r)}
    if not candidates:
        return None, [], (f'no chapter directory found under {project} '
                          f'(looked for Chapter_<n>*.md; saw: {sorted(dirs) or "nothing"})')
    if len(candidates) == 1:
        r, p = next(iter(candidates.items()))
        return p, [], f'single chapter directory: {r}/'
    # more than one: the project must say in writing which is live
    txt, src = status_text(project)
    if not txt:
        return None, [], (f'{len(candidates)} chapter directories and no status file to '
                          f'disambiguate: {sorted(candidates)}')
    # WHICH DIRECTORY A DEAD MARKER CONDEMNS — nearest name, same unit.
    #
    # Three attempts failed before this one, each in a different way, and the
    # failed cases are the reason the rule is what it is:
    #   * a ±400 character window condemned BOTH directories, because a README
    #     says "the first draft (chapters/) was rejected ... the authoritative
    #     continuity is chapters_rebuilt/" in one breath. A marker must not
    #     reach across sentences.
    #   * substring matching condemned Blue Silver's LIVE book: the name
    #     "chapters" matches inside "chapters_rebuilt". Whole words only.
    #   * proximity without a unit condemned the live book again from far
    #     away — "the superseded bluesilver_codex/ files" sat within 400
    #     characters of an unrelated mention of chapters_rebuilt/ and killed it.
    #
    # The rule that survives all three: a marker and the directory it condemns
    # must share a unit — a sentence in prose, a row in a table — and within
    # that unit the marker condemns the NEAREST named whole word.
    units = []
    for line in txt.split('\n'):
        if line.strip().startswith('|'):          # table row: one unit
            units.append(line)
        else:                                      # prose: sentence units
            units.extend(sentences(line))
    units = [u for u in units if u.strip()]

    def mentions(text, dirname):
        return [m.start() for m in re.finditer(
            r'(?<![\w-])' + re.escape(dirname) + r'(?![\w-])', text)]

    dead = set()
    for unit in units:
        names_here = {r: mentions(unit, os.path.basename(r)) for r in candidates}
        names_here = {r: ps for r, ps in names_here.items() if ps}
        if not names_here:
            continue
        for marker in DEAD_MARK.finditer(unit):
            best, best_d = None, None
            for r, ps in names_here.items():
                d = min(abs(marker.start() - p) for p in ps)
                if best_d is None or d < best_d:
                    best, best_d = r, d
            if best is not None:
                dead.add(best)
    live = [r for r in candidates if r not in dead]
    dead = [r for r in candidates if r in dead]

    if len(live) == 1:
        return candidates[live[0]], dead, (f'{live[0]}/ is live; '
                                           f'{", ".join(dead)}/ marked dead in {src}')
    return None, dead, (f'cannot tell which of {sorted(candidates)} is live — {src} does not '
                        f'say. Refusing to guess: a gate that checks the wrong directory '
                        f'reports success over text nobody wrote.')


def dialogue_spans(text):
    """Both quote styles. Counting one of them invents violations in prose that
    uses the other, and this account uses both."""
    body = re.split(r'\n---\n\n## Footer|\n## Footer|\n## Production', text)[0]
    return (len(re.findall(r'"([^"\n]+)"', body))
            + len(re.findall(r'\u201c([^\u201d\n]+)\u201d', body)))


SENT_SPLIT = re.compile(r'(?<=[.!?])["\u2019\u201d\'\u2019]?\s+')

#: Where the author's text ends and the production record begins.
FOOTER_SPLIT = re.compile(r'\n---\n\n## Footer|\n## Footer|\n## Production')


def sentences(text):
    """Split prose into sentences. Handles a closing quote after the stop."""
    return [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]

def body_of(path):
    """The author's text only: the production block is a record, not prose."""
    return FOOTER_SPLIT.split(open(path, encoding='utf-8').read())[0]


def prose_sentences(path):
    """Prose sentences: no headings, no blockquote panels, no planning lines."""
    lines = [l for l in body_of(path).split('\n')
             if l.strip() and not re.match(r'#+\s', l)]
    prose = [l for l in lines if not l.startswith('>') and not PLAN_LINE_RX.search(l)]
    return [s for l in prose for s in sentences(l)]


def measure(path):
    body = body_of(path)
    lines = [l for l in body.split('\n') if l.strip() and not re.match(r'#+\s', l)]
    prose = [l for l in lines if not l.startswith('>') and not PLAN_LINE_RX.search(l)]
    words = len('\n'.join(lines).split())
    sent = [s for l in prose for s in sentences(l)]
    sl = [len(s.split()) for s in sent]
    return dict(name=os.path.basename(path), words=words, dlg=dialogue_spans(body),
                over=[(n, s) for n, s in zip(sl, sent) if n > 60],
                avg=statistics.mean(sl) if sl else 0.0)


EXEMPT_RX = re.compile(r'GATE EXEMPTION:\s*(dialogue-floor)\s*[\u2014\u2013:-]+\s*(.+)')


def find_exemption(project):
    """A project may be excused the dialogue floor, but only in writing.

    The house learned this the expensive way: soul_land_devouring_dragon has
    zero dialogue in its live chapters as LAW (RAILS s45: chapters with no
    panel carry no voices; CANON VOICE LAW s53), and a gate that reports law
    as defect is as wrong as a gate that misses a defect. So an exemption must
    be a sourced line — `GATE EXEMPTION: dialogue-floor — <reason>` — and the
    reason must cite a receipt file that exists inside the project. The
    exemption is then PRINTED on every run. An exemption nobody can check is
    a hole, and an invisible exemption is a silent pass wearing a receipt.
    """
    candidates = ['README.md', 'HANDOFF.md', 'STATUS.md', 'STATE.md', 'NEXT.md']
    foundation = os.path.join(project, 'foundation')
    if os.path.isdir(foundation):
        candidates += ['foundation/' + f for f in sorted(os.listdir(foundation)) if f.endswith('.md')]
    for rel in candidates:
        path = os.path.join(project, rel)
        if not os.path.isfile(path):
            continue
        for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
            m = EXEMPT_RX.search(line)
            if not m:
                continue
            reason = m.group(2).strip()
            cited = re.findall(r'[\w./-]+\.md', reason)
            missing = [c for c in cited if not os.path.isfile(os.path.join(project, c))]
            if not cited:
                return reason, f'{rel}:{i}', ['<none cited>']
            return reason, f'{rel}:{i}', missing
    return None


def gate_book(project, verbose=True):
    """Returns (problems, warnings, chapters_checked, chapters_expected, note)."""
    problems, warnings = [], []
    dirs = chapter_dirs(project)
    live, dead, note = choose_live(project, dirs)
    if live is None:
        return [f'SCOPE: {note}'], warnings, 0, 0, note

    exempt = find_exemption(project)
    if exempt and exempt[2]:
        problems.append(f'EXEMPTION does not cite a receipt that exists '
                        f'({exempt[1]} names {", ".join(exempt[2])}) — an exemption '
                        f'nobody can check is not an exemption')

    files = chapter_files(live)
    expected = len(files)
    if expected == 0:
        return [f'SCOPE: {live} holds no chapter files — a check that executes nothing '
                f'verifies nothing'], warnings, 0, 0, note

    if verbose:
        name = os.path.basename(os.path.abspath(project)) or project
        print(f"\n{name}   [{os.path.relpath(live, project)}]   {note}")
    for p in files:
        m = measure(p)
        per_k = m['dlg'] / m['words'] * 1000 if m['words'] else 0
        band = 'IN' if WORD_BAND[0] <= m['words'] <= WORD_BAND[1] else (
            'OVER' if m['words'] > WORD_BAND[1] else 'UNDER')
        if verbose:
            print(f"    {m['name'][:44]:44s} {m['words']:5d}w band:{band:5s} "
                  f"avg:{m['avg']:4.1f} dlg:{m['dlg']:3d} ({per_k:4.1f}/1k) over60:{len(m['over'])}")
        if m['dlg'] < DIALOGUE_FLOOR and not exempt:
            problems.append(f"{m['name']}: dialogue {m['dlg']} < floor {DIALOGUE_FLOOR}")
        if m['over']:
            problems.append(f"{m['name']}: {len(m['over'])} sentence(s) over 60 words")
        if not exempt and (m['dlg'] < DIALOGUE_FLOOR or per_k < DIALOGUE_BAR):
            warnings.append(f"{m['name']}: below the {DIALOGUE_BAR:.0f}/1k dialogue bar ({per_k:.1f}/1k)")
        if band != 'IN':
            warnings.append(f"{m['name']}: band:{band} ({m['words']}w)")
    for d in dead:
        warnings.append(f'dead directory not gated: {d}/')
    # a derived reader edition must match its author's text
    for derived in DERIVED:
        dd = os.path.join(project, derived)
        if os.path.isdir(dd):
            if len(chapter_files(dd)) != expected:
                problems.append(f'SCOPE: {derived}/ holds {len(chapter_files(dd))} chapters '
                                f'but the live text has {expected} — what ships is not what '
                                f'was gated')
    return problems, warnings, len(files), expected, note


def find_projects(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        if os.path.basename(dirpath).startswith('chapter') and chapter_files(dirpath):
            proj = os.path.dirname(dirpath)
            if proj not in out:
                out.append(proj)
    return sorted(out)


def selftest():
    """A gate that has only ever been seen to pass is a gate nobody tested."""
    import tempfile, shutil
    print('LIVE BOOK GATE — SELFTEST\n' + '=' * 64)
    ok = True
    tmp = tempfile.mkdtemp()

    def case(name, build, want_problem, want_warn=None):
        nonlocal ok
        root = os.path.join(tmp, name)
        shutil.rmtree(root, ignore_errors=True)
        build(root)
        p, w, n, e, _ = gate_book(root, verbose=False)
        got = bool(p)
        good = got == want_problem
        ok &= good
        print(f"  [{'ok ' if good else 'FAIL'}] {name}: "
              f"{'fails' if got else 'passes'}"
              + (f" — {p[0][:70]}" if p else ''))

    def mk(p, name, text):
        os.makedirs(p, exist_ok=True)
        open(os.path.join(p, name), 'w', encoding='utf-8').write(text)

    good_text = ('She came in. "Sit," she said. "Eat," he said. "Now," she said.\n'
                 'He counted the ruts in the road and said nothing more that day.')
    case('a chapter with speech passes',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md', good_text), False)
    case('a chapter with no speech fails',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
                      'He counted the ruts in the road and said nothing to anyone at all.\n'),
         True)
    case('curly quotes are counted',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
                      'She came in. \u201cSit,\u201d she said. \u201cEat,\u201d he said. \u201cNow,\u201d she said.\n'),
         False)
    case('a 70-word sentence fails',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
                      good_text + '\n' + ' '.join(['word'] * 70) + '.\n'), True)
    case('a sourced exemption is honoured',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
                      'He counted the ruts and said nothing to anyone at all.\n')
         or mk(os.path.join(r, 'foundation'), 'RAILS.md', 'law\n')
         or mk(r, 'README.md',
               'GATE EXEMPTION: dialogue-floor \u2014 no-voices law (foundation/RAILS.md)\n'),
         False)
    case('an exemption citing a receipt that does not exist fails',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
                      'He counted the ruts and said nothing to anyone at all.\n')
         or mk(r, 'README.md',
               'GATE EXEMPTION: dialogue-floor \u2014 no-voices law (foundation/NOWHERE.md)\n'),
         True)
    case('an exemption citing no receipt at all fails',
         lambda r: mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
                      'He counted the ruts and said nothing to anyone at all.\n')
         or mk(r, 'README.md', 'GATE EXEMPTION: dialogue-floor \u2014 trust me\n'),
         True)
    case('no chapter directory at all fails',
         lambda r: os.makedirs(os.path.join(r, 'foundation'), exist_ok=True), True)
    case('an empty chapter directory fails',
         lambda r: os.makedirs(os.path.join(r, 'chapters'), exist_ok=True), True)

    def two_dirs(r):
        mk(os.path.join(r, 'chapters'), 'Chapter_01.md',
           'He counted the ruts and said nothing at all to anyone ever.')
        mk(os.path.join(r, 'chapters_rebuilt'), 'Chapter_01.md', good_text)
        open(os.path.join(r, 'README.md'), 'w', encoding='utf-8').write(
            'The first draft (`chapters/`, 15 chapters) was rejected by the author as '
            '"nonsense" and fully rebuilt. The authoritative continuity is chapters_rebuilt/.')
    case('two directories, README names the dead one → gates the live one', two_dirs, False)

    def two_dirs_silent(r):
        mk(os.path.join(r, 'chapters'), 'Chapter_01.md', good_text)
        mk(os.path.join(r, 'chapters_rebuilt'), 'Chapter_01.md', good_text)
    case('two directories, no marker → refuses to guess', two_dirs_silent, True)

    def drift(r):
        mk(os.path.join(r, 'chapters'), 'Chapter_01.md', good_text)
        mk(os.path.join(r, 'manuscript'), 'Chapter_01.md', good_text)
        mk(os.path.join(r, 'manuscript'), 'Chapter_02.md', good_text)
    case('reader edition longer than the author edition fails (two copies)', drift, True)

    shutil.rmtree(tmp, ignore_errors=True)
    print('=' * 64)
    print('SELFTEST PASSED' if ok else 'SELFTEST FAILED — do not trust this gate')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()

    problems, warnings = [], []
    books = 0

    if '--all' in args:
        root = args[args.index('--root') + 1] if '--root' in args else os.getcwd()
        projects = find_projects(root)
        print(f'LIVE BOOK GATE — every book under {root}\n' + '=' * 64)
        live_books = 0
        for proj in projects:
            rel = os.path.relpath(proj, root)
            if is_out_of_scope(rel):
                warnings.append(f'out of scope, not gated: {rel}')
                continue
            live_books += 1
            p, w, n, e, note = gate_book(proj)
            books += 1
            problems += [f'[{rel}] {x}' for x in p]
            warnings += [f'[{rel}] {x}' for x in w]
        print('\n' + '=' * 64)
        print(f'COVERAGE: {books} live book(s) gated · '
              f'{len([w for w in warnings if w.startswith("out of scope")])} out-of-scope path(s) skipped ')
    else:
        path = next((a for a in args if not a.startswith('-')), None)
        if not path:
            print(__doc__)
            return 0
        print('LIVE BOOK GATE\n' + '=' * 64)
        p, w, n, e, note = gate_book(path)
        books = 1
        problems += p
        warnings += w
        print('\n' + '=' * 64)
        print(f'COVERAGE: {n} of {e} live chapter(s) checked under {path}')

    for x in warnings:
        print('WARN  ' + x)
    for x in problems:
        print('FAIL  ' + x)
    print('=' * 64)
    print(f'COVERAGE: {books} book(s) · {len(problems)} hard failure(s) · {len(warnings)} warning(s). '
          f'The band and the dialogue bar are the author\'s call; the floor, over60, '
          f'an empty scope and an ambiguous scope are not.')
    print('FAIL' if problems else 'ALL HARD CHECKS PASS')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())

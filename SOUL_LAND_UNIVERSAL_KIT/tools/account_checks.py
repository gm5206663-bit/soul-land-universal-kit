#!/usr/bin/env python3
"""Account checks — the detectors behind the control centre.

DOCTRINE
--------
One defect keeps appearing in this account in different clothes: *a check that
reports success while covering less than it claims.* Every detector here is
built to make that impossible, and the rules are always the same three:

  1. DECLARE COVERAGE.  Every detector returns ``coverage`` — how many things it
     looked at out of how many exist. A detector that examined nothing says so
     and raises a finding; it never returns a silent zero.
  2. CARRY EVIDENCE.  Every finding carries the exact text or numbers that
     produced it, so a reader can verify it without re-running anything. A
     finding you cannot check is a rumour.
  3. STABLE IDENTITY.  Every finding has an id derived from what it is about
     (kind + location + subject), never from a count or a line number, so runs
     can be diffed and progress measured instead of re-reported.

Severity is a judgement the house has already made: see ``LAWS``. HARD is not
the author's call — a sentence over the ceiling, a missing speaker, a text that
ships out of sync with its source. ADVISORY is the author's call and is reported
without being fatal: the word band, the dialogue bar, a refrain that may be
deliberate.

This module detects and reports. It never edits a manuscript.
"""

import hashlib
import os
import re
import subprocess
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_book_gate as lbg   # noqa: E402  — the house gate, single source of truth

# --------------------------------------------------------------------------
# THE LAWS — one table, cited, so no detector invents its own standard.
# --------------------------------------------------------------------------
LAWS = {
    'over60':          ('hard', 'a sentence over 60 words',
                        'the 60-word ceiling'),
    'dialogue-floor':  ('hard', 'dialogue under the floor of three spoken lines',
                        'the floor needs a speaker on the page'),
    'dialogue-exempt': ('advisory', 'dialogue floor exempt by a declared law',
                        'an exemption must cite a receipt that exists'),
    'scope-refusal':   ('hard', 'the live chapter directory could not be determined',
                        'a gate that checks the wrong directory reports success over text nobody wrote'),
    'source-orphan':   ('hard', 'published text with no author edition',
                        'what ships must be what was gated'),
    'copies-drift':    ('hard', 'the reader edition differs from the author edition',
                        'two copies of one text drift apart unless something compares them'),
    'repeat-in-file':  ('hard', 'the same sentence appears twice inside one chapter',
                        'an accidental duplicate is a defect, not a refrain'),
    'repeat-across':   ('advisory', 'the same sentence appears in more than one chapter',
                        'could be a deliberate refrain; the author decides'),
    'two-homes':       ('advisory', 'one text lives in more than one book or repo',
                        'one text, one home — copies age differently'),
    'receipt-drift':   ('advisory', 'a status file claims a different size than the book has',
                        'give a floor, not a pinned count'),
    'publish-drift':   ('hard', 'the published site holds a different number of chapters than the book',
                        'a build that produces nothing must not report success'),
    'coverage-gap':    ('advisory', 'a detector found more than it listed',
                        'a truncated list is a silent scope loss — say what was omitted'),
    'housekeeping':    ('advisory', 'a machine file or a frozen archive is committed in the repo',
                        'the repository is the artifact — bytecode, editor leftovers and old '
                        'snapshots are dead weight, and a snapshot carries a stale copy of the text'),
    'dead-link':       ('advisory', 'a link in a shipped document points at a file that is not there',
                        'broken navigation is a silent reader loss — a shipped view once carried '
                        '496 dead links'),
    'stale-generated': ('hard', 'a file stamped as generated does not match its source',
                        'a generated file that lies about its source is a copy drifting under a '
                        'receipt — the stamp says it can never have drifted'),
    'ci-gap':          ('advisory', 'a repository carries gate scripts but has no CI workflow',
                        'a gate that only runs when someone remembers is a promise, not a check'),
    'orphan-work':     ('advisory', 'a work with no other home was registered where it was found',
                        'a serial that exists in exactly one place is a book, wherever that '
                        'place is — a shelf, a reference tree, an inbox'),
    'sighting':        ('advisory', 'a chapter-bearing tree outside the register, classified and counted',
                        'exclusion from gating is not exclusion from the register — a tree that '
                        'is not gated still has to be named'),
    'unaccounted-tree': ('hard', 'a chapter-bearing tree the register cannot explain',
                        'coverage is a claim: every tree must be either a registered book or '
                        'a declared sighting, never simply unseen'),
}

VERSION = '1.0'


def law_of(kind):
    sev, detail, doctrine = LAWS.get(kind, ('advisory', kind, ''))
    return sev, detail, doctrine


def finding(kind, repo, book, file, subject, detail, evidence='', extra=None):
    """One finding. The id is about identity, never about size."""
    severity, _, doctrine = law_of(kind)
    fid = hashlib.sha1(f'{kind}|{repo}|{book}|{file}|{subject}'.encode('utf-8')).hexdigest()[:12]
    f = dict(id=fid, kind=kind, severity=severity, repo=repo, book=book, file=file,
             subject=subject, detail=detail, evidence=evidence[:400], law=doctrine)
    if extra:
        f.update(extra)
    return f


def coverage(checked, total, unit):
    return dict(checked=checked, total=total, unit=unit,
                text=f'{checked} of {total} {unit}')


def ran(detector, findings, cover, note=''):
    return dict(detector=detector, findings=findings, coverage=cover, note=note)


# --------------------------------------------------------------------------
# DISCOVERY
# --------------------------------------------------------------------------
def _chapter_trees(root):
    """EVERY directory holding chapter-numbered prose, in every repo, no exclusions.

    This walk is deliberately dumber than find_projects(): it does not care what
    a directory is called or what status files sit beside it. It answers one
    question — where on this disk is there chapter prose — and everything else in
    the register is built on its answer. The register's guarantee: every tree it
    returns is either a registered book or a classified sighting.
    """
    trees = []
    for repo in _repos(root):
        base = os.path.join(root, repo)
        for dp, dns, fns in os.walk(base):
            if '.git' in dp.split(os.sep):
                dns[:] = []
                continue
            dns[:] = [d for d in dns if d not in JUNK_DIRS]
            files = [os.path.join(dp, f) for f in sorted(fns)
                     if f.endswith('.md') and lbg.CHAPTER_RX.match(f)
                     and not lbg.NON_CHAPTER_RX.search(f)]
            if files:
                trees.append(dict(repo=repo, rel=os.path.relpath(dp, root), dir=dp, files=files,
                                  names={os.path.basename(f).lower()[:-3] for f in files}))
    return sorted(trees, key=lambda t: t['rel'])


def _prepare(books):
    """(book, names, words, file_count) for every registered book — read once."""
    out = []
    for b in books:
        fs = book_files(b)
        if not fs:
            continue
        names = {os.path.basename(f).lower()[:-3] for f in fs}
        words = sum(len(open(f, encoding='utf-8', errors='replace').read().split())
                    for f in fs)
        out.append((b, names, words, len(fs)))
    return out


def _words_of(t):
    w = 0
    for f in t['files']:
        try:
            w += len(open(f, encoding='utf-8', errors='replace').read().split())
        except OSError:
            pass
    return w


# Trees that hold chapters but are never a serial of their own: audit
# material, rebuild contracts, staging layers, snapshots, inboxes. They are
# still NAMED by the sightings pass — this rule only says "not a book".
NOT_A_BOOK_RX = re.compile(r'(^|/)(audits?|interventions?|contracts?|semantic_audit|'
                           r'late_arc_rebuild|rebuild_v2|staging|promotion_proposal|'
                           r'accepted_replacement_layers|snapshots?|sources|planning|notes|'
                           r'inbox|uploads?|backups?)(/|$)', re.I)

GENERIC_CH_RX = re.compile(r'^chapter[\s_-]*\d+$')


def _generic(names):
    """True when every chapter file is named 'Chapter_<n>' and nothing else.

    Generic names cannot identify a work. A 116-file tree of chapter_01.md…
    chapter_116.md matched an 8-file tree of the same shape perfectly — score
    1.0 — and was therefore classified as a COPY of an 8-chapter book. That is
    how a 572,000-word serial came within one line of staying invisible even
    after the shelf rule found it. Names that carry no title information are
    never allowed to prove identity on their own.
    """
    return bool(names) and all(GENERIC_CH_RX.match(n) for n in names)


def _match_book(t, prepared):
    """The registered book this tree duplicates, or None.

    Two ways to match, and the size gate guards the weak one:
      · titled chapter names agreeing at 90%+ — the titles are the fingerprint;
      · any name agreement when the two works are within 25% of the same size.
    Generic names on both sides always fall back to the size gate. `prepared`
    is built once per run; re-reading a 572,000-word serial for every candidate
    tree would cost more than the account it describes.
    """
    tw = None
    for b, names, bw, bf in prepared:
        inter = len(t['names'] & names)
        if inter < 3:
            continue
        sc = inter / min(len(t['names']), len(names))
        if sc < 0.6:
            continue
        strong = (sc >= 0.9 and not _generic(t['names']) and not _generic(names))
        if not strong:
            if tw is None:
                tw = _words_of(t)
            if not bw or abs(tw - bw) / bw > 0.25 or abs(len(t['files']) - bf) > 4:
                continue
        return b, sc
    return None


def _under(rel, root_or_dir, root):
    r = os.path.relpath(root_or_dir, root)
    return rel == r or rel.startswith(r + os.sep)


def registry(root):
    """Every book under root, with the live directory already chosen.

    A book is a directory that holds chapters and whose own status files say
    which directory is live. Anything the gate would refuse to guess about is
    returned as a refusal, not as a guess.

    Three additions since 2026-10-12, all one lesson — *a register that only
    lists what it happened to look at is a register of the looking*:

      · SHELF SERIALS. `chapters/<serial>/` is a book layout; the serial is a
        book when the shelf is its only home. When an identical copy exists
        elsewhere it is left to the sightings pass, so defects are counted once.
      · ORPHAN PROMOTION. A tree outside the normal scan — a reference copy —
        becomes a book when it is the only home of its text. Lin Hao / Soul
        Land 3 (101 ch) is a reference copy in an archived repository and had
        never been audited by anything.
      · NO SILENT SKIPS. Every chapter-bearing tree on the disk is either a
        book here or classified by check_sightings(); a tree that fits neither
        is a hard finding, not a shrug.
    """
    trees = {t['rel']: t for t in _chapter_trees(root)}
    direct, shelf = [], []
    for proj in lbg.find_projects(root):
        rel = os.path.relpath(proj, root)
        if lbg.is_out_of_scope(rel):
            continue
        parts = rel.split(os.sep)
        repo = parts[0]
        book = '/'.join(parts[1:]) or repo
        dirs = lbg.chapter_dirs(proj)
        live, dead, note = lbg.choose_live(proj, dirs)
        entry = dict(repo=repo, book=book, path=proj, live=live, dead=dead, note=note, rel=rel)
        if os.path.basename(os.path.dirname(proj)).startswith('chapter'):
            shelf.append(entry)
        else:
            direct.append(entry)

    books = list(direct)
    prepared = _prepare(books)
    for e in shelf:
        t = trees.get(e['rel'])
        if t is None:
            t = dict(repo=e['repo'], rel=e['rel'], dir=e['path'], files=[],
                     names={os.path.basename(f).lower()[:-3]
                            for f in lbg.chapter_files(e['path'])})
        if _match_book(t, prepared):
            continue            # a shelf copy of a registered book — a sighting
        e['promoted'] = True
        e['note'] = ('library shelf serial with no other home anywhere in the '
                     'account — ' + (e['note'] or 'registered from the shelf'))
        books.append(e)
        prepared.extend(_prepare([e]))

    for t in _chapter_trees(root):
        if any(_under(t['rel'], b['path'], root) for b in books):
            continue
        if any(b.get('live') and _under(t['rel'], b['live'], root) for b in books):
            continue
        if any(_under(t['rel'], d, root) for b in books for d in b['dead']):
            continue
        if lbg.DEAD_PATH_RX.search(t['rel']) or NOT_A_BOOK_RX.search(t['rel']):
            continue
        if _match_book(t, prepared):
            continue
        if len(t['files']) < 5:
            continue
        if '/reference/' in t['rel']:
            note = ('reference copy with no other home anywhere in the account — '
                    'registered read-only, so it is audited at all')
        else:
            note = ('found outside the register and is the only home of its text — '
                    'registered so it can be audited at all')
        books.append(dict(repo=t['repo'], book='/'.join(t['rel'].split(os.sep)[1:]) or t['repo'],
                          path=t['dir'], live=t['dir'], dead=[], note=note,
                          readonly=True, promoted=True, rel=t['rel']))
    return books

def book_files(book):
    if not book['live']:
        return []
    return lbg.chapter_files(book['live'])


def chapter_number(path):
    m = re.match(r'chapter[\s_-]*(\d+)', os.path.basename(path), re.I)
    return int(m.group(1)) if m else None


# --------------------------------------------------------------------------
# 1. THE GATE — the per-file laws, with evidence
# --------------------------------------------------------------------------
def check_gate(books, law_path=None):
    findings, checked, total = [], 0, 0
    facts = []
    for b in books:
        total += 1
        exempt = lbg.find_exemption(b['path'])
        if b['live'] is None:
            findings.append(finding('scope-refusal', b['repo'], b['book'], '-',
                                    b['book'], f'cannot tell which directory is live: {b["note"]}',
                                    evidence=b['note']))
            continue
        checked += 1
        files = book_files(b)
        for p in files:
            m = lbg.measure(p)
            per_k = m['dlg'] / m['words'] * 1000 if m['words'] else 0
            band = 'IN' if lbg.WORD_BAND[0] <= m['words'] <= lbg.WORD_BAND[1] else (
                'OVER' if m['words'] > lbg.WORD_BAND[1] else 'UNDER')
            facts.append(dict(repo=b['repo'], book=b['book'], file=m['name'], words=m['words'],
                              dlg=m['dlg'], per_k=round(per_k, 1), band=band,
                              over60=len(m['over']), avg=round(m['avg'], 1),
                              exempt=bool(exempt)))
            if m['dlg'] < lbg.DIALOGUE_FLOOR and not exempt:
                findings.append(finding('dialogue-floor', b['repo'], b['book'], m['name'],
                                        'dialogue',
                                        f"dialogue {m['dlg']} < floor {lbg.DIALOGUE_FLOOR} "
                                        f"(in {m['words']} words)",
                                        evidence=f'{m["dlg"]} spoken lines found in the whole chapter'))
            # Two identical long sentences in one file are two findings with one
            # identity unless the occurrence is part of the id. Five pairs
            # collapsed when a baseline was frozen — and a collapsed finding can
            # never be reported as fixed, because it was never separately known.
            seen_sent = {}
            for n, s in m['over']:
                _key = re.sub(r'\W+', '', s.lower())
                seen_sent[_key] = seen_sent.get(_key, 0) + 1
                findings.append(finding('over60', b['repo'], b['book'], m['name'],
                                        # identity = the WHOLE sentence, so the id survives an
                                        # edit elsewhere in the file. It was the first 80
                                        # characters, which made two long sentences that begin
                                        # alike share an id — 18 findings collapsed into 18
                                        # others when a baseline was frozen, and would have
                                        # been invisible to every future diff.
                                        hashlib.sha1(_key.encode()).hexdigest()[:10]
                                        + f'-{seen_sent[_key]}',
                                        f'{n}-word sentence (ceiling 60)',
                                        evidence=s.strip()))
        if exempt:
            findings.append(finding('dialogue-exempt', b['repo'], b['book'], '-',
                                    b['book'], f'floor exempt: {exempt[0][:120]}',
                                    evidence=f'declared at {exempt[1]}'))
        # the reader edition must be the gated text, by name and by content
        for derived in lbg.DERIVED:
            dd = os.path.join(b['path'], derived)
            if not os.path.isdir(dd):
                continue
            want = {os.path.basename(x) for x in files}
            have = {os.path.basename(x) for x in lbg.chapter_files(dd)}
            for name in sorted(have - want):
                findings.append(finding('source-orphan', b['repo'], b['book'],
                                        f'{derived}/{name}', name,
                                        f'{derived}/{name} ships with no author edition',
                                        evidence=f'{derived}/ holds a chapter that chapters/ does not'))
            for name in sorted(want - have):
                findings.append(finding('source-orphan', b['repo'], b['book'],
                                        f'{derived}/{name}', name,
                                        f'the author edition {name} never reached {derived}/',
                                        evidence=f'chapters/ holds a chapter that {derived}/ does not'))
            # body drift: same names, different words
            for name in sorted(want & have):
                a = lbg.prose_sentences(os.path.join(b['live'], name))
                r = lbg.prose_sentences(os.path.join(dd, name))
                if a == r:
                    continue
                extra_r = [s for s in r if s not in a]
                extra_a = [s for s in a if s not in r]
                findings.append(finding('copies-drift', b['repo'], b['book'],
                                        f'{derived}/{name}', name,
                                        f'{len(extra_a)} sentence(s) only in the author edition, '
                                        f'{len(extra_r)} only in {derived}/',
                                        evidence=(extra_a[:1] or extra_r[:1] or [''])[0][:300]))
    out = ran('gate', findings, coverage(checked, total, 'book(s) with a determined live directory'),
              note='the gate laws: 60-word ceiling, three spoken lines, parity of both copies')
    out['facts'] = facts
    return out


# --------------------------------------------------------------------------
# 2. REPEATED PROSE — the refrain, and the accident
# --------------------------------------------------------------------------
def normalise(s):
    return re.sub(r'\W+', ' ', s.lower()).strip()


def check_dupes(books, min_words=12, limit=400):
    findings, sentences, checked = [], 0, 0
    index = {}
    seen = 0
    for b in books:
        if b['live'] is None:
            continue
        checked += 1
        for p in book_files(b):
            for s in lbg.prose_sentences(p):
                seen += 1
                if len(s.split()) < min_words:
                    continue
                sentences += 1
                index.setdefault(normalise(s), []).append((b, os.path.basename(p), s.strip()))
    # A published snapshot is a derived copy, not a second home — the rule
    # two-homes learned the hard way. If the source carries the sentence, the
    # copy carrying it too is the snapshot doing its job, not a duplicate: this
    # detector was reporting every shared sentence between a book and its own
    # published copy (61 of 66 NEW findings in one run were exactly that).
    # If ONLY a copy carries the sentence, that is drift and it stays a finding.
    # Whatever is ignored is declared in the note, never silently dropped.
    at_source = {k for k, hits in index.items()
                 if any(not is_published_copy(b['book']) for b, _, _ in hits)}
    skipped_copies = 0
    for k in list(index):
        if k not in at_source:
            continue
        keep = [h for h in index[k] if not is_published_copy(h[0]['book'])]
        skipped_copies += len(index[k]) - len(keep)
        index[k] = keep
    clusters = {k: v for k, v in index.items() if len(v) > 1}
    # Deterministic order AND no silent truncation. Sorting only by size left
    # ties in os.walk order, so two runs over the same tree reported 874 and
    # 860 findings — the tool was non-comparable with itself, and the missing
    # ones looked fixed. The sentence text breaks ties; the note says how many
    # were found and how many are listed.
    ranked = sorted(clusters.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    def classify(hits):
        per = {}
        for b, name, text in hits:
            per.setdefault((b['repo'], b['book'], name), []).append(text)
        return per

    # Hard findings get their own budget. A duplicate inside one file is a
    # defect; a refrain across chapters is the author's call. Letting the
    # advisory class compete for listing slots with the hard one meant a defect
    # could be pushed out of the report by a stylistic note — truncation must
    # never hide a hard finding.
    hard = [(k, h) for k, h in ranked if any(len(v) > 1 for v in classify(h).values())]
    soft = [(k, h) for k, h in ranked if not any(len(v) > 1 for v in classify(h).values())]
    ranked = hard + soft[:max(0, limit - len(hard))]
    for key, hits in ranked:
        # the same file twice is an accident; two chapters is possibly a refrain
        per_file = {}
        for b, name, text in hits:
            per_file.setdefault((b['repo'], b['book'], name), []).append((b, text))
        kind = 'repeat-in-file' if any(len(v) > 1 for v in per_file.values()) else 'repeat-across'
        where = '; '.join(f'{k[0]}/{k[2]}' if k[0] == k[1] else f'{k[0]}/{k[1]}/{k[2]}'
                          for k in sorted(per_file))
        first = hits[0][0]
        findings.append(finding(kind, first['repo'], first['book'],
                                sorted(per_file)[0][2],
                                hashlib.sha1(key.encode()).hexdigest()[:10],
                                f'{len(hits)} identical {len(hits[0][2].split())}-word sentence(s) '
                                f'across {len(per_file)} place(s): {where[:200]}',
                                evidence=hits[0][2],
                                extra=dict(occurrences=[dict(repo=r, book=b, file=n) for r, b, n in
                                                        sorted(per_file) for _ in per_file[(r, b, n)]])))
    out = ran('dupes', findings,
              coverage(sentences, seen, f'prose sentence(s) indexed ({min_words}+ words) '
                                        f'of all prose sentences, across {checked} book(s)'),
              note=(f'{len(clusters)} repeated sentence(s) of {min_words}+ words found; '
                    f'sentences under {min_words} words are not candidates'
                    + (f'; the {limit} largest by occurrence are listed'
                       if len(clusters) > limit else '')
                    + (f'; {skipped_copies} published-copy occurrence(s) ignored because '
                       f'their source carries the sentence' if skipped_copies else '')))
    listed = len(hard) + len(soft[:max(0, limit - len(hard))])
    if listed < len(clusters):                     # never a silent truncation
        out['truncated'] = dict(listed=listed, found=len(clusters))
        out['findings'].append(finding(
            'coverage-gap', '-', '-', 'dupes', 'dupes',
            f'dupes found {len(clusters)} repeated sentence(s) and listed {listed} '
            f'({len(hard)} hard duplicates, then the most-repeated refrains) — the rest are '
            f'not in this report',
            evidence=f'raise --dupes-limit to see all {len(clusters)}'))
    return out


# --------------------------------------------------------------------------
# 3. TWO HOME TEXTS — is the same text living in two places?
# --------------------------------------------------------------------------
def is_published_copy(book):
    """A published snapshot path is a derived copy, not a second home."""
    return bool(re.search(r'(^|/)(published-site|published|site|docs|soul-library/chapters)(/|$)', book))


def check_two_homes(books):
    findings = []
    index = {}
    files = 0
    for b in books:
        if b['live'] is None:
            continue
        for p in book_files(b):
            files += 1
            body = lbg.body_of(p)
            h = hashlib.sha1(re.sub(r'\s+', ' ', body).strip().encode('utf-8')).hexdigest()[:12]
            index.setdefault(h, []).append((b, os.path.basename(p)))
    derived = 0
    for h, hits in index.items():
        homes = {(b['repo'], b['book']) for b, _ in hits}
        if len(homes) < 2:
            continue
        # A book and its own published copy are ONE home: the publish step is
        # meant to copy the text. Only two independent books sharing a text is
        # a finding.
        independent = {x for x in homes if not is_published_copy(x[1])}
        if len(independent) < 2:
            derived += len(homes) - len(independent)
            continue
        first = sorted(independent)[0]
        findings.append(finding('two-homes', first[0], first[1], '-', h,
                                f'identical text in {len(homes)} books: '
                                + '; '.join(f'{r}/{b}' for r, b in sorted(homes))[:200],
                                evidence=f'sha {h} — {sorted(n for _, n in hits)[0]}',
                                extra=dict(homes=[dict(repo=r, book=b) for r, b in sorted(homes)])))
    return ran('two-homes', findings,
               coverage(files, files, 'chapter file(s) hashed'),
               note=f'{len(findings)} text(s) shared by two independent books; '
                    f'{derived} twin group(s) are a book and its own published copy, '
                    f'which is what publishing does')


# --------------------------------------------------------------------------
# 4. RECEIPTS — does the book's own paperwork agree with the book?
# --------------------------------------------------------------------------
#: A number only counts as a claim about THIS serial's size when the line is a
#: status sentence about it. "Chapters 1–3 sit over the band" names a subset,
#: and "all 24 chapters live" was about a different book entirely — both were
#: reported as drift before this guard, and both were the detector's mistake.
STATUS_WORDS_RX = re.compile(
    r'live edge|shipped through|\bupdated\b|\bcurrent edge\b|'
    r'\bserial\b|\bthe book\b|\bthis book\b', re.I)

CLAIM_RES = [
    # "chapters 1-10", "chapters 1–6"
    (re.compile(r'chapters?\s+1\s*[–\-—]\s*(\d+)', re.I), 'range'),
    # "live edge Ch24", "shipped chapter 10"
    (re.compile(r'(?:live|shipped|current)\s+(?:edge|chapter)s?[^\d\n]{0,24}(\d+)', re.I), 'edge'),
    # "10 chapters live|written|published|done" — the number must not be the
    # tail of another word ("V2 chapters" is not a count of two chapters)
    (re.compile(r'(?<![\w])(\d+)\s+chapters?\s+(?:live|written|published|done|complete)', re.I),
     'count'),
]
STATUS_FILES = ('README.md', 'HANDOFF.md', 'STATUS.md', 'STATE.md', 'NEXT.md', 'SERIAL_LOG.md',
                'CHANGELOG.md', 'index.html')

#: A line that is talking about history, a plan, or an archived copy is not
#: claiming what the live book is now. Without this guard the detector reported
#: "README says 15, the book has 6" for a line that reads "V1 ARCHIVED (15
#: chapters, pre-rebuild, kept for reference)" — a true statement about a
#: different body of text, counted as a defect. Four findings, four false.
HISTORY_RX = re.compile(
    r'archive|archived|replaced|superseded|pre-?rebuild|former|previous|earlier|'
    r'\bV[12]\b|old\b|history|kept for reference|not moved|remained|was\b|were\b|'
    r'planned|target|goal|roadmap|remaining|outline|todo|will |next arc|draft',
    re.I)


def check_receipts(books):
    findings, checked, total = [], 0, 0
    for b in books:
        if b['live'] is None:
            continue
        total += 1
        files = book_files(b)
        actual_max = max([n for n in (chapter_number(p) for p in files) if n] or [0])
        actual_count = len(files)
        if not actual_max:
            continue
        checked += 1
        for rel in STATUS_FILES:
            path = os.path.join(b['path'], rel)
            if not os.path.isfile(path):
                continue
            for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
                if len(line) > 400 or line.strip().startswith(('|', '>')):
                    continue
                if HISTORY_RX.search(line):
                    continue
                for rx, how in CLAIM_RES:
                    m = rx.search(line)
                    if not m:
                        continue
                    if how != 'edge' and not STATUS_WORDS_RX.search(line):
                        continue           # not a statement about this serial's size
                    said = int(m.group(1))
                    truth = actual_max if how in ('range', 'edge') else actual_count
                    if said == truth:
                        continue
                    # a floor ("220+") is deliberately not a pin and never drifts
                    if '+' in line[max(0, m.start() - 1):m.end() + 1]:
                        continue
                    findings.append(finding('receipt-drift', b['repo'], b['book'], f'{rel}:{i}',
                                            f'{how}:{said}',
                                            f'{rel} says {said}, the book has {truth} '
                                            f'({"chapters" if how == "count" else "as its last chapter"})',
                                            evidence=line.strip()))
    return ran('receipts', findings, coverage(checked, total, 'book(s) with a chapter numbering'),
               note='claims in README/HANDOFF/STATUS/CHANGELOG against the text on disk')


# --------------------------------------------------------------------------
# 5. PUBLICATION — does what ships match what was written?
# --------------------------------------------------------------------------
PUB_RX = re.compile(r'(chapter|ch)[\s_-]*(\d+)', re.I)


def check_publication(books):
    findings, checked, total = [], 0, 0
    for b in books:
        if b['live'] is None:
            continue
        for site in ('docs', 'published-site', 'site', 'website'):
            d = os.path.join(b['path'], site)
            if not os.path.isdir(d):
                continue
            total += 1
            published = [os.path.join(dp, f) for dp, _, fs in os.walk(d) for f in fs
                         if f.lower().endswith(('.html', '.md')) and PUB_RX.search(f)
                         and not lbg.NON_CHAPTER_RX.search(f)]
            have = {n for n in (chapter_number(p) for p in published) if n}
            want = {n for n in (chapter_number(p) for p in book_files(b)) if n}
            checked += 1
            if have != want:
                missing = sorted(want - have)
                extra = sorted(have - want)
                findings.append(finding('publish-drift', b['repo'], b['book'], site, site,
                                        f'{site}/ publishes {len(have)} chapter(s), the book has '
                                        f'{len(want)}'
                                        + (f'; missing {missing[:8]}' if missing else '')
                                        + (f'; published but not in the book {extra[:8]}' if extra else ''),
                                        evidence=f'{site}/ files: {len(published)} chapter-named file(s)'))
    return ran('publication', findings, coverage(checked, total, 'book(s) with a published site'),
               note='in-tree chapter html against the source; the LIVE site is the pages detector')


PAGES_LINK_RX = re.compile(r'href="[^"]*?(?:chapter|ch)[\s_-]*(\d+)', re.I)


def check_pages(books, owner, token=None, timeout=25):
    """Does the LIVE published site match the book?

    Every other publication check reads files in the repository. This one asks
    the thing itself — the Pages URL — because a repository can hold a perfect
    site that was never deployed, and a site can be older than the text. Which
    is the storyos defect: a stage built 0 of 52 chapters and reported success.

    A repo whose Pages site is not up is reported as a coverage gap, not as a
    pass: "I could not look" is not "it is fine".
    """
    import json as _json
    import urllib.request
    findings, checked, total, compared, uncompared = [], 0, 0, 0, []
    by_repo = {}
    for b in books:
        by_repo.setdefault(b['repo'], []).append(b)
    for repo, rbooks in sorted(by_repo.items()):
        total += 1
        api = f'https://api.github.com/repos/{owner}/{repo}/pages'
        req = urllib.request.Request(api, headers={'Accept': 'application/vnd.github+json'})
        if token:
            req.add_header('Authorization', f'token {token}')
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                info = _json.load(r)
        except Exception as e:                       # 404 = no site, anything else = unknown
            code = getattr(e, 'code', None)
            if code == 404:
                continue
            findings.append(finding('publish-drift', repo, '-', 'pages', repo,
                                    f'could not determine the published state: HTTP {code or e}',
                                    evidence=api))
            continue
        # The Pages API reports `url` = the API endpoint itself and `html_url` =
        # the site. Reading `url` made this detector fetch the API as if it were
        # the website, 404 on a private repo, and report three drift findings
        # that were entirely its own mistake.
        url = info.get('html_url') or info.get('url')
        if not url:
            continue
        checked += 1
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                page = r.read().decode('utf-8', 'replace')
        except Exception as e:
            findings.append(finding('publish-drift', repo, '-', 'pages', repo,
                                    f'the published site did not answer: {e}', evidence=url))
            continue
        live_nums = {int(n) for n in PAGES_LINK_RX.findall(page)}
        if len(rbooks) != 1:
            uncompared.append(repo)
            continue
        b = rbooks[0]
        want = {n for n in (chapter_number(p) for p in book_files(b)) if n}
        compared += 1
        if live_nums and live_nums != want:
            missing = sorted(want - live_nums)
            findings.append(finding('publish-drift', repo, b['book'], url, 'site',
                                    f'the live site offers {len(live_nums)} chapter link(s), '
                                    f'the book has {len(want)}'
                                    + (f'; not reachable from the index: {missing[:8]}' if missing else ''),
                                    evidence=url))
        elif not live_nums:
            findings.append(finding('publish-drift', repo, b['book'], url, 'site',
                                    'the live site answered but offers no chapter link at all',
                                    evidence=url[:200]))
    note = (f'{compared} site(s) compared to a book'
            + (f'; {len(uncompared)} left uncompared (repo holds several books): '
               + ', '.join(uncompared[:4]) if uncompared else ''))
    return ran('pages', findings, coverage(checked, total, 'repositor(ies) with a published site'),
               note=note)


ALL = ('gate', 'dupes', 'two-homes', 'receipts', 'publication', 'pages')


# --------------------------------------------------------------------------
# 7. HOUSEKEEPING — machine files and frozen archives inside the repositories
# --------------------------------------------------------------------------
JUNK_DIRS = ('__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache',
             '.ipynb_checkpoints')
JUNK_FILES = ('.DS_Store', 'Thumbs.db')
JUNK_SUFFIX = ('.pyc', '.pyo', '.bak', '.orig', '.rej', '.save', '~')
ARCHIVE_SUFFIX = ('.zip', '.tar.gz', '.tgz', '.tar', '.7z', '.rar')


def _tracked(base):
    """The relative paths git tracks in a repo, or None when git cannot answer."""
    try:
        r = subprocess.run(['git', '-C', base, 'ls-files', '-z'],
                           capture_output=True, timeout=30)
        if r.returncode == 0:
            return {p for p in r.stdout.decode('utf-8', 'replace').split('\0') if p}
    except Exception:                              # git absent, timeout, not a repo
        pass
    return None


def check_housekeeping(root, limit=40):
    """Machine files and archives committed in the repositories under root.

    This is not a prose law — it is the opposite end of the same doctrine. Every
    repository here is read, cloned and re-cloned; a committed .pyc is compiled
    output of a source that is present, a .bak is a superseded hand copy, and an
    archive is a frozen snapshot that carries a stale copy of prose the repo
    already versions properly. Each is advisory: keeping an archive can be a
    deliberate act, so the finding asks the author to say so rather than
    presuming it. What the detector will not do is stay quiet: two such files
    were found on this account's own tree (a .pyc next to its source, a .bak
    next to its live state) and both were removed on 2026-10-11.

    Coverage here is repositories walked, files scanned and hits found — a walk
    that saw nothing says so instead of returning a silent zero.
    """
    repos = sorted(d for d in (os.listdir(root) if os.path.isdir(root) else [])
                   if os.path.isdir(os.path.join(root, d, '.git')))
    hits, files, unverifiable = [], 0, 0
    for repo in repos:
        base = os.path.join(root, repo)
        # WHAT GIT HAS, not what is on disk. Running these tools inside a clone
        # creates __pycache__ that was never committed — the first draft of this
        # detector reported its own author's working files as housekeeping. A
        # file only counts once git tracks it; if git cannot answer, everything
        # on disk there is listed and the note says that is what happened.
        tracked = _tracked(base)
        if tracked is None:
            unverifiable += 1
        for dp, dns, fns in os.walk(base):
            if '.git' in dp.split(os.sep):
                dns[:] = []
                continue
            files += len(fns)
            for name in sorted(dns):
                if name in JUNK_DIRS:
                    rel = os.path.relpath(os.path.join(dp, name), base)
                    if tracked is None or any(t.startswith(rel + '/') for t in tracked):
                        hits.append((repo, os.path.join(dp, name), name, None))
                    dns.remove(name)
            for name in sorted(fns):
                low = name.lower()
                if name in JUNK_FILES or low.endswith(JUNK_SUFFIX) or low.endswith(ARCHIVE_SUFFIX):
                    p = os.path.join(dp, name)
                    rel = os.path.relpath(p, base)
                    if tracked is not None and rel not in tracked:
                        continue
                    size = None
                    if low.endswith(ARCHIVE_SUFFIX):
                        try:
                            size = os.path.getsize(p)
                        except OSError:
                            size = None
                    hits.append((repo, p, name, size))

    findings = []
    for repo, p, name, size in hits[:limit]:
        rel = os.path.relpath(p, root)
        if size is not None:
            detail = (f'archive {name} ({size / 1048576:.2f} MB) is committed — a frozen '
                      f'snapshot inside a repository that already keeps history; if it is '
                      f'meant to be kept, say so')
        elif os.path.isdir(p):
            detail = (f'{name}/ is a machine directory — regenerable from the source '
                      f'beside it, and it re-clones for every reader')
        else:
            detail = (f'{name} is a machine file — compiled or editor output, not prose '
                      f'and not a source of truth')
        findings.append(finding('housekeeping', repo, '-', rel, rel, detail,
                                evidence=rel))
    if len(hits) > limit:                       # never a silent truncation
        findings.append(finding('coverage-gap', '-', '-', 'housekeeping', 'housekeeping',
                                f'housekeeping found {len(hits)} machine file(s) and listed '
                                f'{limit} — the rest are not in this report',
                                evidence=f'raise the limit to see all {len(hits)}'))
    note = (f'{files} file(s) scanned across {len(repos)} repo(s); {len(hits)} machine '
            f'file(s) or archive(s) found' + (f'; {limit} listed' if len(hits) > limit else ''))
    if unverifiable:                            # the fallback is declared, never silent
        note += (f'; git could not be asked in {unverifiable} repo(s), so anything found '
                 f'on disk there is listed unproven')
    return ran('housekeeping', findings,
               coverage(len(repos), len(repos),
                        'repository(ies) walked for machine files and archives'),
               note=note)


# --------------------------------------------------------------------------
# 8. SHARED WALK — git's answer when it can, the disk when it cannot
# --------------------------------------------------------------------------
def _files_repo(base, suffixes=None):
    """(relative paths, mode). mode is 'git' or 'disk' — and 'disk' is declared."""
    tr = _tracked(base)
    if tr is not None:
        out = [p for p in tr if suffixes is None or p.lower().endswith(suffixes)]
        return sorted(out), 'git'
    out = []
    for dp, dns, fns in os.walk(base):
        if '.git' in dp.split(os.sep):
            dns[:] = []
            continue
        dns[:] = [d for d in dns if d not in JUNK_DIRS]
        for f in fns:
            if suffixes is None or f.lower().endswith(suffixes):
                out.append(os.path.relpath(os.path.join(dp, f), base))
    return sorted(out), 'disk'


def _repos(root):
    return sorted(d for d in (os.listdir(root) if os.path.isdir(root) else [])
                  if os.path.isdir(os.path.join(root, d, '.git')))


# --------------------------------------------------------------------------
# 9. DEAD LINKS — navigation in shipped documents
# --------------------------------------------------------------------------
LINK_RX = re.compile(r'\]\(([^)\s]+)\)|(?:href|src)="([^"]+)"')
SCHEME_RX = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*:')
FENCE_RX = re.compile(r'```.*?```|~~~.*?~~~', re.S)
INLINE_RX = re.compile(r'`[^`\n]+`')
SCRIPT_RX = re.compile(r'<script.*?</script>|<style.*?</style>', re.S | re.I)
PLACEHOLDER = {'url', 'link', 'here', 'path', 'target', 'text', 'id', 'name',
               'href', 'src', 'file', 'filename', 'your-file', 'x', 'example'}


def check_links(root, limit=80, max_size=524288):
    """Relative links in tracked .md/.html files whose target does not exist.

    Only relative targets are judged. Anything with a scheme is somebody else's
    problem to host; anchors (`#x`) are in-page; templates (`{name}`) are not
    paths yet. Fenced code blocks are stripped first — an example path inside a
    fence is documentation of a path, not a link to one. Targets that resolve
    outside the repository are counted as unverifiable, not guessed about.
    """
    findings, files, links, dead, unverifiable, too_big, modes = [], 0, 0, 0, 0, 0, set()
    for repo in _repos(root):
        base = os.path.join(root, repo)
        paths, mode = _files_repo(base, suffixes=('.md', '.html'))
        modes.add(mode)
        for rel in paths:
            p = os.path.join(base, rel)
            try:
                if os.path.getsize(p) > max_size:
                    too_big += 1
                    continue
                text = open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            # Fences, inline code and script blocks are not navigation: a path
            # inside them is documentation of a path. The first run of this
            # detector flagged `Always cite with [id](url)` (prose instruction)
            # and caught a JavaScript regex through an html href="$2" — both
            # removed here rather than explained away later.
            if rel.lower().endswith('.md'):
                text = INLINE_RX.sub('', FENCE_RX.sub('', text))
            else:
                text = SCRIPT_RX.sub('', text)
            files += 1
            here = os.path.dirname(p)
            seen = set()
            for m in LINK_RX.finditer(text):
                tgt = (m.group(1) or m.group(2) or '').strip()
                if not tgt or tgt.startswith('#') or SCHEME_RX.match(tgt):
                    continue
                if any(c in tgt for c in '{}<>|`'):
                    continue
                if tgt.lower() in PLACEHOLDER:
                    continue
                tgt = tgt.split('#', 1)[0].split('?', 1)[0]
                tgt = urllib.parse.unquote(tgt).strip()
                if not tgt:
                    continue
                if (rel, tgt) in seen:
                    continue
                seen.add((rel, tgt))
                links += 1
                resolved = os.path.normpath(os.path.join(here, tgt))
                if not resolved.startswith(base + os.sep) and resolved != base:
                    unverifiable += 1
                    continue
                if not os.path.exists(resolved):
                    dead += 1
                    target_rel = os.path.relpath(resolved, base)
                    if len(findings) < limit:
                        findings.append(finding(
                            'dead-link', repo, '-', rel, f'{rel}->{target_rel}',
                            f'{rel} links to {target_rel}, which is not in the repository',
                            evidence=tgt))
    if dead > len(findings):
        findings.append(finding('coverage-gap', '-', '-', 'links', 'links',
                                f'links found {dead} dead target(s) and listed {len(findings)} '
                                f'— the rest are not in this report',
                                evidence=f'raise --links-limit to see all {dead}'))
    note = (f'{files} file(s) scanned, {links} relative link(s) checked, {dead} dead'
            + (f'; {unverifiable} target(s) outside the repository not guessed about'
               if unverifiable else '')
            + (f'; {too_big} file(s) over {max_size // 1024} KB skipped' if too_big else '')
            + (f'; git could not be asked, the disk was walked instead' if 'disk' in modes else ''))
    return ran('links', findings, coverage(files, files, 'document(s) scanned for links'),
               note=note)


# --------------------------------------------------------------------------
# 10. STALE GENERATED — the stamp claims a source; check the claim
# --------------------------------------------------------------------------
STAMP_RX = re.compile(r'GENERATED from\s+([^\s;]+)\s*;\s*SHA256:\s*([0-9a-f]{64})')


def check_generated(root, limit=40):
    """Files that stamp themselves as generated from a source, verified.

    The stamp format is the one the account's renderers write:
    `GENERATED from <path>; SHA256: <sha256-of-source>`. The detector reads the
    source, hashes it, and compares. A mismatch means the view is not the output
    of the file it names — it drifted, or it was hand-edited, and either way the
    stamp is now a claim that is not true. Hard, because nobody reading the view
    can tell without doing exactly this.
    """
    findings, stamped, verified, modes = [], 0, 0, set()
    for repo in _repos(root):
        base = os.path.join(root, repo)
        paths, mode = _files_repo(base)
        modes.add(mode)
        for rel in paths:
            p = os.path.join(base, rel)
            try:
                if os.path.getsize(p) > 1048576:
                    continue
                head = open(p, encoding='utf-8', errors='replace').read(2048)
            except OSError:
                continue
            m = STAMP_RX.search(head)
            if not m:
                continue
            stamped += 1
            src_rel, want = m.group(1), m.group(2).lower()
            src = os.path.normpath(os.path.join(base, src_rel))
            if not src.startswith(base + os.sep) or not os.path.isfile(src):
                if len(findings) < limit:
                    findings.append(finding(
                        'stale-generated', repo, '-', rel, rel,
                        f'{rel} says it was generated from {src_rel}, which is not in '
                        f'the repository — the source of this view cannot be checked',
                        evidence=src_rel))
                continue
            got = hashlib.sha256(open(src, 'rb').read()).hexdigest()
            verified += 1
            if got != want:
                if len(findings) < limit:
                    findings.append(finding(
                        'stale-generated', repo, '-', rel, rel,
                        f'{rel} stamps itself as generated from {src_rel} but that file '
                        f'hashes {got[:12]}…, not the stamped {want[:12]}… — the view has '
                        f'drifted or was edited after generation',
                        evidence=f'{src_rel} sha256 {got} != stamped {want}'))
    if stamped > len(findings) and len(findings) == limit:
        findings.append(finding('coverage-gap', '-', '-', 'generated', 'generated',
                                f'generated views: {stamped} stamped, {len(findings)} listed — '
                                f'the rest are not in this report', evidence='raise the limit'))
    note = (f'{stamped} stamped file(s) found, {verified} verified against its source'
            + (f'; git could not be asked, the disk was walked instead' if 'disk' in modes else ''))
    return ran('generated', findings,
               coverage(stamped, stamped, 'stamped file(s) checked against their source'),
               note=note)


# --------------------------------------------------------------------------
# 11. ENFORCEMENT — does anything run the gates?
# --------------------------------------------------------------------------
GATE_NAME_RX = re.compile(r'(gate|verify|sentinel|lint|check|selftest)', re.I)


def check_enforcement(root, limit=40):
    """Repositories carrying gate scripts, and whether a workflow file exists.

    This is deliberately modest about what it proves: it reports the PRESENCE of
    gate-shaped scripts and the PRESENCE of a workflow file. It does not claim
    the workflow runs the gate, and the detail line says so. A repo with gates
    and no workflow is where the account's enforcement is thinnest, and the
    finding asks for it to be either armed or declared.
    """
    findings, with_gates, with_ci, gap = [], 0, 0, 0
    for repo in _repos(root):
        base = os.path.join(root, repo)
        scripts = []
        for sub in ('tools', 'framework/scripts', 'scripts', 'checks'):
            d = os.path.join(base, sub)
            if os.path.isdir(d):
                scripts += [f'{sub}/{f}' for f in sorted(os.listdir(d))
                            if f.endswith('.py') and GATE_NAME_RX.search(f)]
        wf = os.path.join(base, '.github', 'workflows')
        has_ci = os.path.isdir(wf) and any(f.endswith(('.yml', '.yaml'))
                                           for f in os.listdir(wf))
        if scripts:
            with_gates += 1
        if has_ci:
            with_ci += 1
        if scripts and not has_ci:
            gap += 1
            if len(findings) < limit:
                findings.append(finding(
                    'ci-gap', repo, '-', repo, repo,
                    f'{repo} carries {len(scripts)} gate script(s) ({", ".join(scripts[:3])}'
                    f'{", …" if len(scripts) > 3 else ""}) and no workflow file is present — '
                    f'either arm it in CI or say the gate is run by hand',
                    evidence=', '.join(scripts[:6])))
    # 2026-10-12: the first version declared "13 of 12 gate-carrying repo(s)" —
    # with_ci counts every repo with a workflow, including repos with no gate
    # scripts, so the numerator could exceed the denominator. A coverage line
    # that cannot be true is the exact defect this whole system exists to catch;
    # it was caught here by reading the number instead of trusting it.
    note = (f'{with_gates} repo(s) carry gate scripts, {with_ci} repo(s) carry a workflow '
            f'file, {gap} gate repo(s) have no workflow — presence is all this checks, not '
            f'what a workflow runs')
    return ran('enforcement', findings,
               coverage(with_gates - gap, with_gates,
                        'gate-carrying repo(s) with a CI workflow present'),
               note=note)


# --------------------------------------------------------------------------
# 12. SIGHTINGS — the register's guarantee: nothing is simply unseen
# --------------------------------------------------------------------------
SIGHT_CLASSES = [
    (re.compile(r'sources?/|snapshot', re.I), 'snapshot inside a repository'),
    (re.compile(r'/reference/|_kit_reference', re.I), 'reference material'),
    (re.compile(r'archive', re.I), 'archived material'),
    (re.compile(r'drafts?|pre_line|_alt', re.I), 'working draft'),
    (re.compile(r'audit|contracts?|semantic', re.I), 'audit or contract material'),
    (re.compile(r'late_arc|rebuild|staging|promotion|replacement', re.I),
     'work in progress on a registered serial'),
    (re.compile(r'planning|notes|inbox|uploads?', re.I), 'planning or inbox material'),
]


def check_sightings(root, books, limit=4):
    """Every chapter-bearing tree that is not a registered book, named and counted.

    THE GUARANTEE. On 2026-10-12 this account learned that its register had been
    listing what it happened to look at: a /reference/ exclusion, a sources/
    exclusion and a chapters/-shaped assumption had hidden a 116-chapter serial,
    a 101-chapter serial, an entire library shelf and a whole workshop, and
    nothing in the tooling said a word. This detector exists so that can never
    happen again: every tree holding chapter prose is either a registered book,
    a classified sighting, or a HARD finding. There is no fourth outcome.
    """
    trees = _chapter_trees(root)
    prepared = _prepare(books)
    findings, classes, unexplained, covered = [], {}, [], 0
    for b in books:
        if b.get('promoted'):
            fs = book_files(b)
            if fs:
                w = sum(len(open(f, encoding='utf-8', errors='replace').read().split())
                        for f in fs)
                findings.append(finding(
                    'orphan-work', b['repo'], b['book'], b.get('rel') or b['book'], b['book'],
                    f"registered where it was found — {len(fs)} chapter(s), {w:,} words: {b['note']}",
                    evidence=b['note']))
    for t in trees:
        if any(_under(t['rel'], b['path'], root) for b in books):
            covered += 1
            continue
        if any(b.get('live') and _under(t['rel'], b['live'], root) for b in books):
            covered += 1
            continue
        if any(_under(t['rel'], d, root) for b in books for d in b['dead']):
            covered += 1
            continue
        m = _match_book(t, prepared)
        cls = None
        if m:
            cls = ('library shelf copy of a registered book'
                   if is_published_copy(t['rel']) else 'copy of a registered book')
        else:
            for rx, name in SIGHT_CLASSES:
                if rx.search(t['rel']):
                    cls = name
                    break
            if cls is None and (lbg.DEAD_PATH_RX.search(t['rel'])
                                or NOT_A_BOOK_RX.search(t['rel'])):
                cls = 'working material beside a registered serial'
        if cls is None:
            unexplained.append(t)
            continue
        classes.setdefault(cls, []).append(t['rel'])

    for cls, rels in sorted(classes.items(), key=lambda kv: -len(kv[1])):
        findings.append(finding(
            'sighting', '-', '-', cls, cls,
            f'{len(rels)} chapter-bearing tree(s) outside the register — {cls}; not '
            f'gated, named here: ' + '; '.join(rels[:limit])
            + ('; …' if len(rels) > limit else ''),
            evidence='; '.join(rels[:limit])))
    for t in unexplained:
        findings.append(finding(
            'unaccounted-tree', t['repo'], '-', t['rel'], t['rel'],
            f'{t["rel"]} holds {len(t["files"])} chapter file(s) and is neither a '
            f'registered book nor a classifiable sighting — nothing may simply be unseen',
            evidence='; '.join(os.path.basename(f) for f in t['files'][:3])))
    sighted = sum(len(v) for v in classes.values())
    note = (f'{len(trees)} chapter-bearing tree(s) on disk: {covered} under a registered '
            f'book, {sighted} classified sighting(s)'
            + (f', {len(unexplained)} UNEXPLAINED' if unexplained else '')
            + (' — ' + ', '.join(f'{k}: {len(v)}' for k, v in
                                 sorted(classes.items(), key=lambda kv: -len(kv[1])))[:280]
               if classes else ''))
    return ran('sightings', findings,
               coverage(len(trees) - len(unexplained), len(trees),
                        'chapter-bearing tree(s) accounted for (book or sighting)'),
               note=note)

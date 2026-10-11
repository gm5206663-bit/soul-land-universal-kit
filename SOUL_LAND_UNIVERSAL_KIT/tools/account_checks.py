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
import sys

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
def registry(root):
    """Every book under root, with the live directory already chosen.

    A book is a directory that holds chapters and whose own status files say
    which directory is live. Anything the gate would refuse to guess about is
    returned as a refusal, not as a guess.
    """
    books = []
    for proj in lbg.find_projects(root):
        rel = os.path.relpath(proj, root)
        if lbg.is_out_of_scope(rel):
            continue        # one rule, shared with the gate — see live_book_gate.py
        parts = rel.split(os.sep)
        repo = parts[0]
        book = '/'.join(parts[1:]) or repo
        dirs = lbg.chapter_dirs(proj)
        live, dead, note = lbg.choose_live(proj, dirs)
        books.append(dict(repo=repo, book=book, path=proj, live=live, dead=dead, note=note))
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
    return bool(re.search(r'(^|/)(published-site|published|site|docs)(/|$)', book))


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

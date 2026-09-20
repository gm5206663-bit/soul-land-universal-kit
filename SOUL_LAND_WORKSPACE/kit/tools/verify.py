#!/usr/bin/env python3
"""
SOUL LAND UNIVERSAL KIT — the machine gate.  **UNIFIED, v2, 2026-09-20**

There were two files named verify.py with two different rule sets and two
different verdicts for the same project. This is one file that does both jobs.
Neither previous rule set was weakened; where the two disagreed, the stricter
reading is kept and the disagreement is named in the output.

Usage
    python3 tools/verify.py chapters/                 # chapter gate, one dir
    python3 tools/verify.py chapters/Chapter_07_*.md  # chapter gate, files
    python3 tools/verify.py --project .               # whole project sweep

Exits 0 only when every HARD gate passes. "Mostly passing" is a failure.

--------------------------------------------------------------------------------
WHAT COUNTS AS PROSE  (this is the whole story of v2)
--------------------------------------------------------------------------------
Every chapter in this corpus carries bookkeeping a reader never reads as story:

    # Chapter 21: Round One              <- title
    ## Canon Reference: ...              <- metadata head
    ## Timeline: ...
    ---                                  <- the head ends at the first rule
    ...the actual chapter...
    ---
    ## End of Chapter 21                 <- bookkeeping tail
    ### Chapter Summary: ...              (panel map, butterflies, tests, states)
    ### Character States ...

v1 classified all of that as prose, so the gate read "# Chapter 52" and
"- Project state: Chapter 52 written." as story and failed every chapter in the
corpus for digits the story never wrote. Measured 2026-09-20: prose extraction
returned an empty panel on 230 of 230 chapter files. The gate was working
correctly and measuring the wrong text.

v2 removes three apparatus regions before classifying prose:

    A. fenced blocks      (``` ... ```)                -- as v1
    B. the head           title + metadata, up to and including the first '---'
    C. the tail           from '## End of Chapter N' / '## Footer' to EOF

The rules are conservative ON PURPOSE. A region is stripped only when it cannot
be story: the head is never stripped if it carries dialogue or runs longer than
HEAD_MAX_LINES, and nothing is stripped when the file has no '---' at all.
Anything ambiguous stays in prose, where the gate can still fail on it.
selftest.py red-tests exactly this: digits in the story must still fail, digits
in the head/tail must pass, and CJK in the head must still fail.

--------------------------------------------------------------------------------
GATES
--------------------------------------------------------------------------------
HARD, whole file (apparatus included -- a defect is a defect wherever it sits)
    1. zero characters in a script an English reader cannot read
       -- NOT a blanket non-ASCII ban: em/en dashes, curly quotes, ellipsis,
          the U+25C6 panel marker and box-drawing are all allowed
    2. zero literal backslash-n sequences in prose
    6. no template or placeholder text left behind
       -- never applied to files whose path says template/law/example, or to
          files that exist to show the panel format; they hold slots by design
HARD, prose only (story text, after A/B/C above)
    3. zero digits in prose
    4. at least three spoken dialogue lines
    7. the U+25C6 marker never appears in prose; at most one book-end card,
       opening with "END OF", last in the file
HARD, across a chapter directory
    5. panels contiguous -- no overlap, no gap
ADVISORY, project mode only (reported with counts, never fails the build alone)
    - filename law: ASCII letters, digits, underscore, dot
    - CJK in non-chapter docs (codexes carry name glosses by established
      practice -- reported as a list, awaiting an author ruling)
    - literal backslash-n outside chapter prose (regex text and law text
      legitimately contain it: 14 of 14 hits in this corpus are legitimate)
    - chapters carrying a footer (kit panel discipline prefers a slim top panel)

Notes for whoever edits this next
    - The panel is NOT at file start, so the fence split is the correct
      extraction; a ^-anchored regex silently passes everything.
    - EVERY fenced block is apparatus, not just the first. Joining everything
      after the first fence reclassifies a book-end card as prose and produces
      false positives in gates 3 and 7.
    - The backslash-n check is built from chr(92) so this file does not itself
      contain the artifact it checks for.
    - A gate must not match its own description: placeholder words match
      case-sensitively on a word boundary for that reason.
    - Run selftest.py after ANY edit here. A checker edited into a no-op still
      prints green.
"""

import argparse
import glob
import os
import re
import sys

NL = chr(10)
BS = chr(92)
BACKSLASH_N = BS + "n"

PLACEHOLDER_SLOTS = [
    "<title>", "<start>", "<end>", "<age>", "<rank",
    "<fill", "<what ", "<only if",
]
PLACEHOLDER_WORDS = ["TODO", "FIXME", "PLACEHOLDER", "XXX"]
PLACEHOLDER_WORD_RE = re.compile(
    r"\b(?:" + "|".join(PLACEHOLDER_WORDS) + r")\b"
)

# Straight or curly quotes. Gate A (the project scanner) counted curly quotes;
# several serials use them, and counting only the straight form reported those
# chapters as having no dialogue at all.
DIALOGUE = re.compile(r'["\u201c][^"\u201c\u201d' + NL + r']{4,}["\u201d]')
MARKER = "\u25c6"  # black diamond -- panel/book-end marker
PANEL_RANGE = re.compile(r"years (\d+)\u2013(\d+)")
PANEL_ANY = re.compile(r"years (\d+)(?:\u2013(\d+))?")
DIGITS = re.compile(r"\d[\d,\.]*")

# Digits that are NAMES, not measurements. The rule "exact figures only in
# panels, ledgers, tables and footers" exists to stop invented precision; a
# room number is not precision, it is a name. The corpus runs on these:
# "Room 108" (SL2, every chapter), "Dorm333", "Dorm336", "Rank39", "SP505",
# "ch 17" (SL3/SL4). Two narrow exemptions, both red-tested:
#   (a) letters touching the digits in one token: Dorm333, Rank39, ch17
#   (b) a designation word immediately before: Room 108, Dorm 333, Chapter 21
# Anything else -- "rank 29", "6:04", "year 163", "eight hundred" spelled as
# a number -- still fails.
# One pattern, one pass: the digit is INSIDE the match, so the mask cannot
# leak it. Designation words exempt their own number (Room 108, ch 17); a
# letter touching the digits in one token is an identifier (Dorm333, SP505).
NAME_NUM = re.compile(
    r"(?i:\brooms?\b|\bdorms?\b|\bchapters?\b|\bch\b|\bno\.?)\s*\d[\d,\.]*"
    r"|[A-Za-z]\d[\d,\.]*"
    r"|\d[\d,\.]*[A-Za-z]"
)


def mask_names(text):
    """Blank out digit-runs that are names, for the digits-in-prose gate only.

    Returns text of the same length; every other character untouched.
    """
    return NAME_NUM.sub(lambda m: " " * len(m.group(0)), text)

# --- apparatus boundary -----------------------------------------------------
HRULE_RE = re.compile(r"^-{3,}\s*$")
TRAILER_RE = re.compile(
    r"^#{1,3}\s*(?:End of Chapter\b|Footer\b|Chapter Summary\b)",
    re.IGNORECASE,
)
HEAD_MAX_LINES = 60
TAIL_MAX_LINES = 40
# A trailing block after the last rule is only treated as apparatus when it
# carries one of these signals. Without the keyword requirement, any chapter
# whose closing paragraph follows a scene-break rule would be exempted, and a
# digit there would be hidden. The keyword is what makes the exemption safe.
TAIL_KEYWORDS = (
    "chapter footer",
    "canon touched",
    "character states",
    "canon preserved",
    "panel map",
    "butterfly effect",
    "tests run",
    "wires:",
    "position:",
    "chapter summary",
)
TITLE_RE = re.compile(r"^#\s*(?:Chapter|Prologue|Epilogue|Interlude|Part)\b",
                      re.IGNORECASE)
# A metadata head may QUOTE canon chapter titles ("Wu Zhangkong's Soul Skills"),
# so a quoted span alone cannot disqualify it -- SL3's heads all do this, which is
# why the v2 dialogue guard alone left 116 heads unfixed. A head is apparatus when
# it is short, opens with a heading, and either carries no dialogue or names what
# it is.
HEAD_KEYWORDS = ("canon", "timeline", "growth", "coverage", "source",
                 "anchors", "au:", "panel", "rank")

# Paths that are allowed to contain slot tokens by design.
NO_PLACEHOLDER_PATHS = re.compile(
    r"(template|TEMPLATE|_TEMPLATE|example|EXAMPLE"
    r"|tools/|00_START_HERE|0[0-9]_[A-Z_]+\.md|_LAW\.md|README)",
)


def split_fences(text):
    """Return (panel, outside_text, extra_blocks) for fenced apparatus."""
    parts = text.split("```")
    if len(parts) < 3:
        return "", text, []
    panel = parts[1]
    extra = [parts[i] for i in range(3, len(parts), 2)]
    outside = "".join(parts[i] for i in range(2, len(parts), 2))
    return panel, outside, extra


def strip_apparatus(text):
    """Remove the chapter head and tail, leaving the story.

    Returns (core, info) where info names what was stripped, so the gate can
    print it. An exemption nobody can see is an exemption nobody can audit.
    """
    lines = text.split(NL)
    n = len(lines)
    head_lines = tail_lines = 0

    # --- the title line (always apparatus; SL4-shaped chapters have no head
    # beyond it, and the digit in "# Chapter 4" is not a digit in prose)
    start = 0
    while start < n and not lines[start].strip():
        start += 1
    if start < n and TITLE_RE.match(lines[start].strip()):
        start += 1
        head_lines += 1

    # --- the metadata head: everything up to and including the first rule,
    # when that region is short and reads as apparatus rather than story
    for i in range(start, n):
        if HRULE_RE.match(lines[i]):
            head = NL.join(lines[start:i + 1])
            head_low = head.lower()
            has_heading = any(l.lstrip().startswith("#") for l in lines[start:i])
            quiet = not DIALOGUE.search(head)
            named = any(k in head_low for k in HEAD_KEYWORDS)
            small = (i - start) <= 6
            if (i - start) <= HEAD_MAX_LINES and (
                    (has_heading and (quiet or named))
                    or (small and quiet)):
                head_lines += (i + 1 - start)
                start = i + 1
            break

    # --- the tail, by heading
    end = n
    for i in range(start + (n - start) // 2, n):
        if TRAILER_RE.match(lines[i].strip()):
            j = i
            while j > start and not lines[j - 1].strip():
                j -= 1
            if j > 0 and HRULE_RE.match(lines[j - 1]):
                j -= 1
            tail_lines = n - j
            end = j
            break

    # --- the tail, by keyword (blue_silver's italic footer after a rule)
    if end == n:
        for i in range(n - 1, start, -1):
            if HRULE_RE.match(lines[i]):
                tail = NL.join(lines[i + 1:])
                if (len(lines) - i) <= TAIL_MAX_LINES \
                        and not DIALOGUE.search(tail) \
                        and any(k in tail.lower() for k in TAIL_KEYWORDS):
                    tail_lines = n - i
                    end = i
                break

    info = []
    if head_lines:
        info.append("head")
    if tail_lines:
        info.append("tail")
    return NL.join(lines[start:end]), info


def prose_of(text):
    """The story text of a chapter file: fences gone, head and tail gone."""
    _, outside, _ = split_fences(text)
    core, _info = strip_apparatus(outside)
    return core


# Typographic characters that are correct, portable and reader-visible.
ALLOWED_NON_ASCII = {
    "\u2013",  # en dash
    "\u2014",  # em dash
    "\u2018", "\u2019",  # curly single quotes
    "\u201c", "\u201d",  # curly double quotes
    "\u2026",  # ellipsis
    "\u25c6",  # panel marker
    "\u2248",  # almost equal to
    "\u00d7",  # multiplication sign
    "\u00a0",  # non-breaking space
}


def script_ranges():
    """Code point ranges for scripts an English-language reader cannot read."""
    return [
        (0x3040, 0x30FF),   # hiragana + katakana
        (0x3400, 0x4DBF),   # CJK ext A
        (0x4E00, 0x9FFF),   # CJK unified ideographs
        (0xAC00, 0xD7AF),   # hangul syllables
        (0xF900, 0xFAFF),   # CJK compatibility ideographs
        (0x20000, 0x2FA1F),  # CJK ext B-F
    ]


def check_script(text):
    """Characters in a script the reader cannot read. This is the real gate."""
    bad = []
    for c in text:
        o = ord(c)
        if o < 128 or c in ALLOWED_NON_ASCII:
            continue
        if any(lo <= o <= hi for lo, hi in script_ranges()):
            bad.append(c)
        elif 0x2500 <= o <= 0x257F:  # box drawing -- file trees, diagrams
            continue
        elif o > 0x2500:  # unrecognised non-typographic symbol
            bad.append(c)
    return bad


def is_templateish(path):
    return bool(NO_PLACEHOLDER_PATHS.search(path))


def verify_file(path):
    """Return (failures, warnings, meta) for one chapter file."""
    failures, warnings = [], []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    panel, outside, extra_blocks = split_fences(text)
    prose, apparatus = strip_apparatus(outside)

    # Gate 1 - unreadable script, whole file (apparatus included)
    bad = check_script(text)
    if bad:
        sample = ", ".join(f"U+{ord(c):04X}" for c in dict.fromkeys(bad))
        failures.append(f"unreadable script ({len(bad)} chars): {sample}")

    # Gate 2 - literal backslash-n, prose only (whole file in project mode)
    n = prose.count(BACKSLASH_N)
    if n:
        failures.append(f"literal backslash-n sequence x{n}")

    # Gate 3 - digits in prose (the story only). Names are masked first and
    # remain names; a measurement digit still fails.
    d = DIGITS.findall(mask_names(prose))
    if d:
        failures.append(f"digits in prose: {d[:8]}")

    # Gate 4 - dialogue register. HARD: 07_PROSE_LAW and 09_AUDIT_LAW both list
    # it as hard. The register silently disappears from introspective serials,
    # so it must fail loudly.
    dlg = len(DIALOGUE.findall(prose))
    if dlg < 3:
        failures.append(f"only {dlg} spoken dialogue lines (need >=3)")

    # Gate 6 - placeholders, whole file, templates exempt
    if not is_templateish(path):
        hits = [p for p in PLACEHOLDER_SLOTS if p.lower() in text.lower()]
        hits += sorted(set(PLACEHOLDER_WORD_RE.findall(text)))
        if hits:
            failures.append(f"placeholder text: {hits}")

    # Gate 7 - panel marker discipline
    stray = [l.strip() for l in prose.split(NL) if l.strip().startswith(MARKER)]
    if stray:
        failures.append(
            f"panel marker in prose: {stray[0][:60]!r} "
            f"(the marker is apparatus; it may not appear in prose)"
        )
    cards = [b for b in extra_blocks if MARKER in b]
    if len(cards) > 1:
        failures.append(f"{len(cards)} marker cards in one chapter (at most one)")
    for b in cards:
        first = next((l.strip() for l in b.split(NL) if l.strip()), "")
        if not first.upper().startswith(MARKER + " END OF"):
            failures.append(
                f"marker card does not open with 'END OF': {first[:60]!r}"
            )
    if cards and extra_blocks and extra_blocks[-1] is not cards[-1]:
        failures.append("book-end card is not the last block in the chapter")

    meta = {"dlg": dlg, "words": len(prose.split()), "range": None,
            "apparatus": apparatus}
    m = PANEL_RANGE.search(panel) or PANEL_RANGE.search(text)
    if m:
        meta["range"] = (int(m.group(1)), int(m.group(2)))
    else:
        m2 = PANEL_ANY.search(panel) or PANEL_ANY.search(text)
        if m2:
            lo = int(m2.group(1))
            meta["range"] = (lo, int(m2.group(2)) if m2.group(2) else lo)
        else:
            warnings.append("no parseable year range in panel")

    return failures, warnings, meta


def check_contiguity(results):
    """Gate 5 - panels must be contiguous, no overlap, no gap."""
    problems = []
    prev_hi, prev_name = None, None
    for path, (_f, _w, meta) in results:
        rng = meta.get("range")
        if not rng:
            continue
        lo, hi = rng
        if prev_hi is not None:
            if lo < prev_hi:
                problems.append(
                    f"{os.path.basename(path)}: OVERLAP "
                    f"({prev_name} ends {prev_hi}, this starts {lo})"
                )
            elif lo > prev_hi:
                problems.append(
                    f"{os.path.basename(path)}: GAP "
                    f"({prev_name} ends {prev_hi}, this starts {lo})"
                )
        prev_hi, prev_name = hi, os.path.basename(path)
    return problems


# The author's R5 naming law: upload-safe names. The corpus's own dated-file
# convention (audits/CHAPTER_52_VALIDATION_2026-09-19.md, SL4's entire audit
# tree) uses date hyphens, so hyphen is allowed alongside letters, digits,
# underscore and dot. Spaces, CJK and other punctuation still fail.
FNAME = re.compile(r"^[A-Za-z0-9_.\-]+$")


def project_mode(root):
    """Gate A's sweep, kept: every .md in the project, classified by kind."""
    hard = []
    print("=" * 72)
    print("SOUL LAND PROJECT SWEEP — " + root)
    print("=" * 72)

    md = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            if f.endswith(".md"):
                md.append(os.path.join(dp, f))
    md.sort()

    chapters = [p for p in md if "/chapters/" in p.replace(os.sep, "/")]
    docs = [p for p in md if p not in chapters]

    def rel(p):
        return os.path.relpath(p, root)

    # filename law (whole tree, not only .md)
    bad_names = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            if not FNAME.match(f):
                bad_names.append(os.path.relpath(os.path.join(dp, f), root))
    print(f"[filename-law]      {len(bad_names)} bad names"
          + (f" -> {bad_names[:10]}" if bad_names else " -> clean"))
    if bad_names:
        hard.append("filename law")

    # CJK: hard in chapters, listed for docs
    cjk_ch, cjk_doc = [], []
    for p in md:
        with open(p, encoding="utf-8", errors="replace") as fh:
            t = fh.read()
        if check_script(t):
            (cjk_ch if p in chapters else cjk_doc).append(rel(p))
    print(f"[cjk-sweep]         chapters with unreadable script: {len(cjk_ch)}/{len(chapters)}"
          + (f" -> {cjk_ch[:10]}" if cjk_ch else " -> clean"))
    if cjk_ch:
        hard.append("cjk in chapters")
    print(f"[cjk-docs]          docs carrying CJK: {len(cjk_doc)}/{len(docs)} (advisory, ruling pending)")
    for p in cjk_doc[:15]:
        print(f"                      - {p}")

    # backslash-n: hard in a chapter's STORY, advisory anywhere else.
    # Classify by file KIND, never by where the sequence was found -- a doc whose
    # regex text contains it is not a chapter with a prose defect.
    bsn_prose, bsn_doc = [], []
    for p in md:
        with open(p, encoding="utf-8", errors="replace") as fh:
            t = fh.read()
        if BACKSLASH_N not in t:
            continue
        if p in chapters:
            if BACKSLASH_N in prose_of(t):
                bsn_prose.append(rel(p))
        else:
            bsn_doc.append(rel(p))
    print(f"[backslash-n-story] chapters whose story carries a literal backslash-n: {len(bsn_prose)}"
          + (f" -> {bsn_prose}" if bsn_prose else " -> clean"))
    if bsn_prose:
        hard.append("backslash-n in a chapter story")
    if bsn_doc:
        print(f"[backslash-n-docs]  elsewhere (regex/law text -- usually legitimate): {len(bsn_doc)}")
        for p in bsn_doc[:15]:
            print(f"                      - {p}")

    # digits in chapter stories
    digit_bad = []
    for p in chapters:
        with open(p, encoding="utf-8", errors="replace") as fh:
            t = fh.read()
        body = prose_of(t)
        d = DIGITS.findall(mask_names(body))
        if d:
            digit_bad.append((rel(p), d[:6]))
    print(f"[digits-in-story]   chapters with digits in the story: {len(digit_bad)}/{len(chapters)}")
    for p, d in digit_bad[:20]:
        print(f"                      - {p}: {d}")
    if digit_bad:
        hard.append("digits in story")

    # dialogue + footer advisories
    low = []
    withfooter = 0
    for p in chapters:
        with open(p, encoding="utf-8", errors="replace") as fh:
            t = fh.read()
        body = prose_of(t)
        if len(DIALOGUE.findall(body)) < 3:
            low.append(rel(p))
        if re.search(r"^#{1,3}\s*Footer", t, re.M):
            withfooter += 1
    print(f"[dialogue-report]   chapters under three spoken lines: {len(low)}"
          + (f" -> {low[:10]}" if low else " -> clean"))
    print(f"[footer-report]     chapters carrying a footer: {withfooter}/{len(chapters)}")
    print()
    print("-" * 72)
    if hard:
        print("VERDICT: FAIL — " + "; ".join(hard))
        return 1
    print("VERDICT: PASS — all hard gates clean")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Soul Land chapter verification gate (unified v2)")
    ap.add_argument("paths", nargs="*", help="chapter files or directories")
    ap.add_argument("--project", metavar="ROOT",
                    help="sweep a whole project root (filename law + CJK + digits in story)")
    args = ap.parse_args()

    if args.project:
        return project_mode(args.project)

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            files.extend(sorted(glob.glob(os.path.join(p, "*.md"))))
        else:
            files.extend(sorted(glob.glob(p)))

    if not files:
        print("no files matched")
        return 2

    results, total_words, total_fail, total_warn = [], 0, 0, 0

    print("=" * 72)
    print("SOUL LAND VERIFICATION GATE")
    print("=" * 72)

    for path in files:
        failures, warnings, meta = verify_file(path)
        results.append((path, (failures, warnings, meta)))
        total_words += meta["words"]
        total_fail += len(failures)
        total_warn += len(warnings)

        name = os.path.basename(path)
        rng = f"{meta['range'][0]}-{meta['range'][1]}" if meta.get("range") else "  ?  "
        status = "PASS" if not failures else "FAIL"
        app = ("  [apparatus: " + "+".join(meta["apparatus"]) + "]"
               if meta.get("apparatus") else "  [apparatus: NONE]")
        print(f"{status}  {name:<46} {meta['words']:>6}w  yrs {rng:<10} "
              f"dlg {meta['dlg']:>2}{app}")
        for f in failures:
            print(f"        FAIL  {f}")
        for w in warnings:
            print(f"        warn  {w}")

    print("-" * 72)
    contig = check_contiguity(results)
    for c in contig:
        print(f"FAIL  panel contiguity: {c}")
    total_fail += len(contig)

    print("-" * 72)
    print(f"{len(files)} files  |  {total_words:,} prose words  |  "
          f"{total_fail} failures  |  {total_warn} warnings")

    if total_fail:
        print(f"{NL}RESULT: FAIL — fix every failure before shipping.")
        return 1
    print(f"{NL}RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

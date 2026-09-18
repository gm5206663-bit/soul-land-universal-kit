#!/usr/bin/env python3
"""
SOUL LAND UNIVERSAL KIT — chapter verification gate.

Usage:
    python3 tools/verify.py chapters/            # verify a chapter directory
    python3 tools/verify.py chapters/Chapter_07_*.md

Exits 0 only when every hard gate passes. "Mostly passing" is a failure.

Hard gates
    1. zero characters in a script the reader cannot read (CJK, kana, hangul)
       -- NOT a blanket non-ASCII ban; em/en dashes and the U+25C6 marker are allowed
    2. zero literal backslash-n sequences
    3. zero digits in prose (every fenced block is apparatus and is exempt)
    4. at least three spoken dialogue lines
    5. chapter panels contiguous - no overlap, no gap
    6. no template or placeholder text left behind
    7. the U+25C6 marker never appears in prose; at most one book-end card,
       opening with "END OF", last in the file

Gate scope: gates 1-2 and 6 apply to any prose file. Gates 3-5 and 7 are chapter
gates. Gate 6 must NOT be applied to templates or to law files that show the panel
format -- they contain slot tokens by definition. See 09_AUDIT_LAW.md.

Notes
  - The panel is NOT at file start (the title precedes it), so splitting on the
    fence is the correct extraction. A ^-anchored regex silently passes everything.
  - EVERY fenced block is apparatus, not just the first. Joining everything after
    the first fence reclassifies a book-end card as prose and produces false
    positives in gates 3 and 7. Prose is the even indices past the first fence.
  - The backslash-n check is expressed via chr(92) so this file does not itself
    contain the artifact it is checking for.
  - A gate must not match its own description. Placeholder words are matched
    case-sensitively on a word boundary for that reason.
"""

import argparse
import glob
import os
import re
import sys

NL = chr(10)
BS = chr(92)
BACKSLASH_N = BS + "n"

# Angle-bracket slots are unambiguous template markup: match them loosely.
PLACEHOLDER_SLOTS = [
    "<title>", "<start>", "<end>", "<age>", "<rank",
    "<fill", "<what ", "<only if",
]

# Bare words are an UPPERCASE CONVENTION. Match them case-sensitively on a word
# boundary, so prose that merely *discusses* placeholders ("no placeholder text
# left") does not trip the gate. A case-insensitive substring match here is a
# self-referential false positive: the rule fires on its own description.
PLACEHOLDER_WORDS = ["TODO", "FIXME", "PLACEHOLDER", "XXX"]
PLACEHOLDER_WORD_RE = re.compile(
    r"\b(?:" + "|".join(PLACEHOLDER_WORDS) + r")\b"
)

# Kept for callers that want the flat list.
PLACEHOLDERS = PLACEHOLDER_SLOTS + PLACEHOLDER_WORDS

DIALOGUE = re.compile(r'"[^"' + NL + r']{4,}"')
MARKER = "\u25c6"  # black diamond -- panel/book-end marker
PANEL_RANGE = re.compile(r"years (\d+)\u2013(\d+)")
PANEL_ANY = re.compile(r"years (\d+)(?:\u2013(\d+))?")
DIGITS = re.compile(r"\d[\d,\.]*")


def split_prose(text):
    """Return (panel, prose, extra_blocks).

    Every fenced block is apparatus, not prose. The first is the status panel;
    any later ones are book-end cards or similar. Prose is what sits OUTSIDE all
    of them. Joining everything after the first fence -- the naive approach --
    silently reclassifies a book-end card as prose and produces false positives.
    """
    parts = text.split("```")
    if len(parts) < 3:
        return "", text, []
    panel = parts[1]
    extra = [parts[i] for i in range(3, len(parts), 2)]
    # even indices outside the first fence are real prose
    prose = "".join(parts[i] for i in range(2, len(parts), 2))
    return panel, prose, extra


# Typographic characters that are correct, portable and reader-visible.
# The law is "no unreadable script", NOT "no non-ASCII" -- em/en dashes are
# proper English typography, and U+25C6 is this kit's own panel marker.
ALLOWED_NON_ASCII = {
    "\u2013",  # en dash  (ranges)
    "\u2014",  # em dash  (parenthetical)
    "\u2018", "\u2019",  # curly single quotes
    "\u201c", "\u201d",  # curly double quotes
    "\u2026",  # ellipsis
    "\u25c6",  # black diamond -- panel marker
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
        (0x20000, 0x2FA1F), # CJK ext B-F
    ]


def check_script(text):
    """Return characters in a script the reader cannot read. This is the real gate."""
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


def verify_file(path):
    """Return (failures, warnings, meta) for one chapter file."""
    failures, warnings = [], []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    panel, prose, extra_blocks = split_prose(text)

    # Gate 1 - unreadable script (NOT a blanket non-ASCII ban; em/en dashes are fine)
    bad = check_script(text)
    if bad:
        sample = ", ".join(f"U+{ord(c):04X}" for c in dict.fromkeys(bad))
        failures.append(f"unreadable script ({len(bad)} chars): {sample}")

    # Gate 2 - literal backslash-n
    n = text.count(BACKSLASH_N)
    if n:
        failures.append(f"literal backslash-n sequence x{n}")

    # Gate 3 - digits in prose
    d = DIGITS.findall(prose)
    if d:
        failures.append(f"digits in prose: {d[:8]}")

    # Gate 4 - dialogue register. HARD GATE, not a warning: 07_PROSE_LAW.md and
    # 09_AUDIT_LAW.md both list it as hard. The dialogue register silently
    # disappears from introspective serials, so it must fail loudly.
    dlg = len(DIALOGUE.findall(prose))
    if dlg < 3:
        failures.append(f"only {dlg} spoken dialogue lines (need >=3)")

    # Gate 6 - placeholders. Slots match loosely; convention words match
    # case-sensitively on a word boundary.
    hits = [p for p in PLACEHOLDER_SLOTS if p.lower() in text.lower()]
    hits += sorted(set(PLACEHOLDER_WORD_RE.findall(text)))
    if hits:
        failures.append(f"placeholder text: {hits}")

    # Gate 7 - panel marker discipline.
    # The marker belongs to apparatus. It must never appear in true prose. In
    # apparatus it may only head a book-end card ("END OF ..."), at most one per
    # chapter, and that card must be the last thing in the file.
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

    meta = {"dlg": dlg, "words": len(prose.split()), "range": None}
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
                    f"{os.path.basename(path)}: OVERLAP ({prev_name} ends {prev_hi}, this starts {lo})"
                )
            elif lo > prev_hi:
                problems.append(
                    f"{os.path.basename(path)}: GAP ({prev_name} ends {prev_hi}, this starts {lo})"
                )
        prev_hi, prev_name = hi, os.path.basename(path)
    return problems


def main():
    ap = argparse.ArgumentParser(description="Soul Land chapter verification gate")
    ap.add_argument("paths", nargs="+", help="chapter files or directories")
    args = ap.parse_args()

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
        print(f"{status}  {name:<46} {meta['words']:>6}w  yrs {rng:<10} dlg {meta['dlg']:>2}")
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

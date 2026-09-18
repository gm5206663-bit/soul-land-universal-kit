#!/usr/bin/env python3
"""LAYER 7 — CANON QUOTE VERIFICATION.

Every quoted string attributed to canon in a chapter header is checked against the canon corpus
(372 future chapters on disk + the 35 frozen quote-sources in CODEX/CANON_QUOTE_SOURCES_FROZEN.txt).
chapters. If a quote is not in the corpus, it is either invented, misremembered, or from a chapter we
do not have — and all three need to be known.

WHY THIS EXISTS. The story's headers claim canon backing with verbatim quotes. Nothing ever checked
them. On 2026-08-28 one was verified by hand ("His first soul ring is purple and his physique is
excellent" — real, canon ch 218, down to canon's own typo "HIs") and one near-miss was found: canon's
"Yet Mu Chen said that HE was already a fourth rank blacksmith" refers to WULIN, not Mu Chen, and the
pronoun is easy to misread into a wrong fact about a named character.

Usage: python3 checks/verify_canon_quotes.py [--strict]
"""
import glob, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
import paths as _P
CANON = _P.CANON

def norm(t):
    # 🔴 headers wrap long quotes across lines and every continued line starts with "## ", so the
    # comment markers land INSIDE the quoted string. Four of the first six "unverified" results were
    # this artifact, not bad quotes.
    t = unicodedata.normalize("NFKD", t)
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    t = t.replace("\u2013", "-").replace("\u2014", "-").replace("\u2026", "...")
    return re.sub(r"[^a-z0-9']+", "", t.lower())

# load canon once
corpus = []
for f in sorted(glob.glob(os.path.join(CANON, "canon_*.txt"))):
    corpus.append((int(re.search(r"canon_(\d+)", f).group(1)),
                   norm(open(f, encoding="utf-8", errors="replace").read())))
# 🔴 FROZEN QUOTE-SOURCES (2026-08-29). The adapted-range canon .txt files (23-228) were
# reclaimed to free space; the verbatim text our 57 header quotes verify against was frozen
# into CODEX/CANON_QUOTE_SOURCES_FROZEN.txt first. Load it into the corpus so word-to-word
# verification survives the reclamation. Source of truth remains the archived PDFs.
FROZEN = _P.FROZEN_QUOTES
if os.path.exists(FROZEN):
    fz = open(FROZEN, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"<<<CANON_(\d+)>>>(.*?)<<<END_\1>>>", fz, re.S):
        corpus.append((int(m.group(1)), norm(m.group(2))))
# 🔴 2026-09-18 — the canon corpus is COPYRIGHTED NOVEL TEXT and is deliberately NOT distributed
# with the project (see soul_land_3_adaptive_prodigy/CANON_SOURCE.md). A fresh clone therefore has
# no corpus. Two behaviours, deliberately different:
#   --strict  (what run_all.sh uses, on the machine that has the corpus) -> HARD FAIL. A missing
#             corpus must never be silently excused where the corpus is supposed to exist.
#   default   -> loud SKIP, exit 0, so a fresh clone's suite can still be green for the 12 layers
#             that do not need canon text. The message is unmissable on purpose: a skip that looks
#             like a pass is how a check dies.
if not corpus:
    strict = "--strict" in sys.argv
    print("verify_canon_quotes: NO CANON CORPUS PRESENT")
    print("  looked in: " + CANON)
    print("  frozen   : " + _P.FROZEN_QUOTES)
    if strict:
        sys.exit("verify_canon_quotes: --strict and no corpus — set SL3_CANON / SL3_WORKSPACE")
    print("  ==> LAYER 7 SKIPPED. This is NOT a pass. 85 canon quotes are unverified here.")
    sys.exit(0)
BLOB = " ".join(t for _, t in corpus)

QUOTE = re.compile(r'\*"([^"]{25,220})"\*')   # markdown-italic quoted strings in headers
strict = "--strict" in sys.argv
checked = found = 0
problems = []

for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    # headers only — prose quotes are dialogue we wrote, not canon claims
    head = "\n".join(l for l in open(path, encoding="utf-8", errors="replace").read().split("\n")
                     if l.startswith("#"))
    for m in QUOTE.finditer(head):
        # 🔴 Headers wrap long quotes across lines and each continued line begins with "## ", so the
        # comment markers land INSIDE the captured string ("...sentence\n## that tells..."). Four of
        # the first six "unverified" results were this artifact, not bad quotes. Unwrap before comparing.
        q = re.sub(r"\n\s*#+\s*", " ", m.group(1)).strip()
        # skip lines that are our own dialogue or clearly not canon claims
        if re.search(r"\b(I|we|you)\b", q) and not re.search(r"\b(soul|spirit|ring|rank|blacksmith|craftsman)\b", q, re.I):
            continue
        nq = norm(q)
        if len(nq) < 25:
            continue
        # Skip quotes that are OUR OWN prose or dialogue merely emphasised with *"…"*. Headers use the
        # same markup for a lesson we wrote and for a line we are citing from canon, so use the
        # surrounding words to tell them apart.
        pre = head[max(0, m.start() - 90):m.start()].lower()
        if re.search(r"(lesson|the chapter.s|produces|our |we wrote|means )", pre):
            continue
        checked += 1
        # 🔴 Match on a long SLIDING WINDOW of the normalised quote, not the whole string. Headers
        # routinely quote from the middle of a sentence ("his greatest accomplishment over the last
        # month…" begins after "This was Xie Xie's"), and elide with "...". Whole-string matching
        # reported five real quotes as unverified. A 40-character alnum window is ~7 words, which is
        # long enough to be meaningful and short enough to survive a partial quote.
        parts = [norm(p) for p in re.split(r"\.\.\.|…", q) if len(norm(p)) >= 20] or [nq]
        ok = False
        for p in parts:
            if p in BLOB:
                ok = True
                break
            W = 40
            if len(p) > W:
                for i in range(0, len(p) - W + 1, 10):
                    if p[i:i + W] in BLOB:
                        ok = True
                        break
            if ok:
                break
        if ok:
            found += 1
        else:
            problems.append((n, q[:110]))

print(f"verify_canon_quotes: {found}/{checked} canon quotes verified against {len(corpus)} canon chapters")
for n, q in problems:
    print(f"  UNVERIFIED ch{n}: \"{q}\"")
if problems:
    print(f"\n  These are not necessarily wrong — the corpus is missing ch 28 and everything after "
          f"600. But each one must be accounted for, not assumed.")
if problems and strict:
    sys.exit(1)
sys.exit(0)

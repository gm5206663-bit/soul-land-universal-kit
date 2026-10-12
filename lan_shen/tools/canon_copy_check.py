#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CANON COPY CHECK — the transcription gate.

Doctrine: sl3 presence_audit.py layer 4 ("NO CANON COPYING"), ported and widened,
then corrected on 2026-09-20 after it was found to have a blind spot.

The sl3 original only compared a chapter against the canon files it cited in its
header. That is a weaker test than the one actually wanted: a chapter can absorb a
phrase from canon it read three chapters ago and cite nothing. This version compares
EVERY chapter against EVERY canon extract on disk.

Three checks:

  A. NARRATION n-GRAMS (default 12). Any 12-word run of a chapter's NARRATION
     (quoted speech removed) that appears verbatim in a canon extract. This is
     prose plagiarism, and it is also the fingerprint of a chapter that has
     stopped thinking.

  B. VERBATIM QUOTED SPEECH, run length >= QRUN (default 7). Any contiguous run
     of QRUN or more words inside one quote that appears in canon.

  C. TRANSCRIPTION DENSITY. Total verbatim canon words carried in a chapter's
     dialogue, counting only runs of >= BUDGET_MIN_RUN (default 6) words so that
     unavoidable generic English ("it's the same as", "you don't have to") does
     not inflate the figure. FAIL above BUDGET_FAIL, warn above BUDGET_WARN.

WHY B AND C EXIST, AND WHY THE OLD THRESHOLD WAS WRONG
  B was originally set at 15 words, on the reasoning that a long quote must be a
  deliberate choice rather than a leak. Measured against the corpus that reasoning
  was false: the worst transcription in the serial (chapter three, 297 verbatim
  canon words, including whole scenes of dialogue) passed at 15 because every
  single borrowed run sat between 8 and 14 words — the longest exactly one word
  under the threshold. A gate whose limit is chosen before the evidence is a gate
  that measures nothing.

  The thresholds now come from the corpus. Chapters five to thirteen — the chapters
  written in this serial's own voice — carry verbatim runs no longer than five
  words, and those five are generic function phrases. Chapters one to four, which
  stage canon scenes by transcribing them, carry runs of eight to fourteen. Seven
  is where borrowing starts; six is the floor at which a run stops being
  coincidence. Density separates the two diseases: one kept line is adaptation,
  three hundred verbatim words is a transcript.

  A short canon line kept on purpose is legitimate and this gate does not forbid
  it — the author's own accepted bar re-stages canon scenes and keeps short lines.
  What the gate forbids is a scene that can be dropped into the story unchanged,
  because then the original character has been erased from his own serial.

Fenced blocks (status panels) are excluded from all three — they are apparatus and
may legitimately quote a canon line for reference. A canon receipt may quote canon.
It may never quote the serial.

Run:  python3 tools/canon_copy_check.py            # all chapters vs all canon
      python3 tools/canon_copy_check.py --n 8      # stricter narration grams
      python3 tools/canon_copy_check.py --report   # list every run, no pass/fail
"""

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)

QRUN = 7              # check B: shortest reported verbatim run inside one quote
BUDGET_MIN_RUN = 6    # check C: shortest run counted toward density
BUDGET_WARN = 80      # check C: advisory ceiling, verbatim words per chapter
BUDGET_FAIL = 120     # check C: hard ceiling, verbatim words per chapter


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def ngrams(s, n):
    w = norm(s).split()
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def prose_only(text):
    """Strip every fenced block (panels, book-end cards) — they are apparatus."""
    parts = text.split("```")
    if len(parts) < 3:
        return text
    return NL.join(parts[i] for i in range(2, len(parts), 2))


def narration_only(prose):
    """Remove quoted speech: check A is about narration, not dialogue."""
    return re.sub(r'"[^"]*"', " ", prose)


def quotes(prose):
    return re.findall(r'"([^"]*)"', prose)


def longest_runs(words, haystack, floor):
    """Greedy non-overlapping verbatim runs of >= floor words, longest first."""
    found, i = [], 0
    while i < len(words):
        j = len(words)
        while j > i:
            if " ".join(words[i:j]) in haystack:
                break
            j -= 1
        if j - i >= floor:
            found.append((j - i, " ".join(words[i:j])))
            i = j
        else:
            i += 1
    return found


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=12, help="narration gram length (default 12)")
    ap.add_argument("--qrun", type=int, default=QRUN, help="quoted-speech run length (default 7)")
    ap.add_argument("--budget-fail", type=int, default=BUDGET_FAIL,
                    help="verbatim canon words per chapter that fail (default 120)")
    ap.add_argument("--budget-warn", type=int, default=BUDGET_WARN,
                    help="verbatim canon words per chapter that warn (default 80)")
    ap.add_argument("--report", action="store_true", help="list every run; do not judge")
    ap.add_argument("--chapters", default=os.path.join(ROOT, "chapters", "*.md"))
    ap.add_argument("--canon", default=os.path.join(ROOT, "canon_extract", "chapters", "*.txt"))
    a = ap.parse_args(argv)

    ch_files = sorted(glob.glob(a.chapters))
    cn_files = sorted(glob.glob(a.canon))
    if not ch_files:
        print("no chapter files matched", a.chapters)
        return 2
    if not cn_files:
        print("no canon files matched", a.canon)
        return 2

    print("=" * 78)
    print(f"CANON COPY CHECK — narration {a.n}-grams · quoted runs >= {a.qrun} · "
          f"density fail > {a.budget_fail}w")
    print(f"{len(ch_files)} chapters  x  {len(cn_files)} canon extracts  =  "
          f"{len(ch_files) * len(cn_files)} comparisons")
    print("=" * 78)

    canon = {}
    for c in cn_files:
        with open(c, encoding="utf-8") as f:
            txt = f.read()
        canon[os.path.basename(c)] = (ngrams(txt, a.n), norm(txt))
    # one joined haystack for substring searches; canon file names are not
    # recoverable from it, so run-level attribution uses the per-file norms.
    joined = (" " + NL + " ").join(v[1] for v in canon.values())

    def attribute(run):
        for cname, (_, cn) in canon.items():
            if run in cn:
                return cname
        return "?"

    fails, warns, notes = [], [], []

    for cf in ch_files:
        name = os.path.basename(cf)
        with open(cf, encoding="utf-8") as f:
            text = f.read()
        prose = prose_only(text)
        narr = narration_only(prose)
        ng = ngrams(narr, a.n)
        if not ng:
            notes.append(f"{name}: no narration to check")
            continue

        # ---- check A: narration n-grams -------------------------------------
        hits = 0
        for cname, (cg, _) in canon.items():
            inter = ng & cg
            if inter:
                hits += len(inter)
                first = sorted(inter)[0]
                fails.append(f"[A] {name}: {len(inter)} verbatim {a.n}-gram(s) of NARRATION "
                             f'from {cname} (first: "{first[:70]}...")')

        # ---- checks B and C: quoted speech ----------------------------------
        runs, density = [], 0
        for q in quotes(prose):
            w = norm(q).split()
            if len(w) < min(a.qrun, BUDGET_MIN_RUN):
                continue
            for length, run in longest_runs(w, joined, min(a.qrun, BUDGET_MIN_RUN)):
                runs.append((length, run))
                if length >= BUDGET_MIN_RUN:
                    density += length
        runs.sort(reverse=True)

        if runs:
            longest = runs[0]
            if longest[0] >= a.qrun and not a.report:
                fails.append(f"[B] {name}: {longest[0]}-word verbatim run inside one quote, "
                             f'from {attribute(longest[1])}: "{longest[1][:70]}"')
        if not a.report:
            if density > a.budget_fail:
                fails.append(f"[C] {name}: {density} verbatim canon words in dialogue "
                             f"(ceiling {a.budget_fail}) — this chapter is a transcript, not an "
                             f"adaptation. {len(runs)} borrowed runs.")
            elif density > a.budget_warn:
                warns.append(f"[C] {name}: {density} verbatim canon words in dialogue "
                             f"(advisory {a.budget_warn})")

        status = "CLEAN" if hits == 0 and density <= a.budget_warn else f"{density}w"
        top = f"{runs[0][0]}w" if runs else "-"
        print(f"  {status:<8} {name:<42} {len(ng):>7,} narr-grams  "
              f"{density:>4} verbatim-w  longest {top:>4}")
        if a.report and runs:
            for length, run in runs[:12]:
                print(f"           {length:>3}w  {attribute(run)[:9]}  \"{run[:74]}\"")

    print("-" * 78)
    for n in notes:
        print("  note:", n)
    for w in warns:
        print("  WARN ", w)
    if fails:
        print()
        for f in fails:
            print("  FAIL ", f)
        print()
        print(f"RESULT: FAIL — {len(fails)} copying finding(s).")
        print("Re-stage the scene in this serial's voice. Do not merely shuffle words;")
        print("a reordered 12-gram is still a borrowed thought. A short canon line kept")
        print("on purpose is fine — a scene that drops in unchanged is not.")
        return 1

    print()
    print("RESULT: PASS — no verbatim canon copying detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

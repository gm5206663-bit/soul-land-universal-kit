#!/usr/bin/env python3
"""checks/prose_floor.py — LAYER 1b (new 2026-08-31, THE PROSE LAW).

The user's correction: "you skip things too badly you just write summary… you
so badly summarizing them." The prose floor exists so the summary disease is a
BUILD FAILURE, not a taste argument:

  P1  word counts are REPORTED as information only — LENGTH IS NATURAL, NEVER
      FIXED (user ruling, session r: "if you need 1 lakh words, take it; if it
      needs 10, take it"). No chapter ever fails on length again;
  P2  the appearance line is live: within any window of 3 consecutive chapters
      (67 onward), at least one chapter's prose mentions his appearance/mutation
      vocabulary (mirror, face, jaw, hawk-gold, marks, looks, grown, height,
      peg, older) — APPEARANCE & MUTATION LAW v2.56, enforced at source.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")

FROM_CH = 67
APPEAR_WORDS = re.compile(
    r"mirror|in the face|his face|jaw|hawk-gold|storm-gray|storm-grey|"
    r"marks on his forearms|the marks|blue-black|looks \d|looked sixteen|"
    r"you grew|grown|height|taller|peg|older than the register|year older", re.I)

fails = []
info = []
appear_hits = {}

for fname in sorted(os.listdir(CH)):
    if not (fname.startswith("chapter_") and fname.endswith(".md")):
        continue
    n = int(re.search(r"(\d+)", fname).group(1))
    if n < FROM_CH:
        continue
    txt = open(os.path.join(CH, fname), encoding="utf-8").read()
    cut = txt.find("\n---\n")
    end = txt.find("## End of Chapter")
    header = txt[:cut] if cut != -1 else ""
    prose = txt[cut:end] if cut != -1 and end != -1 else txt
    words = len(prose.split())
    info.append(f"  ch{n}: {words} story words")
    if APPEAR_WORDS.search(prose):
        appear_hits[n] = True

nums = sorted(appear_hits)
for i in range(FROM_CH, max(nums + [FROM_CH]) + 1):
    if not any(k in appear_hits for k in (i - 2, i - 1, i)):
        fails.append(f"P-2 ch{i}: no appearance/mutation vocabulary in prose within "
                     f"a 3-chapter window (APPEARANCE & MUTATION LAW v2.56)")

for f in fails:
    print("FAIL ", f)
if fails:
    sys.exit(1)
print("prose_floor: PASS — appearance line live in every 3-chapter window; "
      f"word counts (natural, no floor):")
for line in info:
    print(line)

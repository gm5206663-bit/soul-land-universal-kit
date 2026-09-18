#!/usr/bin/env python3
"""checks/verify_locks.py — LAYER 2 (new 2026-08-30, from the 'check everything' audit).

Enforces the story's LOCKS and the VOICE LAW against the actual prose of every chapter
(the span between the header '---' and '## End of Chapter'). Footer text is exempt —
footers document the locks and may name them.

FAILS on any of:
  L1  "Divine Stormbringer" in prose (CANCELLED name — THE FOURTH RING LAW)
  L2  "Silver Dragon" in prose (Gu Yue's nature lock)
  L3  a sentence linking Wu Zhangkong to Shrek as his ORIGIN (canon ch204 reveal lock;
      Shrek as a goal/technique-source/Tang-Sect-city is legal and whitelisted)
  L4  the Union being OPENED on-page (D006 — first use still reserved). Mentions are
      legal; only opening-variants fail, and "did not open" is exempt
  L5  Lin Hao putting ON battle armor (BATTLE ARMOR LAW: he may make it, never wear it)
  L6  banned voice tics in prose (THE VOICE LAW): "I would like you to notice",
      "on the record", "this is also a fact", "I have stopped needing to know",
      "I have written that sentence"
  L7  retired measurements in prose: bare "612 kg" / "1,612" / "243 kg" / "318"
  L8  "Soul Scholar rank N" for N>10 (impossible per the RANK RULE)
  L9  "all six" in ch60 (the invitation is for five)
"""
import re
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []

TICS = ["I would like you to notice", "on the record", "this is also a fact",
        "I have stopped needing to know", "I have written that sentence"]

for f in sorted(glob.glob(os.path.join(ROOT, "chapters", "chapter_*.md"))):
    n = int(re.search(r"(\d+)", os.path.basename(f)).group(1))
    txt = open(f, encoding="utf-8").read()
    cut, end = txt.find("\n---\n"), txt.find("## End of Chapter")
    prose = txt[cut:end] if cut != -1 and end != -1 else txt
    flat = re.sub(r"\*", "", prose)

    if re.search(r"divine stormbringer", flat, re.I):
        fails.append(f"L1 ch{n}: 'Divine Stormbringer' appears in prose")
    if re.search(r"silver dragon", flat, re.I):
        fails.append(f"L2 ch{n}: 'Silver Dragon' appears in prose")

    for s in re.split(r"(?<=[.!?])\s+", flat):
        if "Shrek" in s and re.search(r"Zhangkong|his teacher", s):
            if re.search(r"(expelled|origin|came from|hailed from).{0,40}Shrek|Shrek.{0,40}(expelled|origin)", s, re.I):
                fails.append(f"L3 ch{n}: Wu Zhangkong named as Shrek-origin: {s[:100]}")

    for s in re.split(r"(?<=[.!?])\s+", flat):
        if re.search(r"open(ed|ing)?\b.{0,30}\bUnion\b|Union\b.{0,20}\bopen", s) and "did not open" not in s.lower():
            fails.append(f"L4 ch{n}: the Union opened on-page: {s[:100]}")

    for s in re.split(r"(?<=[.!?])\s+", flat):
        if re.search(r"armor|armour", s, re.I) and re.search(r"\b(he|Lin Hao)\b.{0,50}(put on|wore|donned)", s, re.I):
            fails.append(f"L5 ch{n}: Lin Hao dons armor: {s[:100]}")

    for t in TICS:
        if re.search(re.escape(t), flat, re.I):
            fails.append(f"L6 ch{n}: banned voice tic: {t}")

    # L10 — THE CHARACTER LAW (2026-08-31): the user's meta-teaching must never
    # be pasted into a character's mouth. Lecture fingerprints, banned from prose.
    for phrase in ["no law anywhere", "whole existence", "the main engine"]:
        if phrase in flat.lower():
            fails.append(f"L10 ch{n}: doctrine-in-a-mouth fingerprint in prose: {phrase!r}")

    for pat in [r"(?<![0-9,])612 kg", r"1,612", r"(?<![0-9,])243 kg", r"(?<![0-9,])318(?![0-9])"]:
        if re.search(pat, flat):
            fails.append(f"L7 ch{n}: retired measurement {pat!r} in prose")

    if re.search(r"Soul Scholar[ ,]+rank \d+", flat, re.I):
        fails.append(f"L8 ch{n}: 'Soul Scholar rank N' in prose")

    if n == 60 and re.search(r"all six", flat, re.I):
        fails.append(f"L9 ch60: invitation says 'all six' (it is five)")

if fails:
    for x in fails:
        print("FAIL ", x)
    sys.exit(1)
print("verify_locks: PASS — locks, voice tics, retired numbers and rank-rule all clean across all chapters")

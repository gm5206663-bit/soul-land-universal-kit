#!/usr/bin/env python3
"""checks/prose_floor.py — LAYER 1b (THE PROSE LAW, ported).

The user's ruling (verbatim spirit): "complete natural take how much it's take
complete naturally no forced" — LENGTH IS NATURAL, NEVER FIXED. Word counts are
REPORTED as information only; no chapter ever fails on length.

The one hard rule (THE ADAPTABILITY PRESENCE LAW): the OC's innate talent
(user-confirmed: adaptability from birth, a normal kid at the start) must stay
VISIBLE as instinct/personality in the prose. In every window of 3 consecutive
chapters, at least one chapter in which the OC is on-page must carry talent
vocabulary (config: talent_vocab). A window where the OC is off-page everywhere
is exempt (absence is tracked by presence_audit instead).
"""
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
CFG = json.load(open(os.path.join(ROOT, "checks", "config.json"), encoding="utf-8"))

VOCAB = re.compile('|'.join(re.escape(v) for v in CFG['talent_vocab']), re.I)
names = [x for x in (CFG['oc'].get('names') or []) + CFG['oc'].get('aliases', []) if x and x != 'TBD']

fails = []
info = []
present = {}
vocab_hits = {}

for fname in sorted(os.listdir(CH)):
    if not (fname.startswith("chapter_") and fname.endswith(".md")):
        continue
    n = int(re.search(r"(\d+)", fname).group(1))
    txt = open(os.path.join(CH, fname), encoding="utf-8").read()
    end = txt.find("## End of Chapter")
    prose = txt[:end] if end != -1 else txt
    words = len(prose.split())
    info.append(f"  ch{n}: {words} story words (natural — no floor)")
    if names and any(nm in prose for nm in names):
        present[n] = True
    elif CFG['oc']['hero_form'] in prose:
        present[n] = True
    if VOCAB.search(prose):
        vocab_hits[n] = True

if names:
    keys = set(vocab_hits) | set(present)
    for i in range(1, max(keys or [1]) + 1):
        win = range(max(1, i - 2), i + 1)
        if any(k in present for k in win) and not any(k in vocab_hits for k in win):
            fails.append(f"P-1 ch{i}: OC present in a 3-chapter window but no talent vocabulary "
                         f"anywhere in it (ADAPTABILITY PRESENCE LAW)")

for f in fails:
    print("FAIL ", f)
if fails:
    sys.exit(1)
note = "OC name TBD — presence/vocab tracking in STANDBY (set checks/config.json names first)" if not names else ""
print("prose_floor: PASS — word counts natural (no floor)" + (f"; {note}" if note else "; talent vocabulary live in every 3-chapter window"))
for line in info:
    print(line)

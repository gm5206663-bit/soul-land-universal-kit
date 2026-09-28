#!/usr/bin/env python3
"""checks/verify_locks.py — LAYER 2: the story's LOCKS, enforced against the
actual prose of every chapter (everything before '## End of Chapter').
Footers document locks and are exempt.

  L1  'Chameleon' (capital C = hero identity) in prose while Cuff not BOUND
      (lowercase 'chameleon' as animal/metaphor is legal)
  L2  'Versa-Staff' in prose while Cuff not BOUND
  L3  'Evolution!' in prose while Cuff not BOUND
  L4  'Kamé' / 'Kame' / transform phrases in prose before the Kwami arrives
      (footer state: 'Kamé: **not arrived**' means not arrived)
  L5  HAWK MOTH IDENTITY REVEAL: prose may not state/link the identity behind
      Hawk Moth unless D-row REVEAL-HM is ACTIVE in DIVERGENCE_LEDGER.md
  L6  LADYBUG / CAT NOIR IDENTITY REVEALS: same rule, REVEAL-LB / REVEAL-CN
  L7  banned voice tics (config: voice_tics)
  L8  EVOLUTION COOLDOWN LINE: any chapter whose footer shows Evolution used
      must carry a 'cooldown' note in the footer (the 5-minute limit wording
      is USER-TBD — until confirmed, the check only requires the note to exist)
"""
import re
import glob
import os
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []
CFG = json.load(open(os.path.join(ROOT, "checks", "config.json"), encoding="utf-8"))

# reveal-lock overrides from the ledger
active_reveals = set()
led_path = os.path.join(ROOT, "DIVERGENCE_LEDGER.md")
if os.path.exists(led_path):
    led = open(led_path, encoding="utf-8").read()
    for line in led.split("\n"):
        m = re.match(r"^\|\s*(REVEAL-\w+)\s*\|\s*ACTIVE\s*\|", line)
        if m:
            active_reveals.add(m.group(1))

HM_PAT = re.compile(
    r"Hawk Moth[^\n]{0,90}\b(Gabriel|true identity|unmasked|mask is off|is actually)\b"
    r"|\bGabriel\b[^\n]{0,90}\b(is|was|is the one behind|is behind|controls the butterfly suit)\b[^\n]{0,40}\bHawk Moth\b"
    r"|Hawk Moth[^\n]{0,40}\bis (Gabriel|actually Gabriel)\b", re.I)
LB_PAT = re.compile(
    r"Marinette[^\n]{0,70}\b(is|was|became|is the one who is|transforms? into)\b[^\n]{0,30}\bLadybug\b"
    r"|\bLadybug\b[^\n]{0,60}\b(is|was)\b[^\n]{0,20}\bMarinette\b", re.I)
CN_PAT = re.compile(
    r"Adrien[^\n]{0,70}\b(is|was|became|is the one who is|transforms? into)\b[^\n]{0,30}\bCat Noir\b"
    r"|\bCat Noir\b[^\n]{0,60}\b(is|was)\b[^\n]{0,20}\bAdrien\b", re.I)

for f in sorted(glob.glob(os.path.join(ROOT, "chapters", "chapter_*.md"))):
    n = int(re.search(r"(\d+)", os.path.basename(f)).group(1))
    txt = open(f, encoding="utf-8").read()
    end = txt.find("## End of Chapter")
    prose = txt[:end] if end != -1 else txt
    flat = re.sub(r"\*", "", prose)
    footer = txt[end:] if end != -1 else ""

    m_cuff = re.search(r"Cuff:\s*\*\*([^*]+)\*\*", footer)
    m_kame = re.search(r"^Kamé:\s*\*\*([^*]+)\*\*", footer, re.M)
    bound = bool(m_cuff) and m_cuff.group(1).strip().upper().startswith("BOUND")
    kame_state = (m_kame.group(1).strip() if m_kame else "")
    kame_arrived = bool(kame_state) and "not arrived" not in kame_state.lower()

    if not bound:
        if re.search(r"\bChameleon\b", flat):
            fails.append(f"L1 ch{n}: hero identity 'Chameleon' in prose before Cuff: BOUND")
        if "Versa-Staff" in flat:
            fails.append(f"L2 ch{n}: 'Versa-Staff' in prose before Cuff: BOUND")
        if "Evolution!" in flat:
            fails.append(f"L3 ch{n}: 'Evolution!' in prose before Cuff: BOUND")
    if not kame_arrived and re.search(r"Kamé|\bKame\b", flat):
        fails.append(f"L4 ch{n}: Kwami name/phrase in prose before the Kwami arrives")

    if "REVEAL-HM" not in active_reveals and HM_PAT.search(flat):
        m = HM_PAT.search(flat)
        fails.append(f"L5 ch{n}: Hawk Moth identity stated: {flat[max(0,m.start()-40):m.end()+40].strip()[:100]}")
    if "REVEAL-LB" not in active_reveals and LB_PAT.search(flat):
        m = LB_PAT.search(flat)
        fails.append(f"L6 ch{n}: Ladybug identity stated: {flat[max(0,m.start()-40):m.end()+40].strip()[:100]}")
    if "REVEAL-CN" not in active_reveals and CN_PAT.search(flat):
        m = CN_PAT.search(flat)
        fails.append(f"L6 ch{n}: Cat Noir identity stated: {flat[max(0,m.start()-40):m.end()+40].strip()[:100]}")

    for t in CFG["voice_tics"]:
        if t in flat.lower():
            fails.append(f"L7 ch{n}: banned voice tic: {t}")

    m_ev = re.search(r"Evolution:\s*\*\*([^*]+)\*\*", footer)
    if m_ev and re.search(r"\bused\b|\bspent\b|\bactive\b", m_ev.group(1).lower()):
        if "cooldown" not in footer.lower():
            fails.append(f"L8 ch{n}: Evolution marked used but footer carries no cooldown note "
                         f"(5-min hard de-transform fuse — record the clock in the footer)")

for x in fails:
    print("FAIL ", x)
print(f'verify_locks: {len(fails)} FAIL' if fails else "verify_locks: OK")
sys.exit(1 if fails else 0)

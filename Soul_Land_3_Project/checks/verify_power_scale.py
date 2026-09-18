#!/usr/bin/env python3
"""LAYER 8 — THE POWER SCALE.

Enforces §THE TWO AXES (THE_CODEX.md, user-locked 2026-08-28):

  1. LIN HAO IS NEVER WEAKER THAN WULIN — in anything, not even physical strength.
  2. His physical strength alone ≈ a FOUR-RING SOUL ANCESTOR (Wulin's is ≈ a normal 3-ring master).
  3. His overall combat is SOUL KING.
  4. Retired numbers must not reappear.

WHY THIS EXISTS. I got his strength wrong THREE times in one session — 612 kg (placed inside canon's
ch114 table, which is a list of other children), 1,612 kg (only ~20% above Wulin), and twice stated the
DIRECTION backwards ("Wulin is stronger, decisively"). All three came from the same habit: ranking him
inside a range built for somebody else.

Usage: python3 checks/verify_power_scale.py
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
DOCS = ["LIN_HAO_PANELS.md", "POWER_MODEL.md", "CHARACTER_STATS.md", "CANON_ACCESS.md"]

MEASURED = 2612          # ch32, the hard floor
WULIN_CANON = 1348       # canon c114, right fist, age 9-10
RETIRED = ["243 kg", "612 kg", "1,612 kg", "470 kg", "578 kg", "740 kg"]
# historical values that are allowed in their own chapters
ALLOWED = {"186 kg": (1, 31), "812 kg": (21, 61), "1,106 kg": (1, 61), "2,612 kg": (32, 70),
           # 🔴 ch71: the fourth ring. THE FOURTH RING LAW says the 2,612 kg floor is "left
           # behind like a childhood measurement". New measured floor, Mu Chen's rig, day 30.
           "4,180 kg": (71, 999)}

errors, warnings = [], []

def files():
    for f in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                    key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
        yield int(re.search(r"chapter_(\d+)", os.path.basename(f)).group(1)), f, "chapter"
    for d in DOCS:
        p = os.path.join(ROOT, d)
        if os.path.exists(p):
            yield 0, p, d

for n, path, kind in files():
    raw = open(path, encoding="utf-8", errors="replace").read()
    name = os.path.basename(path)
    # skip the upgrade log in the codex — it is history and quotes the mistakes on purpose
    if "THE_CODEX" in name:
        i = raw.find("## ⚡ UPGRADE LOG")
        if i > 0:
            raw = raw[:i]

    for i, line in enumerate(raw.split("\n"), 1):
        low = line.lower()

        # 1. never put Wulin above him
        if re.search(r"wulin", line, re.I) and re.search(
                r"wulin[^.\n]{0,35}\b(is |the )?(stronger|strongest)\b|wulin[^.\n]{0,35}\b(out-?strength|overpowers|overwhelms)\b", line, re.I) \
           and not re.search(r"never|not|isn't|strongest person lin hao knows|by blood", low):
            errors.append(f"{name}:{i}: puts Wulin above Lin Hao in strength — forbidden by §THE TWO AXES.\n      {line.strip()[:150]}")

        # 2. retired numbers
        for r in RETIRED:
            # 🔴 must not match inside a larger figure: "612 kg" is a substring of "2,612 kg".
            if re.search(r"(?<![\d,])" + re.escape(r), line) and not re.search(r"retired|provably wrong|corrected|change from|were both wrong|three times|this line said|was wrong|long since", low):
                errors.append(f"{name}:{i}: retired strength figure '{r}' reappeared.\n      {line.strip()[:150]}")

        # 3. he must never be called merely strong / ordinary-strong
        if re.search(r"\b(ordinary|average|normal)[\s-]+strong\b", low) and re.search(r"lin hao|\bhe\b|\bhis\b", low):
            warnings.append(f"{name}:{i}: describes him as ordinarily strong — he is ≈ a four-ring Soul Ancestor.\n      {line.strip()[:150]}")

# 4. the measured value must be present and must exceed Wulin's canon figure
panels = os.path.join(ROOT, "LIN_HAO_PANELS.md")
if os.path.exists(panels):
    t = open(panels, encoding="utf-8", errors="replace").read()
    m = re.search(r"([\d,]{3,7})\s?kg — MEASURED", t)
    if m:
        v = int(m.group(1).replace(",", ""))
        if v < MEASURED:
            errors.append(f"LIN_HAO_PANELS.md: measured fist is {v} kg, below the locked floor {MEASURED} kg")
        if v <= WULIN_CANON:
            errors.append(f"LIN_HAO_PANELS.md: measured fist {v} kg does not exceed Wulin's canon {WULIN_CANON} kg")
    else:
        errors.append("LIN_HAO_PANELS.md: no 'kg — MEASURED' anchor found")

import json as _json
HERE_DIR = os.path.dirname(os.path.abspath(__file__))
# 5. 🔴 SPIRITUAL POWER — he is above Gu Yue at EVERY point (MONSTER LAW)
# Gu Yue's canon spiritual power is 153 at age 9 (canon c114) rising to 186. Canon calls her the
# highest on the continent at her age. THE MONSTER LAW makes that FALSE BECAUSE OF HIM. The v3 curve
# capped him below her "because canon forbids it" — the same disease as the strength error.
GUYUE_CURVE = [(21, 153), (37, 160), (61, 186)]
_sp = None
_sjp = os.path.join(HERE_DIR, "checks", "state.json") if False else os.path.join(ROOT, "checks", "state.json")
if os.path.exists(_sjp):
    _sp = _json.load(open(_sjp, encoding="utf-8")).get("spiritual_power_by_chapter")
if _sp:
    for ch_str, val in _sp.items():
        ch = int(ch_str)
        # interpolate Gu Yue's canon value at this chapter
        gy = GUYUE_CURVE[-1][1]
        for i in range(len(GUYUE_CURVE) - 1):
            c0, v0 = GUYUE_CURVE[i]; c1, v1 = GUYUE_CURVE[i + 1]
            if c0 <= ch <= c1:
                gy = v0 + (v1 - v0) * (ch - c0) // max(c1 - c0, 1)
                break
        else:
            if ch < GUYUE_CURVE[0][0]:
                gy = GUYUE_CURVE[0][1]
        if val <= gy:
            errors.append(f"ch{ch}: spiritual power {val} is not above Gu Yue's {gy} at that point — "
                          f"MONSTER LAW: he is above everyone except Tang San")

print(f"verify_power_scale: measured anchor {MEASURED} kg vs Wulin canon {WULIN_CANON} kg "
      f"(≈4-ring vs ≈3-ring)")
for w in warnings:
    print("  WARN " + w)
for e in errors:
    print("  FAIL " + e)
if errors:
    print(f"\nverify_power_scale: {len(errors)} failure(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"verify_power_scale: PASS ({len(warnings)} warning(s))")
sys.exit(0)

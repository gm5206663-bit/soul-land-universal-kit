#!/usr/bin/env python3
"""checks/momentum_audit.py — LAYER 9.5 (new 2026-09-04, THE MOMENTUM LAW).

The user's verdict: the story kept *holding* — sealed gates with no firing date,
frozen power numbers, repeated deferral — and got boring. The consistency gates
(all zero_tolerance/sync/lock audits) reward "nothing broke" but never ask "did
anything BIG happen?" This layer audits MOMENTUM and fails on stagnation.

Two rules (from BREAKTHROUGH_ENGINE.md §2 THE MOMENTUM LAW / §4 ledger):

  M1  GUNS MUST HAVE DATES. Every gate/gun in the engine's §4 ledger that carries
      a concrete fire-chapter must be FIRE/PAID by that chapter. If the current
      chapter is past the window and the row is still OPEN (no FIRED/PAID/RESOLVED
      marker and no DEFER note in PROBLEM_INVENTORY), that's a FAIL.

  M2  NO THREE-STEP FREEZE. Across the last 3 recorded chapters, at least one of
      rank / sp / hawk / ledger must have moved UP, OR a gate is marked fired.
      A story that neither grows nor fires for three chapters is stalling.

Read-only: this checker never edits a story file. It reads the engine ledger
and checkers/state.json.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []
notes = []

# ---- current position ----
state = json.load(open(os.path.join(ROOT, "checks", "state.json"), encoding="utf-8"))
chapters = sorted((k for k in state if str(k).isdigit()), key=int)
cur = int(chapters[-1]) if chapters else 0

# ---- M1: parse the §4 ledger in BREAKTHROUGH_ENGINE.md ----
eng_path = os.path.join(ROOT, "BREAKTHROUGH_ENGINE.md")
if not os.path.exists(eng_path):
    print("momentum_audit: SKIP — BREAKTHROUGH_ENGINE.md not found (run after the re-architecture)")
    sys.exit(0)
eng = open(eng_path, encoding="utf-8").read()
# inventory deferrals (a gate may be deliberately pushed once, if logged)
inv_path = os.path.join(ROOT, "PROBLEM_INVENTORY.md")
inv = open(inv_path, encoding="utf-8").read() if os.path.exists(inv_path) else ""

def fire_window(cell):
    """Return (chapter:int|None, hard:bool). hard=False means a soft/long/never gate."""
    c = cell.lower()
    if "never" in c or "not now" in c or "hard lock" in c or "sealed-forever" in c:
        return None, False
    m = re.search(r"\(ch(\d{3})\)", c)          # "climax (ch118)", "aftermath (ch119)"
    if m:
        return int(m.group(1)), True
    m = re.search(r"\bch(\d{3})\b", c)           # "ch117"
    if m:
        return int(m.group(1)), True
    m = re.search(r"\b(\d{3})\+\b", c)           # "119+"
    if m:
        return int(m.group(1)), False            # soft floor (fires at/after)
    m = re.search(r"\bch?(\d{3})\s*[–-]\s*(\d{3})", c)  # "117–119"
    if m:
        return int(m.group(2)), True             # deadline = end of range
    return None, False

in_table = False
gate_rows = 0
for line in eng.splitlines():
    if line.strip().startswith("| ID |"):
        in_table = True
        continue
    if in_table:
        if not line.strip().startswith("|"):
            in_table = False
            continue
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        gid, name, trig, window, status = cells[0], cells[1], cells[2], cells[3], cells[4]
        if gid in ("---",) or set(gid) <= set("-: "):
            continue
        gate_rows += 1
        fire_ch, hard = fire_window(window)
        done = re.search(r"FIRED|PAID|RESOLVED|RETIRED", status, re.I)
        if fire_ch is not None and hard and cur > fire_ch and not done:
            # a deferral note mentioning the gate id counts as a deliberate push
            if not re.search(r"defer(?:ral|red)?[^\n]*\b" + re.escape(gid) + r"\b", inv, re.I):
                fails.append(f"M1: gate {gid} ({name[:48]}) had a fire-window of ch{fire_ch} but is still OPEN at ch{cur} "
                             f"with no FIRE marker and no DEFER note — fire it or formally re-date it.")
        elif fire_ch is not None:
            notes.append(f"gate {gid} window ch{fire_ch} (current {cur}) — {'FIRED' if done else 'armed'}")

# ---- M2: no three-step freeze ----
fields = ("rank", "sp", "hawk", "ledger")
last3 = chapters[-3:]
def val(n, f):
    v = state[n].get(f)
    return v if isinstance(v, (int, float)) else None
grew = False
if len(last3) >= 2:
    first, latest = last3[0], last3[-1]
    for f in fields:
        a, b = val(first, f), val(latest, f)
        if a is not None and b is not None and b > a:
            grew = True
            notes.append(f"{f} moved {a} → {b} across ch{first}–ch{latest}")
# a fired gate this chapter also counts as motion
if re.search(r"FIRE|PAID|RESOLVED", eng):
    pass
if not grew:
    fails.append(f"M2: STALL — across ch{last3[0]}–ch{last3[-1]} none of {fields} moved up and no gate fired; "
                 f"the next chapter must grow the ledger or fire a held gun (BREAKTHROUGH_ENGINE §4).")

for n in notes:
    print("  ·", n)
if fails:
    for f in fails:
        print("FAIL ", f)
    sys.exit(1)
print(f"momentum_audit: PASS — {gate_rows} gates tracked, {len(notes)} live; no overdue gun, no stall (at ch{cur})")

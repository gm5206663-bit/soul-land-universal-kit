#!/usr/bin/env python3
"""checks/sync_audit.py — LAYER 3 (new 2026-08-31, THE SYNC LAW v1.00).

The user's correction: "you should update with every chapter everything that
needed." Chapters 64–67 landed while CHARACTER_STATS (the single source of truth
the footers cite), POWER_MODEL, RELATIONSHIPS and CANON_ACCESS did not move at
all. The footers were verified while the docs around them rotted — the
two-copies disease, one level up.

This layer makes a lagging doc a BUILD FAILURE:

  S1  LIN_HAO_STATUS.md    carries the position chapter and the end values
                           (rank / SP / hawk / ledger)
  S2  CONTINUATION_PROMPT  carries the position chapter and end values
  S3  THE_CODEX            §QUICK REFERENCE carries "end of ch N" + end values
  S4  LIN_HAO_PANELS.md    carries the tracked lines (SP, hawk)
  S5  CHARACTER_STATS §0   "end of fic chapter N" and every ensemble rank
                           parsed and matched against state.json
  S6  CANON_ACCESS.md      names the live canon method (no dead-source doc)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
state = json.load(open(os.path.join(ROOT, "checks", "state.json"), encoding="utf-8"))
fails = []

cur = max(state, key=int)


def last(field):
    v = None
    for n in sorted(state, key=int):
        if state[n].get(field) is not None:
            v = state[n][field]
    return v


rank, sp, hawk, ledger = last("rank"), last("sp"), last("hawk"), last("ledger")
hawk_s = f"{hawk:,}"

# the last chapter that actually records an ensemble
ens = {}
for n in sorted(state, key=int):
    if state[n].get("ensemble"):
        ens = state[n]["ensemble"]

docs = {name: open(os.path.join(ROOT, fname), encoding="utf-8").read()
        for name, fname in [("status", "LIN_HAO_STATUS.md"),
                            ("prompt", "CONTINUATION_PROMPT.md"),
                            ("codex", "THE_CODEX.md"),
                            ("panels", "LIN_HAO_PANELS.md"),
                            ("stats", "CHARACTER_STATS.md"),
                            ("access", "CANON_ACCESS.md"),
                            ("power", "POWER_MODEL.md"),
                            ("rel", "RELATIONSHIPS.md")]}


def need(doc, needle, label):
    forms = {needle, f"{int(needle):,}" if needle.isdigit() else needle}
    if not any(f in docs[doc] for f in forms):
        fails.append(f"S-{label}: {doc} does not carry {needle!r}")


need("status", f"end of Chapter {cur}", "1")
need("status", str(sp), "1")
need("status", hawk_s, "1")
need("status", str(ledger), "1")
need("status", f"rank **{rank}**", "1")

need("prompt", f"end of Chapter {cur}", "2")
need("prompt", str(sp), "2")
need("prompt", hawk_s, "2")

need("codex", f"end of ch {cur}", "3")
need("codex", str(sp), "3")
need("codex", hawk_s, "3")
need("codex", str(ledger), "3")

need("panels", str(sp), "4")
need("panels", hawk_s, "4")

# S5 — CHARACTER_STATS §0 parsed against state.json
m = re.search(r"## 0\. CURRENT STATIONS — end of fic chapter (\d+)", docs["stats"])
if not m:
    fails.append("S-5: CHARACTER_STATS.md has no '## 0. CURRENT STATIONS — end of fic chapter N' block")
else:
    if int(m.group(1)) != int(cur):
        fails.append(f"S-5: CHARACTER_STATS §0 says chapter {m.group(1)}; state says {cur}")
    block = docs["stats"][m.start():docs["stats"].find("\n## ", m.end())]
    for who, val in ens.items():
        if not isinstance(val, int):
            continue
        r = re.search(re.escape(who) + r":\*\* rank \*\*(\d+)\*\*", block)
        if not r:
            fails.append(f"S-5: CHARACTER_STATS §0 has no rank line for {who}")
        elif int(r.group(1)) != val:
            fails.append(f"S-5: CHARACTER_STATS §0 has {who} at {r.group(1)}; state.json says {val}")
    r = re.search(r"Lin Hao:\*\* rank \*\*(\d+)\*\*", block)
    if not r:
        fails.append("S-5: CHARACTER_STATS §0 has no Lin Hao rank line")
    elif int(r.group(1)) != rank:
        fails.append(f"S-5: CHARACTER_STATS §0 has Lin Hao at {r.group(1)}; state.json says {rank}")

# S6 — the live canon method is named
if "readnovelffull" not in docs["access"]:
    fails.append("S-6: CANON_ACCESS.md does not name the live canon source (readnovelffull)")

# S7 — THE SOUL SPIRIT LAW + THE PROSE LAW + the appearance line are carried
# (locked 2026-08-31, sessions n/o: laws that live in one doc only rot; the
#  appearance line is a tracked progression line like rank and hawk)
need("codex", "THE SOUL SPIRIT LAW", "7")
need("codex", "THE PROSE LAW", "7")
need("power", "THE SOUL SPIRIT LAW", "7")
need("status", "SOUL SPIRIT LAW", "7")
need("status", "PROSE LAW", "7")
need("prompt", "SOUL SPIRIT LAW", "7")
need("prompt", "PROSE LAW", "7")
need("panels", "sixteen in the face", "7")
need("panels", "winter-tipped", "7")
need("rel", "winter-tipped", "7")
need("stats", "sixteen in the face", "7")

for f in fails:
    print("FAIL ", f)
if fails:
    sys.exit(1)
print(f"sync_audit: PASS — docs carry end-of-chapter {cur} state "
      f"(rank {rank}, SP {sp}, hawk {hawk_s}, ledger {ledger}, "
      f"{len(ens)} ensemble stations, canon method current, laws + appearance synced)")

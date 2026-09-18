#!/usr/bin/env python3
"""checks/state.py — re-derive story state from the chapter footers.

Rebuilt 2026-08-30 in this workspace (the original checks/ tree was not uploaded).
Layer 0: parses every chapters/chapter_NN.md footer and writes checks/state.json.

Precedence (locked principle D3: "the prose is the story"):
  1. The Character Progression block (hand-written, part of the chapter's own record)
  2. The ## GROWTH header (generated summary at the top of the footer)
Both are captured; where they disagree, Layer 1 (verify_footer_facts.py) FAILS
rather than guessing which is right.

Known parser history (from PROBLEM_INVENTORY D8): the old RE_SP could not see
through '**', took a chain's start instead of its end, and matched narrative
phrases. This parser reads BOTH ends of every 'A → B' chain and records them
separately, and only looks at the footer (after '## End of Chapter'), never at
prose.
"""
import json
import re
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")

def strip(s):
    return s.replace("**", "").replace("*", "").strip()

def chain_val(text, label):
    """Return (end_value, start_value) for 'label A → B' or 'label B' in text."""
    m = re.search(label + r"\s*([\d,]+)\s*(?:→|->)\s*([\d,]+)", text)
    if m:
        return int(m.group(2).replace(",", "")), int(m.group(1).replace(",", ""))
    m = re.search(label + r"\s*([\d,]+)", text)
    if m:
        return int(m.group(1).replace(",", "")), None
    return None, None

state = {}
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"(\d+)", os.path.basename(path)).group(1))
    txt = open(path, encoding="utf-8").read()
    cut = txt.find("## End of Chapter")
    body, footer = (txt[:cut], txt[cut:]) if cut != -1 else (txt, "")

    g = re.search(r"^## GROWTH:(.*?)(?:\n## |\n---|\Z)", footer + "\n---", re.S | re.M)
    growth = strip(g.group(1)) if g else ""
    p = re.search(r"### Character Progression:\n(.*?)(?:\n### |\Z)", footer, re.S)
    prog = strip(p.group(1)) if p else ""
    lh_prog = ""
    m = re.search(r"\*\*Lin Hao:\*\*(.*?)(?:\n- |\n\n|\n###|\Z)", footer, re.S)
    if m:
        lh_prog = " ".join(strip(m.group(1)).split())

    def pick(label):
        a = chain_val(lh_prog, label)
        return a if a[0] is not None else chain_val(growth, label)

    rank, _ = pick(r"rank")
    sp, _ = pick(r"(?:spiritual power|SP)")
    hawk, _ = pick(r"hawk")
    ledger, _ = pick(r"ledger")
    smith = None
    m2 = re.search(r"(\d)(?:st|nd|rd|th)[ -]rank", lh_prog + " " + growth)
    if m2:
        smith = int(m2.group(1))
    rings = None
    WORDNUM = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6}
    m3 = re.search(r"(\d) (?:purple )?rings", lh_prog + " " + growth)
    if not m3:
        m3w = re.search(r"\b(one|two|three|four|five|six) (?:purple |yellow |empty )?rings", lh_prog + " " + growth, re.I)
        if m3w: rings = WORDNUM[m3w.group(1).lower()]
    # "three purple rings, perfectly compatible" etc.
    if m3 and rings is None:
        rings = int(m3.group(1))
    else:
        m3 = re.search(r"rings?: two yellow → two PURPLE", lh_prog + growth, re.I)
        rings = 2 if m3 else rings
    # a ring bestowed mid-chapter counts at chapter end (ch40: "a third ring is bestowed")
    if re.search(r"third (?:ring )?(?:is )?bestowed|\+ one empty third", lh_prog + " " + growth, re.I):
        rings = max(rings or 0, 3)

    # ensemble precedence (fixed 2026-08-31): the '### Ensemble — canon-verified state' block is
    # authoritative; Character Progression lines may carry 'A → B' chains whose START the old
    # single-scan regex grabbed (invisible for 66 chapters because both blocks always agreed).
    ecut = footer.find("### Ensemble")
    esc = footer[ecut:] if ecut != -1 else footer
    ens = {}
    for who in ["Tang Wulin", "Xie Xie", "Gu Yue", "Xu Xiaoyan",
                "Zhang Yangzi", "Wang Jinxi", "Wei Xiaofeng"]:
        mw = re.search(r"\*\*" + who + r":\*\* rank \*?\*?(\d+)", esc)
        if not mw and esc is not footer:
            mw = re.search(r"\*\*" + who + r":\*\* rank \*?\*?(\d+)", footer)
        gone = re.search(r"\*\*" + who + r":\*\*.{0,120}(LEFT|transfers? out|left class zero)",
                         esc, re.S) and not mw
        if mw:
            ens[who] = int(mw.group(1))
        elif gone:
            ens[who] = "out"

    state[n] = {
        "file": os.path.basename(path),
        "title": open(path, encoding="utf-8").readline().strip("# \n").split(":", 1)[-1].strip(),
        "rank": rank, "sp": sp, "hawk": hawk, "ledger": ledger,
        "smith": smith, "rings": rings,
        "growth_rank": (chain_val(growth, r"rank")[0] if growth else None),
        "prog_rank": (chain_val(lh_prog, r"rank")[0] if lh_prog else None),
        "ensemble": ens,
    }

out = os.path.join(ROOT, "checks", "state.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(state, f, indent=1, ensure_ascii=False)

cur = max(state)
print(f"state.json written — {len(state)} chapters, position: end of Chapter {cur}")
def show(k):
    vals = [(n, v[k]) for n, v in state.items() if v[k] is not None]
    if vals:
        print(f"  {k}: {vals[0][1]} → {vals[-1][1]} across {len(vals)} recorded chapters")
for k in ("rank", "sp", "hawk", "ledger", "smith"):
    show(k)
sys.exit(0)

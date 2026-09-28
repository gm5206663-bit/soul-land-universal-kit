#!/usr/bin/env python3
"""CHECK PANELS — the drift guard: every 「...」 panel line in the chapter
bodies must exist in foundation/PANELS.md, and every PANELS.md chapter row
must exist in a chapter body. A frozen or stale meter fails the build.
Run:  python3 soul_land_system_cheat/tools/check_panels.py
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERIAL = os.path.dirname(HERE)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def chapter_panels():
    out = {}
    for p in sorted(glob.glob(os.path.join(SERIAL, "chapters", "Chapter_*.md"))):
        t = open(p, encoding="utf-8").read()
        body = t.split("\n## Footer")[0]
        lines = set()
        for l in body.split("\n"):
            l = l.strip()
            if l.startswith(">"):
                q = norm(l.lstrip("> "))
                if "「" in q:
                    lines.add(q)
        out[os.path.basename(p)] = lines
    return out

def ledger_panels():
    t = open(os.path.join(SERIAL, "foundation", "PANELS.md"), encoding="utf-8").read()
    # only the per-chapter tables (rows starting with | 「), skip grammar placeholders
    lines = set()
    for l in t.split("\n"):
        l = l.strip()
        if l.startswith("| 「"):
            q = norm(l[2:].split("|")[0])
            if "N / N" in q or "NN%" in q:
                continue
            lines.add(q)
    return lines

ch = chapter_panels()
led = ledger_panels()
allch = set().union(*ch.values())
missing_in_ledger = sorted(allch - led)
stale_in_ledger = sorted(led - allch)
for name, lines in ch.items():
    print(f"{name:44s} {len(lines)} panel lines")
print(f"ledger rows: {len(led)}")
ok = True
if missing_in_ledger:
    ok = False
    print("\nDRIFT — in chapters but NOT in PANELS.md (update the ledger):")
    for q in missing_in_ledger: print("   ", q)
if stale_in_ledger:
    ok = False
    print("\nSTALE — in PANELS.md but in NO chapter (update the ledger):")
    for q in stale_in_ledger: print("   ", q)
print("\nPANEL LEDGER", "IN SYNC" if ok else "OUT OF SYNC")
sys.exit(0 if ok else 1)

#!/usr/bin/env python3
"""sl2-golden-lion gate v1.0 — run before EVERY push that touches chapters/.
Exit 0 = GATE PASS. Any FAIL line must be fixed (not bypassed) before push."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []

# 1. foundation presence
for path, why in [
    ("foundation/AUTHORS_LAW.md", "author constitution"),
    ("foundation/CANON_LEDGER.md", "numbered truth"),
    ("foundation/STATUS_PANEL.md", "single-state cards"),
    ("foundation/SERIAL_LOG.md", "serial log"),
    ("foundation/THE_LION_MODULE.md", "lion module"),
    ("foundation/THE_GOLD_REGISTER.md", "golden atlas"),
    ("codex/GLOSSARY.md", "vocabulary"),
]:
    if not os.path.isfile(os.path.join(ROOT, path)):
        fails.append(f"MISSING {path} — {why}")

# 2. ledger rows sequential (001..N)
led = os.path.join(ROOT, "foundation/CANON_LEDGER.md")
if os.path.isfile(led):
    rows = re.findall(r"^(\d{3})\s", open(led, encoding="utf-8").read(), flags=re.M)
    want = [f"{i:03d}" for i in range(1, len(rows) + 1)]
    if rows != want:
        fails.append(f"LEDGER numbering broken: got {rows}")

# 3. panel carries the live cards
pan = os.path.join(ROOT, "foundation/STATUS_PANEL.md")
if os.path.isfile(pan):
    t = open(pan, encoding="utf-8").read()
    for tag in ["HERO", "RING 1", "RING 2", "PENDING", "FORTUNE COMPENSATION QUEUE"]:
        if tag not in t:
            fails.append(f"PANEL missing card section: {tag}")

# 4. chapters: era-law + invention tagging
BANNED = ["Spirit Hall", "spirit hall", "Spirit Empire", "spirit soul", "Spirit Soul", "soul spirit"]
chdir = os.path.join(ROOT, "chapters")
count = 0
if os.path.isdir(chdir):
    for fn in sorted(os.listdir(chdir)):
        if not fn.endswith(".md"):
            continue
        count += 1
        text = open(os.path.join(chdir, fn), encoding="utf-8").read()
        for bad in BANNED:
            if bad in text:
                fails.append(f"{fn}: era-breaker '{bad}' (SL2 law L-02/L-03)")
        if "spirit ring" in text.lower() and "rank" not in text.lower():
            fails.append(f"{fn}: rings present without rank carding — check STATUS_PANEL first")

print(f"chapters: {count} / " + ("GATE PASS" if not fails else "GATE FAIL"))
for f in fails:
    print(" -", f)
sys.exit(0 if not fails else 1)

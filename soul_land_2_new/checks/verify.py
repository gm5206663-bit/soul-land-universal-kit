#!/usr/bin/env python3
"""sl2-golden-lion gate v2.0 — run before EVERY push that touches chapters/.
v2: prose-law enforcement (no-CJK, dialogue floor, 2800-word floor ch3+, Canon Reference header).
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
    ("foundation/JIN_YANG_PAST.md", "past bible"),
    ("codex/GLOSSARY.md", "vocabulary"),
    ("codex/PROSE_METHOD_SL2.md", "prose method"),
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

# 4. P-1 LANGUAGE LAW: no CJK/foreign script anywhere in project text files
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
for dp, dn, fns in os.walk(ROOT):
    for fn in fns:
        if not fn.endswith((".md", ".txt", ".py")):
            continue
        p = os.path.join(dp, fn)
        if CJK.search(open(p, encoding="utf-8").read()):
            fails.append(f"{os.path.relpath(p, ROOT)}: foreign script present (prose law P-1)")

# 5. chapters: era-law + prose-law
BANNED = ["Spirit Hall", "spirit hall", "Spirit Empire", "spirit soul", "Spirit Soul", "soul spirit"]
chdir = os.path.join(ROOT, "chapters")
count = 0
if os.path.isdir(chdir):
    for fn in sorted(os.listdir(chdir)):
        if not fn.endswith(".md"):
            continue
        count += 1
        p = os.path.join(chdir, fn)
        text = open(p, encoding="utf-8").read()
        for bad in BANNED:
            if bad in text:
                fails.append(f"{fn}: era-breaker '{bad}' (SL2 law L-02/L-03)")
        # P-4 dialogue floor: >=3 spoken lines
        pairs = text.count('"') // 2 + text.count("\u201c")
        if pairs < 3:
            fails.append(f"{fn}: only {pairs} dialogue lines (<3, prose law P-4)")
        # P-5 length floor from ch3 onward
        m = re.match(r"Chapter_(\d+)", fn)
        if m and int(m.group(1)) >= 3:
            w = len(text.split())
            if w < 2800:
                fails.append(f"{fn}: {w} words < 2800 floor (prose law P-5)")
        # P-2 header law
        if "Canon Reference:" not in text:
            fails.append(f"{fn}: missing Canon Reference header block (prose law P-2)")

print(f"chapters: {count} / " + ("GATE PASS" if not fails else "GATE FAIL"))
for f in fails:
    print(" -", f)
sys.exit(0 if not fails else 1)

#!/usr/bin/env python3
"""Measure a Devouring Dragon chapter (or all chapters) the house way.

Written s43 (2026-09-21) after a measure-script bug was found: the old
one-sentence-paragraph check stripped trailing punctuation before testing for
it, so it could never fire, and chapter footers claimed "no one-sentence
paragraphs" while the chapters contained short one-line beat paragraphs.
RULING (s43): short one-line beat paragraphs are house style and allowed; the
thing the house bars is the monster single-sentence paragraph, and that is
already barred by the 60-word sentence cap. This tool reports honestly.

Usage:  python3 tools/measure_prose.py chapters/Chapter_17_*.md
        python3 tools/measure_prose.py chapters
"""
import re, statistics, sys, glob, os

RETIRED = ["takers", "the white", "the green", "fold ", "folds", "folding",
           "fringe", "hush", "stillness", "veiling", "the kill-word",
           "standings", "warm breaks", "deep country", "the craft"]

def sentences(block):
    return [s for s in re.split(r'(?<=[.!?])\s+', block) if s.strip()]

def measure(path):
    t = open(path, encoding="utf-8").read()
    body = t.split("## Footer")[0]
    body = "\n".join(l for l in body.split("\n") if not l.startswith("# "))
    paras = [p.strip() for p in body.split("\n") if p.strip() and p.strip() != "---"]
    words = len(body.split())
    prose = re.sub(r'"[^"]*"', "", body)
    sents = sentences(prose)
    lens = [len(s.split()) for s in sents]
    dlg = len(re.findall(r'"([^"]{4,})"', body))
    # one-line beat paragraphs: prose paragraphs holding a single sentence
    beats = 0
    for p in paras:
        if p.startswith('"'):
            continue                      # dialogue line paragraph
        core = re.sub(r'"[^"]*"', "", p).strip()
        if core and len(re.findall(r'[.!?](?=\s|$)', core)) <= 1 and len(core.split()) >= 4:
            beats += 1
    over = [(len(s.split()), s[:70]) for s in sents if len(s.split()) > 60]
    hits = [w for w in RETIRED if w in body.lower()]
    print(f"{os.path.basename(path)}: {words}w | dialogue {dlg} ({dlg/words*1000:.1f}/1000w) | "
          f"avg {sum(lens)/len(lens):.1f} | median {statistics.median(lens):.0f} | max {max(lens)}")
    if over:
        print(f"   OVER 60: {over}")
    print(f"   one-line beat paragraphs: {beats} (allowed, house style)")
    if hits:
        print(f"   RETIRED-WORD HITS (triage): {hits}")
    return words, dlg, max(lens) if lens else 0, beats

if __name__ == "__main__":
    args = sys.argv[1:] or ["chapters"]
    files = []
    for a in args:
        files += sorted(glob.glob(os.path.join(a, "Chapter_*.md"))) if os.path.isdir(a) else [a]
    for f in files:
        measure(f)

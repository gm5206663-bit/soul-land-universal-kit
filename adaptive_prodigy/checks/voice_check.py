#!/usr/bin/env python3
"""voice_check.py — measure the house envelope on one chapter (or a range).

Usage: python3 checks/voice_check.py 65
Reports, per part and whole: prose words, median sentence length, dialogue share
(words inside double quotes). The VOICE LAW baseline is chapters 1-3: short
sentences carry weight; recent-chapter dialogue share has ranged 13.5%-47%.
"""
import re
import sys

n = sys.argv[1] if len(sys.argv) > 1 else "65"
path = f"chapters/chapter_{int(n):02d}.md"
t = open(path, encoding="utf-8").read()
prose = t[t.find("\n---\n"):t.find("## End of Chapter")]
flat = re.sub(r"\*+", "", prose)

parts = re.split(r"\n## ", prose)
for whole in (flat,):
    sents = [x.strip() for x in re.split(r"(?<=[.!?]) +", re.sub(r"\n+", " ", whole)) if x.strip()]
    wl = sorted(len(x.split()) for x in sents)
    tot = sum(wl)
    q = sum(len(m.split()) for m in re.findall(r'"[^"]*"', whole))
    print(f"WHOLE ch{n}: {tot} words · median {wl[len(wl)//2]} · {100*q/tot:.1f}% dialogue")

for part in parts:
    if not part.strip() or part.startswith("# Chapter"):
        continue
    title = part.splitlines()[0][:34]
    body = re.sub(r"\*+", "", part)
    body = re.sub(r"^.*?\n", "", body)
    sents = [x.strip() for x in re.split(r"(?<=[.!?]) +", re.sub(r"\n+", " ", body)) if x.strip()]
    if not sents:
        continue
    wl = sorted(len(x.split()) for x in sents)
    tot = sum(wl)
    q = sum(len(m.split()) for m in re.findall(r'"[^"]*"', body))
    print(f"  {title:<36} {tot:>5} words · med {wl[len(wl)//2]:>2} · {100*q/tot:>5.1f}% dlg")

#!/usr/bin/env python3
"""STYLE GATE — the serial's style laws, self-enforcing.
Hard failures (exit 1): a prose sentence over 60 words; the banned
"the way [clause]" simile construction; a bare (unquoted) panel line.
Warnings: outside the 2,400-3,400 working band (the author may order
over-band carries; the footer records them honestly).
Run:  python3 soul_land_system_cheat/tools/style_gate.py [chapter.md ...]
With no arguments, checks every chapter in chapters/.
"""
import re, sys, glob, os, statistics

IDIOM_OK = ("all the way", "on the way", "opens the way", "the way of", "by the way")
def _exceptions():
    here=os.path.dirname(__file__)
    ex=os.path.join(here,'style_gate_exceptions.txt')
    return [l.split('#')[0].strip() for l in open(ex,encoding='utf-8').read().splitlines() if l.split('#')[0].strip()] if os.path.exists(ex) else []
def the_way_hits(body):
    hits=[]
    for m in re.finditer(r'.{0,40}\bthe way\b.{0,40}', body):
        s=m.group(0); low=s.lower()
        if any(i in low for i in IDIOM_OK): continue
        if any(e.lower() in low for e in _exceptions()): continue
        hits.append(s.strip())
    return hits

def check(path):
    t=open(path,encoding='utf-8').read()
    body=t.split('\n## Footer')[0]
    lines=[l for l in body.split('\n') if l.strip() and not l.startswith('# ')]
    prose=[l for l in lines if not l.startswith('>')]
    panels=[l for l in lines if l.startswith('>')]
    words=len(('\n'.join(lines)).split())
    sent=[s for l in prose for s in re.split(r'(?<=[.!?])\s+',l.strip()) if s]
    sl=[len(s.split()) for s in sent]
    over=[ (n,s) for n,s in zip(sl,sent) if n>60 ]
    tw=the_way_hits(body)
    bare=[l for l in body.split('\n') if l.strip().startswith('「') ]
    dlg=len([l for l in lines if '"' in l])
    band = 'IN' if 2400<=words<=3400 else ('OVER' if words>3400 else 'UNDER')
    hard = bool(over or tw or bare)
    name=os.path.basename(path)
    print(f"{name:42s} {words:5d}w band:{band:5s} avg:{statistics.mean(sl):4.1f} med:{statistics.median(sl):3.0f} max:{max(sl):2d} dlg:{dlg:3d} ({dlg/words*1000:4.1f}/1k) over60:{len(over)} the-way:{len(tw)} bare-panels:{len(bare)}")
    for n,s in over: print(f"    OVER60 [{n}w]: {s[:100]}...")
    for s in tw:      print(f"    THE-WAY: ...{s}...")
    return hard

paths=sys.argv[1:] or sorted(glob.glob(os.path.join(os.path.dirname(__file__),'..','chapters','Chapter_*.md')))
print("THE SYSTEM CHEAT — STYLE GATE\n" + "="*72)
failed=False
for p in paths:
    failed |= check(p)
print("="*72)
print("FAIL" if failed else "ALL HARD CHECKS PASS (band warnings are the author's call)")
sys.exit(1 if failed else 0)

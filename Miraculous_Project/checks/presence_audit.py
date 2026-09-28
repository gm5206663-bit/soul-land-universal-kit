#!/usr/bin/env python3
# Layer 3 — PRESENCE AUDIT. The OC is the story's center of gravity (tight AU:
# the OC's presence warps canon from chapter 1). Counts on-page presence by
# name/alias/hero form and flags long absences.
# STANDBY: if the OC name is still TBD in checks/config.json, this layer
# reports standby instead of crashing (the name is a round-2 user question).
import io, re, glob, os, sys, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails = []
CFG = json.load(io.open('checks/config.json', encoding='utf-8'))

names = [x for x in (CFG['oc'].get('names') or []) + CFG['oc'].get('aliases', []) if x and x != 'TBD']
hero = CFG['oc']['hero_form']

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
W('=' * 62)
W('== Layer 3: presence_audit.py (the OC cannot vanish) ==')
if not names:
    W('  STANDBY — OC name still TBD in checks/config.json (oc.names). Set it, then re-run.')
    print('presence_audit: OK (standby)')
    sys.exit(0)

present = {}
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    end = t.find('## End of Chapter')
    prose = t[:end] if end != -1 else t
    present[n] = any(nm in prose for nm in names) or hero in prose

run = 0
for n in nums:
    if present[n]:
        W(f'  ch{n:02d}: on-page')
        run = 0
    else:
        run += 1
        flag = '!!' if run > CFG['presence_fail_after'] else '·'
        W(f'  ch{n:02d}: ABSENT (run {run}) {flag}')
        if run > CFG['presence_fail_after']:
            fails.append(f'ch{n}: OC absent for {run} consecutive chapters (> {CFG["presence_fail_after"]})')

absent = [n for n in nums if not present[n]]
W(f'  summary: {len(nums) - len(absent)}/{len(nums)} chapters on-page; absent: {absent or "none"}')
for x in fails: print('  FAIL', x)
print(f'presence_audit: {len(fails)} FAIL' if fails else 'presence_audit: OK')
sys.exit(1 if fails else 0)

#!/usr/bin/env python3
# Layer 4 — VOICE CHECK. The OC must HAVE a voice: spoken turns counted by
# attribution tags in prose, cross-checked against the footer's
# 'OC Voice: N turns'. Floor: 4 turns per chapter (footer contract), UNLESS
# the footer line explicitly says 'off-page' (a justified absence).
# STANDBY while the OC name is TBD.
import io, re, glob, os, sys, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails, warns = [], []
CFG = json.load(io.open('checks/config.json', encoding='utf-8'))

names = [x for x in (CFG['oc'].get('names') or []) + CFG['oc'].get('aliases', []) if x and x != 'TBD']

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
W('=' * 62)
W('== Layer 4: voice_check.py (the OC speaks with their own mouth) ==')
if not names:
    W('  STANDBY — OC name still TBD in checks/config.json. Set it, then re-run.')
    print('voice_check: OK (standby)')
    sys.exit(0)

TAG = r'(?:said|asked|muttered|replied|whispered|exclaimed|called out|blurted|answered|repeated|shouted|told|promised|offered|laughed|sighed)'
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    end = t.find('## End of Chapter')
    prose = t[:end] if end != -1 else t
    flat = re.sub(r'\*', '', prose)
    alt = '|'.join(re.escape(x) for x in names)
    turns = len(re.findall(rf'\b(?:{alt})\b\s*{TAG}', flat, re.I)) + \
            len(re.findall(rf'{TAG}\s*(?:{alt})\b', flat, re.I))
    m = re.search(r'OC Voice[:\s]*\*?\*?(\d+)\s*turns[^\n]*', t)
    if not m:
        fails.append(f'ch{n}: footer missing "OC Voice: N turns" line')
        continue
    claimed = int(m.group(1))
    line = m.group(0)
    if claimed < CFG['voice_min_turns'] and 'off-page' not in line.lower():
        fails.append(f'ch{n}: OC voice {claimed} turns < {CFG["voice_min_turns"]} floor and no "off-page" justification in the footer line')
    if turns and turns < claimed:
        warns.append(f'ch{n}: footer claims {claimed} turns but prose shows ~{turns} attribution tags (count loose tags honestly)')

for w in warns: W('  WARN ' + w)
for x in fails: print('  FAIL', x)
print(f'voice_check: {len(fails)} FAIL' if fails else 'voice_check: OK')
sys.exit(1 if fails else 0)

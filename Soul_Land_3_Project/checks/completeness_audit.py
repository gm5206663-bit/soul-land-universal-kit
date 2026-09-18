#!/usr/bin/env python3
# Layer 9 — COMPLETENESS AUDIT (the user's utilization mandate, 09-03:
# "check everything, USE everything, do everything"). An organ that exists
# but is not used is rot with good posture. Hard rules (FAIL) + suggestions.
import io, re, glob, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails, sugg = [], []
nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
newest = nums[-1]

W('=' * 62)
W('== Layer 9: completeness_audit.py (exists is not enough — everything gets USED) ==')

# R1 BANK FRESHNESS — the gold's banks may not age past 6 chapters
sg = io.open('STYLE_GOLD.md', encoding='utf-8').read()
bank_max = max(int(x) for x in re.findall(r'\bc(\d{2,3})\b', sg)) if re.findall(r'\bc(\d{2,3})\b', sg) else 0
if bank_max < newest - 6:
    fails.append(f'R1 bank freshness: STYLE_GOLD cites max c{bank_max}; newest ch{newest} (banks stale >6 — extend the cliff/shape banks)')
else:
    W(f'  R1 banks fresh (max cite c{bank_max} vs ch{newest})')

# R2 GENEALOGY COVERAGE — every STORM/ACTIVE break thread has a genealogy line
led = io.open('DIVERGENCE_LEDGER.md', encoding='utf-8').read()
be = io.open('BUTTERFLY_EFFECTS.md', encoding='utf-8').read()
manual = be[be.find('<!-- MANUAL:START -->'):be.find('<!-- MANUAL:END -->')] if '<!-- MANUAL:START -->' in be else ''
for line in led.split('\n'):
    if re.match(r'^\| D\d+ \| (ACTIVE|HELD) \| (STORM|break) \|', line):
        thread = line.split('|')[4].strip()
        key = thread.replace('the-', '').split('-')[0].lower()
        if key not in manual.lower():
            fails.append(f'R2 genealogy gap: [{thread}] has no genealogy line (births must be mapped)')
if not any(f.startswith('R2') for f in fails):
    W('  R2 genealogy covers every STORM/break thread')

# R3 POWER-BIBLE COVERAGE — the newest power classes must live in POWER_MODEL
pm = io.open('POWER_MODEL.md', encoding='utf-8').read()
recent = ''.join(io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read() for n in nums[-8:])
for kw in ['weapon intent', 'Emperor', 'spirit refin']:
    if kw.lower() in recent.lower() and kw.lower() not in pm.lower():
        fails.append(f'R3 power bible gap: "{kw}" is live in recent chapters but absent from POWER_MODEL')
if not any(f.startswith('R3') for f in fails):
    W('  R3 power bible carries every live power class')

# R4 REGISTRY SUGGESTIONS — held-list names aging without a world row (advisory)
ws = io.open('WORLD_STATE.md', encoding='utf-8').read()
names = set()
for n in nums[-10:]:
    foot = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    i = foot.find('NOT triggered')
    if i != -1:
        seg = foot[i:]
        for m in re.finditer(r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b', seg):
            names.add(m.group(1))
known_skip = {'Divine Stormbringer', 'Sea God', 'Grandmaster Yu', 'Liu Erlong', 'Elder Cai', 'Zhuo Shi', 'Elder Li', 'Wu Zhangkong', 'Shen Yi', 'Mu Chen'}
for nm in sorted(names):
    if nm not in known_skip and nm not in ws:
        sugg.append(f'Registry: "{nm}" appears in held lists but has no WORLD_STATE row')
for s in sugg: W('  SUGGEST ' + s)

# R5 BRIEF TARGETS — the cockpit must keep carrying the standing laws
br = io.open('BRIEF.md', encoding='utf-8').read() if os.path.exists('BRIEF.md') else ''
for probe in ['RECORD STACK', 'COVERAGE IS ELASTIC']:
    if probe not in br:
        fails.append(f'R5 brief lost target: "{probe}" missing from BRIEF.md')
if not any(f.startswith('R5') for f in fails):
    W('  R5 brief carries the standing targets')

W('=' * 62)
for f in fails: print('  FAIL ' + f)
print(f'completeness_audit: {len(fails)} FAIL')
sys.exit(1 if fails else 0)

#!/usr/bin/env python3
# Layer 9 — COMPLETENESS AUDIT (the utilization mandate: check everything,
# USE everything, do everything). An organ that exists but is not used is rot
# with good posture. Hard rules (FAIL) + suggestions.
import io, re, glob, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails, sugg = [], []
nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
newest = nums[-1] if nums else 0

W('=' * 62)
W('== Layer 9: completeness_audit.py (exists is not enough — everything gets USED) ==')

# R1 BANK FRESHNESS — STYLE_GOLD's banks may not age past 6 chapters
if os.path.exists('STYLE_GOLD.md') and nums:
    sg = io.open('STYLE_GOLD.md', encoding='utf-8').read()
    cites = re.findall(r'\bc(\d{2,3})\b', sg)
    bank_max = max(int(x) for x in cites) if cites else 0
    if bank_max < newest - 6:
        fails.append(f'R1 bank freshness: STYLE_GOLD cites max c{bank_max}; newest ch{newest} (banks stale >6 — extend the banks)')
    else:
        W(f'  R1 banks fresh (max cite c{bank_max} vs ch{newest})')

# R2 GENEALOGY COVERAGE — every ACTIVE/STORM D-row thread has a genealogy line
if os.path.exists('DIVERGENCE_LEDGER.md') and os.path.exists('BUTTERFLY_EFFECTS.md'):
    led = io.open('DIVERGENCE_LEDGER.md', encoding='utf-8').read()
    be = io.open('BUTTERFLY_EFFECTS.md', encoding='utf-8').read()
    manual = be[be.find('<!-- MANUAL:START -->'):be.find('<!-- MANUAL:END -->')] if '<!-- MANUAL:START -->' in be else ''
    for line in led.split('\n'):
        m = re.match(r'^\|\s*(D-\d+|REVEAL-\w+)\s*\|\s*ACTIVE\s*\|\s*([^|]+)\|', line)
        if m:
            thread = m.group(2).strip()
            key = thread.replace('the-', '').split('-')[0].split(' ')[0].lower()
            if key and key not in manual.lower() and len(key) > 3:
                fails.append(f'R2 genealogy gap: [{thread}] has no genealogy line in BUTTERFLY_EFFECTS.md manual block')
    if not any(f.startswith('R2') for f in fails):
        W('  R2 genealogy covers every ACTIVE thread')

# R3 POWER-BIBLE COVERAGE — live power vocabulary must live in POWER_MODEL
if os.path.exists('POWER_MODEL.md') and nums:
    pm = io.open('POWER_MODEL.md', encoding='utf-8').read()
    recent = ''.join(io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read() for n in nums[-8:])
    for kw in ['Versa-Staff', 'Evolution', 'resonance', 'camouflage', 'kwami', 'Miraculous']:
        if kw.lower() in recent.lower() and kw.lower() not in pm.lower():
            fails.append(f'R3 power bible gap: "{kw}" is live in recent chapters but absent from POWER_MODEL.md')
    if not any(f.startswith('R3') for f in fails):
        W('  R3 power bible carries every live power class')

# R4 REGISTRY SUGGESTIONS — names in Character States / NOT triggered without a W-row
if os.path.exists('WORLD_STATE.md') and nums:
    ws = io.open('WORLD_STATE.md', encoding='utf-8').read()
    names = set()
    for n in nums[-10:]:
        foot = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
        for secname in ('Character States', 'NOT triggered'):
            i = foot.find(secname)
            if i != -1:
                seg = foot[i:foot.find('##', i + 1) if foot.find('##', i + 1) != -1 else len(foot)]
                for m2 in re.finditer(r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b', seg):
                    if m2.group(1) not in ('Character States', 'NOT triggered', 'State Line', 'Spectator Test'):
                        names.add(m2.group(1))
    skip = {'KIDZ Plus', 'Place des', 'TVi Tower', 'Weather Girl', 'Grand KIDZ', 'Dupain Cheng', 'Agreste Family', 'Cafe Reserve'}
    for nm in sorted(names):
        if nm not in skip and nm not in ws:
            sugg.append(f'Registry: "{nm}" appears in footer sections but has no WORLD_STATE row')
    for s in sugg: W('  SUGGEST ' + s)

# R5 BRIEF TARGETS — the cockpit must keep carrying the standing laws
if os.path.exists('BRIEF.md'):
    br = io.open('BRIEF.md', encoding='utf-8').read()
    for probe in ['BUTTERFLY LAW', 'NO FORCED LENGTH']:
        if probe not in br:
            fails.append(f'R5 brief lost target: "{probe}" missing from BRIEF.md (rerun checks/brief.py)')
    if not any(f.startswith('R5') for f in fails):
        W('  R5 brief carries the standing laws')

# R6 ORE COVERAGE — every slot marked ORE DONE in SEASON1_INDEX has a file on disk
idx = io.open('canon_extract/SEASON1_INDEX.txt', encoding='utf-8').read()
for m in re.finditer(r'^#\s*(\d{2})\s*\|[^|]*\|[^|]*\|[^|]*\|\s*ORE DONE', idx, re.M):
    if not glob.glob(f'canon_extract/episodes/s1e{int(m.group(1)):02d}_*.txt'):
        fails.append(f'R6 ore claim: slot {m.group(1)} marked ORE DONE but no file in canon_extract/episodes/')

W('=' * 62)
for f in fails: print('  FAIL ' + f)
print(f'completeness_audit: {len(fails)} FAIL' if fails else 'completeness_audit: OK')
sys.exit(1 if fails else 0)

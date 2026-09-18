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

# R6 LIVING PRESENCE (user mandate 09-03: "soul skills of Lin Hao completely ignored" -
# named things that stop appearing silently die; measured: Wind-Step 47 ch silent, Gale Talon 32)
import re as _re6, io as _io6, glob as _g6
_chs = sorted(int(_re6.findall(r'\d+', f)[0]) for f in _g6.glob('chapters/chapter_*.md'))
_new = _chs[-1]
def _prose(n):
    t = _io6.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    e = t.find('## End of Chapter')
    return t[:e] if e != -1 else t
_pi = _io6.open('PROBLEM_INVENTORY.md', encoding='utf-8').read()
def _debt(tag): return f'BH{tag}' in _pi
# a) skill currency (Hawk-Soul Union exempt: reserved by law D006/K7)
for _sk in ['Wind-Step', 'Gale Talon', 'Domineer', 'Frost Abyss']:
    _last = max([n for n in _chs if _re6.search(_sk, _prose(n))] or [0])
    if _new - _last > 12:
        if not _debt(4):
            fails.append(f'R6 skill {_sk}: last on-page ch{_last} ({_new-_last} ch silent) and no BH4 debt logged')
        else:
            sugg.append(f'R6 skill {_sk} silent {_new-_last} ch (BH4 logged - owed ch102/103)')
# b) bond currency: Wulin + bond-vocabulary in one prose within 5 ch, or BH5
_bv = _re6.compile(r'ledger|captain|the roof|his brother|the hem|confer')
if not any(('Wulin' in _prose(n) and _bv.search(_prose(n))) for n in _chs[-5:]):
    if not _debt(5): fails.append('R6 bond: no Wulin bond-vocabulary beat in 5 chapters and no BH5 debt logged')
    else: sugg.append('R6 bond beat >5 ch (BH5 logged - owed soon)')
# c) ensemble rotation: each of the four in prose within 3 ch, or BH5
for _nm in ['Wulin', 'Xie Xie', 'Xiaoyan', 'Gu Yue']:
    if not any(_nm in _prose(n) for n in _chs[-3:]):
        if not _debt(5): fails.append(f'R6 ensemble: {_nm} absent from prose 3 chapters and no BH5 debt logged')
        else: sugg.append(f'R6 ensemble {_nm} absent 3 ch (BH5 logged)')
# d) mutation-stage currency: stage vocabulary within 10 ch, or BH1
_ms = _re6.compile(r'storm-gray|hawk-gold|glacier|scale-|sheen|near-silver|lengthened|the marks|breath fog')
if not any(_ms.search(_prose(n)) for n in _chs[-10:]):
    if not _debt(1): fails.append('R6 mutation stage: no stage vocabulary in 10 chapters and no BH1 debt logged')
    else: sugg.append('R6 mutation stage quiet 10 ch (BH1 logged - the deep-water reveal owed)')
if not any(f.startswith('R6') for f in fails):
    W('  R6 living presence: skills/bond/ensemble/mutation current or debt-logged')

W('=' * 62)
for f in fails: print('  FAIL ' + f)
print(f'completeness_audit: {len(fails)} FAIL')
sys.exit(1 if fails else 0)

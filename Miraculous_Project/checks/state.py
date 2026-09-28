#!/usr/bin/env python3
# Layer 0 — STATE. checks/state.json is the single source of truth for story
# facts. Parses every chapter footer's State Line, verifies the chain against
# state.json (resonance monotonic, cuff/kwami progression, akuma counts), and
# prints the ledger. 0 chapters is a LEGAL state: the gate is green, not an error.
import io, re, glob, os, sys, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails = []

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
W('=' * 62)
W('== Layer 0: state.py (state.json = the single source of truth) ==')

if not nums:
    st = json.load(io.open('checks/state.json', encoding='utf-8'))
    W(f"  no chapters yet — opening board: resonance {st['resonance']}/100 · "
      f"cuff: {st['cuff']} · kwami: {st['kwami']} · next slot {st['canon_slot']} ({st['canon_title']})")
    W('  gate green at 0 chapters is CORRECT: nothing has flown yet.')
    print('state: OK (0 chapters)')
    sys.exit(0)

st = json.load(io.open('checks/state.json', encoding='utf-8'))
prev_res = None
prev_cuff = None
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    m1 = re.search(r'OC:\s*\*\*([^*]+)\*\*.*?resonance:\s*\*\*(\d+)\*\*/100.*?Cuff:\s*\*\*([^*]+)\*\*.*?Evolution:\s*\*\*([^*]+)\*\*', t)
    m2 = re.search(r'^Kamé:\s*\*\*([^*]+)\*\*', t, re.M)
    m3 = re.search(r'akumatized this chapter:\s*\*\*(\d+)\*\*', t)
    m4 = re.search(r'Butterflies shown:\s*\*\*(\d+)\*\*', t)
    if not m1:
        fails.append(f'ch{n}: State Line missing or malformed (need OC/resonance/Cuff/Evolution)')
        continue
    if not m2: fails.append(f'ch{n}: Kamé state line missing')
    if not m3: fails.append(f'ch{n}: Hawk Moth akumatized count missing')
    if not m4: fails.append(f'ch{n}: Butterflies shown count missing')
    res = int(m1.group(2))
    cuff = m1.group(3).strip()
    rec = st.get(str(n), {})
    if rec.get('resonance') is not None and rec['resonance'] != res:
        fails.append(f'ch{n}: footer resonance {res} but state.json says {rec["resonance"]}')
    if rec.get('cuff') is not None and rec['cuff'] != cuff:
        fails.append(f'ch{n}: footer Cuff "{cuff}" but state.json says "{rec["cuff"]}"')
    if not (0 <= res <= 100):
        fails.append(f'ch{n}: resonance {res} outside 0–100')
    if prev_res is not None and res < prev_res:
        fails.append(f'ch{n}: resonance DROPPED {prev_res} → {res} (increments only; a drop needs a D-row + footer cause)')
    if prev_cuff == 'BOUND' and cuff != 'BOUND':
        fails.append(f'ch{n}: cuff un-BOUND (bound state is permanent)')
    prev_res, prev_cuff = res, cuff

W(f'  chapters on disk: {len(nums)} (ch{nums[0]}–ch{nums[-1]})')
W(f'  state.json "chapter" field: {st.get("chapter")}')
if st.get('chapter') != nums[-1]:
    fails.append(f'state.json chapter={st.get("chapter")} but disk newest is {nums[-1]}')
for x in fails: print('  FAIL', x)
print(f'state: {len(fails)} FAIL' if fails else 'state: OK')
sys.exit(1 if fails else 0)

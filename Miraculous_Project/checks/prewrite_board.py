#!/usr/bin/env python3
# PREWRITE BOARD — print BEFORE drafting a chapter. Assembles everything the
# writer must know: next canon slot + ore status, active/held D-rows, identity
# lock status, world pressure, and the footer contract reminder.
import io, re, glob, os, sys, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print

st = json.load(io.open('checks/state.json', encoding='utf-8'))
CFG = json.load(io.open('checks/config.json', encoding='utf-8'))
nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
newest = nums[-1] if nums else 0

W('=' * 62)
W(f'== PREWRITE BOARD — writing chapter {newest + 1} ==')

# --- canon ---
idx = io.open('canon_extract/SEASON1_INDEX.txt', encoding='utf-8').read()
slot = st.get('canon_slot', 1)
m_slot = re.search(rf'^#\s*{slot:02d}\s*\|\s*\d+\s*\|([^|]+)\|([^|]*)\|([^|]*)', idx, re.M)
title, fr, ore_status = ('?', '?', '?')
if m_slot:
    title, fr, ore_status = m_slot.group(1).strip(), m_slot.group(2).strip(), m_slot.group(3).strip()
ore_file = f'canon_extract/episodes/s1e{slot:02d}_*.txt'
ore_exists = glob.glob(ore_file)
W(f'  canon slot: {slot}/26 — {title} (FR: {fr}) · N° {100 + slot}')
W(f'  ore: {"EXISTS -> " + ", ".join(os.path.basename(x) for x in ore_exists) if ore_exists else "MISSING — extract first (SEASON1_INDEX.txt recipe)"}')
if not ore_exists:
    W('  !! DO NOT DRAFT THE CHASE/EPISODE BEATS WITHOUT ORE. Distill, then write.')

# --- identity lock ---
bound = str(st.get('cuff', '')).upper().startswith('BOUND')
kame = st.get('kwami', 'not arrived')
W(f'  identity lock: {"LIFTED" if bound else "ENGAGED — banned in prose: Chameleon / Versa-Staff / Evolution! / Kamé (if Kwami not arrived)"}')
W(f'  Kwami state: {kame} · Cuff state: {st.get("cuff")} · Evolution: {st.get("evolution")} · resonance: {st.get("resonance")}/100')

# --- D-rows ---
if os.path.exists('DIVERGENCE_LEDGER.md'):
    led = io.open('DIVERGENCE_LEDGER.md', encoding='utf-8').read()
    W('  D-rows:')
    for line in led.split('\n'):
        m = re.match(r'^\|\s*(D-\d+|REVEAL-\w+)\s*\|\s*(ACTIVE|HELD|RESOLVED|DORMANT)\s*\|\s*([^|]*)\|\s*([^|]*)\|', line)
        if m:
            tag = {'ACTIVE': '>>', 'HELD': '··', 'RESOLVED': '✓ ', 'DORMANT': '--'}[m.group(2)]
            W(f'    {tag} {m.group(1)} [{m.group(2)}] {m.group(3).strip()}: {m.group(4).strip()[:80]}')

# --- world pressure ---
W('  world pressure (WORLD_STATE.md registry):')
rows = []
for line in io.open('WORLD_STATE.md', encoding='utf-8'):
    if re.match(r'^\| W\d+ \|', line):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) >= 6:
            rows.append(dict(id=c[0], name=c[1], kind=c[2], probes=[p.strip() for p in c[3].split('/') if p.strip()], goal=c[4], move=c[5]))
prose_map = {}
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    prose_map[n] = t[:t.find('## End of Chapter')].lower()
press = []
for r in rows:
    ls = 0
    for n in nums:
        if any(p.lower() in prose_map[n] for p in r['probes']):
            ls = max(ls, n)
    age = (newest - ls) if ls else 999
    thresh = {'near': 8, 'object': 10, 'due': 6}.get(r['kind'])
    if thresh and age >= thresh:
        press.append((age, r, ls))
for age, r, ls in sorted(press, key=lambda x: x[0], reverse=True):
    W(f'    RED {r["name"]} — age {age if ls else "∞ (never on-page)"} — goal: {r["goal"][:70]}')
if not press:
    W('    (none flagged yet — the near-world is young)')
W('  RULE: pressure PROPOSES, never mandates — an honest HOLD is an answer.')

# --- footer contract reminder ---
W('  FOOTER CONTRACT (THE_CODEX §FOOTER): State Line (OC/talent/resonance/Cuff/Evolution + Kamé + Hawk Moth + Butterflies shown) · Spectator Test · OC Voice ≥4 turns · D-rows cited · Panel (non-Keal beat, L-17) · Canon Anchors · Butterflies This Chapter (≥3) · Character States · NOT triggered.')
W('=' * 62)

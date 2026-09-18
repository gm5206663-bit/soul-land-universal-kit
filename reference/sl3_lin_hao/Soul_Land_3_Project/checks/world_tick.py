#!/usr/bin/env python3
# Layer 8 — WORLD TICK (the living-world engine; WORLD_STATE.md is the registry).
# Recomputes every entity's clock from actual PROSE (footers don't count as life),
# flags aging actors, and emits the pressure questions. Fails only if the registry
# is unparseable — pressure is information, not verdict (LAW pp symmetry).
import io, re, glob, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fail = []

rows = []
for line in io.open('WORLD_STATE.md', encoding='utf-8'):
    if re.match(r'^\| W\d+ \|', line):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) >= 6:
            rows.append(dict(id=c[0], name=c[1], kind=c[2],
                             probes=[p.strip() for p in c[3].split('/') if p.strip()],
                             goal=c[4], move=c[5]))
if not rows:
    print('world_tick: FAIL — WORLD_STATE.md unparseable'); sys.exit(1)

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
lastn = nums[-1]
prose = {}
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    prose[n] = t[:t.find('## End of Chapter')].lower()

def last_seen(r):
    best = 0
    for n in nums:
        if any(p.lower() in prose[n] for p in r['probes']):
            best = max(best, n)
    return best

W('=' * 62)
W('== Layer 8: world_tick.py (the world between chapters — silence must be a decision) ==')
near = object_ = due = far = 0
press = []
for r in rows:
    ls = last_seen(r)
    age = (lastn - ls) if ls else 999
    k = r['kind']
    if k == 'near': near += 1
    elif k == 'object': object_ += 1
    elif k == 'due': due += 1
    else: far += 1
    thresh = {'near': 8, 'object': 10, 'due': 6}.get(k)
    if thresh and age >= thresh:
        press.append((age, r, ls))
W(f'  registry: {len(rows)} entities — {near} near · {object_} objects · {due} due · {far} far')
if press:
    W('  WORLD PRESSURE (answer each before writing: derive an offscreen beat — a line, a scene — or HOLD knowingly):')
    for age, r, ls in sorted(press, key=lambda x: x[0], reverse=True):
        flag = '\U0001F534' if age >= 16 else '\U0001F7E1'
        W(f'    {flag} {r["name"]} — age {age if ls else "∞ (never on-page)"} (last prose ch{ls if ls else "—"}) — their goal: {r["goal"][:66]}')
        W(f'       implied move: {r["move"][:84]}')
else:
    W('  no flagged entities — the near-world is young; the far-world listed in WORLD_STATE.md')
W("  RULE: pressure PROPOSES, never mandates (LAW pp symmetry) — an honest HOLD is an answer; accidental silence is not.")
W('=' * 62)
print('world_tick: OK')

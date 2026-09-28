#!/usr/bin/env python3
# Builds BUTTERFLY_EFFECTS.md — the complete evidence base of every butterfly
# already flown, mined from chapter footers (the 'Butterflies This Chapter'
# section, any list style) + the session registry + the manual genealogy block.
# Regenerate after any chapter sync:  python3 checks/build_butterfly_effects.py
# Manual blocks between <!-- MANUAL:START/END --> markers are preserved.
import io, re, os, glob
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def clean(l):
    l = l.strip()
    l = re.sub(r'^(?:[-*\u00b7]|\d+\.\s*|\u2705\s*|\u2014\s*)+', '', l).strip()
    return l

def digest(b):
    b = re.sub(r'\s+', ' ', b).strip()
    return b if len(b) <= 168 else b[:168].rsplit(' ', 1)[0] + ' \u2026'

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
lastn = nums[-1] if nums else 0
t1, none_list = {}, []
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    m = re.match(r'#\s+Chapter\s+\d+[:\s]+(.+)', t)
    title = m.group(1).strip() if m else ''
    sec, grabs = '', []
    for raw in t.split('\n'):
        h = raw.strip()
        if h.startswith('#'):
            sec = h
            continue
        if 'Butterflies This Chapter' in sec:
            c = clean(h)
            if c and c != '---':
                grabs.append(c)
        elif h.startswith('#') or 'End of Chapter' in sec:
            pass
    if grabs:
        t1[n] = (title, grabs)
    else:
        none_list.append(n)

tot1 = sum(len(g) for _, g in t1.values())
manual = ''
if os.path.exists('BUTTERFLY_EFFECTS.md'):
    m2 = re.search(r'<!-- MANUAL:START -->.*?<!-- MANUAL:END -->',
                   io.open('BUTTERFLY_EFFECTS.md', encoding='utf-8').read(), re.S)
    if m2:
        manual = m2.group(0)

ERAS = [
    ('ERA 0 \u2014 first storm (ch1\u20136): the new kid lands in S1', 1, 7),
    ('ERA 1 \u2014 the hunt widens (ch7\u201313)', 7, 14),
    ('ERA 2 \u2014 mid-season (ch14\u201320)', 14, 21),
    ('ERA 3 \u2014 origins & finale (ch21\u201326)', 21, 27),
]

out = ['# BUTTERFLY_EFFECTS.md \u2014 every butterfly that has already flown (auto-generated)',
       '*The evidence base behind `DIVERGENCE_LEDGER.md` \u2014 mined from the chapter footers themselves. Regenerate: `python3 checks/build_butterfly_effects.py`.*',
       f'**{len(t1)} chapters carry butterfly sections \u00b7 {tot1} effects listed \u00b7 {len(none_list)} chapters list none: {none_list or "none"}.**',
       '']
if lastn:
    for label, a, b in ERAS:
        era = [n for n in nums if a <= n < b]
        if not era:
            continue
        k = sum(len(t1[n][1]) for n in era if n in t1)
        withsec = sum(1 for n in era if n in t1)
        out += [f'## {label} \u2014 {withsec}/{len(era)} chapters \u00b7 {k} effects', '']
        for n in era:
            title, grabs = t1.get(n, ('', []))
            if not grabs:
                continue
            out.append(f'- **ch{n} \u2014 {title or "(see file)"}:**')
            out += [f'  - {digest(g)}' for g in grabs]
        out.append('')
out.append(manual.strip() if manual else '<!-- MANUAL:START -->\n(genealogy lines live here: one per ACTIVE/STORM D-row thread — birth, first flight, current shape)\n<!-- MANUAL:END -->')
io.open('BUTTERFLY_EFFECTS.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'built: sections in {len(t1)} ch ({tot1} effects); none: {none_list}')

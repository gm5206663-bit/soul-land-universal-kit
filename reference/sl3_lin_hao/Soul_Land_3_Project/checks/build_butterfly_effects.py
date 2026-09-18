#!/usr/bin/env python3
# Builds BUTTERFLY_EFFECTS.md — the complete evidence base of every butterfly
# already flown, mined from chapter footers (ALL list styles) + an AU-keyword
# evidence pass over the remaining footer sections + the session registry.
# v2 (2026-09-03): v1 read dash bullets only and undercounted a whole numbered-
# list era (user caught it). v2 reads any list style.
# Regenerate after any chapter sync:  python3 checks/build_butterfly_effects.py
# Manual blocks between <!-- MANUAL:START/END --> markers are preserved.
import io, re, os, glob
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TIER1 = ['Butterflies this chapter', 'AU / Butterfly', 'Butterfly Effects Shown',
         'AU Divergences (locked)', 'AT / Mutations Shown', 'Adaptation Talent Shown']
T2SECS = ['Chapter Summary', 'Ensemble', 'Character Progression', 'Chapter end state',
          'Canon Facts Established', 'World Details Shown']
KW = re.compile(r'\b(AU|ours|original|butterfl|divergen|canon has no|not in canon|the fifth)\b', re.I)
ERAS = [('ERA 0 \u2014 Glorybound (ch1\u20133): the variant hawk is born', 1, 4),
        ('ERA 1 \u2014 Eastsea early (ch4\u201312): the hawk hunts, the mutations embody', 4, 13),
        ('ERA 1.5 \u2014 the numbered-list years (ch13\u201337): arms-races, half-open secrets \u2014 quieter, NOT silent (v1\u2019s dash-only harvester misread them)', 13, 38),
        ('ERA 2 \u2014 Eastsea late (ch38\u201363): the AU wakes; the class re-forms around a fifth', 38, 64),
        ('ERA 3 \u2014 Shrek (ch64\u2013{last}): the exam; the ledger; the storm era', 64, 999)]

def clean(l):
    l = l.strip()
    l = re.sub(r'^(?:[-*\u00b7]|\d+\.\s*|\u2705\s*|\u2014\s*)+', '', l).strip()
    return l

def digest(b):
    b = re.sub(r'\s+', ' ', b).strip()
    return b if len(b) <= 168 else b[:168].rsplit(' ', 1)[0] + ' \u2026'

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
lastn = nums[-1]
t1, ev, none_list = {}, {}, []
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    title = (re.match(r'#\s+Chapter\s+\d+:\s*(.+)', t) or [None, ''])[1] if re.match(r'#\s+Chapter\s+\d+', t) else ''
    m = re.match(r'#\s+Chapter\s+\d+:\s*(.+)', t)
    title = m.group(1).strip() if m else ''
    sec, grabs, evid = '', [], []
    for raw in t.split('\n'):
        h = raw.strip()
        if h.startswith('#'):
            sec = h; continue
        if not (h and h != '---'):
            continue
        if any(s in sec for s in TIER1):
            c = clean(h)
            if c: grabs.append(c)
        elif any(s in sec for s in T2SECS) and KW.search(h):
            c = clean(h)
            if c and len(c) > 12: evid.append(c)
    if grabs: t1[n] = (title, grabs)
    if evid: ev[n] = evid[:3]
    if not grabs and not evid: none_list.append(n)

tot1 = sum(len(g) for _, g in t1.values())
tote = sum(len(v) for v in ev.values())
manual = ''
if os.path.exists('BUTTERFLY_EFFECTS.md'):
    m = re.search(r'<!-- MANUAL:START -->.*?<!-- MANUAL:END -->',
                  io.open('BUTTERFLY_EFFECTS.md', encoding='utf-8').read(), re.S)
    if m: manual = m.group(0)

reg = io.open('BUTTERFLY_REGISTRY.md', encoding='utf-8').read() if os.path.exists('BUTTERFLY_REGISTRY.md') else ''
sessions = [l.strip(' #') for l in reg.split('\n') if re.match(r'^###?+\s+Session', l)]

out = [f'# BUTTERFLY_EFFECTS.md \u2014 every butterfly that has already flown (ch1\u2013{lastn})',
'*The evidence base behind `DIVERGENCE_LEDGER.md` \u2014 mined from the chapter footers themselves (v2: ALL list styles \u00b7 dashes, numbered, checkmarks) plus an AU-keyword evidence pass over summaries/ensembles/states, plus the session registry.',
f'**{len(t1)} chapters carry butterfly sections \u00b7 {tot1} effects \u00b7 {len(ev)} chapters yield evidence lines \u00b7 {tote} captured \u00b7 {len(none_list)} chapters yield neither: {none_list or "none"}.**',
'',
'*v1 defect, kept honest: it read dash bullets only, misreporting the numbered-list era (ch13\u201363) as silent. The user caught it \u2014 \u201ccheck again, there are many more.\u201d They were right: the quiet years were never quiet.*',
'']
for label, a, b in ERAS:
    label = label.replace('{last}', str(lastn))
    era = [n for n in nums if a <= n < b]
    if not era: continue
    k = sum(len(t1[n][1]) for n in era if n in t1)
    withsec = sum(1 for n in era if n in t1)
    out += [f'## {label} \u2014 {withsec}/{len(era)} chapters \u00b7 {k} effects', '']
    for n in era:
        title, grabs = t1.get(n, ('', []))
        evid = ev.get(n, [])
        if not grabs and not evid: continue
        out.append(f'- **ch{n} \u2014 {title or "(see file)"}:**')
        out += [f'  - {digest(g)}' for g in grabs]
        out += [f'  \u00b7 *(evidence)* {digest(e)}' for e in evid]
    out.append('')
if sessions:
    out += [f'## THE SESSION REGISTRY \u2014 {len(sessions)} recorded sessions (full text: `BUTTERFLY_REGISTRY.md`)', '']
    out += [f'- {s}' for s in sessions]
    out.append('')
out.append(manual.strip() if manual else '<!-- MANUAL:START -->\n(genealogy lives here)\n<!-- MANUAL:END -->')
io.open('BUTTERFLY_EFFECTS.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'built: sections in {len(t1)} ch ({tot1} effects) + evidence in {len(ev)} ch ({tote} lines); neither: {none_list}')

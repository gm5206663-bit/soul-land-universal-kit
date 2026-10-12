#!/usr/bin/env python3
"""Layer 6 — WORKSPACE AUDIT (original 09-02; guards added 09-03; REBUILT 09-03
after a self-inflicted edit destroyed the original checks — the destruction was
caught because the sync-fails vanished while docs were stale. Lesson BF3.)
Checks: state-vs-ALL-footers · S-1..S-5 doc sync · canon range+NEXT vs disk ·
live-block uniqueness · soft-hyphen ban · voice-tic ban · hygiene ·
CJK ban · BRIEF freshness · heading staleness."""
import io, re, sys, glob, os, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('== Layer 6: workspace_audit.py ==')
fails = []

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
newest = nums[-1]
st = json.load(io.open('checks/state.json', encoding='utf-8'))
cur = st[str(newest)]
sp = cur['sp']; sp_c = f'{sp:,}'

# --- S-1..S-5: the live docs carry current truth ---
for p, probes in [
    ('LIN_HAO_STATUS.md',  [f'end of Chapter {newest}', sp_c]),
    ('CONTINUATION_PROMPT.md', [f'end of Chapter {newest}', sp_c, str(sp)]),
    ('THE_CODEX.md',       [f'end of ch {newest}', sp_c]),
    ('CODEX/05_PROJECT_SOUL_LAND_3.md', [f'end of ch {newest}', sp_c]),
    ('LIN_HAO_PANELS.md',  [sp_c]),
]:
    t = io.open(p, encoding='utf-8').read()
    for pr in probes:
        if pr not in t:
            fails.append(f'S: {p} does not carry {pr!r}')
cs = io.open('CHARACTER_STATS.md', encoding='utf-8').read()
if f'end of fic chapter {newest}' not in cs:
    fails.append(f'S-5: CHARACTER_STATS §0 says chapter {newest-1}; state says {newest}')

# --- state.json vs EVERY footer (the chain) ---
for n in nums:
    v = st[str(n)]
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    m = re.search(r'### Ranks at chapter end: Lin Hao \*\*(\d+)\*\* · SP \*\*([\d,]+)\*\* · hawk \*\*([\d,]+)\*\* · ledger \*\*(\d+)\*\*', t)
    if not m:
        continue  # pre-modern formats are Layer 0's (state.py) jurisdiction
    got = dict(rank=int(m.group(1)), sp=int(m.group(2).replace(',', '')), hawk=int(m.group(3).replace(',', '')), ledger=int(m.group(4)))
    for k in ('rank', 'sp', 'hawk', 'ledger'):
        if v.get(k) is not None and got[k] != v[k]:
            fails.append(f'ch{n}: footer {k}={got[k]} but state says {v[k]}')

# --- canon range + NEXT vs disk ---
disk = sorted(int(re.findall(r'canon_(\d+)', f)[0]) for f in glob.glob('canon_extract/chapters/canon_*.txt'))
ca = io.open('CANON_ACCESS.md', encoding='utf-8').read()
mr = re.search(r'229\u2013(\d+)', ca)
if mr and int(mr.group(1)) != disk[-1]:
    fails.append(f'CANON_ACCESS: stale range 229-{mr.group(1)} (disk hi {disk[-1]})')
mn = re.search(r'NEXT: canon (\d+) = (\d+)', ca)
if mn:
    want = 10716111 + (int(mn.group(1)) - 266)
    if int(mn.group(1)) != disk[-1] + 1 or int(mn.group(2)) != want:
        fails.append(f'CANON_ACCESS: NEXT map says {mn.group(1)} (should be {disk[-1]+1} = {want})')

# --- live-block uniqueness (the ghost-duplicate guard) ---
for p, pat in [('LIN_HAO_STATUS.md', r'^Current soul rank'), ('LIN_HAO_STATUS.md', r'^## Position:')]:
    c = len(re.findall(pat, io.open(p, encoding='utf-8').read(), re.M))
    if c != 1:
        fails.append(f'{p}: {c} live blocks matching "{pat}" (want exactly 1)')

# --- soft-hyphen / control-char ban ---
for f in sorted(glob.glob('chapters/chapter_*.md')) + glob.glob('*.md'):
    t = io.open(f, encoding='utf-8').read()
    for ch, name in [('\u00ad', 'soft hyphen U+00AD'), ('\u200b', 'ZWSP'), ('\ufeff', 'BOM')]:
        if ch in t:
            fails.append(f'{f}: {name}')

# --- voice-tic ban (restored list — BF3: the known subset; extend on next carry) ---
TICS = ['on the record']
for f in sorted(glob.glob('chapters/chapter_*.md')):
    t = io.open(f, encoding='utf-8').read()
    prose = t[:t.find('## End of Chapter')]
    for tic in TICS:
        if tic in prose.lower():
            fails.append(f'{f.split("/")[-1]}: banned voice tic: {tic}')

# --- hygiene ---
for f in (['LIBRARY.md'] if os.path.exists('LIBRARY.md') else []):
    t = io.open(f, encoding='utf-8').read()
    if 'DOULOLO' in t:
        fails.append(f'{f}: DOULOLO reference (dead source; remove)')
    for ln, line in enumerate(t.split('\n'), 1):
        if 'deleted' in line.lower() and 'upload' in line.lower() and 'never' not in line.lower():
            fails.append(f'{f}:{ln} deleted-uploads claim (the corrected fact)')

# --- CJK ban (the ch100 stray-ideograph class; allowlist: the system-window marker) ---
for f in sorted(glob.glob('chapters/chapter_*.md')):
    for ln, line in enumerate(io.open(f, encoding='utf-8'), 1):
        bad = [c for c in re.findall(r'[\u3400-\u9fff\uf900-\ufaff]', line) if c not in '\u5168\u80fd\u7cfb']
        if bad:
            fails.append(f'{f.split("/")[-1]}:{ln} stray CJK {"".join(bad[:3])}')

# --- BRIEF freshness (the cockpit may never point at a past chapter) ---
if os.path.exists('BRIEF.md'):
    bt = io.open('BRIEF.md', encoding='utf-8').read()
    m = re.search(r'position: end of chapter (\d+)', bt)
    if not m or int(m.group(1)) != newest:
        fails.append(f'BRIEF.md stale: says {m.group(1) if m else "nothing"}; newest is {newest} (rerun checks/brief.py)')

# --- heading staleness (a heading claiming END OF CHAPTER N must be current) ---
for f in glob.glob('*.md') + ['CODEX/05_PROJECT_SOUL_LAND_3.md']:
    for ln, line in enumerate(io.open(f, encoding='utf-8'), 1):
        if line.startswith('#'):
            m = re.search(r'END OF CHAPTER (\d+)', line)
            if m and int(m.group(1)) != newest:
                fails.append(f'{f}:{ln} heading claims END OF CHAPTER {m.group(1)}; newest is {newest} (refresh the core, not just the log)')

for x in fails: print('  FAIL', x)
print(f'workspace_audit: {len(fails)} FAIL')
sys.exit(1 if fails else 0)

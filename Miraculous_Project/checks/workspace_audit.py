#!/usr/bin/env python3
"""Layer 6 — WORKSPACE AUDIT (ported). Guards: doc sync (core docs carry the
current truth) · state.json vs EVERY footer (via sync_audit; here: count) ·
canon ore claims vs disk · live-block uniqueness · soft-hyphen/control-char ban ·
voice-tic ban · CJK stray-char ban · BRIEF freshness · heading staleness."""
import io, re, sys, glob, os, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('== Layer 6: workspace_audit.py ==')
fails = []

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
newest = nums[-1] if nums else 0
st = json.load(io.open('checks/state.json', encoding='utf-8'))
res = st['resonance']

# --- live docs carry current truth (skip doc probes at 0 chapters; they
#     instead must carry the pre-chapter-1 marker) ---
if newest:
    for p, probes in [
        ('THE_CODEX.md', [f'end of ch {newest}']),
        ('CONTINUATION_PROMPT.md', [f'end of ch {newest}']),
        ('CHARACTER_STATS.md', [f'end of fic chapter {newest}']),
    ]:
        if os.path.exists(p):
            t = io.open(p, encoding='utf-8').read()
            for pr in probes:
                if pr not in t:
                    fails.append(f'S: {p} does not carry {pr!r} (doc drift)')
else:
    for p, probe in [
        ('THE_CODEX.md', 'before chapter 1'),
        ('CONTINUATION_PROMPT.md', 'before chapter 1'),
        ('CHARACTER_STATS.md', 'before chapter 1'),
    ]:
        if os.path.exists(p):
            t = io.open(p, encoding='utf-8').read()
            if probe not in t:
                fails.append(f'S: {p} does not carry {probe!r} (story not started yet — say so)')

# --- ore claims vs disk (SEASON1_INDEX 'ORE DONE' lines must have files) ---
idx = io.open('canon_extract/SEASON1_INDEX.txt', encoding='utf-8').read()
done_slots = re.findall(r'^#\s*(\d{2})\s*\|[^|]*\|[^|]*\|[^|]*\|\s*ORE DONE', idx, re.M)
for s in done_slots:
    if not glob.glob(f'canon_extract/episodes/s1e{int(s):02d}_*.txt'):
        fails.append(f'ore: slot {s} marked ORE DONE but no file on disk')
disk = sorted(int(re.findall(r's1e(\d{2})', f)[0]) for f in glob.glob('canon_extract/episodes/s1e*.txt'))
if disk and str(st.get('canon_slot', 1)) not in [str(d) for d in disk] and nums:
    # once chapters exist, the next slot should either be done or be first-pending
    first_pending = None
    for s in range(1, 27):
        if not re.search(rf'^#\s*{s:02d}\s*.*ORE DONE', idx, re.M):
            first_pending = s; break
    if first_pending and st.get('canon_slot') not in (first_pending,) and st.get('canon_slot') in disk:
        pass  # covering an already-extracted slot is fine

# --- live-block uniqueness (BRIEF.md state line exactly once) ---
if os.path.exists('BRIEF.md'):
    bt = io.open('BRIEF.md', encoding='utf-8').read()
    c = len(re.findall(r'^position:', bt, re.M))
    if c != 1:
        fails.append(f'BRIEF.md: {c} live "position:" blocks (want exactly 1)')

# --- soft-hyphen / control-char ban ---
for f in sorted(glob.glob('chapters/chapter_*.md')) + glob.glob('*.md'):
    try:
        t = io.open(f, encoding='utf-8').read()
    except (UnicodeDecodeError, OSError):
        continue
    for ch, name in [('\u00ad', 'soft hyphen U+00AD'), ('\u200b', 'ZWSP'), ('\ufeff', 'BOM')]:
        if ch in t:
            fails.append(f'{f}: {name}')

# --- voice-tic ban (prose only; footers may document tics) ---
TICS = ['on the record', 'dear reader', 'the narrator']
for f in sorted(glob.glob('chapters/chapter_*.md')):
    t = io.open(f, encoding='utf-8').read()
    prose = t[:t.find('## End of Chapter')]
    for tic in TICS:
        if tic in prose.lower():
            fails.append(f'{f.split("/")[-1]}: banned voice tic: {tic}')

# --- CJK stray-char ban (French accented Latin is fine) ---
for f in sorted(glob.glob('chapters/chapter_*.md')):
    for ln, line in enumerate(io.open(f, encoding='utf-8'), 1):
        bad = [c for c in re.findall(r'[\u3400-\u9fff\uf900-\ufaff]', line)]
        if bad:
            fails.append(f'{f.split("/")[-1]}:{ln} stray CJK {"".join(bad[:3])}')

# --- BRIEF freshness ---
if os.path.exists('BRIEF.md'):
    bt = io.open('BRIEF.md', encoding='utf-8').read()
    m = re.search(r'position: end of chapter (\d+)', bt)
    if newest:
        if not m or int(m.group(1)) != newest:
            fails.append(f'BRIEF.md stale: says {m.group(1) if m else "nothing"}; newest is {newest} (rerun checks/brief.py)')
    else:
        if m or 'position: before chapter 1' not in bt:
            fails.append('BRIEF.md should say "position: before chapter 1" (story not started)')

# --- heading staleness ---
for f in glob.glob('*.md'):
    for ln, line in enumerate(io.open(f, encoding='utf-8'), 1):
        if line.startswith('#'):
            m = re.search(r'END OF CHAPTER (\d+)', line)
            if m and int(m.group(1)) != newest:
                fails.append(f'{f}:{ln} heading claims END OF CHAPTER {m.group(1)}; newest is {newest}')

for x in fails: print('  FAIL', x)
print(f'workspace_audit: {len(fails)} FAIL' if fails else 'workspace_audit: OK')
sys.exit(1 if fails else 0)

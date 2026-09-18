#!/usr/bin/env python3
# Layer 7 — DIVERGENCE ENGINE + BUTTERFLY LAW.
#   D1  ledger rows: ids unique, statuses valid
#   D2  every D-row cited in a footer exists in DIVERGENCE_LEDGER.md
#   D3  ACTIVE rows must be cited in at least one footer (an active thread
#       that no chapter advances is a ghost) — exempt while 0 chapters exist
#   D4  BUTTERFLY LAW: footer "Butterflies shown: N" with N >= 3, and the
#       'Butterflies This Chapter' section carries at least N bullets
import io, re, glob, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails, warns = [], []
CFG_MIN = 3

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
W('=' * 62)
W('== Layer 7: divergence_engine.py (the ledger + butterfly law) ==')

led_rows = {}
if os.path.exists('DIVERGENCE_LEDGER.md'):
    for line in io.open('DIVERGENCE_LEDGER.md', encoding='utf-8'):
        m = re.match(r'^\|\s*((?:REVEAL-)?[A-Z]+-\d+|REVEAL-\w+)\s*\|\s*(ACTIVE|HELD|RESOLVED|DORMANT)\s*\|\s*([^|]*)\|', line)
        if m:
            if m.group(1) in led_rows:
                fails.append(f'D1: duplicate ledger id {m.group(1)}')
            led_rows[m.group(1)] = (m.group(2), m.group(3).strip())
else:
    fails.append('D1: DIVERGENCE_LEDGER.md missing')

cited_anywhere = set()
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    end = t.find('## End of Chapter')
    footer = t[end:] if end != -1 else ''
    md = re.search(r'D-rows Cited[:\s]*(.+)', footer)
    if md:
        cited = {x.strip() for x in md.group(1).split(',') if re.match(r'^[A-Z]+-\d+$|^REVEAL-[A-Z]+$', x.strip())}
        cited_anywhere |= cited
        for c in cited:
            if c not in led_rows:
                fails.append(f'D2 ch{n}: cites {c} which does not exist in DIVERGENCE_LEDGER.md')
    else:
        fails.append(f'D2 ch{n}: footer missing "D-rows Cited" line')

    mb = re.search(r'Butterflies shown:\s*\*\*(\d+)\*\*', footer)
    if not mb:
        fails.append(f'D4 ch{n}: footer missing "Butterflies shown: N"')
        continue
    shown = int(mb.group(1))
    if shown < CFG_MIN:
        fails.append(f'D4 ch{n}: Butterflies shown {shown} < {CFG_MIN} (BUTTERFLY LAW)')
    sec = footer.split('Butterflies This Chapter')[-1]
    sec = sec.split('###', 1)[0]
    bullets = [l for l in sec.split('\n') if re.match(r'^\s*[-*]\s*\S', l)]
    if len(bullets) < shown:
        fails.append(f'D4 ch{n}: footer shows {shown} butterflies but lists {len(bullets)} bullets (list them all)')

if led_rows and nums:
    for did, (status, thread) in led_rows.items():
        if status == 'ACTIVE' and did not in cited_anywhere:
            fails.append(f'D3: {did} is ACTIVE but no chapter cites it (advance it or demote to HELD)')
    W(f'  ledger: {len(led_rows)} rows · cited in footers: {len(cited_anywhere)}')
elif not nums:
    W('  0 chapters — active-thread rule exempt (the story has not started)')

for w in warns: W('  WARN ' + w)
for x in fails: print('  FAIL', x)
print(f'divergence_engine: {len(fails)} FAIL' if fails else 'divergence_engine: OK')
sys.exit(1 if fails else 0)

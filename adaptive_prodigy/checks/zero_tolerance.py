#!/usr/bin/env python3
"""Layer 4 — ZERO-TOLERANCE CHECKS (created 09-01, after the full library absorption).

Sources (library/):
  - universal_storyline_writing_corrections.md §16 (zero-tolerance list)
  - universal_drafting_mistake_lessons.md ("every number needs a source"; the rigorous-artifact trap)
  - adaptation_talent_framework.md + Master Foundation (NON-SENTIENCE — the talent never speaks)
  - canon_first_oc_woven_chapter_style.md (no abstract-cliff register)
  - FANFICTION_FRAMEWORK.md §8 (no chapter without verified canon on disk)

Every check is grep-able or arithmetic — no judgment calls in this layer.
"""
import io, re, glob, os, sys

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails, warns = [], []

chapters = sorted(glob.glob('chapters/chapter_*.md'), key=lambda f: int(re.search(r'(\d+)', f).group(1)))

# 1. TALENT NON-SENTIENCE (absolute — the talent never speaks)
SENT = re.compile(r'(talent|adaptation)\s+(said|spoke|says|warned|whispered|told|urged|murmured|asked|replied|announced)', re.I)
# 2. BANNED ABSTRACT-CLIFF REGISTER
BANNED = ['everything was about to change', 'nothing would ever be the same', 'little did they know', 'doULOLO'.lower()]

for f in chapters:
    t = io.open(f, encoding='utf-8').read()
    n = int(re.search(r'(\d+)', f).group(1))
    # cut footer from prose checks (summary sections quote laws; scan prose only, before '## End of Chapter')
    cut = t.find('## End of Chapter')
    prose = t[:cut] if cut != -1 else t
    for m in SENT.finditer(prose):
        fails.append(f'ch{n}: sentient-talent voice: "{prose[max(0,m.start()-30):m.end()+30].strip()[:80]}"')
    for b in BANNED:
        if b in prose.lower():
            fails.append(f'ch{n}: banned phrase: "{b}"')
    # 3. CANON FILES CITED MUST EXIST (no chapter without verified canon on disk)
    for cn in set(re.findall(r'canon_(\d{3})', t)):
        if not (os.path.exists(f'canon_extract/chapters/canon_{cn}.txt') or os.path.exists(f'canon_extract/chapters/canon_{cn}_excerpt.txt')):
            fails.append(f'ch{n}: cites canon_{cn}.txt — NOT ON DISK')
    # 4. FOOTER LINE EXISTS
    if n >= 80 and '### Ranks at chapter end:' not in t:
        fails.append(f'ch{n}: no ranks-at-chapter-end footer line')
    # 5. TRIALS ARITHMETIC (every "a·b·c = N" must sum)
    for vec, tot in re.findall(r'(\d+(?:\u00b7\d+)+)\s*=\s*(\d+)', t):
        s = sum(int(x) for x in vec.split('\u00b7'))
        if s != int(tot):
            fails.append(f'ch{n}: trials arithmetic {vec} = {tot} (true sum {s})')
    # 6. WORD FLOOR (summary-as-chapter guard; prose section only)
    if len(prose.split()) < 900:
        warns.append(f'ch{n}: prose only {len(prose.split())} words (<900)')

# 7. INDEXED CROSS-CHECK: newest chapter cites the newest canon or states its canon range
newest = chapters[-1]
t = io.open(newest, encoding='utf-8').read()
if not re.search(r'canon[_ ]ch?s? ?2\d\d|canon_\d{3}', t):
    fails.append(f'{newest}: newest chapter carries no canon citation')

print('== Layer 4: zero_tolerance.py ==')
for w in warns: print('  WARN', w)
for f_ in fails: print('  FAIL', f_)
print(f'zero_tolerance: {len(fails)} FAIL · {len(warns)} WARN · {len(chapters)} chapters scanned')
sys.exit(1 if fails else 0)

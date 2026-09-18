#!/usr/bin/env python3
"""Layer 5 — PRESENCE AUDIT (law oo, the user's 09-02 correction). Gates ch92+.
1. PRESENCE: Lin Hao markers in prose >= 5 (a person in the room, not a ghost).
2. VOICE: footer declares 'LH voice: N turns' with N >= 4, person-voice.
3. BUTTERFLIES: footer carries '### Butterflies this chapter' with >= 3 '- **B' cause->effect lines.
4. NO CANON COPYING: narration 12-grams must not appear in any cited canon file
   (12-gram rule); no verbatim quoted speech of 15+ words from canon.
"""
import io, re, glob, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails = []
def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', s.lower())).strip()
def ngrams(s, n=12):
    w = norm(s).split()
    return {' '.join(w[i:i+n]) for i in range(len(w)-n+1)}

for f in sorted(glob.glob('chapters/chapter_*.md'), key=lambda x: int(re.search(r'(\d+)', x).group(1))):
    n = int(re.search(r'(\d+)', f).group(1))
    if n < 92: continue
    t = io.open(f, encoding='utf-8').read()
    cut = t.find('\n---\n'); end = t.find('## End of Chapter')
    prose, footer = t[cut:end], t[end:]
    # 1 presence
    marks = len(re.findall(r'Lin Hao|the fifth', prose, re.I))
    if marks < 5: fails.append(f'ch{n}: presence markers {marks} < 5 (ghost-pattern)')
    # 2 voice declared
    m = re.search(r'LH voice:\s*(\d+) turns', footer)
    if not m: fails.append(f'ch{n}: footer missing "LH voice: N turns"')
    elif int(m.group(1)) < 4: fails.append(f'ch{n}: LH voice {m.group(1)} turns < 4')
    # 3 butterflies
    b = footer.find('### Butterflies this chapter')
    cnt = 0
    if b != -1:
        seg = footer[b:footer.find('###', b+4)]
        cnt = len(re.findall(r'^- \*\*B', seg, re.M))
    if cnt < 3: fails.append(f'ch{n}: butterflies {cnt} < 3 (footer must list cause->effect)')
    # 4 no canon copying
    cites = set(re.findall(r'canon ch (\d{3})', t[:600]))
    noquote = re.sub(r'"[^"]*"', ' ', prose)
    ch_grams = ngrams(noquote)
    for c in cites:
        cp = f'canon_extract/chapters/canon_{c}.txt'
        if not os.path.exists(cp): continue
        cg = ngrams(io.open(cp, encoding='utf-8').read())
        hit = ch_grams & cg
        if hit: fails.append(f'ch{n}: {len(hit)} verbatim 12-gram(s) from canon {c} (first: "{sorted(hit)[0][:70]}...")')
        for q in re.findall(r'"([^"]*)"', prose):
            if len(q.split()) >= 15 and norm(q) in norm(io.open(cp, encoding='utf-8').read()):
                fails.append(f'ch{n}: 15+ word verbatim quote from canon {c}')
print('== Layer 5: presence_audit.py (law oo; gates ch92+) ==')
for x in fails: print('  FAIL', x)
print(f'presence_audit: {len(fails)} FAIL')
sys.exit(1 if fails else 0)

import json, re, io, os, glob
os.chdir('/home/user/Soul_Land_3_Project')
st = json.load(open('checks/state.json'))
chs = {int(k): v for k, v in st.items() if k.isdigit()}
print('== A. state.json ground truth ==')
for key in ('rank','sp','hawk','ledger','smith'):
    n = [c for c,v in chs.items() if v.get(key) is not None]
    seq = [(c, chs[c][key]) for c in sorted(n)]
    mono = all(seq[i][1] <= seq[i+1][1] for i in range(len(seq)-1)) if key!='ledger' else True
    print(f'{key}: recorded in {len(n)} chapters; last={seq[-1]}; monotonic={mono}; anomalies=' +
          str([p for p in seq if seq.index(p)>0 and p[1]<seq[seq.index(p)-1][1]]))
ens = chs[79].get('ensemble', {})
print('ch79 ensemble:', ens)

print('\n== B. registry last-echo verification ==')
def has(ch, pat):
    t = io.open(f'chapters/chapter_{ch:02d}.md', encoding='utf-8').read()
    return bool(re.search(pat, t))
claims = [
 ('Zhang Yangzi @78', 78, r'Zhang Yangzi'),
 ('Wang Jinxi @67', 67, r'Wang Jinxi'),
 ('Track @76', 76, r'Track'),
 ('guardian/black ring @76', 76, r'black ring|jiao'),
 ('confession echo @75', 75, r'juice'),
 ('kneel @74', 74, r'kneel'),
 ('wager @79', 79, r'wager'),
 ('spring report @79', 79, r'sixth gate'),
 ('proctors record @79', 79, r'stroke|margin'),
 ('Yaluo metals @74', 74, r'Heavy Silver|Yaluo|Sky Dragon'),
 ('armor pact @74', 74, r'armor'),
 ('appetite @79', 79, r'breakfast|appetite'),
 ('Xiaoyan tank @79', 79, r'third|conserv'),
 ('tin @75', 75, r'\btin\b'),
 ('Mu Xi @69', 69, r'Mu Xi'),
 ('Long Hengxu @55', 55, r'Long Hengxu'),
 ('Wei Xiaofeng @60', 60, r'Wei Xiaofeng'),
 ('plural firsts @76', 76, r'blood-answer|spirit-answer'),
 ('five-hand shape @79', 79, r'five|shape|threes'),
]
for label, ch, pat in claims:
    print(f'{"PASS" if has(ch, pat) else "FAIL"}  {label}')

print('\n== C. stale-token sweep in docs ==')
stale = ['1,399', '3,111', '2,768', 'Soul King (51', '107 opponents', 'rank 36', '\\b289\\b',
         'END OF CHAPTER 6', 'end of chapter 6', 'end of ch 6', 'rank 18,', 'rank 21 ', 'rank 23,']
for f in ['THE_CODEX.md','LIN_HAO_STATUS.md','LIN_HAO_PANELS.md','CHARACTER_STATS.md','POWER_MODEL.md','RELATIONSHIPS.md','CANON_ACCESS.md','CONTINUATION_PROMPT.md']:
    t = io.open(f, encoding='utf-8').read().split('\n')
    hits = [(i+1, l.strip()[:90]) for i, l in enumerate(t) if any(re.search(s, l) for s in stale)]
    if hits:
        print(f'-- {f}:')
        for i, l in hits[:8]: print(f'   L{i}: {l}')

print('\n== D. RELATIONSHIPS section headers ==')
for i, l in enumerate(io.open('RELATIONSHIPS.md', encoding='utf-8').read().split('\n'), 1):
    if re.match(r'^# [0-9]', l): print(f'L{i}: {l[:110]}')
t = io.open('RELATIONSHIPS.md', encoding='utf-8').read()
sec10 = t[t.find('# 10.'):]
for mk in ('**71**', '**72**', '**75**', '**79**'):
    print(f'S10 has {mk}:', mk in sec10)

print('\n== E. ch5/6 badge + ch68 soul-age ==')
for c in (5, 6):
    t = io.open(f'chapters/chapter_{c:02d}.md', encoding='utf-8').read()
    m = [l.strip()[:80] for l in t.split('\n') if re.search(r'badge', l, re.I)]
    print(f'ch{c} badge lines:', m[:2] if m else 'none')
later = []
for f in sorted(glob.glob('chapters/chapter_*.md')):
    n = int(re.search(r'(\d+)', f).group(1))
    if n > 6:
        t = io.open(f, encoding='utf-8').read()
        for l in t.split('\n'):
            if re.search(r'badge', l, re.I): later.append((n, l.strip()[:70]))
print('later badge mentions:', later[:4] if later else 'none')
t68 = io.open('chapters/chapter_68.md', encoding='utf-8').read()
print('ch68 hawk/soul-age lines:', [l.strip()[:80] for l in t68.split('\n') if re.search(r'\b(9|10|11)\d\d\b|hawk', l)][:4])

print('\n== F. roster names in RELATIONSHIPS tables ==')
names = sorted(set(re.findall(r'^\| \*\*([^*|]+)\*\* \|', t, re.M)))
print(len(names), 'names:', ', '.join(names))

print('\n== G. new-person scan ch63-79 (title words) ==')
roster = set(names) | {'Lin Hao','Tang Wulin','Gu Yue','Xie Xie','Na\'er','Zhuo Shi'}
for n in range(63, 80):
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    for m in re.finditer(r'(Elder|President|Saint|Master|Director|Examiner|Proctor|Sister|Brother) ([A-Z][a-z]+(?: [A-Z][a-z]+)?)', t):
        if m.group(2) not in roster:
            print(f'ch{n}: {m.group(0)}')

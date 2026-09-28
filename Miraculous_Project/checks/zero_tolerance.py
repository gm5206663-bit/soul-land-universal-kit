#!/usr/bin/env python3
# Layer 1 — ZERO TOLERANCE. Things that are NEVER allowed in prose (footers exempt):
#   Z1  banned meta-narration phrases (config: banned_meta)
#   Z2  12-gram copy overlap against canon ore (canon_extract/**/*.txt) —
#       distill the ore, never paste it
#   Z3  non-sentience of Hawk Moth: in S1 Hawk Moth is a VOICE and an unseen
#       presence; the prose may not give him a body (Hawk Moth + body verb)
import io, re, glob, os, sys, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails = []
CFG = json.load(io.open('checks/config.json', encoding='utf-8'))

# --- canon gram bank (ore files only) ---
canon_words = []
for f in glob.glob('canon_extract/**/*.txt', recursive=True):
    for tok in re.findall(r"[a-z']+", io.open(f, encoding='utf-8').read().lower()):
        canon_words.append(tok)
CANON_GRAMS = {tuple(canon_words[i:i+12]) for i in range(len(canon_words) - 11)} if len(canon_words) > 12 else set()

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
W('=' * 62)
W('== Layer 1: zero_tolerance.py (never-allowed list) ==')

verbs = CFG['hawkmoth_body_verbs']
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    end = t.find('## End of Chapter')
    prose = t[:end] if end != -1 else t
    flat = re.sub(r'\*', '', prose).lower()
    toks = re.findall(r"[a-z']+", flat)

    for b in CFG['banned_meta']:
        if b in flat:
            fails.append(f'Z1 ch{n}: banned meta phrase "{b}"')
    for i in range(len(toks) - 11):
        g = tuple(toks[i:i+12])
        if g in CANON_GRAMS:
            fails.append(f'Z2 ch{n}: 12-gram copy from canon ore: {" ".join(g[:8])}…')
            break
    for s in re.split(r'(?<=[.!?])\s+', prose):
        if re.search(r'\bHawk Moth\b', s) and re.search(r'\b(' + '|'.join(verbs) + r')\b', s, re.I):
            fails.append(f'Z3 ch{n}: Hawk Moth given a body: {s.strip()[:90]}')

W(f'  canon gram bank: {len(CANON_GRAMS)} 12-grams from {len(glob.glob("canon_extract/**/*.txt", recursive=True))} ore files')
for x in fails: print('  FAIL', x)
print(f'zero_tolerance: {len(fails)} FAIL' if fails else 'zero_tolerance: OK')
sys.exit(1 if fails else 0)

# checks/prewrite_board.py — THE MANDATORY STEP-0 BOARD (session ac: "not words, but seriously")
# Machine output only. Run BEFORE every chapter; act on what it says; never write past a red flag.
import json, re, io, glob, subprocess, os
os.chdir('/home/user/Soul_Land_3_Project')
W = print
W("=" * 62)
W("THE PREWRITE BOARD — machine output, step 0 (before every chapter)")
W("=" * 62)

# [1] suite baseline
r = subprocess.run(['sh', 'checks/run_all.sh'], capture_output=True, text=True)
fails = [l for l in r.stdout.splitlines() if l.startswith('FAIL')]
exits = [l for l in r.stdout.splitlines() if 'exit' in l]
W(f"[1] SUITE: {exits[-1] if exits else 'NO EXIT LINE'} | FAIL lines: {len(fails)}")
for l in fails: W("    " + l[:120])

# [2] state ground truth
st = json.load(open('checks/state.json'))
ch = {int(k): v for k, v in st.items() if k.isdigit()}
lc = max(ch)
W(f"[2] STATE: {lc} chapters on disk; end state: " +
  str({k: ch[lc].get(k) for k in ('rank', 'sp', 'hawk', 'ledger')}) +
  " | ensemble: " + str(ch[lc].get('ensemble')))

# [3] registry live obligations
reg = io.open('BUTTERFLY_REGISTRY.md', encoding='utf-8').read()
W("[3] REGISTRY — obligations live for ch86+ / DUE / forward:")
for line in reg.splitlines():
    if line.startswith('| **') and re.search(r'ch8[6-9]|ch9[0-9]|DUE|NEXT|forward|long line', line, re.I):
        if '✅' not in line.split('|')[3 if len(line.split('|')) > 3 else 2]:
            W("    " + line[:155])

# [4] defect scan — the "use everything" gaps, measured
prose = {}
for f in sorted(glob.glob('chapters/chapter_*.md')):
    n = int(re.search(r'(\d+)', f).group(1))
    t = io.open(f, encoding='utf-8').read()
    cut = t.find('\n---\n'); end = t.find('## End of Chapter')
    prose[n] = t[cut:end] if (cut != -1 and end != -1) else t
lastn = max(prose)
W("[4] DEFECT SCAN (gap = chapters since last on-page):")
for name, pat in [
    ("Talent-named      ", r'Adaptation Talent|the talent that had|the oldest thing he owned'),
    ("Witness-aloud     ", r'thousand-year soul skill|farms the edges|herding|seen and spared'),
    ("System 「全能」    ", r'Comprehensive|全能'),
    ("Techniques        ", r'Grain Cut|The Question|Answering Stroke|Unwritten|Still Water'),
    ("Sword-alive       ", r'Frost Abyss|the sword'),
    ("Smith-life        ", r'forge|hammer|anvil|smith'),
    ("The-bill/wire     ", r'worthy enough|not joking|priced an education|the bill'),
    ("Brother-thread    ", r'his brother|brother-shaped|the brother'),
]:
    hits = [n for n, p in prose.items() if re.search(pat, p, re.I)]
    mx = max(hits) if hits else 0
    gap = (lastn - mx) if hits else 999
    flag = "\U0001F534" if gap >= 8 else ("\U0001F7E1" if gap >= 5 else "\u2705")
    W(f"    {flag} {name} last ch{mx}  (gap {gap})")

# [5] canon position + fetch order (COMPUTED from disk + the +3 offset map)
nums = sorted(int(re.search(r'(\d+)', f).group(1)) for f in glob.glob('canon_extract/chapters/canon_*.txt'))
hi = nums[-1]; lo = hi
while (lo - 1) in nums:
    lo -= 1
nxt = hi + 1
W(f"[5] CANON: contiguous working set {lo}\u2013{hi} (isolated: {[n for n in nums if n < lo]}) | NEXT: canon {nxt} = their chapter-{nxt + 3}, title-verify BEFORE writing")
import re as _re
_pairs = []
import glob as _g
for _f in sorted(_g.glob('chapters/chapter_*.md')):
    _n = int(_re.findall(r'\d+', _f)[0])
    _ms = _re.findall(r'canon ch (\d+)|\bch (\d{3})\b', io.open(_f, encoding='utf-8').read(500))
    _ms = [a or b for a, b in _ms]
    if _ms: _pairs.append((_n, max(int(x) for x in _ms)))
_spans = [b-a for (_, a), (_, b) in zip(_pairs, _pairs[1:]) if b-a > 0]
_straight = 0
for _s in reversed(_spans):
    if _s == 1: _straight += 1
    else: break
W(f"    coverage: trailing canon/fic ratio {round(sum(_spans[-8:])/max(1,len(_spans[-8:])),2)} · 1:1 lockstep streak {_straight} (LAW pp §7: coverage is ELASTIC — fetch ahead when an arc is mid-flight; declare the span; lockstep is a smell)")
idxp = 'canon_extract/CANON_INDEX_23_600.txt'
if os.path.exists(idxp):
    for ln in io.open(idxp, encoding='utf-8', errors='replace'):
        m = re.match(r'\s*(\d+)\s+(.+)', ln)
        if m and int(m.group(1)) == nxt:
            W(f"    expected title (fuzzy \u2014 index glues title+first-line): {m.group(2).strip()[:60]}")
            break

# [6] footer carry (COMPUTED from state.json + the newest chapter's ranks line)
st = json.load(io.open('checks/state.json', encoding='utf-8'))
cur = max(int(k) for k in st)
e = st[str(cur)]
lf = io.open(f'chapters/chapter_{cur}.md', encoding='utf-8').read()
m = re.search(r'### Ranks at chapter end:.*', lf)
W(f"[6] FOOTER CARRY (ch{cur}, state.json + footer): rank {e.get('rank')} · SP {e.get('sp')} · hawk {e.get('hawk')} · ledger {e.get('ledger')}")
W("    footer: " + (m.group(0)[:150] if m else "MISSING RANKS LINE"))

# [7] MOTIF KEEP-ALIVE (STYLE_GOLD.md — the good-things law; enrich when due, never force)
W("[7] MOTIF KEEP-ALIVE (gold; \U0001F7E1 gap>=10 \U0001F534 gap>=16 — consult STYLE_GOLD.md):")
for name, pat in [
    ("the drawer        ", r'the drawer'),
    ("hall-that-hears   ", r'hall that hears'),
    ("price/correct-chg ", r'correct change|the price of|priced'),
    ("grain-read        ", r'the grain'),
    ("first-hand-in     ", r'first hand in|first one in, because it always'),
    ("the-margin        ", r'the margin'),
]:
    hits = [n for n, pp in prose.items() if re.search(pat, pp, re.I)]
    mx = max(hits) if hits else 0
    gap = (lastn - mx) if hits else 999
    flag = "\U0001F534" if gap >= 16 else ("\U0001F7E1" if gap >= 10 else "\u2705")
    W(f"    {flag} {name} last ch{mx}  (gap {gap})")
W("    STYLE: dialogue-load is a dial (lesson 44-66% / hush 8-15% / standard 13-30%); 1-2 gold patterns per chapter, never a checklist.")
W("=" * 62)

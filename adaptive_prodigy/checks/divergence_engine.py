#!/usr/bin/env python3
# Layer 7: DIVERGENCE ENGINE (LAW pp — natural divergence; canon is ore, not fate)
# Parses DIVERGENCE_LEDGER.md, computes canon-streak + storm-clock + thread pressure,
# prints the FORWARD-TICK questions to answer BEFORE writing any chapter.
# Fail conditions (rare, real): ledger unparseable · derivation not SHOWN on a streak (ch94+). Clocks are smells, not quotas (LAW pp symmetry).
import io, re, sys, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fail = []
W("=" * 62)
W("== Layer 7: divergence_engine.py (LAW pp: canon = ore, trajectory ours) ==")

# --- 1. ledger ---
rows = []
for line in io.open('DIVERGENCE_LEDGER.md', encoding='utf-8'):
    if re.match(r'^\| D\d+ \|', line):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) >= 8:
            rows.append(dict(id=c[0], status=c[1], mag=c[2], thread=c[3],
                             cause=c[4], effect=c[5], horizon=c[6], paid=c[7]))
        elif len(c) == 7:
            rows.append(dict(id=c[0], status=c[1], mag=c[2], thread=c[3],
                             cause=c[4], effect=c[4], horizon=c[5], paid=c[6]))
if not rows:
    fail.append('ledger unparseable (no D-rows)')
act = [r for r in rows if r['status'] == 'ACTIVE']
held = [r for r in rows if r['status'] == 'HELD']
storms = [r for r in rows if r['mag'] == 'STORM']
W(f"  ledger: {len(rows)} rows — {len(act)} ACTIVE · {len(held)} HELD · {len(storms)} STORM-class")

# --- 2. canon-full streak (the forcing smell) ---
def classify(n):
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    m = re.search(r'## Canon Reference:([^\n]*)', t)
    if not m: return '?'
    return 'full' if re.search(r'\bfull\b', m.group(1), re.I) else 'mixed'
nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
streak = 0
for n in reversed(nums):
    if classify(n) == 'full': streak += 1
    else: break
fp = sum(1 for n in nums[-10:] if "canon's own" in io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read().lower())
flag = "\U0001F534" if streak >= 6 else ("\U0001F7E1" if streak >= 3 else "\u2705")
W(f"  {flag} canon-full streak: {streak} chapters — a SMELL, not a verdict: verify derivation (convergence by honest causes is allowed; silent obedience is not; neither is manufactured divergence)")
lastn = nums[-1]
if streak >= 3 and lastn >= 94:
    newest = io.open(f'chapters/chapter_{lastn:02d}.md', encoding='utf-8').read()
    cites = sorted(set(re.findall(r'D\d\d', newest)))
    if not cites:
        fail.append(f'streak {streak} and ch{lastn} cites no ledger rows — SHOW the derivation (D-rows in the footer), or let the causes break the streak; never force either way')
    else:
        W(f"    derivation SHOWN ({', '.join(cites)}) — the spine was earned from OUR causes; it stands")

# --- 3. storm clock (originality budget) ---
lastn = nums[-1]
def paid_ch(r):
    m = re.findall(r'ch(\d+)', r['paid'])
    return max(int(x) for x in m) if m else 0
storm_paid = [paid_ch(r) for r in storms if paid_ch(r)]
clock = lastn - max(storm_paid) if storm_paid else 99
flag = "\U0001F534" if clock >= 8 else ("\U0001F7E1" if clock >= 5 else "\u2705")
W(f"  {flag} storm-clock: {clock} chapters since a STORM thread paid — a SMELL, not a quota: if a cause demands payment, pay it; if threads are honestly HELD, hold; NEVER manufacture a storm")

# --- 4. FORWARD-TICK (answer before writing; anything is allowed — record the cause) ---
W("-" * 62)
W("FORWARD-TICK — for each ACTIVE thread: canon would say…? OUR state implies…? DECIDE, then record the cause:")
for r in sorted(act, key=lambda r: (r['mag'] != 'STORM', r['id'])):
    W(f"  {r['id']} [{r['mag']}] {r['thread']}: {r['cause'][:60]} -> {r['effect'][:60]}…")
W("  RULES: ours wins over canon · breaks mean canon's event is DEAD (do not resurrect) ·")
W("  HELD threads pay on their own horizons · new facts need causes from this ledger · numbers need sources (ours).")
W("=" * 62)
if fail:
    print("divergence_engine: " + str(len(fail)) + " FAIL"); [print("  FAIL " + f) for f in fail]; sys.exit(1)
print("divergence_engine: OK")

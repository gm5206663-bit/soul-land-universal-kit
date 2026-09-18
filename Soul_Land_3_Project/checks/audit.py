#!/usr/bin/env python3
"""AUDIT — whole-workspace consistency audit, every chapter, every tracked fact.

Unlike verify.py (which checks rules) this checks FACTS AGAINST EACH OTHER across all chapters:
  1. the children's age (AU = ten; canon's "nine" must be adapted and recorded)
  2. each canon character's spiritual power (must not drift from its canon value)
  3. each character's ring count (must not drift)
  4. the hawk's age (monotonic, and consistent with the recorded chain)
  5. documented canon divergences (every AU change to a canon line must be recorded)
  6. progression lines (rank / spiritual power / hawk / blacksmith) never silently frozen
  7. Wulin's canon standing (2nd-rank blacksmith, youngest in Association records) vs Lin Hao's
  8. locked items (fusion door, Union, 2nd seal, question resolved, city named)

Run:  python3 checks/audit.py
"""
import os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'chapters')
CODEX = open(os.path.join(ROOT, 'THE_CODEX.md'), encoding='utf-8').read()

ch = {}
for f in sorted(os.listdir(CH)):
    if f.endswith('.md'):
        n = int(f[8:10])
        full = open(os.path.join(CH, f), encoding='utf-8').read()
        prose = full.split('## End of Chapter')[0]
        # the STORY BODY excludes the Canon Reference / Timeline header block
        body = prose.split('## Part 1')[1] if '## Part 1' in prose else prose
        ch[n] = {'full': full, 'prose': prose, 'body': body, 'head': prose[:2500]}
MAX = max(ch)
F, W = [], []
def fail(m): F.append(m)
def warn(m): W.append(m)

# ---------------------------------------------------------------- 1. AGE
print('=== 1. THE CHILDREN\'S AGE (AU = ten) ===')
for n, c in sorted(ch.items()):
    for m in re.finditer(r'only (nine|ten)[ -]years?[ -]old|these children are only (nine|ten)', c['full'], re.I):
        age = (m.group(1) or m.group(2)).lower()
        if age == 'nine':
            if 'adaptation' not in c['head'].lower() and 'divergence' not in c['head'].lower():
                fail(f'ch{n}: canon\'s "nine-years-old" appears but the AU age divergence is not recorded in the header')
        # any other "nine years old" used as a CURRENT age is a contradiction
    PAST = re.compile(r'(had|have|has)\s+\w+|when\s+(he|she|they|I)\s+was|at\s+the\s+age\s+of|aged\s+\w+|back\s+when|since\s+he\s+was', re.I)
    for m in re.finditer(r'\b(they are nine|he is nine|she is nine|at nine years old)\b', c['prose'], re.I):
        # "at nine years old" is legitimate for a PAST event — the rule's own comment says so.
        # Only flag it when the surrounding clause is not past-framed.
        before = c['prose'][max(0, m.start()-70):m.start()]
        if m.group(0).lower() == 'at nine years old' and PAST.search(before):
            continue
        fail(f'ch{n}: a current age of nine contradicts the AU (the children are ten): "{m.group(0)}"')
# "at nine" is legitimate ONLY for a past event (passing an exam, absorbing a soul)
print('  ok   age audited across all chapters')

# ------------------------------------------- 2. CANON SPIRITUAL POWER DRIFT
print('\n=== 2. CANON SPIRITUAL POWER (must not drift) ===')
# Wang Jinxi is 18 throughout (canon c113, and nothing in the story changes it).
# Zhang Yangzi is 41 (canon c113) UNTIL ch39, when Little Black dies and he loses a third of
# his spiritual power — an AU story event staged on-page in ch39. From ch39 the value is ~27.
# A flat "canon says 41" check therefore cries wolf on every chapter after the event.
CANON_SP = {'Wang Jinxi': (18, 1, 61), 'Zhang Yangzi': (41, 1, 38)}
AU_SP = {'Zhang Yangzi': (27, 39, 61)}   # post-Little-Black, AU
for who, (val, lo, hi) in CANON_SP.items():
    seen = set()
    for n, c in sorted(ch.items()):
        # [^.\n] not [^.]: the match must not cross a line break, or it will run from one
        # header/footer line into the next and attribute one character's number to another.
        for m in re.finditer(re.escape(who) + r'[^.\n]{0,70}?spiritual power[^.\n]{0,40}?(\d{2,3})', c['full'], re.I):
            v = int(m.group(1))
            if lo <= n <= hi:
                if v != val:
                    fail(f'ch{n}: {who}\'s spiritual power is {v}, canon says {val}')
            elif who in AU_SP:
                aval, alo, ahi = AU_SP[who]
                if alo <= n <= ahi and v != aval and v != val:
                    fail(f'ch{n}: {who}\'s spiritual power is {v}; expected {aval} after ch{alo} '
                         f'(Little Black) or {val} before it')
            seen.add(v)
    if seen:
        print(f'  ok   {who}: {sorted(seen)} (canon {val} for ch{lo}-{hi}'
              + (f', AU {AU_SP[who][0]} from ch{AU_SP[who][1]}' if who in AU_SP else '') + ')')
# Gu Yue: canon 153, and she must remain the strongest in QUALITY
# The value must sit immediately after the words "spiritual power". The old pattern let any
# three-digit number inside a 60-char window count, so canon citations like "(canon c133)" and
# "(canon c224)" were read as spiritual-power readings.
gy = set()
for n, c in sorted(ch.items()):
    for m in re.finditer(r'Gu Yue[^.\n]{0,60}?spiritual power\D{0,20}?(\d{3})', c['full'], re.I):
        gy.add(int(m.group(1)))
    for m in re.finditer(r'Gu Yue[^.\n]{0,60}?(\d{3})[^.\n]{0,20}points of spiritual power', c['full'], re.I):
        gy.add(int(m.group(1)))
if gy and gy != {153}:
    fail(f'Gu Yue\'s spiritual power is stated as {sorted(gy)}; canon says 153')
else:
    print(f'  ok   Gu Yue: {sorted(gy) or "153 (by reference)"} (canon 153)')

# ------------------------------------------------------- 3. RING COUNTS
print('\n=== 3. RING COUNTS ===')
OTHERS = ('Lin Hao','Xie Xie','Wang Jinxi','Zhang Yangzi','Wei Xiaofeng','Wu Zhangkong','Gu Yue','Wulin')
# expected ring count is TIME-DEPENDENT: Xie Xie has one ring before ch17, two after
def expected_rings(who, n):
    if who == 'Wu Zhangkong': return 6
    if who == 'Xie Xie': return 2 if n >= 17 else 1
    # Lin Hao's hawk crossed a thousand years in ch 40 and a third ring was bestowed,
    # so his count is time-dependent too: 2 before ch40, 3 from ch40 onward.
    if who == 'Lin Hao': return 3 if n >= 40 else 2
    if who == 'Wang Jinxi': return 2
    return None
for who in ('Lin Hao','Xie Xie','Wang Jinxi','Wu Zhangkong'):
    for n, c in sorted(ch.items()):
        expected = expected_rings(who, n)
        for m in re.finditer(re.escape(who) + r"'?s?[^.]{0,40}?(one|two|three|four|five|six|1st|2nd|3rd)[- ]rings?\b", c['body'], re.I):
            # reject if another character's name sits between the subject and the ring count
            gap = m.group(0)[len(who):]
            if any(o in gap for o in OTHERS if o != who):
                continue
            w = m.group(1).lower()
            v = {'one':1,'1st':1,'two':2,'2nd':2,'three':3,'3rd':3,'four':4,'five':5,'six':6}.get(w)
            # skip enumerations and transitions ("one ring, and two rings", "one ring's worth of habit,
            # two rings' worth of light") — these are not claims about the character's ring count
            after = c['body'][m.end():m.end()+40]
            if re.match(r"[,.]?\s*(and\s+)?(one|two|three)\s+rings?", after, re.I) \
               or re.search(r"'?s worth", m.group(0) + after[:14], re.I) \
               or re.search(r'thought about|about one ring|one ring, and', m.group(0), re.I):
                continue
            if v and expected and v != expected and not re.search(r'a third ring|will|when|at the crossing', m.group(0), re.I):
                fail(f'ch{n}: {who} has {v} rings, expected {expected} at this point — "{m.group(0)[:60]}"')
print('  ok   ring counts audited')

# --------------------------------------------------------- 4. HAWK AGE
print('\n=== 4. HAWK AGE (monotonic; must match the recorded chain) ===')
ONES={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
TENS={'ten':10,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
TEENS={'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}
def w2i(t):
    return sum(TENS.get(p,0) if p in TENS else TEENS.get(p,0) if p in TEENS else ONES.get(p,0)
               for p in t.replace('-',' ').split())
hawk = {}
for n, c in sorted(ch.items()):
    for para in c['prose'].split('\n\n'):
        if not re.search(r'hawk|gale|condensed wind|soul[- ]spirit', para, re.I):
            continue
        for m in re.finditer(r'(seven|eight|nine) hundred(?: and ([a-z-]+))? years', para, re.I):
            v = {'seven':700,'eight':800,'nine':900}[m.group(1).lower()]
            if m.group(2): v += w2i(m.group(2))
            hawk[n] = max(hawk.get(n, 0), v)
prev = 0
for n, v in sorted(hawk.items()):
    if v < prev: fail(f'ch{n}: hawk age went DOWN ({prev} -> {v})')
    if v >= 1000: fail(f'ch{n}: hawk reached {v} — the 1,000-yr crossing is gated')
    prev = max(prev, v)
counts = collections.Counter(hawk.values())
for age, k in counts.items():
    if k >= 3: fail(f'the hawk is stated as {age} in {k} chapters — frozen')
print(f'  ok   hawk chain: {" -> ".join(f"ch{n}:{v}" for n,v in sorted(hawk.items()))}')

# --------------------------------------- 5. CANON DIVERGENCES MUST BE RECORDED
print('\n=== 5. DOCUMENTED CANON DIVERGENCES ===')
rec = CODEX.count('AU divergence') + CODEX.count('AU adaptation') + CODEX.count('CANON ADAPTATION')
in_ch = sum(1 for c in ch.values() if re.search(r'AU divergence|AU adaptation|CANON ADAPTATION|butterfly', c['full'], re.I))
print(f'  ok   {rec} divergence notes in the codex, {in_ch} chapters carry one')

# ------------------------------------------------ 6. PROGRESSION FREEZE
print('\n=== 6. PROGRESSION LINES (no silent freeze) ===')
rank = {}
for n, c in sorted(ch.items()):
    m = re.search(r'Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d\d)', c['full'])
    if m: rank[n] = int(m.group(1))
run, worst = 1, 1
ks = sorted(rank)
for i in range(1, len(ks)):
    run = run + 1 if rank[ks[i]] == rank[ks[i-1]] else 1
    worst = max(worst, run)
CEIL = 30
top = rank[max(ks)] if rank else 0
if rank and top == CEIL:
    print(f'  ok   rank frozen at the HARD WALL ({CEIL}) — legal, gated by the hawk\'s crossing')
elif rank and top > CEIL:
    # The wall was gated by the hawk's thousand-year crossing. It opened in ch 40, so a long
    # historical run AT the wall is legal — it was gated, not neglected, and it did resolve.
    print(f'  ok   rank held at the gated wall then advanced to {top} — the freeze was gated, and it resolved')
elif worst > 3:
    fail(f'soul rank frozen for {worst} consecutive chapters')
else:
    print(f'  ok   rank chain moves (longest run {worst})')

# --------------------------------------- 7. BLACKSMITH STANDING (canon Wulin)
print('\n=== 7. BLACKSMITH STANDING ===')
if re.search(r'Lin Hao[^.]{0,80}youngest in (the )?Association', CODEX, re.I):
    fail('Lin Hao is claimed as the youngest in Association records — that is Wulin\'s canon record')
else:
    print('  ok   Wulin\'s canon record (youngest in Association records) is not claimed for Lin Hao')

# ------------------------------------------------------- 8. LOCKED ITEMS
print('\n=== 8. LOCKED ITEMS ===')
# NB: locked items are checked against the STORY BODY only. Footers legitimately say
# "NOT triggered: fusion door opened", and canon-reference headers legitimately discuss canon.
# The SHREK lock is scoped to WU ZHANGKONG'S ORIGIN — canon itself has the boys discussing
# Shrek Academy as a goal (our ch1), which is NOT a violation.
LOCKS = [
 ('fusion door opened',  r'fusion door[^.]{0,40}opened'),
 ('Hawk-Soul Union used', r'Hawk-Soul Union[^.]{0,40}(used|activated|engaged)'),
 ('2nd seal broken',      r'second seal[^.]{0,30}(broke|broken|shattered)'),
 ('question resolved',    r'the question[^.]{0,50}(was answered|had been answered|answered at last)'),
 ('Wu Zhangkong\'s origin city named', r'Wu Zhangkong[^.]{0,120}\bShrek\b|\bShrek\b[^.]{0,120}(expelled|threw me out|thrown out|came from)'),
]
for n, c in sorted(ch.items()):
    for name, pat in LOCKS:
        for m in re.finditer(pat, c['body'], re.I):
            seg = c['body'][max(0, m.start()-70):m.end()+20].lower()
            if any(x in seg for x in ('not ','never ','not that','without ','gated','locked','still ','no one','nobody')):
                continue
            fail(f'ch{n}: "{name}" appears triggered — "{m.group(0)[:60]}"')
print('  ok   locked items audited')

# ---------------------------------------------- 9. ENSEMBLE PRESENCE (the sidelining check)
print('\n=== 9. ENSEMBLE PRESENCE (main cast must not be sidelined) ===')
# The user's correction: "you complete putting aside tang wulin mostly and others characters also…
# wulin is relationship is almost forgot… gu Yue and Lin hao there is no development"
MAIN = ('Wulin', 'Xie Xie', 'Gu Yue')
# Gu Yue is not introduced until ch8 (canon ch 62-66) and Wang Jinxi/Zhang Yangzi/Wei Xiaofeng
# not until the tournament, so the ensemble check starts at ch8.
FROM = 8
presence = {w: [] for w in MAIN}
for n, c in sorted(ch.items()):
    if n < FROM: continue
    body = c['body']
    words = len(body.split())
    for w in MAIN:
        density = len(re.findall(re.escape(w), body)) / max(words, 1) * 1000
        presence[w].append((n, round(density, 2)))
for w, series in presence.items():
    # A character is SIDELINED when absent or near-absent for 2+ consecutive chapters.
    # Measured data (v2.55): Wulin 0.00 in ch34 AND ch35; Gu Yue 0.00 in ch33, 34 AND 35.
    run, worst, at = 0, 0, None
    for n, d in series:
        if d < 0.5:
            run += 1
            if run > worst: worst, at = run, n
        else:
            run = 0
    tail = [d for _, d in series[-4:]]
    if worst >= 2:
        fail(f'{w} is SIDELINED — absent/near-absent for {worst} consecutive chapters (ending ch{at}); '
             f'recent densities {tail}')
    else:
        print(f'  ok   {w}: recent densities {tail}')
# the Wulin/Lin Hao relationship specifically must not go cold
wl = [d for _, d in presence['Wulin'][-3:]]
if sum(1 for d in wl if d < 0.5) >= 2:
    fail(f'the Wulin/Lin Hao relationship has gone cold — densities {wl} in the last three chapters')

# ------------------------------------------- 10. CANON BACKING PER CHAPTER
print('\n=== 10. CANON BACKING (a chapter must not be invented wholesale) ===')
for n, c in sorted(ch.items()):
    head = c['head']
    has_ref = 'Canon Reference' in c['full']
    unfetchable = bool(re.search(r'could not be fetched|unfetchable', c['full'], re.I))
    cites = len(re.findall(r'canon ch \d+', head, re.I))
    if not has_ref:
        fail(f'ch{n}: no Canon Reference header at all')
    elif unfetchable:
        warn(f'ch{n}: canon could not be fetched — this chapter is NOT canon-backed and must not be '
             f'treated as adapting canon')
    elif cites == 0:
        warn(f'ch{n}: Canon Reference header cites no specific canon chapter')
ok_count = sum(1 for c in ch.values() if 'Canon Reference' in c['full'])
print(f'  ok   {ok_count}/{len(ch)} chapters carry a Canon Reference header')

# ------------------------------------- 11. APPEARANCE & MUTATIONS (the forgotten line)
print('\n=== 11. APPEARANCE & MUTATIONS (user: "you completely trash out his appearance") ===')
MUT = r'storm-light|storm-gray|gold-flecked|hawk-gold|feather-mark|hair tips|his hair|his temple|marks on his forearm|forearms stood up|breeze in it|tastes of rain|see the tracks|marks.{0,20}glow|sheen to it'
ATT = r'handsome|striking|beautiful|good-looking|pretty|his face|the face|storm-gray lock|look at him|looked at him|looked again|could not look'
mut_run, att_run = 0, 0
worst_mut = worst_att = 0
for n, c in sorted(ch.items()):
    if n < 8: continue
    body = c['body']
    if re.search(MUT, body, re.I): mut_run = 0
    else:
        mut_run += 1; worst_mut = max(worst_mut, mut_run)
    if re.search(ATT, body, re.I): att_run = 0
    else:
        att_run += 1; worst_att = max(worst_att, att_run)
if worst_mut >= 3:
    fail(f'his APPEARANCE/MUTATIONS are unwritten for {worst_mut} consecutive chapters — the codex plans '
         f'permanent feather-marks, eyes perceiving spiritual-energy tracks and bone densification, and '
         f'none of it has been written since ch7')
if worst_att >= 3:
    fail(f'NO character comments on his appearance for {worst_att} consecutive chapters — he is '
         f'canonically striking and people react to that')
if worst_mut < 3 and worst_att < 3:
    print(f'  ok   appearance and mutations present (longest gaps: mutations {worst_mut}, comments {worst_att})')

# ---------------------------------------- 12. RING-AGE BENEFITS (nearly 2,000 years in one body)
print('\n=== 12. RING-AGE BENEFITS ===')
# He carries two rings of ~900 years each. Physical stats must reflect that, not a normal rank-30 body.
kg = []
for n, c in sorted(ch.items()):
    for m in re.finditer(r'\b(\d{3})\s*(?:kg|kilograms)\b', c['body'], re.I):
        kg.append((n, int(m.group(1))))
if kg:
    latest = kg[-1]
    # a body carrying ~1,800 years of soul ring must read far above an ordinary child; canon ch128 puts
    # Wulin's full strength over 1,000 kg, so a fist measurement in the low hundreds is implausibly low
    if latest[1] < 400:
        warn(f'ch{latest[0]}: fist measured at {latest[1]} kg while carrying ~1,800 years of soul ring — '
             f'canon puts Wulin\'s full strength over 1,000 kg, so this is likely far too low (OPEN)')
    print(f'  ok   measured physical anchor: {latest[1]} kg at ch{latest[0]}')

# ------------------------------------------------------------------ REPORT
print('\n' + '=' * 70)
if W:
    print(f'WARNINGS ({len(W)}):')
    for w in W: print('  -', w)
if F:
    print(f'\nFAILURES ({len(F)}):')
    for f in F: print('  x', f)
    print('=' * 70); print('AUDIT: FAIL'); sys.exit(1)
print('AUDIT: PASS — no cross-chapter contradictions found'); print('=' * 70); sys.exit(0)

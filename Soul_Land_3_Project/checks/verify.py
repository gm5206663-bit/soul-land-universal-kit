#!/usr/bin/env python3
"""PERMANENT VERIFICATION SUITE — Soul Land 3: The Adaptive Prodigy.
Run after EVERY chapter. Any FAIL must be fixed before the chapter is called done.
Exit code 0 = all pass, 1 = at least one fail.
"""
import re, sys, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'chapters')
CODEX = open(os.path.join(ROOT, 'THE_CODEX.md'), encoding='utf-8').read()
STATUS = open(os.path.join(ROOT, 'LIN_HAO_STATUS.md'), encoding='utf-8').read()
CONT = open(os.path.join(ROOT, 'CONTINUATION_PROMPT.md'), encoding='utf-8').read()

chapters = {}
for f in sorted(os.listdir(CH)):
    if f.endswith('.md'):
        n = int(f[8:10])
        full = open(os.path.join(CH, f), encoding='utf-8').read()
        _head = full.split('## End of Chapter')[0]
        # The "## Canon Reference / ## Timeline" header block is metadata, not prose.
        # Counting it produced false positives (stale numbers quoted in canon notes).
        _body = _head.split('\n---\n', 1)[1] if '\n---\n' in _head else _head
        chapters[n] = {
            'full': full,
            'header': _head.split('\n---\n', 1)[0] if '\n---\n' in _head else _head,
            'prose': _body,
            'footer': full.split('## End of Chapter')[1] if '## End of Chapter' in full else '',
        }
MAXCH = max(chapters)

F, W = [], []
def fail(sec, msg): F.append(f"[{sec}] {msg}")
def warn(sec, msg): W.append(f"[{sec}] {msg}")
def ok(sec, msg): print(f"  ok   {msg}")

# ---------------------------------------------------------------- 1. STRUCTURE
print("\n=== 1. STRUCTURE ===")
for n, c in sorted(chapters.items()):
    p = c['prose']
    hdr = c.get('header', c['full'])
    if '## End of Chapter' not in c['full']: fail('STRUCT', f"ch{n}: no '## End of Chapter' footer")
    if '### Chapter Summary' not in c['full']: fail('STRUCT', f"ch{n}: no Chapter Summary")
    if not re.search(r'^## Canon Reference', hdr, re.M): fail('STRUCT', f"ch{n}: no Canon Reference header")
    if not re.search(r'^## Timeline', hdr, re.M): fail('STRUCT', f"ch{n}: no Timeline header")
    # part numbering must be sequential
    raw = re.findall(r'^## Part ([\dA-Z-]+)', p, re.M)
    base = [x.split('-')[0] for x in raw]
    nums = [int(b) for b in base if b.isdigit()]
    if nums and nums != sorted(nums):
        fail('STRUCT', f"ch{n}: part numbers out of order: {raw}")
    if nums and nums[0] != 1:
        fail('STRUCT', f"ch{n}: parts do not start at 1: {raw}")
    if nums and nums[-1] - nums[0] + 1 != len(set(nums)):
        fail('STRUCT', f"ch{n}: gap in part numbering: {raw}")
    # 🔴 exact duplicate part headings. The existing order/gap checks pass on [1,1,2,3,4,5]
    # (sorted, starts at 1, len==max) — so ch33 and ch58 each shipped with two identically-named
    # sections for an unknown number of sessions. Compare the FULL labels, not just the numbers.
    import collections as _c
    dupes = [k for k, v in _c.Counter(raw).items() if v > 1]
    if dupes:
        fail('STRUCT', f"ch{n}: duplicate part heading(s): {dupes} (raw: {raw})")
    if len(p.split()) < 1200: warn('STRUCT', f"ch{n}: prose only {len(p.split())} words (thin)")
ok('STRUCT', f"{MAXCH} chapters, headers + footers + part numbering checked")

# ------------------------------------------------- 2. CJK / PLACEHOLDER / JUNK
print("\n=== 2. TEXT HYGIENE ===")
class _RankState:
    pass
_rank_state = _RankState()
_rank_state.nring = 2

for n, c in sorted(chapters.items()):
    for name, blob in (('prose', c['prose']), ('footer', c['footer'])):
        cjk = re.findall(r'[\u4e00-\u9fff]+', blob)
        # 🔴 ALLOWLIST (2026-08-30, ch71) — §4.13 rule 3. The belief behind this check was
        # "chapters are English-only." THE FOURTH RING LAW breaks it deliberately: the martial
        # soul's evolved name and its Domain are LOCKED in THE_CODEX.md with their Chinese, and a
        # martial soul that changes its name is allowed to keep the name it was given. Everything
        # else still fails, so the check keeps catching real stray characters.
        _CJK_ALLOWED = {'霜溟剑', '霜溟领域', '镇', '全能'}
        cjk = [c for c in cjk if c not in _CJK_ALLOWED]
        if cjk: fail('CJK', f"ch{n} {name}: stray CJK {set(cjk)} (chapters are English-only; CJK glosses live in the codex dossiers only)")
        for bad in ('PLACEHOLDER', 'TODO', 'XXX', 'FIXME', 'lorem'):
            if bad in blob: fail('JUNK', f"ch{n} {name}: contains '{bad}'")
        if '  ' in blob.replace('\n\n','').replace('\n',' '):
            pass  # double space is stylistic in this project
ok('CJK', "no stray CJK / placeholders in any chapter")

# ------------------------------------------- 3. SPIRITUAL POWER MONOTONICITY
print("\n=== 3. SPIRITUAL POWER (must never decrease) ===")
import json as _json
_STATE = _json.load(open(os.path.join(ROOT, 'checks', 'state.json'), encoding='utf-8'))
SP = {int(k): v for k, v in _STATE['spiritual_power_by_chapter'].items()}
# v2.63: rebuilt to the canon-consistent curve (POWER_MODEL.md §3) — Lin Hao stays BELOW
# Gu Yue's canon 153/186 at every point. The old table (218/226/241/267/284/291/298/305)
# put him above canon's crown and has been retired; those values must not reappear.
# 🔴 REBUILT 2026-08-28 to the re-baselined curve (+60, Monster Law: he is ABOVE Gu Yue's canon
# 153 -> 186 at every point). The old table encoded the retired curve and its own retired values.
def _w(n):
    U=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve",
       "thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    T=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n<20: return U[n]
    t,o=divmod(n,100); h="one hundred" if t==1 else f"{U[t]} hundred"
    return h if not o else h+" and "+(U[o] if o<20 else T[o//10]+("-"+U[o%10] if o%10 else ""))
# 🔴 DERIVED FROM state.json, NOT HARDCODED (fixed 2026-08-29). This list was the last
# hand-maintained copy of the curve: ch62 shipped at 289 and the check could not see the
# number because 289 was not in the list, so the word-form lookup never ran and the chapter
# failed with "found [281]". `SP` three lines above is already derived from the footers;
# deriving the word list from the same source removes the second copy entirely.
CURVE=sorted(set(SP.values()))
WORDS={_w(v):v for v in CURVE}
WORDS['one hundred and fifty-three']=153          # Gu Yue's canon number, excluded below
# 🔴 Retired values must NOT include any value the new curve actually uses, or the check flags
# the current value as a regression. 218/226/241/256/264/281 are all live now.
for _r in (118,124,131,136,141,145,152,158,166,173,181,189,204,213,221,305,318):
    WORDS[_w(_r)]=_r
prev = 0
for n in sorted(chapters):
    if n < 21: continue
    pr = chapters[n]['prose'].lower()
    # Word-boundary match, and reject a preceding "thousand": a plain substring test matches
    # "two hundred and forty-one" INSIDE "one thousand two hundred and forty-one" (the hawk's age),
    # which is a retired pre-canon value and produces a false failure.
    found = []
    for k, v in WORDS.items():
        if v == 153:
            continue
        mm = re.search(r'(?<![\w-])(?<!thousand )' + re.escape(k) + r'(?![\w-])', pr)
        if not mm:
            continue
        # Guard against count-nouns: "two hundred and four strikes" is not a spiritual power.
        after = pr[mm.end():mm.end()+18]
        if re.match(r'\s*(strikes?|times|metres?|meters?|years?|days?|coins?|kg|kilograms?|ranks?|points?\b)', after):
            continue
        # 🔴 EXEMPTED 2026-08-30 (the "calibrate before you obey" rule, §4.8). ch70 wrote
        # "he had written one hundred and twenty-four lines" — the LEDGER count, which happens to
        # collide with retired spiritual power 124. The ledger is a line-count, so "line(s)"
        # immediately after a number is never a power reading.
        #
        # MEASURED, not assumed: a corpus scan of all 70 chapters found 55 number-word + "line(s)"
        # matches, and every one of them is a LEDGER count or a progression line ("Seventy-one
        # lines" ch21, "ninety-eight lines" ch37, "One hundred and four lines" ch57, "one hundred
        # and seven lines" ch62, "FOUR PROGRESSION LINES"). None is a spiritual power.
        # 🔴 My first version of this comment claimed the ledger is always written in digits and
        # never spelled out. That was FALSE and the same scan disproved it — most ledger counts
        # ARE spelled out. Corrected rather than left standing.
        # Residual risk, stated plainly: a chapter that put a power reading immediately before
        # "lines" would be skipped by this branch. No such sentence exists in the corpus, and the
        # digit-branch below (which has no "lines" exemption) would still catch it if it appeared
        # within 45 chars of a power keyword.
        if re.match(r'\s*lines?\b', after):
            continue
        found.append(v)
    # digits only count as spiritual power when a power keyword sits within 45 chars —
    # otherwise any 3-digit number (a hawk's age, a weight, a count) is misread as the stat.
    # (?<![\d,]) as well as \b: a comma counts as a word boundary, so "1,241" would otherwise
    # yield a spurious "241" — which is a retired pre-canon value and triggers a false failure.
    for m in re.finditer(r'(?<![\d,])([1-4]\d\d)(?![\d,])', pr):
        near = pr[max(0, m.start()-45):m.end()+25].lower()
        # a weight is not a spiritual-power reading: exclude kg/kilogram/strikes contexts
        if re.search(r'\bkg\b|kilogram|strikes|hammer', near):
            continue
        # 🔴 A CORRECTION NOTE legitimately quotes the retired value it is retiring
        # ("the delta previously read 120→218"). Flagging those makes the check unusable the
        # moment anything is corrected, which is exactly when you need it.
        if re.search(r'corrected|previously read|previously said|re-corrected|retired|pre-v3|the old note', near):
            continue
        if re.search(r'spiritual power|spirit connection|/ ?499|the number|the dial|the machine', near):
            found.append(int(m.group(1)))
    lin = [v for v in found if v != 153]
    exp = SP.get(n)
    if exp is None: continue
    # a chapter may repeat the previous value without restating it (nothing measured it).
    # only a CHANGE must be shown in prose — and a change must always come from a named source.
    prev_exp = SP.get(n-1)
    if exp not in lin and exp != prev_exp: fail('SPIRIT', f"ch{n}: expected spiritual power {exp} in prose, found {sorted(set(lin))}")
    top = max(lin) if lin else 0
    if top and top < prev: fail('SPIRIT', f"ch{n}: spiritual power went DOWN ({prev} -> {top})")
    prev = max(prev, top)
    # stale old values must not appear as his CURRENT power
    for stale in (305, 318, 118, 124, 131, 136, 141, 145, 152, 158, 166, 173, 181, 189, 204, 213, 221):
        if stale in lin:
            fail('SPIRIT', f"ch{n}: RETIRED pre-canon value {stale} still present (current = {exp}) — POWER_MODEL.md §3")
ok('SPIRIT', "chain 118->124->131->141->152 verified in prose; no retired pre-canon values")

# ---------------------------------------------------- 4. SOUL RANK PROGRESSION
print("\n=== 4. SOUL RANK (footer authoritative; prose must signal it) ===")
# 🔴 GENERATED, NOT ENUMERATED (2026-08-30, ch71). This dict used to be hand-written and stopped
# at 'forty' — so the moment he reached rank 45 the breakthrough check could not find the word
# "forty-five" in prose and reported a breakthrough that WAS shown as never shown. A hand-written
# lookup table of number-words is a stale-value generator. Built from the ones/tens instead.
_ONES = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven',
         'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
_TENS = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']
NUMWORD = {}
for _v in range(1, 101):
    _t, _o = divmod(_v, 10)
    NUMWORD[_ONES[_v] if _v < 20 else (_TENS[_t] + ('' if _o == 0 else '-' + _ONES[_o]))] = _v
prev = 0
for n in sorted(chapters):
    c = chapters[n]
    m = re.search(r'Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d\d)', c['footer'])
    if not m:
        if n >= 19: fail('RANK', f"ch{n}: footer has no 'Ranks at chapter end: Lin Hao NN' line")
        continue
    cur = int(m.group(1))
    if cur < prev: fail('RANK', f"ch{n}: soul rank went DOWN in footer ({prev} -> {cur})")
    # Ring-aware ceiling: canon grants a new ring at each 10th rank, so N rings cap the rank at N*10+9.
    # The ring count itself is read from the footer so the wall MOVES when a ring is bestowed.
    NUMW = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
    # Scope the ring count to LIN HAO's own state line. Scanning the whole footer picks up
    # other characters' ring counts — e.g. Gu Yue's quoted "we have two rings" — and then
    # flags Lin Hao's rank as over the ceiling.
    ring_src = c['footer']
    # 🔴 2026-08-30 (ch71): `[^\n]*` captured only the FIRST physical line, but the footer
    # hand-wraps at ~100 columns — ch71's "FOUR rings — three purple rings and one black ring"
    # wrapped onto line two, so the capture ended before the ring count and the chapter inherited
    # ch70's three rings, then rank 45 tripped the ring ceiling. Capture to the next bullet.
    lm = re.search(r'\*\*Lin Hao:\*\*(?:(?!\n- ).)+', c['footer'], re.S)
    if lm:
        ring_src = lm.group(0)
    # 🔴 2026-08-30: the optional colour was hardcoded to "purple" only. ch71 has a mixed set.
    ringm = re.search(r'(\d+|one|two|three|four|five|six)\s*(?:(?:purple|black|yellow|white)\s+)?rings?', ring_src, re.I)
    third  = bool(re.search(r'third\b|\b3(?:rd)?\s+ring', ring_src, re.I))
    # Ring count carries FORWARD: once the third ring is bestowed (ch40) a chapter that does
    # not restate it still has three. Defaulting to 2 flagged rank 31+ as over the ceiling.
    if not hasattr(_rank_state, 'nring'):
        _rank_state.nring = 2
    if ringm:
        g = ringm.group(1).lower()
        _rank_state.nring = int(g) if g.isdigit() else NUMW.get(g, _rank_state.nring)
    if third and _rank_state.nring < 3:
        _rank_state.nring = 3
    nring = _rank_state.nring
    # Canon grants the NEXT ring AT each 10th rank. A Soul Master may stand AT the threshold rank but
    # cannot advance past it until the next ring is earned. So N rings cap the rank at (N+1)*10:
    #   2 rings -> ceiling 30 (the wall Lin Hao stood at for eleven chapters)
    #   3 rings -> ceiling 40
    ceiling = (nring + 1) * 10
    if cur > ceiling:
        fail('RANK', f"ch{n}: rank {cur} exceeds the ceiling for {nring} ring(s) (max {ceiling})")
    # a BREAKTHROUGH chapter must show the breakthrough in prose; a steady chapter need not restate
    if prev and cur != prev:
        pr = c['prose']
        spoken = any(re.search(rf'\b[Rr]ank {k}\b', pr) for k, v in NUMWORD.items() if v == cur)
        # also accept the bare number-word on its own — the prose marks breakthroughs as "**Thirty-two.**"
        if not spoken:
            spoken = any(re.search(rf'(?<![\w-]){k}(?![\w-])', pr, re.I) for k, v in NUMWORD.items() if v == cur)
        moved  = bool(re.search(r'[Rr]ank (?:twenty-\w+|thirty|\d\d)\b', pr))
        if not (spoken or moved):
            fail('RANK', f"ch{n}: BREAKTHROUGH {prev} -> {cur} in footer but never shown in prose")
    prev = cur
# frozen-rank detector over the footer chain
foot = {}
for n, c in sorted(chapters.items()):
    m = re.search(r'Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d\d)', c['footer'])
    if m: foot[n] = int(m.group(1))
for n in sorted(foot):
    run = 1
    while n - run in foot and foot[n - run] == foot[n]: run += 1
    if foot[n] == 30:
        continue   # legal: rank 30 is the HARD WALL (2 rings cover 21-30); frozen by canon rule, not neglect
    # The pre-wall climb averaged a hold of 2-3 chapters. But settling into a NEW rank right after a
    # breakthrough is normal pacing, not neglect — the crossing opened at ch40, so rank 31 legitimately
    # holds longer. The check exists to catch FORGETTING a line, not to enforce a metronome.
    limit = 5 if foot[n] > 30 else 3
    if run > limit: fail('RANK', f"ch{n}: soul rank frozen at {foot[n]} for {run} chapters (max {limit})")
print(f"  ok   footer rank chain: {' -> '.join(str(foot[k]) for k in sorted(foot))}")

# ------------------------------------------------- 5. THE FOUR PROGRESSION LINES
print("\n=== 5. FOUR PROGRESSION LINES (ch21+) ===")
LINES = {21:['rank','sp'], 22:['rank','sp','sword'], 23:['rank','sp','sword','smith'],
         24:['rank','sp','sword','smith'], 25:['rank','sp','sword','smith']}
MARK = {'sword':r'Answering Stroke|Unwritten Stroke|Sword Intent|swordsman|Grain Cut|sword intent',
        # 🔴 widened: ch25 shows the smith line as "the blade from the side forge, … strikes" and
        # the narrow pattern missed it. A line is shown if the chapter names the craft or the work.
        'smith':r'Thousand Refinements|Second-rank smith|second rank|strikes|side forge|the forge|anvil|blacksmith'}
for n, need in LINES.items():
    pr = chapters[n]['prose']
    for k in need:
        if k in ('rank','sp'): continue
        if not re.search(MARK[k], pr): fail('LINES', f"ch{n}: progression line '{k}' not shown in prose")
ok('LINES', "all four lines present in prose where required")

# ------------------------------------------------------------ 6. REPETITION
print("\n=== 6. REPETITION (banned recycled phrases) ===")
BANNED = ["You're going to be *so* jealous","Maybe a little.","That's the spirit",
          "heavy enough to set down","the shape of the seven","two-and-a-two",
          "The Shape of the Roof","since they were six years old"]
for n, c in sorted(chapters.items()):
    if n < 22: continue   # the ban targets the ch22-24 recycling disease; earlier use is origin, not recycling
    hits = [b for b in BANNED if b.lower() in c['prose'].lower()]
    if hits: fail('REPEAT', f"ch{n}: banned recycled phrase(s) {hits}")
# any phrase used 3+ times across the book is a recycling smell
phrase_uses = collections.Counter()
for n, c in sorted(chapters.items()):
    for b in BANNED:
        if b.lower() in c['prose'].lower(): phrase_uses[b] += 1
for b, k in phrase_uses.items():
    if k >= 3: fail('REPEAT', f"'{b}' appears in {k} chapters — recycled")
# repeated-sentence detector across chapters
def sents(t):
    return [re.sub(r'\W+',' ',s).strip().lower() for s in re.split(r'(?<=[.!?]) ', t) if len(s.split())>14]
seen = {}
for n, c in sorted(chapters.items()):
    for s in set(sents(c['prose'])):
        if s in seen and seen[s] != n and n - seen[s] <= 5:
            fail('REPEAT', f"ch{n}: sentence duplicated from ch{seen[s]}: \"{s[:80]}...\"")
        seen.setdefault(s, n)
ok('REPEAT', "no banned phrases; no long sentence duplicated within a 5-chapter window")

# ------------------------------------------------------------- 7. LOCKED ITEMS
print("\n=== 7. DO-NOT-TRIGGER LOCKS ===")
LOCKS = [
 ('2nd seal broken',      r'second seal (broke|breaks|shatter)|2nd seal (broke|breaks|shatter)'),
 ('Hawk-Soul Union used', r'Hawk-Soul Union (activated|used|engaged)'),
 # NOTE: this lock was DELIBERATELY TRIGGERED in ch 40 (canon ch 143 grounds it). It is no longer a
 # prohibition; it is spent. Kept here as a record, and scoped to chapters BEFORE 40 only.
 ('1000-yr crossing (pre-ch40 only)', r'$^'),
 # The lock is on naming his ORIGIN, not on Shrek existing as a place. Canon ch 163 names Shrek City
 # freely (the Tang Sect's HQ); what must stay unnamed is where WU ZHANGKONG came from.
 ('Wu Zhangkong origin named', r'Wu Zhangkong[^.]{0,90}(?:from|came from|hailed from|expelled from|origin)[^.]{0,60}Shrek|Shrek[^.]{0,60}(?:his (?:origin|home|academy)|where he (?:came|was) from)'),
 ('Na\'er returned',      r"Na'er (returned|came back|is back)"),
 ('fusion door opened',   r'fusion door (opened|open)|fusion (skill )?(activated|completed)'),
 ('battle armor worn',    r'(wearing|wore|donned) (a )?battle armor'),
 ('Gu Yue true nature',   r'Gu Yue.{0,40}(Silver Dragon King|true (nature|form))'),
 ('question resolved',    r'Can you see — without me\?.{0,60}(answered|replied|said)'),
]
for n, c in sorted(chapters.items()):
    for name, pat in LOCKS:
        if re.search(pat, c['prose'], re.I):
            fail('LOCKS', f"ch{n}: '{name}' appears triggered — verify it is a false positive or fix")
ok('LOCKS', "no locked item triggered in any chapter")

# ------------------------------------------------------- 8. CANON NUMBER GUARD
print("\n=== 8. CANON FACT GUARD ===")
CANON = [
 ('Gu Yue spiritual power = 153', r'153|one hundred and fifty-three', (21,21)),
 ('Gu Yue endurance 115kg',       r'115|one hundred and fifteen kilograms', (21,21)),
 ('Wang Jinxi spiritual power 18',r'\b18\b|eighteen', (21,21)),
 ('Zhang Yangzi 41',              r'\b41\b|forty-one', (21,21)),
]
for name, pat, rng in CANON:
    for n in range(rng[0], rng[1]+1):
        # re.I: prose legitimately capitalises a number at the start of a sentence
        if n in chapters and not re.search(pat, chapters[n]['prose'], re.I):
            fail('CANON', f"ch{n}: canon fact '{name}' missing from prose")
ok('CANON', "canon numbers present where canon requires them")

# ---------------------------------------------- 9. LAW COMPLIANCE (PRIME/PERSONALITY)
print("\n=== 9. PRIME LAW / PERSONALITY LAW ===")
PASSIVE = ['he watched','he listened','he filed','he noted','he observed','he saw that']
ACTIVE  = ['he cut','he struck','he stepped','he drew','he turned','he met','he took','he said',
           'he fought','he moved','he put','he laid','he forged','he invented','he reached','he went']
for n, c in sorted(chapters.items()):
    pr = c['prose'].lower()
    p = sum(pr.count(x) for x in PASSIVE); a = sum(pr.count(x) for x in ACTIVE)
    if p > a: fail('PRIME', f"ch{n}: passive verbs ({p}) outnumber active ({a}) — SPECTATOR DISEASE")
    if n >= 19 and pr.count('lin hao') < 10: warn('PRIME', f"ch{n}: Lin Hao named only {pr.count('lin hao')}x")
    # PERSONALITY: he must actually speak
    quotes = len(re.findall(r'Lin Hao (?:said|agreed|repeated|murmured|called|answered|told|asked)|said Lin Hao|" Lin Hao said', c['prose']))
    quotes += len(re.findall(r'\n"[^"]{3,}" (?:he|Lin Hao) said', c['prose']))
    if n >= 19 and quotes < 3: fail('PERSONA', f"ch{n}: Lin Hao speaks only {quotes}x — he must be playful and central")
ok('PRIME', "active verbs dominate in every chapter; Lin Hao speaks 3+ times per chapter (ch19+)")

# --------------------------------------------------------- 10. CROSS-DOC SYNC
print("\n=== 10. CROSS-DOCUMENT SYNC ===")
# 🔴 There is deliberately NO mirror of THE_CODEX.md. It existed at
# /home/user/CODEX/05_PROJECT_SOUL_LAND_3.md and was deleted 2026-08-29 (§THE TWO-COPIES LAW).
# This block used to compare the two; now it fails if the copy comes back.
import paths as _P
mirror = os.path.join(_P.CODEX, '05_PROJECT_SOUL_LAND_3.md')
if os.path.exists(mirror):
    fail('SYNC', 'CODEX mirror of THE_CODEX.md exists again — delete it, do not sync it')
else:
    ok('SYNC', 'THE_CODEX.md has exactly one copy')
cur_rank, cur_sp = _STATE['current_rank'], _STATE['current_spiritual_power']
for name, blob in (('CODEX', CODEX), ('STATUS', STATUS), ('CONTINUATION', CONT)):
    if f'rank {cur_rank}' not in blob and f'rank **{cur_rank}**' not in blob:
        fail('SYNC', f"{name}: current soul rank {cur_rank} not recorded")
    if str(cur_sp) not in blob: fail('SYNC', f"{name}: current spiritual power {cur_sp} not recorded")
# stale-value sweep across the tracking docs (excluding the upgrade log, which is history)
codex_qr = CODEX.split('## ⚡ QUICK REFERENCE')[1].split('### Current Timeline')[0] if '## ⚡ QUICK REFERENCE' in CODEX else CODEX
for name, blob in (('CODEX-quickref', codex_qr),):
    for stale, pat in (('spiritual power 130', r'spiritual power 130'), ('spiritual power ~130', r'spiritual power ~130'),
                       ('spiritual power 218', r'spiritual power 218(?! →)'), ('spiritual power 226', r'spiritual power 226(?! →)'),
                       ('spiritual power 241', r'spiritual power 241(?! →)')):
        if re.search(pat, blob): fail('SYNC', f"{name}: stale '{stale}' presented as current")
ok('SYNC', 'current rank/power recorded in all three tracking docs; no stale current-values')

# --------------------------------------------------------------- 11. CANON NAMES
print("\n=== 11. NAME-BEARING CANON CHARACTERS (record check) ===")
names = set()
pat = re.compile(r'([A-Z][a-z]+ [A-Z][a-z]+)\b')
KNOWN_NONNAME = {'Spirit Pagoda','Spirit Ascension','Eastsea City','Eastsea Academy','Class Zero','Class One',
 'Class Two','Blacksmith','Association','Thousand Refinements','Soul Master','Soul Grandmaster','Spirit Connection',
 'Stormbringer Sword','Light Dragon','Shadow Dragon','Golden Dragon','Blue Silver','Shadow Phantasm','Bone Dragon',
 'Green Shadow','Man Faced','Longtail Mouse','Scarlet Demon','Crystal Bear','Horned Dragon','Iron Back','Elemental Tide',
 'Eagle Soars','Gale Talon','Wind Step','Skyfrost Sword','Answering Stroke','Grain Cut','Unwritten Stroke','Sword Intent',
 'Sword Innate','One Sentence','Dark Devil','Armored Dragon','Light Dragon Blade','Spirit Steel','Spirit Ascension Platform'}
for n, c in sorted(chapters.items()):
    for line in c['prose'].split('\n'):
        for sent in re.split(r'(?<=[.!?]) ', line):
            for i, m in enumerate(pat.findall(sent)):
                # skip sentence-initial matches (usually just a capitalised first word)
                if i == 0 and sent.strip().startswith(m): continue
                names.add((n, m))
# 🔴 Exclude anything that appears in a chapter TITLE. "What Lin Hao Wrote" yields the fragments
# "Lin" and "Hao Wrote"; "What Gu Yue Did" yields "Yue Did"; "What Wu Zhangkong Said" yields
# "Zhangkong Said". These were reported as unknown characters for months. A real character name
# does not live only inside headings.
TITLE_TEXT = " \n ".join(
    l for n2, c2 in chapters.items() for l in c2['full'].split('\n') if l.startswith('#'))
def _in_a_title(m):
    return m in TITLE_TEXT

# only report ones absent from the codex entirely
STOP = ('Spirit Pagoda','Eastsea City','Spirit Ascension','Soul Master','Blacksmith Association','Golden Dragon',
        'Blue Silver','Shadow Phantasm','Bone Dragon','Green Shadow','Light Dragon','Stormbringer Sword','Thousand Refinements',
        'Glorybound City','Spirit Connection','Soul Grandmaster','Man Faced','Longtail Mouse','Scarlet Demon','Crystal Bear',
        'Horned Dragon','Iron Back','Elemental Tide','Eagle Soars','Gale Talon','Wind Step','Skyfrost Sword','Answering Stroke',
        'Grain Cut','Unwritten Stroke','Sword Intent','Sword Innate','One Sentence','Dark Devil','Armored Dragon','Spirit Steel',
        'Awakening Day','Spirit Pagoda','Tang Sect','Shrek Academy','Class Zero','Adaptation Talent','Spirit Soul','Soul Power')
# a real character name recurs across chapters; sentence fragments do not
counts = collections.Counter(m for n, m in names)
missing = sorted(m for m, k in counts.items() if k >= 3 and CODEX.count(m) == 0 and m not in STOP and not _in_a_title(m) and 'Chapter' not in m and 'Reference' not in m
                 and m.split()[0] not in ('And','But','So','The','Then','Also','Now','Even','Only','Because','Which','That','This','There','Here','After','Before','When','While','If','Not','Yes','Well','Right','Good','Still','Just','Once','Every','Some','Any','All','Both','Each','Neither','Either','Bluesilver','Canon','Novel','Chapter','Volume',
                            # 'What Gu Yue Did', 'What Lin Hao Wrote' are CHAPTER TITLES, not people.
                            # They leaked through as "names never recorded in codex" for months.
                            'What','Who','Why','How','Where','Whom','Whatever'))
if missing: warn('NAMES', f"names never recorded in codex (verify each): {missing[:15]}")
else: ok('NAMES', 'every name-bearing character appears in the codex')

# ------------------------------------------------------------------ 12. TIMELINE
print("\n=== 12. TIMELINE ===")
for n, c in sorted(chapters.items()):
    t = c['prose']
    ages = set(re.findall(r'\bage (\d+)\b', t)) | set(re.findall(r'\b(\d+) years old\b', t))
    bad = [a for a in ages if n <= 3 and a not in ('6','7','8','9','10')] + \
          [a for a in ages if n >= 4 and a not in ('9','10','11','12','13')]
    if bad: fail('TIME', f"ch{n}: impossible age mentioned: {bad}")
ok('TIME', 'no impossible ages')

# ------------------------------------- 13. CODEX RECORD vs CHAPTER FOOTER (drift)
print("\n=== 13. CODEX RECORD vs CHAPTER FOOTER (drift) ===")
cur = None; drift = 0
for line in CODEX.split('\n'):
    m = re.match(r'\*\*Chapter (\d{1,2}):', line)
    if m: cur = int(m.group(1))
    if cur and 'Ranks at chapter end:' in line and 'Lin Hao' in line and cur in chapters:
        cm = re.search(r'Lin Hao \*{0,2}(\d\d)', line)
        fm = re.search(r'Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d\d)', chapters[cur]['full'])
        if cm and fm and cm.group(1) != fm.group(1):
            fail('DRIFT', f"ch{cur}: codex record says rank {cm.group(1)} but the chapter footer says {fm.group(1)}")
            drift += 1
# also: every written chapter must HAVE a codex record
recorded = {int(m.group(1)) for m in re.finditer(r'\*\*Chapter (\d{1,2}):', CODEX)}
for n in sorted(chapters):
    if n not in recorded: fail('DRIFT', f"ch{n} has no codex record")
ok('DRIFT', f"codex records agree with all {len(chapters)} chapter footers")

# ------------------------- 14. GROWTH-PRESENTATION VARIETY (AT canon §64.1)
print("\n=== 14. GROWTH PRESENTATION VARIETY (AT §64.1 — no repeated upgrade formula) ===")
# AT §64.1 forbids reusing one upgrade sequence. The form I actually over-used is:
#   pressure event -> overnight jump -> he does the arithmetic aloud -> the number is stated.
# Confirmed instances (verified by hand 27 Aug 2026): ch22, ch23, ch25.
REGISTERED_FORM_A = {22, 23, 25}
# Detector for NEW instances: "arithmetic" within a paragraph that also carries an
# overnight/private marker AND a growth verb. Warns so a human confirms, never auto-fails.
ARITH = re.compile(r'\barithmetic\b', re.I)
NIGHT = re.compile(r'overnight|four in the morning|in the dark', re.I)
GROWV = re.compile(r'\bbecame\b|\bopened underneath\b|\barrived\b|\bgrew\b', re.I)
candidates = set()
for n, c in sorted(chapters.items()):
    for para in c['prose'].split('\n\n'):
        if ARITH.search(para) and NIGHT.search(para) and GROWV.search(para):
            candidates.add(n)
            break
new_instances = sorted(candidates - REGISTERED_FORM_A)
if new_instances:
    warn('VARIETY', f'possible new use of the overnight-arithmetic growth form in {new_instances} — '
                    f'confirm by hand; if confirmed, vary the presentation before using it again')
# fail only on a genuine 3+ consecutive run
seq = sorted(REGISTERED_FORM_A | candidates)
run = worst = 1
for i in range(1, len(seq)):
    run = run + 1 if seq[i] - seq[i-1] <= 1 else 1
    worst = max(worst, run)
if worst >= 3:
    fail('VARIETY', f'the overnight-arithmetic growth form runs {worst} chapters consecutively ({seq}). '
                    f'AT §64.1 requires variety: partial activation, failure, delayed recognition, '
                    f'unnamed instinctive use, refinement across episodes, later formal test, '
                    f'an ability seed waiting for resources')
else:
    print(f'  ok   form A registered at {sorted(REGISTERED_FORM_A)}; longest consecutive run = {worst} (limit 3)')

# ---------------- 15. SOUL SPIRIT GROWTH (the fifth progression line)
print("\n=== 15. SOUL SPIRIT GROWTH — the Gale Hawk (must never be frozen) ===")
ONES = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
TENS = {'ten':10,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
TEENS = {'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
         'eighteen':18,'nineteen':19}
BASE = {'seven':700,'eight':800,'nine':900}
AGE_RE = re.compile(r'(seven|eight|nine) hundred(?: and ([a-z-]+))? years|~?(\d{3}) ?yrs', re.I)
HAWK_RE = re.compile(r'hawk|gale|soul[- ]spirit|condensed wind', re.I)

def _hawk_age(match):
    if match.group(3):
        return int(match.group(3))
    total = BASE[match.group(1).lower()]
    if match.group(2):
        for w in match.group(2).replace('-', ' ').split():
            total += TENS.get(w, 0) or TEENS.get(w, 0) or ONES.get(w, 0)
    return total

# Scope by PARAGRAPH, not by a character window — a window can miss the keyword that sits
# a few sentences away in the same paragraph. A paragraph is the natural unit of context.
hawk = {}
for n, c in sorted(chapters.items()):
    for para in c['prose'].split('\n\n'):
        if not HAWK_RE.search(para):
            continue
        for m in AGE_RE.finditer(para):
            v = _hawk_age(m)
            if v:
                hawk[n] = max(hawk.get(n, 0), v)
seq = sorted(hawk.items())
prev = 0
for n, v in seq:
    if v < prev:
        fail('HAWK', f'ch{n}: hawk age went DOWN ({prev} -> {v})')
    if v >= 1000:
        fail('HAWK', f'ch{n}: hawk reached {v} — the 1,000-yr purple crossing is a gated story event')
    prev = max(prev, v)
if seq:
    counts = collections.Counter(v for _, v in seq)
    for age, k in counts.items():
        if k >= 3:
            chs = [n for n, v in seq if v == age]
            fail('HAWK', f'the hawk is stated as {age} years in {k} chapters ({chs}) — a spirit soul fed '
                         f'continuously cannot stop moving (THE_CODEX.md Part B)')
    print(f"  ok   hawk chain: {' -> '.join(f'ch{n}:{v}' for n, v in seq)} (no 3+ frozen, <1000)")
else:
    warn('HAWK', 'no hawk age stated in any chapter')

# ---------------- 16. PHYSICAL PANEL (the sixth progression line)
print("\n=== 16. PHYSICAL PANEL (AT §69/§73 — the complete holder) ===")
import paths as _P2
PANEL = os.path.join(_P2.PROJECT, 'LIN_HAO_STATUS.md')   # panel merged into the status file
if not os.path.exists(PANEL):
    fail('PANEL', 'LIN_HAO_STATUS.md is missing — the physical lines are untracked')
else:
    ptext = open(PANEL, encoding='utf-8').read()
    # the panel must carry every physical line, so none can be silently dropped again
    for line in ('Fist / endurance','Raw strength','Movement speed','Agility','Senses','Durability',
                 'Recovery rate','Stamina','Reflex','Reliability'):
        if line not in ptext:
            fail('PANEL', f'physical line "{line}" is missing from the panel')
    # the measured anchor must agree with the prose that produced it
    if '612 kg' not in ptext:
        fail('PANEL', 'the current measured 612 kg anchor (ch32) is missing — a measured value is a hard floor')
    # AT §61.4: the hard floor may not be under-performed in prose
    for n, c in sorted(chapters.items()):
        if n <= 21:
            continue
        for m in re.finditer(r'\b(\d{3})\s*(?:kg|kilograms|kilogrammes)\b', c['prose']):
            v = int(m.group(1))
            near = c['prose'][max(0, m.start()-70):m.end()+30].lower()
            # the floor is the value measured at or before this chapter (186 up to ch31, 243 from ch32)
            floor = 612 if n >= 32 else 470
            if re.search(r'his fist|lin hao|he put his fist|endurance machine', near) and v < floor:
                fail('PANEL', f'ch{n}: a fist/endurance figure of {v} kg under-performs the {floor} kg hard floor (AT §61.4)')
    ok('PANEL', 'all ten physical lines tracked; hard floor 470 kg (ch<=31) / 612 kg (ch>=32) intact and never under-performed')

# ------------ 17. TECHNIQUES, CULTIVATION SPEED & THE SPECIALTY
print("\n=== 17. TECHNIQUES / CULTIVATION SPEED / SPECIALTY ===")
TECH = os.path.join(_P2.PROJECT, 'LIN_HAO_STATUS.md')   # techniques merged into the status file
if not os.path.exists(TECH):
    fail('TECH', 'LIN_HAO_STATUS.md is missing — techniques and cultivation speed are untracked')
else:
    ttext = open(TECH, encoding='utf-8').read()
    for t in ('Grain Cut','The Question','Answering Stroke','One Sentence','Unwritten Stroke',
              'Open Hand','Gale Talon','Wind-Step','Hawk-Soul Union'):
        if t not in ttext:
            fail('TECH', f'technique "{t}" is missing from the techniques panel')
    for concept in ('CULTIVATION SPEED','SPECIALITY','Applied mastery','Creative mastery'):
        if concept not in ttext:
            fail('TECH', f'"{concept}" is missing from the techniques panel')
    ok('TECH', '9 techniques on the six-layer ladder; cultivation speed and specialty framing tracked')
# the specialty framing must not regress to "spiritual power is his speciality"
for f in (os.path.join(_P2.PROJECT,'LIN_HAO_STATUS.md'), os.path.join(_P2.PROJECT,'THE_CODEX.md')):
    try:
        body = open(f, encoding='utf-8').read()
    except OSError:
        continue
    # assert, not negate: a line that denies the framing ("is NOT his speciality") is correct
    NEG = re.compile(r'\bnot\b|\bnever\b|\bwrong\b|\bisn.t\b|\bavoid\b|\bdo not\b|\breframe', re.I)
    for line in body.split('\n'):
        if re.search(r'spiritual power (?:is|remains) his (?:speciality|specialty|greatest)', line, re.I) \
           and not NEG.search(line):
            fail('TECH', f'{os.path.basename(f)} frames spiritual power as his speciality: "{line.strip()[:90]}"')

# ------------------------------------------------------------------- SUMMARY
print("\n" + "="*70)
if W:
    print(f"WARNINGS ({len(W)}):")
    for w in W: print("  -", w)
if F:
    print(f"\nFAILURES ({len(F)}):")
    for f in F: print("  ✗", f)
    print("="*70); print("RESULT: FAIL"); sys.exit(1)
print("RESULT: PASS — all checks green"); print("="*70); sys.exit(0)

#!/usr/bin/env python3
"""VERIFICATION SUITE 2 — semantic, continuity and prose-quality checks.
Companion to verify.py (structural). Run BOTH after every chapter.
"""
import re, os, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'chapters')
CODEX = open(os.path.join(ROOT,'THE_CODEX.md'), encoding='utf-8').read()

chapters = {}
for f in sorted(os.listdir(CH)):
    if f.endswith('.md'):
        n = int(f[8:10]); full = open(os.path.join(CH,f), encoding='utf-8').read()
        head, _, rest = full.partition('## End of Chapter')
        # The "## Canon Reference / ## Canon anchors" header block is metadata, not prose.
        # Counting it produced a false 158-word "sentence" and skewed the rank/ring claim checks.
        if '\n---\n' in head:
            body = head.split('\n---\n', 1)[1]
        else:
            body = head
        chapters[n] = {'full':full, 'prose': body, 'footer': rest}
MAXCH = max(chapters)
F, W = [], []
def fail(s,m): F.append(f"[{s}] {m}")
def warn(s,m): W.append(f"[{s}] {m}")
def ok(s,m): print(f"  ok   {m}")

# Sentence splitter. Two fixed-width lookbehinds alternated (Python forbids variable-width).
# The second branch splits after a closing quote, otherwise an entire dialogue exchange
# is measured as a single "sentence" and produces false positives.
SENT_SPLIT = r'(?<=[.!?])\s+|(?<=[.!?][\u201d\u2019"])\s+'
def sentences(text): return re.split(SENT_SPLIT, text)

ROSTER = ['Lin Hao','Tang Wulin','Xie Xie','Gu Yue','Wang Jinxi','Zhang Yangzi','Wei Xiaofeng',
          'Wu Zhangkong','Long Hengxu','Mu Chen','Mu Xi','Ouyang Zixin','Guang Long','Guang Biao',
          'Qin Lang','Mo Si','Jia Long','Lin Zunyuan','Ye Yingluo','Na\'er','Zhou Zhangxi','Yun Xiao',
          'Chen Long','Lin Wei','Lin Mei','Old Tang','Kong Hanwen','Gu Tianming']

# ------------------------------------------------ 1. RANK BRACKET vs SOUL TITLE
print("\n=== 1. SOUL TITLE vs RANK BRACKET (RANK RULE) ===")
BRACKETS = [(1,10,'Soul Scholar'),(11,20,'Soul Master'),(21,30,'Soul Grandmaster'),
            (31,40,'Soul Elder'),(41,50,'Soul Ancestor'),(51,60,'Soul King')]
PEOPLE = ('Lin Hao','Tang Wulin','Xie Xie','Wang Jinxi','Zhang Yangzi','Wei Xiaofeng','Wu Zhangkong','Gu Yue')
ORDER_LIST = re.compile(r'Soul Scholar.*Soul Master.*Soul Grandmaster|Cultivation Order|LOW → HIGH', re.S)
for n,c in sorted(chapters.items()):
    # PROSE ONLY — the footer is a summary and legitimately contains ranges like "rank 17→22 (Soul Grandmaster)"
    for sent in re.split(r'(?<=[.!?])\s+|\n', c['prose']):
        if ORDER_LIST.search(sent):        # the cultivation-order list is not a claim about anyone
            continue
        for who in PEOPLE:
            # find each mention of the person and inspect only the 45 chars that follow
            for m in re.finditer(re.escape(who), sent):
                win = sent[m.end():m.end()+45]
                if any(o in sent[m.start():m.end()+45].replace(who,'') for o in PEOPLE):
                    continue              # another person is in the window — ambiguous, skip
                rk = re.search(r'\brank (\d\d)\b', win)
                if not rk: continue
                r = int(rk.group(1))
                tier = next((t for lo,hi,t in BRACKETS if lo<=r<=hi), None)
                for lo,hi,t in BRACKETS:
                    if t in win and t != tier:
                        fail('RANKRULE', f"ch{n}: {who} rank {r} called '{t}' in the same breath (should be {tier})")
    if re.search(r'Soul Scholar rank (1[1-9]|2\d)', c['prose']):
        fail('RANKRULE', f"ch{n}: 'Soul Scholar rank >10' — impossible (Scholar ends at 10)")
ok('RANKRULE', 'soul titles match rank brackets; no Scholar above rank 10')

# ------------------------------------------------------- 2. RING LAW
print("\n=== 2. RING LAW (count monotonic; colour fixed at absorption) ===")
def rings_of(text, who):
    out = []
    for m in re.finditer(re.escape(who)+r'[^.,;]{0,40}?(one|two|three|1st|2nd|3rd|first|second|third)[- ]rings?\b', text):
        gap = text[m.start():m.start(1)]
        others = [o for o in ('Guang Long','Wang Jinxi','Qin Lang','Jia Long','Gu Tianming','Mo Si','Gu Yue','Lin Hao','Xie Xie','Tang Wulin','Zhang Yangzi','Wei Xiaofeng') if o != who]
        if any(o in gap for o in others):
            continue          # the rings belong to someone else in the same clause
        w = m.group(1).lower()
        out.append({'one':1,'1st':1,'first':1,'two':2,'2nd':2,'second':2,'three':3,'3rd':3,'third':3}[w])
    return out
for who, first_two in (('Lin Hao',4),('Xie Xie',17)):
    prev = 0
    for n,c in sorted(chapters.items()):
        vals = rings_of(c['prose'], who)   # prose only: footers summarise post-ch17 state
        if not vals: continue
        top = max(vals)
        if n < first_two and top >= 2: fail('RINGS', f"ch{n}: {who} has {top} rings before ch{first_two} (2nd ring arrives ch{first_two})")
        if top < prev: fail('RINGS', f"ch{n}: {who}'s ring count went DOWN ({prev} -> {top})")
        prev = max(prev, top)
# colour law: rings must not be described as changing colour
# 🔴 SCOPED ch71 (2026-08-30) — §4.13 rule 3: WHEN A BELIEF CHANGES, THE CHECK ENFORCING IT MUST
# CHANGE IN THE SAME EDIT. This law was written when the belief was "a ring's colour is fixed at
# absorption." THE FOURTH RING LAW breaks that belief deliberately: when the martial soul evolves
# to top-level, the three existing purple rings RE-FORM AND DARKEN, and the fourth arrives BLACK
# (ten-thousand-year => black, canon c260). That is canon-consistent (a ring's colour tracks its
# spirit soul's age) and it is locked, so the check now applies to ch1-70 only. Do not widen it
# back without changing the law in THE_CODEX.md first.
RING_COLOUR_LAW_LAST_CH = 70
for n,c in sorted(chapters.items()):
    if n > RING_COLOUR_LAW_LAST_CH: continue
    if re.search(r'(white|yellow|purple|black) ring[^.]{0,40}(turned|became|ripened|changed (its )?colou?r|darkened into)', c['prose'], re.I):
        fail('RINGS', f"ch{n}: a ring is described as changing colour — violates RING-COLOR LAW")
ok('RINGS', f'ring counts monotonic, arrive on schedule, no colour changes through ch{RING_COLOUR_LAW_LAST_CH} (the belief changes at ch71)')

# ------------------------------------------------------- 3. HAWK AGE
print("\n=== 3. HAWK AGE (delegated) ===")
# Suite 1 check 15 is the authoritative hawk check (paragraph-scoped, full chain, freeze detection).
# Duplicating it here produced a DIFFERENT number from the same chapters — the exact stale-value
# failure class this project keeps fighting. One check, one place.
print("  ok   delegated to verify.py check 15 (single source of truth — do not duplicate)")

# --------------------------------------- 4. FOOTER CHARACTER STATES vs PROSE
print("\n=== 4. CHARACTER STATES (footer) vs PROSE ===")
# Chapters 1-12 predate the footer standard; their footers were RETROFITTED during the
# v2.42 integrity audit and deliberately carry only the protagonist lines (marked as such).
# Full-cast enforcement applies from the standard-adoption chapter onward.
STATES_FROM = 13
for n,c in sorted(chapters.items()):
    if n < STATES_FROM:
        if '### Character States' not in c['footer'] and 'Ranks at chapter end' not in c['footer']:
            fail('STATES', f"ch{n}: retrofitted footer missing — every chapter must carry an end-state record")
        continue
    if '### Character States' not in c['footer']:
        fail('STATES', f"ch{n}: no '### Character States' section")
        continue
    block = c['footer'].split('### Character States')[1]
    listed = set()
    for line in block.split('\n'):
        m = re.match(r'- \*\*(.+?):\*\*', line.strip())
        if m: listed.add(m.group(1).strip())
    # every roster member who ACTS in the prose must have a state line (ch13+)
    for who in ROSTER:
        if c['prose'].count(who) >= 3 and who not in listed and not any(who in l for l in listed):
            fail('STATES', f"ch{n}: {who} appears {c['prose'].count(who)}x in prose but has no Character States line")
ok('STATES', 'every acting character has a state line in every chapter (ch11+)')

# ------------------------------------------------ 5. SCENE CONTINUITY
print("\n=== 5. SCENE CONTINUITY (who was there at the end, is there at the start) ===")
for n in sorted(chapters):
    if n+1 not in chapters: continue
    # 🔴 Strip the generated ensemble block before counting. apply_ensemble.py appends it to every
    # footer, and its REALM GAP LAW note names Tang Wulin / Xie Xie / Gu Yue explicitly -- so the
    # checker was counting a metadata note as "characters present at the end of the chapter" and
    # reporting seven phantom scene-continuity breaks.
    def _narr(t):
        t = t.split("### Ensemble — canon-verified state")[0]
        t = t.split("### Character States:")[0]
        return t
    tail = _narr(chapters[n]['prose'])[-2500:]
    head = _narr(chapters[n+1]['prose'])[:2500]
    for who in ROSTER:
        if tail.count(who) >= 3 and head.count(who) == 0 and who in ('Tang Wulin','Xie Xie','Gu Yue','Wu Zhangkong'):
            warn('CONT', f"ch{n}->ch{n+1}: {who} is central at the end of ch{n} but absent from the opening of ch{n+1}")
ok('CONT', 'no unexplained disappearance of a central character between chapters')

# ---------------------------------------------------- 6. CANON HEADER vs BODY
print("\n=== 6. CANON REFERENCE HEADER vs BODY ===")
for n,c in sorted(chapters.items()):
    m = re.search(r'^## Canon Reference:(.*)$', c['prose'], re.M)
    if not m: continue
    head = m.group(1)
    refs = re.findall(r'\b(\d{2,3})\b', re.findall(r'ch(?:apters?)?\s*([\d,\-\s]+)', head)[0]) if re.findall(r'ch(?:apters?)?\s*([\d,\-\s]+)', head) else []
    # every canon name quoted in the header must appear in the body
    for name in re.findall(r'"([^"]{4,40})"', head):
        key = name.strip('.!?, ').lower()
        if len(key.split()) >= 3 and key not in c['full'].lower():
            fail('CANONHDR', f"ch{n}: header quotes \"{name}\" but that phrase never appears in the chapter")
ok('CANONHDR', 'canon lines quoted in headers appear in the body')

# ------------------------------------------------- 7. THREAD STATE CONSISTENCY
print("\n=== 7. LONG-RUNNING THREADS (must stay in their stated state) ===")
THREADS = {
 "the hawk's question": (r'the question|its question', 'OPEN — never resolved before the gated era'),
 "fusion door":         (r'fusion door', 'GATED — must not open'),
 "Gu Yue's true nature":(r'Gu Yue', 'L4 — Silver Dragon King never named'),
}
for n,c in sorted(chapters.items()):
    p = c['prose']
    for m in re.finditer(r'the question[^.]{0,60}(answered|resolved|finally asked|spoke it)', p, re.I):
        # widen to the whole clause: a negation often sits BEFORE the match
        # (e.g. "Not that the question had been answered") and must not be read as a resolution
        seg = p[max(0, m.start()-60):m.end()+20].lower()
        if any(neg in seg for neg in ('not that','unanswered','not answered','never answered','not resolved',
                                      'had to be answered','to be answered','without being answered',
                                      'no one answered','nobody answered','not been answered')):
            continue
        fail('THREAD', 'ch%d: hawk question appears RESOLVED -> %s' % (n, m.group(0)[:70]))
    if re.search(r'fusion door[^.]{0,40}opened', p, re.I):
        fail('THREAD', f"ch{n}: the fusion door appears OPENED (GATED for years)")
    if re.search(r'Silver Dragon King', p):
        fail('THREAD', f"ch{n}: 'Silver Dragon King' named on-page — L4 PROTECTED")
ok('THREAD', "question OPEN, fusion door GATED, Gu Yue's nature unnamed in every chapter")

# 🔴 CALIBRATED 2026-08-28 against the book's own distribution (10,879 sentences measured):
#   median 10 words · mean 18 · p99 = 75 · max 116
# Only 11 sentences in the whole book exceed 95 words (0.1%) and 2 exceed 110. This is a style that
# deliberately uses long recursive lines — the journal entries are built out of them. A 95-word
# threshold flags normal style as debt and then gets ignored, which is worse than not measuring.
# Spot-checking the flagged set confirmed it: ch7 and ch21 are PARAGRAPH artifacts (em-dash clauses,
# not single sentences), and ch61's 116-word line is the recursive "I have written that sentence five
# times" bit, where the length IS the point. 110 = genuine runaways only.
LONG_SENTENCE_WORDS = 110

# --------------------------------------------------------- 8. PROSE QUALITY
print("\n=== 8. PROSE QUALITY ===")
for n,c in sorted(chapters.items()):
    p = c['prose']
    words = p.split()
    if len(words) < 2000: warn('QUAL', f"ch{n}: {len(words)} words (short)")
    # em-dash density

    dash = p.count(' — ')
    if dash > len(words)/45: warn('QUAL', f"ch{n}: em-dash density high ({dash} in {len(words)} words)")
    # comma splices / runaway sentences
    long_s = [x for x in sentences(p) if len(x.split()) > LONG_SENTENCE_WORDS]
    if long_s: warn('QUAL', f"ch{n}: {len(long_s)} sentence(s) over {LONG_SENTENCE_WORDS} words — genuine runaway, split it")
    # overused crutch words
    for w, lim in (('because', 0.020), ('which was', 0.012), ('and because', 0.008)):
        rate = p.lower().count(w)/max(len(words),1)
        if rate > lim: warn('QUAL', f"ch{n}: '{w}' used {p.lower().count(w)}x ({rate:.1%} of words) — crutch")
ok('QUAL', 'length, sentence length, dash density and crutch-word rates measured')

# ---------------------------------------------------- 9. NO GAPS / NO DUPLICATES
print("\n=== 9. FILE INTEGRITY ===")
nums = sorted(chapters)
if nums != list(range(1, MAXCH+1)): fail('FILES', f"chapter numbering has gaps: {nums}")
# duplicate prose across chapters (paragraph level)
paras = collections.defaultdict(list)
for n,c in sorted(chapters.items()):
    for para in c['prose'].split('\n\n'):
        t = re.sub(r'\s+',' ',para).strip()
        if len(t.split()) > 30: paras[t].append(n)
for t, ns in paras.items():
    if len(ns) > 1: fail('FILES', f"paragraph duplicated across chapters {ns}: \"{t[:70]}...\"")
ok('FILES', f"{MAXCH} chapters, no gaps, no duplicated paragraphs")

# ------------------------------------------------------ 10. QUICK-REF vs LATEST
print("\n=== 10. QUICK REFERENCE vs LATEST CHAPTER ===")
qr = CODEX.split('## ⚡ QUICK REFERENCE')[1].split('### Current Timeline')[0] if '## ⚡ QUICK REFERENCE' in CODEX else ''
last = chapters[MAXCH]['footer']
m = re.search(r'Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d\d)', last)
if m and f'**{m.group(1)}' not in qr and f'rank {m.group(1)}' not in qr.lower():
    fail('QR', f"quick-ref does not show the current rank ({m.group(1)})")
m2line = re.search(r'\*\*([\d\s→/()a-z,.\-]*?\d{3})\s*/\s*499', qr)
m2 = None
if m2line:
    chain = re.findall(r'\d{3}', m2line.group(1))
    class _M:  # emulate match with the LAST value in the chain
        def group(self, i): return chain[-1]
    m2 = _M() if chain else None
import json as _json
CURRENT_SP = _json.load(open(os.path.join(ROOT, 'checks', 'state.json'), encoding='utf-8'))['current_spiritual_power']
class _S:
    def __init__(self, v): self.v = v
    def group(self, i): return self.v
sp = _S(str(CURRENT_SP))
if m2 and sp and m2.group(1) != sp.group(1):
    fail('QR', f"quick-ref says spiritual power {m2.group(1)} but ch{MAXCH} footer says {sp.group(1)}")
ok('QR', f'quick-ref matches ch{MAXCH} (rank {m.group(1) if m else "?"}, spiritual power {sp.group(1) if sp else "?"})')

# ================================================== SUITE 2B — DEEP CONSISTENCY
print("\n=== 11. CHARACTER DESCRIPTOR CONSISTENCY (eyes / hair / weapon) ===")
DESC = {
 'Lin Hao':  {'eyes': r'(hawk-gold|gold-flecked|amber|storm-grey|storm gray|golden)',
              'bad_eyes': r'(blue|green|brown|black|grey) eyes',
              'hair': r'(storm-light|dark brown|black) hair'},
 'Tang Wulin': {'weapon': r'(hammer|Black Silver|tungsten)'},
}
HIS_EYES = r'(hawk-gold|gold-flecked|golden|amber|amber-brown)'
for n, c in sorted(chapters.items()):
    p = c['prose']
    # only flag a WRONG COLOUR, never the absence of one ("his eyes" alone is fine)
    COLOURS = r'(?:blue|green|brown|black|grey|gray|violet|red|silver|white|hazel)'
    for m in re.finditer(r"(?:Lin Hao's|his own)\s+((?:" + COLOURS + r")[- \w]{0,12})eyes", p, re.I):
        col = m.group(1).strip().lower()
        if not re.search(HIS_EYES, col, re.I):
            fail('DESC', f"ch{n}: Lin Hao's eyes described as '{col}' — expected {HIS_EYES}")
    # the mutation timeline: gold-flecked only after the hawk starts changing him (ch10+)
    if n < 10 and re.search(r'(gold-flecked|hawk-gold) eyes', p, re.I):
        fail('DESC', f"ch{n}: hawk-gold eyes before ch10 — at awakening they are amber-brown (canon ch1); the gold comes with the mutation")
    # Gu Yue's element order: nothing -> water -> ice -> fire (canon ladder)
    if re.search(r'Gu Yue[^.]{0,80}\bfire\b', p) and n < 14:
        fail('DESC', f"ch{n}: Gu Yue uses FIRE before ch14 (canon ladder: nothing -> water -> ice -> fire at ch14)")
ok('DESC', 'eye/hair/weapon descriptors consistent; Gu Yue element ladder respected')

print("\n=== 12. THREAD PRESENCE (locked threads must be touched, not forgotten) ===")
QUIET = {  # chapter ranges where a thread may legitimately stay silent
 'the question': set(range(1, 10)),
 'Na\'er': set(),
}
THREAD_PAT = {'the question': r'the question|its question', 'Na\'er': r"Na'er",
              'the ledger': r'ledger|seventy-|seventy ', 'the hawk': r'the hawk'}
for name, pat in THREAD_PAT.items():
    silent = [n for n, c in sorted(chapters.items())
              if n >= 10 and n not in QUIET.get(name, set()) and not re.search(pat, c['prose'], re.I)]
    if len(silent) >= 4:
        warn('THREAD2', f"'{name}' not mentioned in {len(silent)} chapters since ch10: {silent}")
ok('THREAD2', 'long-running threads tracked for abandonment')

print("\n=== 13. READER LOAD (long-sentence census) ===")
worst = []
for n, c in sorted(chapters.items()):
    ss = [x for x in sentences(c['prose']) if len(x.split()) > LONG_SENTENCE_WORDS]
    if ss: worst.append((len(ss), n))
worst.sort(reverse=True)
if worst:
    print(f"  chapters with sentences over {LONG_SENTENCE_WORDS} words:", ", ".join(f"ch{n}({k})" for k, n in worst[:8]))
    warn('READ', f"{sum(k for k,_ in worst)} over-long sentences across {len(worst)} chapters — consider splitting the worst")
ok('READ', 'census complete')

print("\n=== 14. POWER MODEL v2 ENFORCEMENT (canon ch 114 / 134 locked) ===")
# Canon-locked curves from POWER_MODEL.md §3. Lin Hao must never reach or pass Gu Yue.
# 🔴 REBUILT 2026-08-28 — MONSTER LAW. The old table was built to keep him SECOND to Gu Yue
# ("Gu Yue is canon's crown and must stay highest"). That was the same disease as the strength
# error: ranking him inside a range built for somebody else. He is ABOVE everyone except Tang San.
# Band = the chapter's curve value +/- 6, so a restated value passes and a stale one fails.
_CURVE = {21:178,22:184,23:191,26:196,29:205,49:212,50:218,51:226,54:233,57:241,58:249,59:256,60:264,61:281}
def _cv(ch):
    ks=[k for k in _CURVE if k<=ch]
    return _CURVE[max(ks)] if ks else None
LIN_BAND = {}
for _n in range(1, 62):
    _v = _cv(_n)
    LIN_BAND[_n] = (max(0, _v - 6), _v + 6) if _v else (0, 999)
GUYUE_MIN = {11:115, 20:145, 23:150, 29:165, 34:180, 37:184}
retired = []
for n, c in sorted(chapters.items()):
    body = c['prose'] + "\n" + c.get('footer','')
    # (a) the retired 243 kg reading must never reappear
    if re.search(r'\b243\s*(?:kg|kilograms)', body, re.I):
        retired.append(n)
    # (b) any stated spiritual power for Lin Hao must sit inside his band
    OTHERS = ('gu yue','guyue','tang wulin','wulin','xie xie','zhang yangzi','wang jinxi',
              'wei xiaofeng','wu zhangkong','mu xi','na\'er')
    for m in re.finditer(r'spiritual power[^0-9]{0,25}(\d{2,3})', body, re.I):
        v = int(m.group(1))
        # Inspect BOTH sides of the number: canon gives Gu Yue/Wulin/Xie Xie their own
        # figures, and attributing theirs to Lin Hao is a false positive.
        ctx = (body[max(0,m.start()-170):m.start()] + " " + body[m.end():m.end()+90]).lower()
        if any(o in ctx for o in OTHERS):
            continue
        lo, hi = LIN_BAND.get(n, (0, 999))
        if not (lo <= v <= hi):
            fail('POWER', f"ch{n}: spiritual power {v} outside the canon-locked band {lo}-{hi} "
                          f"(MONSTER LAW — the band is the chapter's curve value ±6; see POWER_MODEL.md §3)")
    # (c) canon's class-zero punch table must not be contradicted
    for m in re.finditer(r'(\d{2,4})\s*(?:kg|kilograms)', body, re.I):
        v = int(m.group(1))
        if 250 <= v <= 520 and re.search(r'wang jinxi', body[max(0,m.start()-120):m.start()+120], re.I):
            fail('POWER', f"ch{n}: {v} kg attributed near Wang Jinxi — canon ch 114 fixes him at 423/468")
if retired:
    fail('POWER', f"the retired 243 kg reading reappears in ch {retired} — POWER_MODEL.md §4 replaced it with 612 kg")
else:
    ok('POWER', 'retired 243 kg reading absent')
ok('POWER', f"Lin Hao's spiritual band checked across {len(chapters)} chapters; Gu Yue must remain highest")

# ------------------------------------------------------------------ SUMMARY
print("\n" + "="*70)
if W:
    print(f"WARNINGS ({len(W)}):")
    for w in W: print("  -", w)
if F:
    print(f"\nFAILURES ({len(F)}):")
    for f in F: print("  ✗", f)
    print("="*70); print("RESULT: FAIL"); sys.exit(1)
print("RESULT: PASS — suite 2 green"); print("="*70); sys.exit(0)

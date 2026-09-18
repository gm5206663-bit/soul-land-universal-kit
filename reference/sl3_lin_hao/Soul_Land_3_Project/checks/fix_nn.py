import io, re, glob
os_err = []
import os
os.chdir('/home/user/Soul_Land_3_Project')

def patch(path, pairs):
    t = io.open(path, encoding='utf-8').read()
    for old, new in pairs:
        assert t.count(old) == 1, (path, 'ANCHOR MISS/x' + str(t.count(old)), old[:70])
        t = t.replace(old, new)
    io.open(path, 'w', encoding='utf-8').write(t)
    print('fixed:', path, f'({len(pairs)} edits)')

# timeline block: span replace (multi-line anchor unreliable)
t = io.open('THE_CODEX.md', encoding='utf-8').read()
i = t.find('- **Time elapsed:**')
j = t.find('Canon ch 230 onward not yet used.**')
assert i != -1 and j != -1, 'timeline span miss'
j += len('Canon ch 230 onward not yet used.**')
new_tl = '''- **Time elapsed:** 7 years since Awakening Day · three years since the tournament (canon 229's cut walked as scenes, ch63-69)
- **Age:** everyone in class zero is **13**
- **Location:** **Shrek City** — the make-up exam: three trials done in fourteen seconds, five-for-five; more trials called; the wager alive behind the numbers
- **Setting:** 10,000 years after Soul Land 2
- RED **Next milestones: THE FOURTH TRIAL (canon 259 - FETCH FIRST) · THE OWED SCENES O1/O2 (the evolution, per the ledger's five requirements; the fourth ring's skill - see BUTTERFLY_REGISTRY par A) · the duel CONDITIONAL (failure-only; WZK: 'Win.') · the smiths' summons.** RED **"Divine Stormbringer" is CANCELLED - never name or foreshadow it.**
- **Canon position:** canon 229-258 MINED (disk range 229-258); **canon 259 = their chapter-262, fetch and title-verify BEFORE ch80.**'''
new_tl = new_tl.replace('RED', '\ud83d\udd01', 2) if False else new_tl
t = t[:i] + new_tl + t[j:]
io.open('THE_CODEX.md', 'w', encoding='utf-8').write(t)
print('fixed: THE_CODEX.md (timeline block)')

# quick extra recon printed for the record
print('Zhou Zhangxi mentions:', sum(1 for f in glob.glob('chapters/chapter_*.md') if 'Zhou Zhangxi' in io.open(f, encoding='utf-8').read()))
t69 = io.open('chapters/chapter_69.md', encoding='utf-8').read()
i = t69.lower().find('badge')
print('ch69 badge ctx:', re.sub(r'\s+', ' ', t69[i-120:i+220])[:300])

# ---------- 1. THE_CODEX ----------
patch('THE_CODEX.md', [
 ("🔴 **CURRENT AGE 1,399 (ch61). BOTH CROSSINGS HAVE HAPPENED:",
  "🔴 **CURRENT AGE 3,151 (ch79). BOTH CROSSINGS HAVE HAPPENED:"),
 ("His hawk is at 1,399 years. Every one of these stacks on the same foundation:",
  "His hawk is at 3,151 years (ch79). Every one of these stacks on the same foundation:"),
 ("1. **The realm itself** — Soul Elder, not Soul Grandmaster.\n2. **Three rings vs two** — an extra skill and a third more soul power to spend.\n3. **Three PURPLE rings** — thousand-year souls.",
  "1. **The realm itself** — rank 45, four rings, past Soul Elder entirely.\n2. **Four rings vs two** — two extra skills and double the soul power to spend.\n3. **Three PURPLE rings + one BLACK** — thousand-year souls and one ten-thousand-year."),
 ("4. **A 1,399-year spirit soul** raising strength, speed, soul power, reaction and tenacity at once (c131).",
  "4. **A spirit soul now past three thousand years (3,151 at ch79; 1,399 at c131)** raising strength, speed, soul power, reaction and tenacity at once."),
 ("mechanism is the **Adaptation Talent plus a 1,399-year spirit soul**, both of which refi",
  "mechanism is the **Adaptation Talent plus a spirit soul now past three thousand years**, both of which refi"),
 ("effective combat power SOUL EMPEROR (61–70), ceiling Emperor peak (ruled ch68)",
  "effective combat power SOUL EMPEROR (61–70) baseline; all-out SOUL SAGE (71–80) — reserved (the HYH calibration, 2026-09-01)"),
 ("fist **2,612 kg** · 🔨 **5th rank — Master Craftsman (ch67; the metal told him)**",
  "fist **2,612 kg at ten — rebased past the machine's 5,000 kg ceiling at ch68 (the era table keeps both truths)** · 🔨 **5th rank — Master Craftsman (ch67; the metal told him)**"),
 ("### Current Ranks — END OF CHAPTER 69 (Age 13 · the duel lost honestly; the train to Shrek City)",
  "### Current Ranks — END OF CHAPTER 79 (Age 13 · Shrek City — the make-up exam: three trials done in fourteen seconds, five-for-five; the fourth trial called)"),
 ("| 🔴 **Lin Hao (OC)** | **45 — fourth ring TAKEN (title unnamed on purpose)** | **3 PURPLE + 1 BLACK (10,000-yr dragon jiao)** | **2,740** | **FROST ABYSS SWORD (top-level) + Gale Hawk 3,095 yrs + the dragon jiao** · 🔨 5th-rank Master Craftsman · ⚔️ Sword Intent · **Frost Abyss Domain (folded) · Domineer** · **effective SOUL EMPEROR (61–70)** · **ledger 165 — line 109 unfinished** · 「全能」 **Comprehensive — the seventh System, on a form nobody read** |",
  "| 🔴 **Lin Hao (OC)** | **45 — fourth ring TAKEN (title never said on-page)** | **3 PURPLE + 1 BLACK (10,000-yr dragon jiao)** | **2,824** | **FROST ABYSS SWORD (top-level) + Gale Hawk 3,151 yrs + the dragon jiao** · 🔨 5th-rank Master Craftsman · ⚔️ Sword Intent (one stroke spent ch77; held) · **Frost Abyss Domain (folded) · Domineer** · **effective SOUL EMPEROR (61–70); all-out SOUL SAGE — reserved** · **ledger 168 — line 109 FINISHED (ch71); last line: 'He woke. We're good enough. The academy came himself.'** · **trials 10·10·10 · the Track spent (six gates of seams) · the maintenance report filed (the smiths invoked)** · 「全能」 **Comprehensive — the seventh System, on a form nobody read** |"),
 ("two rings, ~4,000 yrs (canon c232) **+ the external right-claw soul bone (canon c240–241)** | **499 — the bottleneck (canon c231); the seal set complete, unbroken** |",
  "two rings, ~4,000 yrs (canon c232) **+ the external right-claw soul bone (canon c240–241)** | **499 — the bottleneck (canon c231); 🔴 the SECOND SEAL BROKEN (ch78 — GOLDEN DRAGON BODY, the hunger law); the third-seal clock running** | **trials 10·10·10 — THE CATCH (the first examinee in the trial's history to grab a blade; fourteen seconds)** |"),
 ("Light Dragon Dagger + Shadow Dagger (twin) · **going to Shrek** ·",
  "Light Dragon Dagger + Shadow Dagger (twin) · **at Shrek — trials 10·10·10 · the rumor-flash · 'you cannot bench breakfast'** ·"),
 ("**going to Shrek** · 🔴 **ch62: he told her the whole of it and she said nothing** · 🔒 **Silver Dragon King, nobody knows** |",
  "**at Shrek — trials 8·10 (canon's recall; the capped run); the arrangement + the blush ch79 were canon's own, uninterpreted** · 🔴 **ch62: he told her the whole of it and she said nothing · ch71: THE CONFESSION — her silence kept, the wire dormant by law** · 🔒 **Silver Dragon King, nobody knows** |"),
 ("Starwheel Ice Staff · night-only · **going to Shrek** |",
  "Starwheel Ice Staff · night-only · **at Shrek — trials 10·10·10 on a one-third tank (conserving)** |"),
 ("| Who | State at ch69 |", "| Who | State at ch79 (audit nn — was ch69) |"),
 ("Cleans **Long Bing's** grave. |",
  "Cleans **Long Bing's** grave. **ch77: heard the wager at the trial door — 'Win. The five of you pass everything. That was already the assignment. The duel is what happens if you fail.'** |"),
 ("Assessed Lin Hao at ch61: *\"If he has three rings by the time he's fifteen, his body will likely transform again.\"* |",
  "Assessed Lin Hao at ch61: *\"If he has three rings by the time he's fifteen, his body will likely transform again.\"* **ch73–79: proctor of the make-up exam — the card returned and paid ('He's in the water. Three days now…'); 'Ask the cards'; the sword promised after the exam; the wager witnessed; the file's three pages (the sword-line, the golden ring, the spring report); the smiths to be summoned.** |"),
 ("— *\"Ask somebody else about the Ice.\"* |",
  "— *\"Ask somebody else about the Ice.\"* **The call owed from Shrek City (ch80s) — his student famous in the halls' iron without him; converges with the smiths' summons (ch79).** |"),
 ("### Current Timeline — end of ch62",
  "### Current Timeline — end of ch79 (audit nn — this block had said ch62: age 10, Skysea, 'next milestone: the fourth-ring arc' — an arc that concluded at ch68)"),
 ("Soul Scholar (1-10) → Soul Master (11-20) → Soul Grandmaster (21-30) → Soul Elder (31-40) → Soul Ancestor (41-50) →",
  "Soul Scholar (1-10) → Soul Master (11-20) → Soul Grandmaster (21-30) → Soul Elder (31-40) → ⚠️ Soul Ancestor (41-50 — label UNVERIFIED in our canon extract; the story never says his title aloud) →"),
 ("- **🔴 CURRENT (end of ch62) — SOUL ELDER RANK 36. THE WALL OPENED AT ch40.**",
  "- **🔴 CURRENT (end of ch79) — RANK 45, HELD SINCE ch68 (the black ring's jump). THE WALL OPENED AT ch40.**"),
 ("Current: spiritual power **289** · hawk **1,406 yrs** · **three purple rings** · fist **2,612 kg** (≈ a four-ring Soul Ancestor) · ledger **109, last line unfinished** · smith **4th rank (Grandmaster)** · ⚔️ Sword Intent · effective combat **SOUL KING (51–60)**. Next gate: **rank 40 → the fourth ring.**",
  "Current (ch79): spiritual power **2,824** · hawk **3,151 yrs** · **three purple + one black ring** · fist **2,612 kg at ten, past the 5,000 ceiling at ch68** · ledger **168, line 109 FINISHED** · smith **5th rank (Master Craftsman)** · ⚔️ Sword Intent · effective combat **SOUL EMPEROR (61–70); all-out SOUL SAGE — reserved**. Next gate: **the fifth-ring era (cap 50) — and the exam's duel, conditional.**"),
 ("- **Next gates:** rank 30 bottleneck → **3rd ring from the HAWK** (LOCKED DECISION — see \"1,000-Year Qualitative Change\"; no purchased soul) → purple crossing bestows command-adaptive 3rd skill → Soul Elder (projected mid-academy)",
  "- **Next gates:** the fifth-ring era (four rings cap at 50 per the (rings+1)×10 rule — five ranks of headroom) · the exam's duel (conditional) · the smiths' summons (ch79 wire)"),
 ("| 2. **SPIRITUAL POWER** | **289** | every fight; pressure compounds (GROWTH LAW) · 🔴 ch62: **+8 from WATCHING, not fighting** — the rule was incomplete |",
  "| 2. **SPIRITUAL POWER** | **2,824 (ch79)** | every fight; pressure compounds (GROWTH LAW) · 🔴 ch62: **+8 from WATCHING, not fighting** — the rule was incomplete |"),
 ("| 4. **BLACKSMITH RANK** | **🔨 4th rank (Grandmaster)** — Master Craftsman is rank **5** (canon c40) |",
  "| 4. **BLACKSMITH RANK** | **🔨 5th rank — Master Craftsman (ch67; second-youngest in Branch records)** |"),
 ("| 5. **SPIRIT SOUL** | **🌪 hawk 1,399 years** — lightning crossing (900) and purple crossing (1,000) both **done** |",
  "| 5. **SPIRIT SOUL** | **🌪 hawk 3,151 years (ch79)** — lightning crossing (900) and purple crossing (1,000) both **done** |"),
 ("| 6. **LEDGER / EXPERIENCE** | **107 opponents adapted** |",
  "| 6. **LEDGER / EXPERIENCE** | **168 lines (line 109 FINISHED, ch71)** |"),
 ("| 7. **PHYSICAL PANEL** | **fist 2,612 kg (measured ch32, hard floor)**; nine other lines established but unmeasured |",
  "| 7. **PHYSICAL PANEL** | **fist 2,612 kg at ten (ch32 floor) — the ch68 rebase passed the machine's 5,000 kg ceiling**; the other lines deepen with the spirits |"),
 ("| 🔴 **EFFECTIVE COMBAT POWER** | **SOUL KING (51–60), ceiling Soul King peak** | locked — see §THE ADVANTAGE LEDGER |",
  "| 🔴 **EFFECTIVE COMBAT POWER** | **SOUL EMPEROR (61–70) baseline; all-out SOUL SAGE (71–80) — reserved** | locked — §THE ADVANTAGE LEDGER + the HYH calibration (2026-09-01) |"),
 ("Historical pace for reference: rank 11 at 8½ (ch 3) → 22 by first winter (ch 4) → 30 (ch 22, the old wall) → **31 at ch40 when the third ring was bestowed** → **36 at ch61**.",
  "Historical pace for reference: rank 11 at 8½ (ch 3) → 22 by first winter (ch 4) → 30 (ch 22, the old wall) → **31 at ch40 when the third ring was bestowed** → 36 at ch61 → **45 at ch68 (the black ring) — held through the exam (ch79); the cap is now 50.**"),
])

# ---------- 2. CONTINUATION_PROMPT ----------
patch('CONTINUATION_PROMPT.md', [
 ("- **Effective combat power: 🔴 Soul King (51–60)**, ceiling Soul King peak\n- **Effective combat power: 🔴 SOUL EMPEROR (61–70)**, ceiling Emperor peak (ruled ch68; was Soul King from ch40)",
  "- **Effective combat power: 🔴 SOUL EMPEROR (61–70) baseline; all-out SOUL SAGE (71–80) — reserved (the HYH calibration, 2026-09-01; the audit nn removed a contradictory dead 'Soul King (51–60)' line that sat directly above this one)**"),
 ("- **4 rings** · spiritual power **2,768** · hawk **3,111** ·",
  "- **4 rings** · spiritual power **2,824** · hawk **3,151** ·"),
 ("- **Ledger 165 (line 165 in different ink: the intermediate guardian, ten thousand years)** — line 109 stays unfinished (ch62–68): said to Wulin in halves (ch66); Gu Yue has not heard it; the second half is a delivery with an address, and the address is not the book ·",
  "- **Ledger 168 (line 168: 'He woke. We're good enough. The academy came himself.')** — line 109 FINISHED (ch71: *'I love her. Told her. Not expecting a Yes. She said nothing. That is the nothing we agreed on. Everything is as before.'*) ·"),
])

# ---------- 3. CHARACTER_STATS ----------
t = io.open('CHARACTER_STATS.md', encoding='utf-8').read()
old = "1,399-year spirit soul"
assert t.count(old) == 1, ('STATS anchor', t.count(old))
t = t.replace(old, "the hawk — 3,151 years now (1,399 at c131)")
io.open('CHARACTER_STATS.md', 'w', encoding='utf-8').write(t)
print('fixed: CHARACTER_STATS.md (1)')

# ---------- 4. RELATIONSHIPS ----------
patch('RELATIONSHIPS.md', [
 ("# 2. TANG WULIN (唐舞麟) — canon protagonist, rank 18, one purple ring",
  "# 2. TANG WULIN (唐舞麟) — canon protagonist, rank 28 (AU pace), two rings + the right-claw soul bone, GOLDEN DRAGON BODY (the second seal broken, the hunger law live); trials 10·10·10 — the first examinee ever to catch a blade"),
 ("# 3. GU YUE (古月) — rank 21 Soul Grandmaster, two rings, spiritual power 153 at nine",
  "# 3. GU YUE (古月) — rank 31 (AU), three rings, Spirit Sea; trials 8·10 (canon's recall + the capped run); ch71's confession received in silence — the wire dormant by law"),
 ("# 4. XIE XIE (谢邂) — rank 23, two rings, highest soul power in class zero",
  "# 4. XIE XIE (谢邂) — rank 33, three rings; trials 10·10·10; the mecha half of the pact"),
 ("# 5. THE THREE WHO LEFT OR STOOD APART",
  "# 5. THE THREE WHO LEFT OR STOOD APART (+ the Eastsea schoolmates)"),
 ("Roster verified against the prose: 31 named characters.",
  "Roster: 38 named rows in the tables below (machine-counted, audit nn) · new named persons ch63–79: Elder Li only (title-scan verified) · Zhou Zhangxi's missing row found and added (audit nn)."),
])
t = io.open('RELATIONSHIPS.md', encoding='utf-8').read()
m = re.search(r'\|\s*\* \* \*|\|\s*---', t)
# insert Zhou row after Wei Xiaofeng's row in section 5
i5 = t.find('# 5.')
rows = re.findall(r'^\| \*\*Wei Xiaofeng\*\*.*\|$', t[i5:], re.M)
assert rows, 'Wei row in sec5 not found'
anchor = rows[0]
newrow = anchor + "\n| **Zhou Zhangxi** | Eastsea schoolmate (not class zero). Corroborated the smith rumour — *\"heard about the Association badge and the ten-year-old second-rank smith from four separate witnesses.\"* (Row added audit nn — he had none.) | ch6 onward |"
t = t[:i5] + t[i5:].replace(anchor, newrow, 1)
io.open('RELATIONSHIPS.md', 'w', encoding='utf-8').write(t)
print('fixed: RELATIONSHIPS.md (Zhou row)')

# S10: append the missing record entries after the highest-numbered row
t = io.open('RELATIONSHIPS.md', encoding='utf-8').read()
s10 = t.find('# 10.')
sec = t[s10:]
nums = [(int(m.group(1)), m.start()) for m in re.finditer(r'^\| (?:🔴 )?\*\*(\d+)\)\*\* |^\| (?:🔴 )?\*\*(\d+)\*\*', sec, re.M)]
rows_iter = [(int(m.group(1) or m.group(2)), m.start(), m.end()) for m in re.finditer(r'^\| (?:🔴 )?\*\*(\d+)\*\*.*\|$', sec, re.M)]
assert rows_iter, 'no numbered rows in S10'
last = max(rows_iter, key=lambda r: r[0])
add = (
 "\n| 🔴 **71** | **THE CONFESSION (the user's seed, staged near-verbatim):** *\"I love you.\" He said it plainly, no wind before it, the sixth stroke of sentences.* … *\"And Gu Yue said nothing.\"* **Line 109 finished, complete, dated:** *\"I love her. Told her. Not expecting a Yes. She said nothing. That is the nothing we agreed on. Everything is as before.\"* |\n"
 "| **72** | **The room was dark:** *\"somewhere in him, in a room he had not known he kept, there had been a candle burning… only this morning, at a birthday table with fourteen small fires going out on command, had he understood the room was dark.\"* He did not show it — *\"Steady was a garment he had cut to his own measurements.\"* The first hurt, carried quiet; never asked about. |\n"
 "| **73–79** | The exam: nothing forced, nothing read, nothing spent of it. **ch75's juice box is canon's own beat between her and WULIN** (canon 253, verbatim) — rendered uninterpreted, as law demands. ch79's arrangement and blush: likewise canon's own. The wire stays dormant; the ordinariness is the wound's exact shape, and it is his. |"
)
insert_at = s10 + last[2]
t = t[:insert_at] + add + t[insert_at:]
io.open('RELATIONSHIPS.md', 'w', encoding='utf-8').write(t)
print('fixed: RELATIONSHIPS.md (S10 +71/+72/+73-79 after row', last[0], ')')

# ---------- 5. LIN_HAO_STATUS traces ----------
patch('LIN_HAO_STATUS.md', [
 ("- rank: 5 → **45** across 79 recorded chapters (Soul Emperor-effective; the 41–50 title unnamed on purpose)",
  "- rank: 5 → **45** across 78 recorded footers (held since ch68; effective Soul Emperor 61–70, all-out Soul Sage reserved; the band title never said on-page)"),
 ("- spiritual power: 41 → **2,824** across 57 recorded chapters",
  "- spiritual power: 41 → **2,824** across 60 recorded footers"),
 ("- hawk: 906 → **3,151** years across 45 recorded chapters",
  "- hawk: 906 → **3,151** years across 48 recorded footers"),
 ("- ledger: 78 → **168** across 15 recorded chapters (168 held mid-exam, ch76–79)",
  "- ledger: 78 → **168** across 25 recorded footers (168 held mid-exam, ch76–79)"),
 ("- smithing: 3 → **5** (Master Craftsman) across 16 recorded chapters",
  "- smithing: 3 → **5** (Master Craftsman) across 21 recorded footers (last recorded ch72)"),
])

# ---------- 6. BUTTERFLY_REGISTRY ----------
patch('BUTTERFLY_REGISTRY.md', [
 ("| **The estate metals (Yaluo lot)** | ch70 | kit worked once (ch74) | ch74 |",
  "| **The estate metals (Yaluo lot — Heavy Silver + Sky Dragon Iron)** | ch70 | carried; named in the footers ch76–78 | ch78 |"),
 ("| **The wager + duel** | ch76 | taken; conditional (WZK: \"the duel is what happens if you fail\") | ch79 |",
  "| **The wager + THE EXAM DUEL** (≠ the ch69 teacher-duel, fought and lost honestly in 61 s) | ch76 | taken; conditional (WZK: \"Win… The duel is what happens if you fail\") | ch79 |"),
])
print('ALL FIXES APPLIED')

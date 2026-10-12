import io
io_txt = io.open('/home/user/Soul_Land_3_Project/LIN_HAO_PANELS.md', encoding='utf-8').read()

def patch(path, pairs):
    t = io.open(path, encoding='utf-8').read()
    for old, new in pairs:
        assert t.count(old) == 1, (path, 'MISS', old[:60])
        t = t.replace(old, new)
    io.open(path, 'w', encoding='utf-8').write(t)
    print('fixed:', path)

P = '/home/user/Soul_Land_3_Project/LIN_HAO_PANELS.md'
patch(P, [
 ("### Immediate condition — end of ch 69 (supersedes the ch 62 block below on body/appearance)",
  """### Immediate condition — end of ch 79 (the exam era; supersedes the ch 69 block below)

**No open wounds, no debt, no suppression, no restraint in force.** The exam has cost him grammar,
not muscle: three trials answered — the SPIRIT-answer (trial 1), the second answer run in the seams of
six falling gates (trial 3 — *the Track spent; the trial never learned his name*), one stroke's worth
of Sword Intent spent at trial 2 (the edge taken off a War Stomp; canon's own margin, provided).
**The maintenance report filed** — the sixth gate's tired spring priced by a half-second palm-read;
the smiths invoked. Spiritual power **2,824** · hawk **3,151** · ledger **168 (held mid-exam)** ·
rank **45 (held since ch68)**. The sword's three voices held; the domain folded; the dragon's joining
held at 95 seconds in the evening cold. **Soul power is still the constraint, not the body — and the
duel (if it is ever fought) is failure-conditional: WZK's standing word is "Win."**

### Immediate condition — end of ch 69 (historical; superseded on exam-era condition)"""),
 ("| **Current status** | **THE WALL OPENED IN ch40.** Two rings covered 21–30; the third ring was bestowed at the 1,000-year crossing and the ceiling moved to **40**. He has **four ranks of headroom** before the fourth ring is required | ch40 |",
  "| **Current status** | **The fourth ring TAKEN (ch68): three purple + one BLACK (the ten-thousand-year jiao); rank 40 → 45; the ceiling is now 50 — five ranks of headroom before the fifth-ring era** | ch68 footers; audit nn (this row had still said 'four ranks of headroom before the fourth ring') |"),
 ("| 🔴 **Effective combat power** | **SOUL KING (51–60), ceiling Soul King peak — 15 to 24 ranks above his own number.** See `THE_CODEX.md` §THE ADVANTAGE LEDGER | locked v2.91 |",
  "| 🔴 **Effective combat power** | **SOUL EMPEROR (61–70) baseline; all-out SOUL SAGE (71–80) — reserved** (the HYH calibration, 2026-09-01; the old King-band ruling is dead). See `THE_CODEX.md` §THE ADVANTAGE LEDGER | locked HYH |"),
])

# re-embed the refreshed panels into STATUS (STATUS tail after the panels marker = the panels file)
t = io.open('/home/user/Soul_Land_3_Project/LIN_HAO_STATUS.md', encoding='utf-8').read()
i = t.find('# LIN HAO — PERMANENT REFERENCE PANELS')
assert i != -1
panels = io.open(P, encoding='utf-8').read()
t = t[:i] + panels
io.open('/home/user/Soul_Land_3_Project/LIN_HAO_STATUS.md', 'w', encoding='utf-8').write(t)
print('re-embedded panels into LIN_HAO_STATUS.md')

patch('/home/user/Soul_Land_3_Project/POWER_MODEL.md', [
 ("""- 🔴 **THE CONSEQUENCE THAT WAS MISSED:** canon says *"if his spirit soul was upgraded, then the soul
  skills it provided would be upgraded too."* So **Gale Talon and Hawk-Soul Union both upgraded to
  thousand-year tier at ch40** — and no chapter shows it. Tracked as **F1** in
  `PROBLEM_INVENTORY.md`; `verify_ensemble.py` §7c warns on every run until it is written.
- **Effective combat power is 🔴 SOUL KING (51–60), ceiling Soul King peak** — 15 to 24 ranks above his
  own number. See `THE_CODEX.md` §THE ADVANTAGE LEDGER for the benchmark against normal 3rd/4th/5th-ring
  masters, and §THE REALM GAP LAW for why a lower-realm character cannot defeat him.""",
  """- 🔴 **THE CONSEQUENCE THAT WAS MISSED (and then mis-tracked):** canon says *"if his spirit soul was
  upgraded, then the soul skills it provided would be upgraded too."* **Gale Talon and Hawk-Soul Union
  both upgraded to thousand-year tier at ch40.** The old claim here — "no chapter shows it; tracked as
  F1" — was RETRACTED 2026-08-29: **Talon's upgrade IS on-page in ch40** (*"a thirty-metre deadfall comes
  apart instead of opening"*). What is genuinely unwritten is **Hawk-Soul Union's** upgrade — reserved
  with its first use (D006), and now tracked as **O1/O2 in `BUTTERFLY_REGISTRY.md` §A** (the evolution
  scene + the fourth ring's skill, due in the exam interstice).
- **Effective combat power — era note (audit nn):** this section's v2 ruling was the King band; it is
  **dead twice over** — superseded at ch68 and by the HYH calibration (2026-09-01): **SOUL EMPEROR
  (61–70) baseline; all-out SOUL SAGE (71–80), reserved.** See `THE_CODEX.md` §THE ADVANTAGE LEDGER
  and §THE REALM GAP LAW (v2.91: punching up is canon — the law governs STRANGENESS, not victory)."""),
])

patch('/home/user/Soul_Land_3_Project/THE_CODEX.md', [
 ("⚔️ Sword Intent · 🔴 **effective combat power SOUL KING (51–60), ceiling Soul King peak · rank 40 = AT THE WALL: the fourth ring (K2) is NEXT** · line 109 stays unfinished (ch62–68)",
  "⚔️ Sword Intent · 🔴 **effective combat power: the King-band ruling is DEAD — superseded at ch68 and by the HYH calibration: SOUL EMPEROR (61–70) baseline; all-out SOUL SAGE (71–80), reserved** · line 109 FINISHED (ch71)"),
 ("🔴 **CURRENT (end of ch62): rank 23, TWO rings, highest soul power in class zero EXCEPT LIN HAO (canon c184 scoped by the BUTTERFLY LAW — canon says it about a class that does not contain him), going to Shrek.",
  "🔴 **CURRENT (end of ch79, audit nn — this line had said 'rank 23, TWO rings' from ch62): rank 33, THREE rings (Soul Elder band), AT Shrek — trials 10·10·10 · the rumor-flash. Highest soul power in class zero EXCEPT LIN HAO (canon c184 scoped by the BUTTERFLY LAW — canon says it about a class that does not contain him)."),
])

patch('/home/user/Soul_Land_3_Project/CONTINUATION_PROMPT.md', [
 ("the audit nn removed a contradictory dead 'Soul King (51–60)' line that sat directly above this one)",
  "the audit nn removed a contradictory dead King-band line that sat directly above this one"),
])
print('ALL LAYER-2 FIXES APPLIED')

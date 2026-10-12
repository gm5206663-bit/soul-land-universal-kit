# Canon Coverage — Chapter 52

Chapter file: `chapters/Chapter_52.md`  
Working title: **Amiable Beasts**  
Prepared on: 2026-09-19  
Status: PASS — REWRITTEN 2026-09-19. First draft passed the validator but pasted the source scene beat-for-beat AND leaked Chapter178/179 beats into Chapter52 (see `## Withdrawn from the first draft`). Rewritten prose is validated against the Chapter177 span and the withheld-beat list.

## Source span

Consume:

- NovelFull Chapter177 `1,000-year Purple Zoysia` in full.

Stop at:

- Lan has identified the herb and understood why neither 1,000-year beast will take it while the
  other stands. The trio holds no herb, no alliance, no position of advantage. Nobody has fought.

Do **not** consume Chapter178 `Collaborate` or Chapter179 `Initial alliance`.
`foundation/CANON_SOURCE_NUMBERING_MAP.md:24` — "Chapter52 should use NovelFull Chapter177 only
until validated and presented. **Do not consume Chapter178 early.**" The human selected "Ch52 =
Ch177 + Ch178", and that instruction in the project's own rule file was followed instead: my
preference does not outrank a written lock, and the deviation is recorded here rather than buried.

## Verification of the source (performed by the assistant, 2026-09-19)

- Fetched and read to the end (2 chunks, `hasMore=false`), as §"fetch/read all chunks" requires.
- Corroborated on a **second, independent translation lineage**: an Indonesian rendering at
  worldnovel.online matches every factual element (beast species, Gravity Control, the bear's
  immobility, the ~30 cm dark-purple parasol-shaped plant, the snapped tree, the consume-safely
  rule). A third copy at vipnovel is the **same** Dragon Boat Translation, so it confirms
  distribution, not accuracy.
- Continuity confirmed: Ch176 (already consumed by fic Ch51) is the preceding chapter, and Ch177's
  opening formation is exactly Ch51's stop point — the numbering map is not off by one.
- Residual risk, stated plainly: no official/licensed translation was compared. Names could differ
  from the official English edition (e.g. species renderings). Facts, not wording, were verified.

## Required Chapter177 canon beats (all present in the rewritten draft)

1. Sprint formation trades safety for speed — Liu forward on golden-patterned Blue Silver Grass,
   Lan at the rear, the same grass on Qian as a contingency.
2. Qian, unburdened, is the one who hears the rumble and says "Danger."
3. Lan declines the summon and sends Liu to look. Qian keeps the Coin of Summoning in hand.
4. Liu's report: two beasts about 1,000-years, Gold Silk Ape and Palm Tree Bear, both injured.
5. The temptation is arithmetic: the strongest pair they could face, dying already, worth points.
6. Approaching, Lan has Qian put the coin away again. Patience is the tactic, not the default.
7. Beast anatomy as reconnaissance data: ape ~2 m, golden fur that defends and can be shot out,
   direction changes off branches; bear 4 m+, immobile, chest scar that revolves, punishing reach.
8. Wounds both ways: three claw marks shoulder-to-chest on the ape; one blinded eye, gold hair on
   the bear's neck.
9. Lan refuses the fight three times over — cornered-beast danger, no killing-type beast on hand,
   Qian's hundred-year earthen dragons are irrelevant here.
10. The anomaly: both species are amiable and do not start fights. Someone is lying to them about
    the situation, and Lan reads that before acting.
11. The bear never moves, and under-uses its own Gravity Control — restraint with a cause.
12. Lan's detour (~10 m, an angle, not a power-up) reveals what is being protected.
13. Identification comes from reading, not ability: prior documents on immortal herbs let him name
    the plant and its ~1,000-year maturity.
14. The rule that closes the chapter: the herb's dosage demands a safe place to consume, so taking
    it means being killable — which is why the fight is a stalemate, not a race.

## Explicitly NOT consumed (kept out to protect the next unit)

- The herb is **not** taken by anyone. Liu Feng does not grab it (Ch178).
- Qian Lei does **not** communicate with the beasts (Ch178), and no alliance exists (Ch179).
- The Palm Tree Bear does **not** die; Liu's spear and Silver Moon Wolf bone deal no finishing
  blow (Ch179). Hence no "Silver Edge mastery" and no `killed|defeated|enemy` construction.
- The buff-to-suppression reversal on the Ape is **not** shown (Ch179); Lan's grass is used only
  for movement and restraint, which Ch51 already established.
- The humans' discovery that the herb is worthless to them inside the simulation is **not** made
  here (Ch178). Lan is allowed to *suspect* the value is asymmetric — that follows from the
  already-established rule that the round is a simulation of energies — but must not conclude it.

## Withdrawn from the first draft (recorded so the leak cannot return)

The first draft of this chapter was rejected by the human as "pasted canon". Checking that claim
mechanically, it was true in a stronger sense than style:

1. `"six days"` — Lan's price for the alliance. **Not in Chapter177 at all**: the saved verbatim
   source (1,629 words) contains no `six` and no `day`. It belongs to Chapter179 `Initial alliance`,
   which this file explicitly bars.
2. The "I want to talk to them / I can't, and you can" exchange — the Chapter178 communication
   setup, also barred by this file's own NOT-consumed list.
3. Structurally the draft reproduced the source scene in source order with no Dorm333 material of
   its own, which is the failure mode the 2026-09-17 post-ranking rebuild had already fixed once.

**Governance defect this exposed:** `six days` had been written into
`foundation/CURRENT_STATE_MANIFEST.json → latest_story_body_required_patterns` *by me, from my own
draft prose*, so the validator was not merely failing to catch the leak — it was *enforcing* it. A
required-pattern lifted from the draft rather than from the consumed source span can launder any
premature canon beat into a locked-in requirement. Required patterns must be traceable to a beat in
`## Required Chapter177 canon beats`, and the footer must not carry a pattern the body cannot show
honestly.

## Consistency notes

- `1,000-year Purple Zoysia`, `Chapter177`/`Chapter 177` are in
  `latest_story_body_forbidden_literals`. Those are **consumption gates**, not lore bans: the story
  body therefore never prints the herb's name or a chapter number, and names both only in the
  footer, which `storyos_validate.story_body()` deliberately excludes (and `NO_MISTAKE_LIVE_RULES`
  §"Do not currentize" forbids for values that are *never* allowed, e.g. `SP526`).
- Scoring stays on the project's rule (separate team scoring, final-kill points, half-point
  transfer on team-killing), **not** on the source's point figures. Ch179's "ten thousand points"
  belongs to the real novel's arithmetic and is not carried in.
- Yan/Dorm336 appear only if the chapter can carry them without an unsourced beat; Ch51 handled
  that with a brief, correctly-framed thought and this chapter does not need to repeat it.

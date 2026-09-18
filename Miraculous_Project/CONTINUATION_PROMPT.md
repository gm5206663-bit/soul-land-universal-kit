# CONTINUATION_PROMPT.md — cold-start brief for the next session
**Position: end of ch 4** · resonance 38/100 · Cuff: BOUND · Kwami: BOUND (arrived slot 1)

## WHAT THIS IS
A Miraculous Ladybug fanfic project built on the Soul Land 3 handoff framework (full
machine port). Tight S1 AU: a new kid (the OC, holder of the Chameleon Cuff / Kwami
Kamé / hero form Chameleon) enters Paris, and their presence warps Season 1 from
chapter 1. Canon tracked episode-by-episode in PRODUCTION ORDER (101–126, 26 slots).
Tone: like canon. Length: complete and natural, never forced (L-2).

## RESTORE PROTOCOL (do this, in order, before writing anything)
1. Read `THE_CODEX.md` — the laws and the footer contract (the whole constitution).
2. Read `BRIEF.md` — the current cockpit (auto-generated; if stale, rerun
   `python3 checks/brief.py`).
3. Run `bash checks/run_all.sh` — the gate MUST be green before any new chapter.
4. Run `python3 checks/prewrite_board.py` — it prints the next slot, ore status,
   identity-lock state, active D-rows, and world pressure.
5. Check `PROBLEM_INVENTORY.md` for OPEN items (all user questions answered).

## STATE OF THE BUILD
- Machine: ported and running — 12 layers + cockpit + gate in `checks/`
  (config.json holds all tunables + the OC name markers).
- Canon: spine verified (26 slots, production order) in
  `canon_extract/SEASON1_INDEX.txt`; slot 1 ore DONE
  (`canon_extract/episodes/s1e01_stormy_weather.txt`); slot 2 ore DONE
  (`canon_extract/episodes/s1e02_the_evillustrator.txt`); slot 3 ore DONE
  (`canon_extract/episodes/s1e03_lady_wifi.txt`); slot 4 ore DONE
  (`canon_extract/episodes/s1e04_princess_fragrance.txt` — Princess Fragrance, N°104,
  title-verified 2026-09-04). **Ch 4 written + synced (slot 4 ore consumed; end of ch 4).** Next: slot 5 (Dark Cupid) — ore pending.
- Docs: THE_CODEX, POWER_MODEL (the user's binding power spec — THE DISTINCTION +
  TEMPORAL FRAMING + USER-GOVERNED all in place), WORLD_STATE, CHARACTER_STATS,
  RELATIONSHIPS, STYLE_GOLD, DIVERGENCE_LEDGER (D-001…D-005 ACTIVE),
  BUTTERFLY_EFFECTS, CANON_ACCESS, PROBLEM_INVENTORY.
- Foundation: **upgraded 2026-09-04** (full SL3 audit, user mandate "upgrade the
  foundation"). THE_CODEX now carries the mature laws — Natural-Divergence (L-1),
  Presence (L-9), Voice (L-10) — plus **new L-17–L-22** (Perspective Panels, Character
  Causality, Natural Consequence, the Character Law, Red-Test, Use Everything). Every
  chapter footer now needs a **`### Panel`** line (a non-Keal beat, L-17). POWER_MODEL
  carries the full **Adaptation Talent canon**; STYLE_GOLD carries the **Voice Law** and
  **Canon-First OC-Woven craft**. See PROBLEM_INVENTORY item 9.
- Chapters: 3 —
  - `chapters/chapter_01.md` "The Green Blur" (slot 1, Stormy Weather, complete;
    cuff bound mid-storm; 6 butterflies; OC 6 turns).
  - `chapters/chapter_02.md` "Super Nathan" (slot 2, The Evillustrator, complete;
    6 butterflies; OC 12 turns; the green hand witnessed by both heroes).
  - `chapters/chapter_03.md` "Eight Fifty" (slot 3, Lady Wifi, complete;
    6 butterflies; OC 6 turns; the stumble — Marinette trips into Keal at the gate
    at eight fifty, he finds her cute and amusing, has NO idea who she is; the
    green gap — a camouflaged hand holds the freezer door for the half-frozen
    Adrien, witnessed by Adrien alone).
  Next: slot 4 (Princess Fragrance) — ore DONE; write ch4 with the upgraded
  laws (L-17 Panel, canon-first craft, L-1 natural divergence).

## OPEN USER QUESTIONS — ALL ANSWERED 2026-09-04 (round 2)
1. Evolution limit → canon-derived: 5 min after use, hard de-transform, powers gone
   until the next transform (POWER_MODEL.md).
2. OC = **Keal Walker**, 13, the Walker family — **NEW ARRIVAL in Paris, twelve days in
   the city as of the start of ch 2 (thirteen days as of the end of ch 3)** (the new
   kid at Dupont; grouped into the center table in ch 2; his seat and table in ch 3). Talent (binding, 2026-09-04 FINAL): his OWN NATURE — part
   of him, not an external tuner; because it is him it depends on him, and its
   effect works on EVERY SINGLE PART of him (body, mind, voice, reflexes,
   coordination, emotions, instincts, social sense — every function): very strong,
   handsome, intelligent, "all things" — as his nature, human-level, never a
   superpower. The "human ceiling" framing is REPLACED — do not use it.
   THE DISTINCTION (binding): the adaptability ABILITY (Miraculous of Adaptability
   — active camouflage, Versa-Staff, Evolution!) is COMPLETELY A DIFFERENT THING
   from the adaptation TALENT — not the talent amplified, and the talent not its
   base; the Cuff adds a different thing, it does not make the talent "more" (the
   talent is his nature whether or not the Cuff exists).
   USER-GOVERNED (binding): the talent's specifics are decided by the user — never
   invented. Written as witnessed excellence + adaptation under pressure, never as
   invisibility (L-14).
3. Cuff/Kamé arrive **in S1E1, mid-storm** (D-004): the cuff was on his wrist since
   childhood as an inert matte-grey band; Kamé binds at the crisis beat.
4. Entry (revised 2026-09-04): NEW ARRIVAL — the Walker family has just moved to Paris
   (eleven days at slot 1); Keal is the new kid; ch1 opens the morning of the first storm.

## LIVE THREADS (ch2 end state)
- D-003: the city's argument is now "IS the new kid the green one?" (two clear
  crisis-faces on camera vs the unprovable blur).
- D-005: the voice has watched the storm vlog, marked the science classroom, and
  said "the one between you. The green one. I saw you too." — no identification yet.
- D-004: the heroes (both of them) have now SEEN the green hand — nameless, unprovable.
- Keal's drawer: red mask in the library / black mask at the door / the girl at the
  door / "awesome" about the blond boy — he is NOT asking it questions yet.
- Evolution: still unused (first use reserved for its own witnessed slot).
- Identity locks: all three ENGAGED (REVEAL-HM/LB/CN not present in the ledger).

## THE NEXT SEVEN STEPS (when the user returns)
1. `bash checks/run_all.sh` — gate green (it was green after ch2).
2. `python3 checks/prewrite_board.py` — it will show slot 3 (Lady Wifi), ore
   MISSING: extract the ore first (SEASON1_INDEX.txt recipe — fandom
   /wiki/Lady_Wifi chunk 0 infobox verify → Plot/Characters → distill).
3. Read DIVERGENCE_LEDGER (all five D-rows ACTIVE — the next flights are logged in
   BUTTERFLY_EFFECTS.md's manual block).
4. Draft chapter 3 (slot 3, Lady Wifi) — the hero form is public-once-twice
   (the anchor + the green hand); Evolution is still UNUSED.
5. Footer per THE_CODEX §FOOTER (≥3 butterflies, ≥4 voice turns, D-rows cited,
   canon anchors).
6. Sync ritual: state.json (top-level mirror + "3" record) → update ledger
   Current shapes → update genealogy manual block → WORLD_STATE rows for new
   on-page names → regenerate BUTTERFLY_EFFECTS + BRIEF (the gate does it).
7. Gate green → chapter 3 exists.

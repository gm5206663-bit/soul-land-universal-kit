# PREWRITE — Chapter 8 "Clean Hands"

**Status:** board recorded AFTER the draft. The board is the record, not a gate that was
run first; this is logged in SERIAL_LOG as a process deviation.

## Canon anchors (live coverage)
- **Canon 011 "Astonishing Recovery"** — the closed-door argument (Lang Yue refuses; Tang
  Ziran persuades her). FIREWALL 4: Lan Shen gets a murmur and a chair only. He never learns
  what was said.
- Mang Tian's verdict (six-star blacksmith; "unusually gifted"). Carried to Lan Shen as a
  number over the counter (Su Wan: "six stars on his name-board"), not as the speech.
- The job decided after supper: Lang Yue, the noodle street, six to eleven, eleven federation
  coins a day, a bowl. Starts Monday. Name spelled **Lang Yue** (see the name conflict below).
- Morning after: the boy's arms unhurt; "feel more powerful"; the mother credits the father
  for the medicine he never smeared. Held, unexplained. Lan Shen says "Did he," and nothing more.
- The father's long look at the boy's hands at the pump — Class-M, held.
- Na'er's awakening named as next year's Awakening Day (calendar pin: Year 1).
- The shoulder light across the gap at night — seen, never inspected (Firewall 4).

## Canon NOT staged here
- Canon 012 (the detector teacher's black book, "who taught you that word") — untouched.
  Lin Ximeng appears only as a lesson and a pause at the window.
- The forehead pattern (canon 011, Tang Wulin). Not seen by Lan Shen.

## Continuity inputs
- Ch7 closed on Day 4 night; ch8 is the fifth school day, the morning after the closed door.
- Five chalk marks on the cupboard door (streak, col 1).
- Spoon terms from ch7 used again at supper ("whole bowl tonight, twice tomorrow, then the spoon").
- Mang Tian's workshop hour continues; "Not yet" is Lan Shen's answer to "Then stop."

## Name conflict (AUTHOR CALL — do not resolve silently)
- `codex/CHARACTERS.md` says the mother is **Lang Yue** (with g) and Lan Shen's sister is
  **Lan Yue** (no g), and that no shipped chapter uses both. The shipped text agrees for the
  mother (ch2, ch4, ch5, ch7 all "Lang Yue"). `CANON_NOTES.md` (canon 011 receipt) says the
  project holds "Lan Yue" in prose. CONTINUITY row 6 writes the mother's job as "LAN YUE".
- This chapter uses **Lang Yue** for the mother, matching the shipped text. CONTINUITY row 6
  and the canon 011 receipt note are flagged as conflicting. The author should decide.

## Measured gates (after rebuild of the draft)
- verify.py PASS (3,192 prose words; below the 3,800 band in REBUILD_PLAN — see SERIAL_LOG).
- style_gate PASS: dialogue 20.7%, sentence median 10 all / 9 narration, ", and" 8.8/1k.
- canon_copy PASS. banned_token PASS. zero ? and ! in prose.
- plain_word advisory: "the door" x2 (one is the literal door of the Lan shop).

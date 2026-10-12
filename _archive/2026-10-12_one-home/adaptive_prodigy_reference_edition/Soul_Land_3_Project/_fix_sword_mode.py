import io

def patch(path, pairs):
    t = io.open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert t.count(old) == 1, (path, old[:60], t.count(old))
        t = t.replace(old, new)
    io.open(path, "w", encoding="utf-8").write(t)
    print("patched:", path)

# ── ch76: the sword never goes under; the scale fails, not the boy ──
patch("chapters/chapter_76.md", [
 ("The cold rose off it and met the hall's pressure, and the pressure was the GREATER mountain and the cold knew it, tributary to a river, and it did not retreat and it did not kneel; it went deep, the way water does under weight. The hawk tightened its grip on his shoulder to the edge of pain, winter-tipped feathers flat. His arms goosefleshed from wrist to elbow over the marks.\n\nHe counted dragon scales until the count was steady. Then he stopped counting, because beside him Xiaoyan was going under, and Wulin was already moving",
  "The cold rose off it and met the hall's pressure, and the pressure was the GREATER mountain, and the ring went deep under it — which was water's nature, and the ring was a river thing. A tributary does not shame the river.\n\nThe sword was another matter.\n\nThe sword had never once in his life been underneath anything, and it was not underneath this. The King's pressure came down and broke around his spirit the way a current breaks around a keel — met, parted, passed on — and the Intent stood in him the way it had stood at ten years old in front of grown men: temperature, edge, and no vocabulary in it for kneeling. The blood in the paint was a king's. Kings are not obeyed by swords. The hawk tightened its grip on his shoulder to the edge of pain, winter-tipped feathers flat, his arms goosefleshed wrist to elbow over the marks — and he stood in the Gold-eyed Black Dragon King's own hall with his spine unhandled, reading the painting.\n\nThen he stopped reading, because beside him Xiaoyan was going under, and Wulin was already moving"),
 ("They bowed without being told — and Elder Li, passing, looked once at Lin Hao. The look held for two full seconds, one elder's surprise at a room with two kinds of monster in it.\n\n\"Nine,\" he said, to nobody, and kept walking.\n\n\"Thank you, Elder Li.\" Shen Yi's eyes lit, and lit, and lit.",
  "They bowed without being told — and Elder Li, passing, stopped in front of Lin Hao. The look held for two full seconds, and then a third and a fourth, and it was not approval anymore. It was a man taking his own instrument out of its case and finding the scale too short.\n\n\"The hall scores endurance,\" he said to Shen Yi, without taking his eyes off the boy. \"How long a child stands under the King's blood. This one's spirit never went under it. It answered standing.\" A pause with dry amusement in it. \"The scale has no number for that. Call it ten. The first spirit-answer this hall has ever scored — and the first blood-answer, in the same morning.\" He kept walking.\n\n\"Thank you, Elder Li.\" Shen Yi's eyes lit, and lit, and lit."),
 ("and **the fourth ring TURNED OVER in him** — the ten-thousand-year jiao's cold meeting the Gold-eyed Black Dragon King's drop and going deep, *tributary to a river* — while",
  "and **the fourth ring TURNED OVER in him** — the ten-thousand-year jiao's cold meeting the King's drop and going deep (water's nature; a tributary does not shame the river) — **and the sword never went under: KINGS ARE NOT OBEYED BY SWORDS** — while"),
 ("the scoring — **Wulin FULL MARKS (the hall's historic first aura-answer); the others eight; Lin Hao NINE**, unexplained;",
  "the scoring — **Wulin FULL MARKS (canon's historic first, relabeled true: the hall's first BLOOD-answer); the others eight; Lin Hao TEN — the hall's first SPIRIT-answer: \"the scale has no number for a spirit that answers standing\"**;"),
 ("**EFFECT:** the pressure scene doubles — Wulin's canon coat wraps FIVE, and Lin Hao's score is **9** (AU, within canon's system): the elder's two-second look and one unexplained number, because the TEN belongs to the golden boy alone. The room now holds **two kinds of monster** — and the wager is believable in that corridor because the elder JUST saw both.",
  "**EFFECT:** the pressure scene doubles — Wulin's canon coat wraps FIVE, and the scoring DOUBLES: **Wulin's 10 = the hall's first BLOOD-answer (canon's historic first, kept and named true); Lin Hao's 10 = the hall's first SPIRIT-answer** — the elder took his instrument out and found the scale too short (*\"the scale has no number for a spirit that answers standing\"*). Two firsts in one morning; the hall had never scored one. The wager is believable in that corridor because the elder JUST watched the scale fail."),
 ("· trial 1 **9/10** · line 109 spent",
  "· trial 1 **10/10 — the hall's first SPIRIT-answer (Wulin's 10 = the first blood-answer)** · line 109 spent"),
])

# ── docs that carry the 9 ──
patch("POWER_MODEL.md", [
 ("Lin Hao 9/10 (AU, unexplained).",
  "Lin Hao 10/10 — the hall's first SPIRIT-answer (the scale had no number for a spirit that answers standing; Wulin's 10 = the first blood-answer)."),
])
patch("CHARACTER_STATS.md", [
 ("trial 1 — 9/10 (AU; Wulin 10, the hall's first aura-answer)",
  "trial 1 — 10/10, the hall's first SPIRIT-answer (Wulin's 10 = the first blood-answer; the scale had no number for a spirit that answers standing)"),
])
patch("THE_CODEX.md", [
 ("trial 1: 9/10; the fourth ring turned over in the King's blood",
  "trial 1: 10/10 — the hall's first SPIRIT-answer; the fourth ring turned over — and THE SWORD NEVER WENT UNDER (kings are not obeyed by swords)"),
])
patch("LIN_HAO_PANELS.md", [
 ("Trial 1: 9/10 (Wulin 10, historic).",
  "Trial 1: 10/10 — the hall's first SPIRIT-answer (Wulin's 10 = the first blood-answer; the scale too short for him)."),
])
patch("CONTINUATION_PROMPT.md", [
 ("the scoring — **Wulin FULL MARKS (the hall's historic first aura-answer); the others eight; Lin Hao NINE**, unexplained;",
  "the scoring — **Wulin FULL MARKS (the hall's first BLOOD-answer, canon's historic first kept true); the others eight; Lin Hao TEN — the hall's first SPIRIT-answer: \"the scale has no number for a spirit that answers standing\"**;"),
 ("· ledger **168 held** · trial 1: **9/10**.)",
  "· ledger **168 held** · trial 1: **10/10, the hall's first spirit-answer**.)"),
])
print("ALL PATCHES DONE")

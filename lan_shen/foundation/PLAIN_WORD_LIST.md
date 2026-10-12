# PLAIN WORD LIST — the serial's private vocabulary, classified

**Why this file exists.** Kit `07_PROSE_LAW.md` gained two laws on 2026-09-21, imported here
with the author's corrections verbatim:

> **SCOPE LAW (s39):** *"Why you making nonsense by writing nonsenses like it becomes boring,
> wyrite what needs to write not everything , you can skip"*
>
> **PLAIN LANGUAGE LAW (s40):** *"What the hell even this writeing style what you can't write
> clear that can be understood, why this poem type nonsenses"*

The laws are kit-level (authority tier 3). Full import and application plan: `STYLE_LAW.md`
§10–§11. **They apply FORWARD from ch15.** Shipped chapters are not retroactively rewritten —
that is the rebuild trap that cost `blue_silver` 90,000 words, and `STYLE_LAW.md` §0.5
already runs the same doctrine for sentence DNA.

This is NOT a ban list. The kit's rule #2: *no invented code nouns as narration — if a
sentence only makes sense to someone who knows the serial's private vocabulary, rewrite it.*
Rule #3: in-world names may appear **in speech**, and in narration **only where the scene
explains them**. The classes below apply that to what this serial actually built.

---

## CLASS A — RETIRED FROM NARRATION (zero allowed; a hit is a defect)

*(none at classification time — the audit found no term requiring retirement)*

## CLASS B — FLAGGED: narration allowed ONLY where the scene carries its anchor

The serial established these in-scene, most with a physical origin. A new chapter may use
them only if the anchor exists somewhere the reader can reach — first use in the serial
explained, later uses legible from context. Any use that leans on the reader *remembering
codex* rather than *reading prose* is a defect.

| Term | Anchor | First explained | Verdict |
|---|---|---|---|
| **the bank** | the grass bank in the garden, counted | ch6–ch9 (a physical bank of grass) | keep — physical |
| **the Wednesdays** | the weekly measure day | ch12: measuring begins; ch13: *"On Wednesdays Lin Ximeng came to two desks"* | keep — scene-established |
| **the flat line** | four minutes, ten weeks | ch12's own chapter object | keep — self-anchoring |
| **the door** | rank ten | ch2's class lesson, said aloud: *"rank ten is the door"* | keep — explained in class. ⚠️ baseline count 49 across the serial is MOSTLY literal doors (the step, the shop); the figure is meaningless without the context lines — which is why the tool prints them |
| **the ticket** | Lan Yue's noodle ticket | ch12 (physical object, in scene) | keep — physical |
| **the jar-washing** | the storeroom job | ch11 (offer on the books) | keep — scene-established |
| **the case man / the carry man** | Old Pei | ch13 named as infrastructure; ch14 introduced in person BEFORE the nickname appears in narration | keep — introduced before use |
| **the second row** | the notebook's shelf position | ch5+ (physical, repeated in scene) | keep — physical |
| **the column of fours** | the black-book column | ch12 (the reader watches it fill) | keep — scene-established |
| **the summer field** | Year 0's bank at peak | ch11, explicitly read as calendar | keep — dated in-scene |
| **the third door** | Track 7's third door | ch4 (Mang Tian's hall, in scene) | keep — dialogue-named |
| **the stairs** | 🔴 his FELT soul-power climb, no integer | ch14, deliberately unwritten | **WATCH.** Never explained aloud. Reads clearly ONLY with the progression context beside it. Rule: from ch15 either anchor it in-scene or replace with plain phrasing. No new metaphor-nouns in its family without an anchor. |
| **the roads would dry** | Pei's deadline phrase | ch14, said by Pei in speech first | keep — speech-anchored |
| **the file** | the accumulating attention on him | seeded ch10–ch14 across separate scenes (Yan Song, Qin Wu, the black book) | **WATCH.** The word has no single in-scene anchor chapter; it is codex-vocabulary bleeding toward prose. Plain-phrase it in narration ("what the school had written about him") until one scene names it. |

## CLASS C — HARD RULE FOR ANY NEW TERM (forward, from ch15)

1. A new figurative/heap noun may appear in NARRATION only if the same scene (or an earlier
   one) gives its anchor in plain sight. Speech may carry anything a character would say.
2. The subject of a narration sentence is a thing or a body; ideas never carry it (kit
   law §11.4). *(Audit note: this serial's remembered/forgot DNA does the opposite on
   purpose — "the jar remembered balm" — but there the subject IS a body/object, which is
   exactly what the law asks. The DNA and the law agree.)*
3. Write it once: no paragraph explains a paragraph; chapters do not close by re-telling.
   Consequence line: one. (kit law §10.1–3. Ch13/ch14's closing montages are **grandfathered
   forward-ruled**: from ch15 the close is one consequence line or a scene, not a summary.)
4. Overview openings are out: open in scene (kit §10.2). Ch14 opened on the shop in winter —
   borderline; ch15 opens inside a scene.
5. Budget is per-serial: the kit's 2,400–3,000 figure was calibrated to the Devouring Dragon
   serial's bloat (4,008→2,728). The author's own voice bar runs 4.0–5.4k+ and this serial's
   13-chapter shape (4.3–6.5k) is measured and accepted. **The principle binds; the number
   goes on the watch list, not the prose.** If a chapter's length is explanation-layer, the
   length is a defect; compress the explanation, never the scene.

---

**Check:** `python3 tools/plain_word_check.py chapters/*.md` — advisory, never fails;
prints every Class A hit and every Class B hit with line numbers so the writer sees the
noun budget on one screen before shipping.

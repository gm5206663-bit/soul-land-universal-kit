# RAILS.md — the laws of Qian Xun Ji Reborn

Every rail has a receipt (where it was paid for) and a check (how it fails on
bad input). Nothing here is new law — each rail restates a ruling that already
binds this serial. Never delete a rail: archive it with a dated receipt and
say why in `SERIAL_LOG.md`.

## k01 — the style gate (Grey Wolf style)

**Law:** third person limited, past tense, sensory and grounded; place first;
body band 2400–3400 words; sentence average ~14–18 words, median 11–14, no
sentence over 60 words; dialogue low (well under 5 lines per 1000 words);
no "the way [clause]" simile (allowlist: all the way / on the way / by the
way / the way of / opens the way / out of the way); no receipt dumps in
prose — the footer holds the receipts.

**Receipt:** R19 ("What the hell are wrong completely wrong with writing
style"); the gate rebuilt to the Grey Wolf project's measured style.

**Check:** `tools/measure_chapter.py` — hard failures (any sentence over 60,
any banned the-way, any jargon) exit 1; the word band is a warning. Every
footer's numbers come from this tool, run at ship time. (k06)

## k02 — no system, no jargon, embodied only

**Law:** no system window, no voice, no readout, no second mind, no reward
engine — in prose the talent is never named. Technical terms stay in
foundation docs. In chapters: breath, blood, bone, heat. (R17)

**Check:** `tools/measure_chapter.py` jargon scan (terms list in the tool),
plus eyes on every gain scene.

## k03 — the night law

**Law:** no explicit sexual content, ever. The assault is "that thing / that
night" only — no graphic detail, no flashback scene. Bibi Dong's healing is
physical only: gentle holy light, never pillar, never judgement. No memory
wipe. She is never told he is not the real Qian Xun Ji. (R4, R16, R23)

**Check:** eyes on every Bibi Dong scene against R4/R16; grep for banned
shapes when a chapter touches her.

## k04 — phenomena level

**Law:** breakthroughs and core beats carry phenomena-level staging, as the
donghua shows it — vortex, ripples, wings, pupil, pillars, domain expansion,
outer sensing — checked against donghua canon, not wiki text alone. (R18)

**Check:** the chapter footer's receipt line names the phenomena shown and
the canon receipt they were built from.

## k05 — canon-strict, no nerfing, no inflating

**Law:** nothing nerfed to protect the OC; nothing inflated to protect a
scene. Rings show their true colors. Era facts hold — no human has a soul
core in this era; the OC is the first. Every stage crossing answers the five
questions before it is written: what changed, what caused it, what did he
already possess that made this possible, what failed first, what limitation
remains. (R7, R13, R8; Master Foundation v2.0 §5)

**Check:** receipts in the footer; a `SERIAL_LOG.md` note for every stage
crossing with its five answers.

## k06 — measured claims

**Law:** every number that ships — word counts, metrics, counts, claims —
comes from a measurement run at ship time, never from memory or hope.

**Receipt:** 2026-10-07 sweep — Ch01's footer claimed ~2700w; the file
measured over 3,500w. Claims without measurement are how that happens.

**Check:** run `tools/measure_chapter.py` in the same turn as the commit; the
footer records the numbers it printed.

## k07 — naturally (no forced plot)

**Law:** the story goes naturally, by butterfly effects from what truly
happened; no pre-decided ends. The far era (Tang San), Bibi Dong's road, and
the secret's keeping are explicitly not pre-decided (R22, R23, R24). A scene
that exists to steer toward a locked outcome is against this rail.

**Check:** no mechanical check. The receipt is in writing: every arc-opening
`SERIAL_LOG.md` entry answers — what did the last state make possible?

## k08 — read before shipping

**Law:** a chapter ships only after it has been read whole against this gate
and the canon — gate green, numbers measured, footers honest. The author made
this the standing order on 2026-10-07 for Ch01–Ch02 (R26) and it stands for
every chapter after.

**Check:** `SERIAL_LOG.md` entry naming the read, the measured numbers, and
what the read found; footer carries the same.

## k09 — archive, never delete

**Law:** superseded work is archived with a dated marker — never deleted. Any
move or park of a path obliges a sweep of every checker for stale paths before
the next ship.

**Receipt:** the v3 chapter and the wiki-style codex draft were archived (not
deleted) at adoption, 2026-10-07.

**Check:** `_archive/` markers exist for every retired file; grep the tools
for retired paths after any move.

## k10 — plain language

**Law:** docs and prose are plain. No decorated jargon, no word that needs a
decoder; names and terms live in `GLOSSARY.md` and are used as the glossary
defines them. (Fleet plain-language law, applied here.)

**Check:** eyes; the glossary is updated in the same turn a term enters the
story.

# RAILS.md — the laws of The Grey Wolf

Every rail has a receipt (where it was paid for) and a check (how it fails on
bad input). Rails restate laws this serial already lives by — nothing here is
new. Never delete a rail: archive it with a dated receipt and say why in
`SERIAL_LOG.md`.

## k01 — style laws, self-enforcing

**Law:** no prose sentence over 60 words; no banned "the way [clause]"
simile (allowlist: all the way / on the way / opens the way / the way of /
by the way); no bare (unquoted) panel line; working band 2400–3400 words,
sentence average around 14–18.

**Check:** `tools/style_gate.py` — hard failures exit 1, band is warning;
per-chapter footer records `over60:0 the-way:0 bare:0` honestly.

## k02 — panel economy

**Law:** FULL status panel at every gate/gain beat; **zero panel lines at
every other beat** (F22: only when there is an update or a gain). Chapters
carry none where the serial's law says none.

**Check:** `tools/check_panels.py` — panel ledger IN SYNC with `STATUS.md`;
frozen meter fails the build.

## k03 — meters

**Law:** everything that grows feeds every open meter; 100% is an
evolution/gate moment, never a resting terminal (F14/F23 family as carried in
`RULINGS_LOG.md`). Each meter keeps its own pace law in `METERS.md`.

**Check:** `METERS.md` vs `STATUS.md` vs panel ledger — the drift guard fails
the build on mismatch.

## k04 — canon receipts

**Law:** nothing enters a chapter unverified. Canon goes as canon goes where
the story does not touch it; what the story touches is computed, changed,
logged. Sources declared in `CANON_ACCESS.md`.

**Check:** receipts in `CANON_GROUND.md`; canon-strict audit recorded in
`SERIAL_LOG.md` (v5.4.3 pass, 2026-09-26).

## k05 — STATUS is the truth

**Law:** every number current, nothing fixed from memory — if a number is not
in `STATUS.md`, it does not exist yet.

**Check:** panel drift guard (`check_panels.py`) + `run_all.py` step 4.

## k06 — ship gate

**Law:** no chapter ships without `tools/run_all.py` green — manuscript →
style gate → site → panel check. Never weaken a gate to pass it.

**Check:** `run_all.py` exit 0 before ship, before and after work.

## k07 — canon adjacency

**Law:** walk beside canon, not through it. Huo Yuhao's beats are not
displaced; the OC's road runs parallel and crossing points are chosen and
logged, never accidental.

**Check:** canon-strict audit lines in `STATUS.md` / `SERIAL_LOG.md`; the
road record in `STATUS.md` §0.

## k08 — clean and clear

**Law:** plain speech, no nonsense spam, no repetition — the author's strike
of 2026-09-26 ("What the hell nonsense you started to write again… clean and
clear", `SERIAL_LOG.md` row 28) plus the method's structural Clean-and-clear
law. No new F-number: gaps are never filled by agents.

**Check:** style gate metrics + chapter footer bands; measure, don't argue.

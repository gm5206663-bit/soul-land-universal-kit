# 2026-09-20 — gates unified (archive)

Two different files named `verify.py` existed in this repo:

- `verify_gate_b_288line.py` — the chapter gate (7 gates, panels, contiguity,
  with selftest) from `SOUL_LAND_UNIVERSAL_KIT/tools/`.
- `verify_gate_a_93line.py` — the project-root scanner (CJK sweep, backslash-n,
  filename law, digits in chapter bodies) from `SOUL_LAND_WORKSPACE/kit/tools/`.

They produced different verdicts for the same project, and Gate B misread
chapter apparatus (title, metadata head, bookkeeping tail) as prose, failing
every chapter in the corpus for digits the story never wrote.

On 2026-09-20 they were reconciled into a single `verify.py` (v2.1) with the
selftest extended to 22 cases (apparatus boundary red-tested both directions;
name-digits exempt, measurement digits still fatal; CJK still fatal
file-wide). The unified gate is now installed, byte-identical, in all three
locations:

- `SOUL_LAND_UNIVERSAL_KIT/tools/`
- `SOUL_LAND_WORKSPACE/kit/tools/`
- (sister repo) `soul-land-projects/SOUL_LAND_UNIVERSAL_KIT/tools/`

These archived copies are kept per the archive law: never deleted, never
edited in place. The living gate is the unified one.

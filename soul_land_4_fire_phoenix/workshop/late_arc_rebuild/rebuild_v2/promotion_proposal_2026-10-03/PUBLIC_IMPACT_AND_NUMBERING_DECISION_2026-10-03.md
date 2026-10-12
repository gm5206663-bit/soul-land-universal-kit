# Public Impact and Numbering Decision — V2 Promotion Proposal

**Status:** decision document; no files have been promoted.  
**Date:** 2026-10-03.

## 1. Verified current public edge

The recovered public StoryOS layer contains accepted prose through:

- `Chapter_52.md` — **Chapter 52, _Amiable Beasts_**;
- public live edge: Chapter 52;
- stated source edge: the Chapter-177 Purple Zoysia setup;
- Chapter 53: quarantined/superseded, not an accepted public chapter.

The V2 line is therefore **not** a routine continuation patch. It replaces the public C48–C52 run and supplies the next causal movements in a different, deliberately compressed form.

## 2. Exact replacement impact

| Current public file | Current public title | V2 source unit | V2 title | Promotion type |
|---|---|---|---|---|
| `Chapter_48.md` | _The Line in the Stars_ | V2 C48 | _The Line We Keep_ | Full replacement |
| `Chapter_49.md` | _No Pattern Underfoot_ | V2 C49 | _What They Carry_ | Full replacement |
| `Chapter_50.md` | _The Forest Counts Separately_ | V2 C50 | _Two Maps of the Forest_ | Full replacement |
| `Chapter_51.md` | _The Cost of Quiet_ | V2 C51 | _The Cost of Quiet_ | Full replacement despite matching title |
| `Chapter_52.md` | _Amiable Beasts_ | V2 C52 | _What the Ground Keeps_ | Full replacement and source-unit consolidation |
| — | No accepted public C53+ | V2 C54 | _What a Favor Costs_ | New causal unit |
| — | No accepted public C53+ | V2 C55 | _What We Leave Open_ | New causal unit |
| — | No accepted public C53+ | V2 C60 | _The Price of Keeping_ | New causal unit; consolidation endpoint |

## 3. Why direct filename copying is invalid

V2 is intentionally built from **eight causal units**:

`48, 49, 50, 51, 52, 54, 55, 60`

The absences are substantive, not accidental:

- V2 C52 absorbs the former C53 midpoint.
- V2 C60 replaces the old five-part C56–C60 route/withdrawal loop.

Copying those internal labels into public filenames would leave a reader-facing `52 → 54 → 55 → 60` sequence. Filling the gaps with cosmetic chapters would reverse the structural rebuild. Publishing unnumbered gaps would break the public serial model.

## 4. Author choice required

### Option A — **Contiguous public renumbering** (recommended)

Keep V2’s internal labels as workshop provenance, but publish one continuous public sequence:

| Proposed public file/heading | V2 body supplied | Notes |
|---|---|---|
| Public C48 — _The Line We Keep_ | V2 C48 | Replaces current C48. |
| Public C49 — _What They Carry_ | V2 C49 | Replaces current C49. |
| Public C50 — _Two Maps of the Forest_ | V2 C50 | Replaces current C50. |
| Public C51 — _The Cost of Quiet_ | V2 C51 | Replaces current C51. |
| Public C52 — _What the Ground Keeps_ | V2 C52 | Replaces current C52 and carries the complete old C52/C53 movement. |
| Public C53 — _What a Favor Costs_ | V2 C54 | Renumbered public presentation only; source V2 file remains untouched. |
| Public C54 — _What We Leave Open_ | V2 C55 | Renumbered public presentation only; source V2 file remains untouched. |
| Public C55 — _The Price of Keeping_ | V2 C60 | Renumbered public presentation only; source V2 file remains untouched. |

**Benefits:** reader-contiguous; honors the causal-unit rebuild; does not create filler; keeps V2 provenance intact in its protected layer.  
**Cost:** the public endpoint becomes Chapter 55 rather than Chapter 60, and state/navigation must explicitly record the internal-to-public mapping.

### Option B — **Range-labelled public units**

Publish the major consolidated units under visible range labels, for example:

- `Chapter 52–53 — What the Ground Keeps`
- then `Chapter 54 — What a Favor Costs`
- `Chapter 55 — What We Leave Open`
- `Chapter 56–60 — The Price of Keeping`

**Benefits:** preserves the historical V2 scope labels in reader-facing titles.  
**Costs:** requires a nonstandard public filename/state model; risks reader confusion and technical incompatibility with a one-file-per-integer Chapter system.

### Option C — **Keep V2 author-review-only**

Make no public update now.

**Benefits:** preserves the recovered public baseline exactly.  
**Cost:** V2 remains a reviewed replacement candidate rather than the accepted continuation.

### Option D — **Author-specified numbering**

Any other numbering scheme may be selected, but it must retain all three safeguards:

1. no filler chapters merely to preserve former labels;
2. no silent conflation of internal V2 labels with public labels;
3. no C61 creation.

## 5. Recommendation

**Option A** is recommended if the author approves promotion. It treats V2’s structural consolidation as real, protects its internal provenance, and produces a usable reader-facing sequence. It must be explicitly approved before a staging copy is generated.

## 6. Required authorization language

A safe approval must state both parts, for example:

> “Approve V2 as the public replacement and use contiguous public renumbering (Option A). Archive the prior public C48–C52 only; do not create C61.”

An approval of prose quality alone is not enough to authorize public overwrites or choose a numbering model.

## 7. Selection record

The author selected **Option A — contiguous public C48–C55** on 2026-10-03. The resulting candidate exists at:

`staging_option_A_contiguous_public_C48_C55/`

That selection authorized staging only. It did **not** authorize applying the candidate to the recovered public layer, changing state/gate files, or creating C56/C61.

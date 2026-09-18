# CANON SOURCE — what is deliberately NOT in this repository

This repository is **public**. Three things were excluded on purpose.

## What is excluded, and why

| Excluded | Size | Why |
|---|---|---|
| `98_CANON_SOURCE_PDFS_2026-08-28.tar.gz` | 13 M | Seven PDFs of *Soul Land 3 / Legend of the Dragon King* — **copyrighted novel text** (fan translation). |
| `98_CANON_SOURCE_PDFS_337-600_2026-08-28.tar.gz` | 11 M | Two more PDFs, canon chapters 337–600. Same reason. |
| `canon_extract/chapters/` | 4 M · 372 files | The extracted text of canon chapters 229–600. |
| `CODEX/CANON_QUOTE_SOURCES_FROZEN.txt` | 296 K | Verbatim text of the 35 canon chapters our quoted lines verify against. |

**This is not a preference.** Publishing a novel's text in a public repository is a copyright
problem regardless of who translated it, and it risks a takedown against the whole repo — including
the 71 original chapters and the entire verification framework, which are the parts worth keeping.
The existing repository already followed this convention: it contained no PDFs and no canon chapter
files before this commit.

What *is* here is original writing plus **short attributed quotations** used for adaptation and
commentary, which is ordinary fan-fiction practice.

---

## What this costs

**Layer 7 of the suite cannot run without the corpus.** It verifies that every line attributed to
canon in a chapter header actually appears in canon, word for word. In the authoring workspace it
reports **85/85 verified against 407 canon chapters.** Here it prints:

```
verify_canon_quotes: NO CANON CORPUS PRESENT
  ==> LAYER 7 SKIPPED. This is NOT a pass. 85 canon quotes are unverified here.
```

and `run_all.sh` drops `--strict` so the other twelve layers still run for real. **The message is
loud by design** — a skip that looks like a pass is how a check quietly dies.

It also costs a real limitation on the work itself. 🔴 **Reading a quote is not reading a chapter.**
`CANON_COMPARISON_ch66-71.md` documents four facts that were wrong in published chapters even though
every quotation was verbatim and correctly attributed — including one case where a real canon line
was attached to the wrong character entirely. Layer 7 can prove a line *exists*; it cannot prove it
*belongs to the person we gave it to*. Only reading the chapters in full catches that, and reading
them in full requires the corpus.

---

## Restoring it, if you already own the source

The suite resolves every path through `checks/paths.py`. Point it at a corpus you have locally:

```bash
# either the corpus alone
SL3_CANON=/path/to/canon_extract/chapters SL3_WORKSPACE=.. sh checks/run_all.sh

# or a whole authoring workspace laid out as <WS>/CODEX, <WS>/canon_extract/chapters
SL3_WORKSPACE=/path/to/workspace sh checks/run_all.sh
```

`paths.has_canon()` decides whether Layer 7 runs in strict mode. Nothing else in the suite needs it.

The corpus can be rebuilt from the PDFs with `canon_extract/ingest.py`, which is likewise not
distributed here — but note its own recorded caveat: **canon chapters 47, 61 and 102 are not cleanly
re-extractable** by it, because of out-of-order PDF markers. Verified not load-bearing.

---

## What was verified before the corpus was excluded

So that the exclusion does not erase the evidence:

- **85/85** canon quotes attributed in chapter headers verified word-for-word against 407 chapters.
- **30/30** header quotes in ch66–71 verified, after one was corrected: it had been a close
  paraphrase sitting inside quotation marks as if it were a verbatim pull.
- The full audit of ch66–71 against canon 288–307 is written up in
  [`CANON_COMPARISON_ch66-71.md`](CANON_COMPARISON_ch66-71.md), including what was wrong.

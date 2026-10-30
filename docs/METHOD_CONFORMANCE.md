# METHOD CONFORMANCE — the account measured against the law

**Measured 2026-10-30.** Thirteen repositories, five rules, one command. This file is the
scorecard, the method behind it, and the shortest honest path for each repository that fails.

The law is [`gm5206663-bit/how-to-write-fanfiction`](https://github.com/gm5206663-bit/how-to-write-fanfiction)
— *How to Write Gated Fan Fiction*, guide edition **v3.3**, law revision **v5.7**. It was read,
not remembered: `VERSION_OF_RECORD.md`, `README.md`, `docs/03_gates_and_audits.md`, and
`tools/check_manifest.py` were cloned and read before a single row below was written.

One command reproduces everything here:

```
python3 tools/method/conformance.py --root <folder-of-clones>     # the matrix
python3 tools/method/conformance.py --selftest                    # proves the auditor can fail
```

`--selftest` runs nine fixtures that inject each defect in turn. A conformance auditor that has
never been shown failing is not an auditor, it is an opinion — rule 1 of the guide, applied to
this file.

---

## 1. What "conformant" means — the five rules, straight from the guide

| id | requirement | where the guide says it |
|---|---|---|
| **R1** | a **one-command battery** that runs several checks and exits 0 | `docs/03` — "The battery is one command and must exit 0" |
| **R2** | a **selftest that injects defects** and proves the gates can fail | `docs/03` rule 1 |
| **R3** | **independent proof** — `MANIFEST.sha256`, or an outside scan | `docs/03` rule 3 · `tools/check_manifest.py` |
| **R4** | **same-turn state** — a status/ledger that is rebuilt, not remembered | `README` big idea 4 |
| **R5** | the repository **names the law** — one copy of one thing | `README` big idea 5 |

R5 is not decoration. The guide's own argument is that a method with twelve copies becomes twelve
methods; the pointer is what keeps the copies from drifting. A repository that never names the
guide cannot be corrected by it.

---

## 2. The matrix

`ok` = the rule holds. `.` = it does not. Score is out of five.

| repository | R1 | R2 | R3 | R4 | R5 | score | what it is |
|---|:--:|:--:|:--:|:--:|:--:|---:|---|
| how-to-write-fanfiction | ok | ok | ok | ok | ok | **5/5** | *the law — 5/5 is the calibration* |
| soul-land-universal-kit | ok | ok | ok | ok | ok | **5/5** | Soul Land corpus + workshop |
| supergirl-adrian-vale | ok | ok | ok | ok | . | 4/5 | Supergirl serial |
| the-authors-desk | ok | ok | . | ok | . | 3/5 | account navigation |
| soul-library | ok | ok | . | . | ok | 3/5 | the reader shelf |
| pokemon-adaptation | . | ok | . | ok | ok | 3/5 | Pokémon serial |
| adaptation-talent | . | . | ok | ok | ok | 3/5 | the doctrine repo |
| mcu_eternal_fanfic | . | ok | . | ok | . | 2/5 | MCU serial |
| stark_heir | . | ok | . | ok | . | 2/5 | MCU serial |
| sara | . | . | ok | . | ok | 2/5 | the author's own rules |
| the-universal-storyline-creation | . | ok | . | ok | . | 2/5 | the protocol repo |
| storyos-site | . | . | . | ok | . | 1/5 | the site |
| gm5206663-bit (profile) | . | . | . | . | ok | 1/5 | the profile README |

Per rule, counted from the run: **R1 5 of 13 · R2 9 of 13 · R3 5 of 13 · R4 10 of 13 · R5 7 of 13.**

Eight of thirteen repositories cannot be checked in one command. That is the headline, and it is
the same defect everywhere: the gates exist, but no single door runs them. The rule that holds up
best is R2 (9 of 13) — the account has been good at proving gates can fail — and the rule that
holds up worst is the one with no code in it: R3, proof of bytes, and R5, naming the law.

### Two things this matrix already changed in the kit itself

1. **The kit cited the law zero times.** The repository holding the whole Soul Land corpus and
   thirteen gated projects never named `how-to-write-fanfiction`, while five much smaller
   repositories cited it correctly. Fixed in this pass — `README.md` and `AGENTS.md` now carry the
   pointer, and `AGENTS.md` quotes the three rules that govern every change here.
2. **The kit had no battery of its own.** Every battery in it belonged to a serial
   (`lan_shen/checks/run_all.sh`, `adaptive_prodigy/checks/run_all.sh`). The repository you could
   not check in one command was the one holding everything. `tools/run_all.sh` is that command.

---

## 3. Four false passes this auditor produced before it was trusted

Recorded because a measurement tool's failures are the only reason to believe its successes.

| false pass | why it happened | the fix |
|---|---|---|
| the kit scored R1 on `adaptive_prodigy/checks/run_all.sh` | a serial's battery credited to the repository that contains the serial | battery search limited to the repository's own level (`root`, `tools/`, `checks/`, `.github/workflows/`) |
| the kit scored R2 on `tools/ship_chapter.py` | any file naming two checks counted, including a **writer** | a battery must be *named* like one (`run_all`, `battery`, `gate`, `check_all`, …) **and** invoke two or more distinct files that exist |
| the kit scored R5 on `HISTORY.md` | a passing mention in a changelog scored the same as a pointer at the door | R5 reads root `README.md` / `AGENTS.md` / `index.md` only |
| supergirl scored **no** battery | the detector only understood `python3 tools/x.py`; that repository launches checks with `subprocess.run([sys.executable, …])` | invocation lines are found by keyword **and** a ±1-line window, then resolved to real files |

A false **gap** is as damaging as a false pass — someone then "fixes" a working repository. The
last row is why `--selftest` now has a Python-battery fixture.

Also tightened: R3 no longer accepts a drift *script* or a report that archived someone else's
manifest (both scored falsely on 2026-10-30), and R4 no longer accepts a mistakes ledger — a
ledger records the past, only a rebuilt panel knows the present.

---

## 4. The one red gate in the account, and it is not a tooling problem

`adaptive_prodigy` — Soul Land 3 — is the only repository whose battery runs and **fails**:

```
FAIL  L4 ch116: the Union opened on-page: "He opened the Union for ten seconds and folded it;
      opened it for fifteen and folded it; let it come a dozen times in a morning…"
```

This is a real canon-lock spend, not a parser artefact:

- `checks/verify_locks.py` L4 encodes **D006 — "first use still reserved"**. Mentions are legal;
  opening is not; `"did not open"` is explicitly exempt.
- `CONTINUATION_PROMPT.md` lists **"the Union opening"** in the HELD set, twice.
- `DIVERGENCE_LEDGER.md` D19: `Union opening` — **HELD**.
- `PROBLEM_INVENTORY.md` M5: *"Union (held shut BY NAME in the fight)"*.
- `BUTTERFLY_REGISTRY.md` O1 records that ch69 **reported the Union without opening it** — *"the
  door stays shut; first use still reserved — the lock checker enforced it, correctly."*
- And `chapter_116.md`'s own header says: **"no sealed gate is touched."**

The chapter opens it three times, in a training drill, and then rides the dragon-fusion behind it.

**This is the author's decision, not a repair a tool may make.** Rewriting prose is the author's
word. Three defensible rulings, and the gate is right under all of them until one is made:

1. **The chapter is wrong** — the drill teaches the *hinge* without opening the door. Rewrite in the
   author's hand; the lock stands.
2. **The lock is released** — the author rules that first use now happens at ch116. Then D006 is
   amended in the ledger, registry and prompt *in the same commit*, and `verify_locks.py` L4 is
   changed **with its selftest updated** — never loosened silently.
3. **The chapter is not canon yet** — it sits past the "101 chapters green" line; hold it out of the
   gate's reach by recording its status honestly, not by narrowing the gate's reach by accident.

Until one is chosen, `sh tools/run_all.sh` exits 1 and says so on screen. That is the correct
behaviour of a gate that works.

---

## 5. The per-repository plan — smallest change first

Ordered so each step is one browser session and nothing breaks if a session stops halfway.
The user does not use a terminal; every step is a GitHub web-UI action.

### Tier 0 — already done, in this repository

| repo | change | state |
|---|---|---|
| soul-land-universal-kit | `tools/run_all.sh` added; `README.md` + `AGENTS.md` cite the law | ✅ this pass |
| soul-land-universal-kit | R5 was the kit's only gap | ✅ closed |

### Tier 1 — one line, four repositories (five minutes each, highest return)

R5 is a pointer. Nothing else in these repositories needs to move.

| repo | add to `README.md`, directly under the title | closes |
|---|---|---|
| supergirl-adrian-vale | the standard law paragraph (§6.1) | R5 |
| the-authors-desk | the standard law paragraph | R5 |
| storyos-site | the standard law paragraph | R5 |
| mcu_eternal_fanfic · stark_heir | the standard law paragraph | R5 (both) |
| the-universal-storyline-creation | the standard law paragraph | R5 |

### Tier 2 — a battery, five repositories

The kit ships the template; each repository gets a thin runner at its own level. **These are not
copies of the law** — they are the door to the repository's own checks, and each one is ~15 lines.

| repo | what its battery should run | why |
|---|---|---|
| sara | `tools/check_sara.py` + its own selftest | the check exists; nothing calls it |
| adaptation-talent | manifest verify + link check | has a manifest, no runner |
| pokemon-adaptation | `tools/style_gate.py` + `tools/canon_copy.py` if present | one gate, never joined to another |
| mcu_eternal_fanfic · stark_heir | `tools/mcu_verify.py` + manifest verify | the verify tool is real and has a 9-fixture selftest; nothing runs both |
| storyos-site | `scripts/drift.py` + link check | the drift script exists and is never run from one door |
| the-universal-storyline-creation | its selftest + protocol check | selftest exists, unreachable |

### Tier 3 — the independent proof, six repositories

`MANIFEST.sha256` at the repository root, generated by a committed script and checked by the
battery. This is the one rule nobody can fake, and it is one file plus one step per repo.

Order: `storyos-site` → `soul-library` → `the-authors-desk` → `mcu_eternal_fanfic` →
`stark_heir` → `the-universal-storyline-creation`.

`soul-library` deserves its own line: its `sentinel.html` looks like proof and is not — it contains
no hashes at all (verified: zero `sha256` matches). A status page is a claim about state; a manifest
is proof about bytes.

### Tier 4 — same-turn state, four repositories

`sara`, `soul-library`, `gm5206663-bit` (profile), and `the-universal-storyline-creation` have no
rebuilt status file. The guide's Ship Law needs one generated from the tree at the end of every
turn, so the answer to "what is true now" cannot be a stale paragraph.

---

## 6. The artifacts, copy-ready

### 6.1 The law paragraph — one line at the top of a README

> **The method:** this repository is held to
> [`how-to-write-fanfiction`](https://github.com/gm5206663-bit/how-to-write-fanfiction)
> (guide v3.3 / law v5.7). Where the two disagree, the guide wins. One command checks this
> repository: `sh tools/run_all.sh`.

### 6.2 The thin runner — `tools/run_all.sh`

Copy from this repository and edit the two marked lines. It prints which checks ran, so a check
that silently stops existing is visible instead of being assumed.

### 6.3 The manifest step

```
python3 tools/check_manifest.py --write    # after agreeing the tree is what you meant
python3 tools/check_manifest.py            # must print the same tree back
```

Never regenerate a manifest to make a gate green. The manifest records what the author accepted;
re-stamping an unaccepted change forges the receipt.

---

## 7. Standing limits of this measurement

Stated so the next agent does not read more into this file than it contains.

- **Static, not executed.** The auditor reads trees; it does not run the other twelve repositories.
  So R1–R5 record that the machinery *exists and is wired*, not that it is currently green. The
  one repository that was actually executed — the kit — is the one with a red gate (`§4`).
- **Depth-limited by design.** A battery belongs to a repository, not to a project inside it. The
  kit's fourteen serials each having their own gate does not make the kit conformant; that is the
  very confusion this file exists to end.
- **A name is not a behaviour.** `sara` has `tools/check_sara.py` and no battery;
  `mcu_eternal_fanfic` has only `mcu_verify.py` and yet a real R2 selftest. Both directions of
  error were live in this account.
- **R5 is a pointer, not an agreement.** A repository can cite the guide and still break every rule
  in it. The pointer is necessary, not sufficient.

---

## 8. The corpus layer — measuring what is there, not what the battery looked at

Added 2026-10-30, after the first version of this file. The battery in §2 covers **five of the
fourteen** projects in this repository, because only five carry a `checks/run_all.sh`. The guide
names that exact failure in doc 06, about the tool that was written to prevent it:

> **`register.py`** measures every book and every chapter-bearing tree on the account and prints
> what it found — nothing on disk holding prose may be unnamed. It exists because the account's own
> tools had been registering *what they happened to look at, not what was there*.

The kit already had `register.py` and `account.py`. What it did not have was either of them inside
the battery — so the account's own tool was itself unregistered. Two layers now run every time:

| layer | what it proves | 2026-10-30 |
|---|---|---|
| `6 account control centre` | 16 books · 283 chapters · 1,211,566 words · **33 of 33** chapter-bearing trees accounted for | 0 hard · 6 advisory |
| `7 register drift` | `REGISTER.md` still equals what the tree produces | PASS |

That is the difference between a battery over five projects and a battery over everything on disk.

### Three defects the corpus layer exposed in one run

**1. `housekeeping` examined zero repositories on a single-repo root.** It carried its own copy of
the "which repositories exist" walk instead of calling `_repos()`. `_repos()` had been taught that
the root may *be* the repository; the copy had not. So on `--root soul-land-universal-kit` it walked
nothing and printed `0 of 0 repository(ies) walked` — a clean-looking zero, on the repository holding
the whole corpus. One implementation now, not two.

**2. `generated` examined 0 of 0 while three files declared themselves generated.** Its stamp regex
wanted `GENERATED from <path>; SHA256: …`. `REGISTER.md` says *"Generated … Regenerate it; never edit
it."* — a declaration with no hash, which the detector read as no file at all. It now counts both:
**0 of 3 checked against a hash**, and names all three. An unhashed stamp is a real gap, and it was
invisible.

**3. Two coverage lines, zero subjects, no finding.** Now an invariant: **every detector whose
coverage total is 0 must emit a finding saying so** — `empty-coverage` (hard) when it expects
subjects, `thin-coverage` (advisory) when the empty set is legitimate. The selftest removes the
invariant and confirms the check goes red, so it cannot be quietly deleted.

**4. A gate that mutates the repository invents the drift it was hired to find.** The first version
of layer 6 wrote refreshed `account_report.*` into the tracked tree. That broke their byte-identity
with the copies in `SOUL_LAND_WORKSPACE/kit/` — the duplicate-group count in `tools/check.py` fell
from 25 to 19 because I had made six previously-identical files differ. Caught by noticing the count
*moved the wrong way*; reverted, and the layer now writes to `${TMPDIR}`. **The battery is read-only.**
Regenerating state is an explicit act (`tools/register_drift.py --write`), never a side effect of
checking something.

### The open item this leaves — the account register, 17 days old, in two places

`SOUL_LAND_UNIVERSAL_KIT/REGISTER.md` and `SOUL_LAND_WORKSPACE/kit/REGISTER.md` are **byte-identical
copies** of a whole-account register generated **2026-10-13 10:54** over *"a full clone set"*:
**24 books · 377 chapters · 1,624,963 words · 70 sentences over 60 words**.

Neither can be checked from this checkout, because this checkout is not a full clone set. Both are
now declared exemptions in `tools/register_drift.py` — and the "it is a copy" half of that
declaration is **checked** (byte equality), not trusted. What is still true, and is the author's call:

- the numbers are 17 days old and are the account's published size claim;
- the pair is one copy of one thing too many;
- nothing regenerates them, because nothing here has all twelve repositories.

Either delete the pair (the root register is the one this repository can actually prove), or
regenerate them from a full clone set and give them a hash stamp this repository can verify.

### What the corpus layer deliberately does not do

It does not gate prose. The 70 sentences over 60 words in that account register, and the
`dialogue-exempt` book, are author-facing measurements, not tool verdicts. §4 is the one place where
a corpus measurement becomes a blocking finding, and it blocks because a written lock is being
contradicted — not because a number looks high.

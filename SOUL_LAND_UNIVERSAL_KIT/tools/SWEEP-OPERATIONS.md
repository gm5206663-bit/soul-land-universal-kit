# The scheduled account sweep — operating contract

The weekly `account-sweep` workflow measures the public account. It does not
edit prose, rule on author decisions, or require zero findings to finish green.
A green run means **the measurement completed**, not **every book passed**.
Read the verdict and coverage in the run summary and download the evidence.

## Three different outcomes

| Outcome | Job result | Meaning |
|---|---|---|
| Complete, no hard findings | success | All discovered public repositories cloned; checkers finished; no hard Control Centre findings. Advisories may remain. |
| Complete, findings present | success | Same complete scope; hard findings remain visible in the reports. They are not suppressed or repaired automatically. |
| Incomplete discovery or execution | failure | API error, empty inventory, failed clone, checker crash, missing evidence or inconsistent exit code. Never interpret the smaller result as health. |

## What changed on 2026-10-16

- `sweep_inventory.py` walks every API page, including accounts larger than one
  hundred repositories. It records each repository's archived flag, default
  branch and exact cloned HEAD. It refuses duplicate/unsafe names, unexpected
  owners, empty discovery and existing destinations. Every attempted clone gets
  a success or failure receipt; any failure stops the measurement job.
- `sweep_evidence.py` distinguishes normal checker exit 1 (findings) from
  interrupted execution. It requires a completed gate verdict and all three
  Control Centre artifacts, the expected offline detector coverage, nonempty
  chapter facts, and a hard-finding count consistent with the exit code.
- `control-centre-tests` runs the detector, discovery, evidence, gate and scope
  regression suites whenever their source or either workflow changes.
- Stale repository totals are now checked on the desk README, desk Pages front
  door and profile README. Both digits and English zero–twenty are understood,
  including hyphenated “twelve-repository” and inline HTML markup. Historical
  receipts and story prose are not repository-total targets. Canonical book
  totals retain their existing scan and historical-receipt exemptions.

## Reproduce without a token

Run from the kit repository root, using a **new, empty destination**:

```bash
python3 SOUL_LAND_UNIVERSAL_KIT/tools/sweep_inventory.py \
  --root /tmp/account-fresh --out-prefix /tmp/inventory
python3 SOUL_LAND_UNIVERSAL_KIT/tools/account.py report \
  --root /tmp/account-fresh --out-prefix /tmp/account-report
```

`account.py report` exits 1 when hard findings exist. This is expected; do not
pipe away or ignore the status without checking the produced evidence.

```bash
python3 SOUL_LAND_UNIVERSAL_KIT/tools/sweep_evidence.py \
  report /tmp/account-report 1
```

Supply the **actual** checker status in the last argument (0 or 1), not an
assumed value. The workflow captures it directly.

## Scope and recovery limits

- Public discovery cannot reveal private repositories. A successful public
  inventory does not prove that the owner has no private repositories.
- API discovery and sequential clones are not an atomic snapshot: each recorded
  HEAD is the revision actually read. Repositories can change during a run.
- `account-clones.tgz` contains shallow working snapshots, not complete Git
  history. It excludes inaccessible private repositories and may be partial on
  a failed run. Read `sweep-inventory.json` and `sweep-inventory-heads.json`
  before using it for recovery.
- Artifacts have GitHub's finite retention window. Durable dated management
  receipts belong in the public `the-authors-desk` repository, not only in an
  expiring artifact or on a working machine.
- The broad standalone house gate and the Control Centre use different discovery
  scopes. Compare each coverage ledger; do not merge their verdict counts.
- Live Pages API checks require separate authenticated execution. The scheduled
  public sweep's validated coverage is its offline detector set.

## Regression commands

```bash
cd SOUL_LAND_UNIVERSAL_KIT/tools
python3 account_selftest.py
python3 sweep_inventory_selftest.py
python3 sweep_evidence_selftest.py
python3 live_book_gate.py --selftest
bash gate_selftest.sh
python3 selftest.py
```

The command results, not a manually maintained test-count badge, are the source
of truth. New historical receipts preserve the count measured on their date.

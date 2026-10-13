# tools/ — the ship script

**What it is:** [`ship_chapter.py`](ship_chapter.py) — the root-level ship helper for shipping
a chapter through its gates.
**Where the gates actually live:** the kit's own tooling is in
[`../SOUL_LAND_UNIVERSAL_KIT/tools/`](../SOUL_LAND_UNIVERSAL_KIT/tools/) —
`selftest.py` and `account_selftest.py` (the gates that gate the gates), `live_book_gate.py`
(the prose gate), `register.py` (regenerates [`../REGISTER.md`](../REGISTER.md)),
`account.py` / `account_checks.py` (the account sweep).
**Law:** never weaken a gate to pass it; run the serial's own verify before and after any change.
Map: [`../README.md`](../README.md).*
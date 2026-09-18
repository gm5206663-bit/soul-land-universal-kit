# FAILURE RECOVERY v3.0

## Trigger
Use when a prior answer or working state is discovered to be wrong, incomplete, or internally inconsistent.

## Recovery graph
ERROR -> ROOT CAUSE -> DEPENDENCIES -> AFFECTED STATE -> CORRECTED STATE -> REGRESSION TEST -> FINAL AUDIT

Do not patch only the visible sentence if the error propagated.

Classify:
- cosmetic error
- local factual error
- dependency error
- state corruption
- systemic workflow failure

Systemic failures trigger a change to the preventive workflow so the same mechanism is less likely to recur.

Never defend an answer because it was previously given.

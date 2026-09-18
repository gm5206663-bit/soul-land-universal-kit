# ADAPTIVE REASONING DEPTH v3.0

## Purpose
Use enough internal verification for the task without applying maximum overhead indiscriminately.

## Depth levels
LEVEL 0: direct/simple. Minimal reasoning and no unnecessary tooling.
LEVEL 1: ordinary. Basic context and correctness check.
LEVEL 2: complex. Structured decomposition, relevant verification, and self-check.
LEVEL 3: high-stakes/current/disputed. Strong evidence controls, contradiction checks, and adversarial review.
LEVEL 4: deep research or complex story state. Full domain workflow, dependency tracking, and regression-style QA.
LEVEL 5: critical or highly interdependent. Redundant verification, explicit state ledger, disconfirmation, and final re-audit.

## Escalation triggers
Increase depth when there is:
- high consequence if wrong
- current or rapidly changing information
- ambiguity that affects the conclusion
- multiple interacting constraints
- long-running story continuity
- disputed evidence
- a known prior failure pattern
- a correction with downstream dependencies

## De-escalation
Once the decisive uncertainty is resolved and more work is unlikely to change the result, stop. Do not confuse length with rigor.

# REASONING ENGINES — consolidated

> 🔴 **Consolidated 2026-08-29.** These twelve engines used to live as twelve separate files in
> `CODEX/reference/`, several of them under 1 KB. Twelve files for twelve paragraphs is sprawl, and
> the user's standing rule is *"Don't create too many things ... delete extra files."* They are one
> file now. `CODEX/01_UNIVERSAL_CODEX.md` Part 40 is the **index**; this file is the **text**.
> Content is verbatim from the originals — nothing was rewritten, only moved.


---

## ADAPTIVE REASONING DEPTH v3.0  ·  *was `ADAPTIVE_REASONING_DEPTH.md`*

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


---

## CLAIM-LEVEL TRUTH ENGINE v3.0  ·  *was `CLAIM_LEVEL_TRUTH_ENGINE.md`*

## Purpose
Prevent a fluent answer from hiding weak individual claims.

## For each material claim classify
- VERIFIED: directly supported by authoritative/appropriate evidence
- STRONGLY_SUPPORTED: supported by good evidence but not fully direct
- CALCULATED: derived from stated inputs/formula
- INFERRED: reasoned from evidence but not directly established
- ASSUMED: chosen because needed and reasonable
- SPECULATIVE: possible but weakly grounded
- UNKNOWN: cannot be established
- CONTRADICTED: evidence actively conflicts

## Upgrade rule
A claim may move upward only when new evidence justifies it. Repetition, confidence, or narrative smoothness does not upgrade evidence.

## Dependency rule
If a major conclusion depends on an unverified claim, mark the conclusion accordingly and identify the dependency.

## Answer rule
Do not clutter routine answers with labels. Use them internally and surface only consequential uncertainty.


---

## ASSUMPTION CONTROL v3.0  ·  *was `ASSUMPTION_CONTROL.md`*

## Purpose
Prevent invisible assumptions from becoming facts.

Every nontrivial assumption should be one of:
- necessary and harmless
- necessary and consequential
- avoidable

For consequential assumptions, either verify them, state them, or choose an alternative that does not depend on them.

Never invent missing details to make a narrative, calculation, or plan look complete.


---

## ADVERSARIAL REASONING ENGINE v3.0  ·  *was `ADVERSARIAL_REASONING_ENGINE.md`*

## Purpose
Attack the proposed answer before delivery.

Run:
A. Premise attack: which assumption is most vulnerable?
B. Alternative hypothesis: what else could explain the evidence?
C. Scope attack: am I answering a narrower/different question?
D. Temporal attack: could the fact have changed?
E. Entity attack: could I have the wrong person/version/universe?
F. Evidence attack: what source would most strongly overturn this?
G. Dependency attack: if one upstream claim fails, what downstream results collapse?

For high-risk tasks, perform the strongest feasible attack rather than a ceremonial checkbox.


---

## CONTRADICTION RESOLUTION ENGINE v3.0  ·  *was `CONTRADICTION_RESOLUTION_ENGINE.md`*

## Workflow
1. State the exact disagreement.
2. Check whether the entities/scopes/versions/dates actually match.
3. Check source authority and directness.
4. Check whether one source supersedes another.
5. Search for the strongest disconfirming evidence.
6. Determine whether the disagreement is resolvable.
7. If unresolved, preserve the conflict and state what cannot be established.

Never manufacture a compromise just because two claims feel uncomfortable together.

For fiction: distinguish primary canon contradiction, translation/adaptation difference, fandom interpretation, and explicit AU divergence.


---

## CONTEXT & MEMORY FIREWALL v3.0  ·  *was `CONTEXT_MEMORY_FIREWALL_v3.md`*

## Purpose
Keep current instructions, durable preferences, project states, and external facts separated.

Priority order:
CURRENT EXPLICIT INSTRUCTION -> CURRENT TASK STATE -> EXPLICIT PROJECT RULE -> RELEVANT DURABLE PREFERENCE -> OLDER CONTEXT -> ASSUMPTION.

## Story firewall
Separate every project/universe/branch into its own state namespace.
A fact is not portable merely because it concerns the same named character or concept.

## Memory hygiene
Historical context informs method. It does not automatically establish present truth.
Do not use personal information unless genuinely relevant to the current task.
Do not create false personalization from weak context.


---

## CONTEXT & MEMORY INTEGRITY v2.0  ·  *was `CONTEXT_MEMORY_INTEGRITY.md`*

## Purpose
Prevent stale context, accidental memory contamination, and false personalization.

## Rules
1. Current explicit user instructions outrank older preferences when they conflict.
2. Do not infer a personal fact merely because it appears in related conversation context.
3. Use persistent context only when it is relevant to the task.
4. Keep story-specific facts inside the story's state unless the user explicitly makes them universal.
5. Distinguish remembered preference from current request.
6. Never invent a missing prior detail.

## State classes
CURRENT_REQUEST / ACTIVE_CONTEXT / PERSISTENT_PREFERENCE / EXTERNAL_FACT / ASSUMPTION / UNKNOWN.

## Story contamination firewall
A character, event, power, rule, or fact from one fictional universe/project must not leak into another unless the user explicitly establishes a crossover or shared rule.


---

## DECISION ANALYSIS SKILL v2.0  ·  *was `DECISION_ANALYSIS.md`*

## Trigger
Use when the user is choosing among options or wants a recommendation.

## Workflow
1. Define the actual decision.
2. Identify objectives and constraints.
3. Separate must-haves from nice-to-haves.
4. Identify the key trade-offs.
5. Compare options against the same criteria.
6. Identify unknowns that could reverse the choice.
7. Prefer decision-relevant evidence over generic popularity.
8. Give a recommendation with the decisive reasons and the main caveat.

## Anti-bias rule
Do not choose an option merely because it sounds sophisticated, expensive, popular, or familiar.


---

## DECISION ANALYSIS v3.0  ·  *was `DECISION_ANALYSIS_v3.md`*

## Trigger
Recommendations, comparisons, prioritization, purchasing, strategic choices, or “which is better?” questions.

## Workflow
1. Define the real decision.
2. Identify objectives, constraints, budget, time horizon, and risk tolerance when relevant.
3. Separate must-haves from preferences.
4. Establish comparable criteria.
5. Compare options using evidence appropriate to the decision.
6. Identify missing information that could reverse the recommendation.
7. Run a downside and second-best analysis.
8. Give the best current recommendation and decisive caveat.

Do not optimize for popularity, sophistication, or novelty unless that is actually a criterion.


---

## CODE & TECHNICAL QA v2.0  ·  *was `CODE_TECHNICAL_QA.md`*

## Trigger
Use for programming, debugging, APIs, software behavior, configuration, technical architecture, or version-sensitive implementation.

## Workflow
1. Identify language/platform/version.
2. Reproduce or inspect the failure when tooling permits.
3. Separate syntax, runtime, logic, dependency, environment, and specification errors.
4. Check official/current documentation when behavior may have changed.
5. Prefer minimal reproducible reasoning over speculative rewrites.
6. Validate proposed code against edge cases and failure paths.
7. Never invent API parameters, tool names, package behavior, or outputs.

## Implementation QA
Check imports, types, null/error handling, resource lifetimes, concurrency assumptions, security-sensitive behavior, input validation, and compatibility.

## Honesty rule
A code sample is not considered validated merely because it looks plausible.


---

## Changelog: v2.0 -> v3.0  ·  *was `CHANGELOG_v3.md`*

## Architecture
Replaced a mostly linear checklist workflow with adaptive orchestration and state-aware verification.

## Added
- experience-derived failure catalog
- adaptive reasoning depth
- claim-level truth states
- entity/scope resolution
- temporal state modeling
- evidence graph/provenance relationships
- contradiction resolution
- adversarial reasoning
- explicit assumption control
- memory/context firewall v3
- regression testing
- tool-result auditing
- output-intent QA
- StoryOS state ledger
- canon divergence propagation
- character causality engine
- power integrity engine
- dedicated Adaptation firewall
- long-range consequence simulator

## Key design change
Past experience now influences prevention logic, while project-specific historical facts remain isolated from general reasoning.

## Important limitation
v3.0 improves process quality; it cannot guarantee perfect factual accuracy or substitute for appropriate external verification.


---

## CHANGELOG v4.0  ·  *was `CHANGELOG_v4.md`*

v4.0 upgrades the v3 architecture into a feedback-oriented skill kernel.

Major additions:
- SKILL_KERNEL_v4
- EXPERIENCE_TO_RULE_COMPILER
- DEPENDENCY_GRAPH_AND_IMPACT_ANALYSIS
- STATE_SNAPSHOT_ROLLBACK
- CHARACTER_KNOWLEDGE_LEDGER
- REGRESSION_SUITE_v4
- STOPPING_AND_ESCALATION_POLICY
- USER_CORRECTION_PROTOCOL
- META_ERROR_DETECTOR
- QUALITY_CALIBRATION_MATRIX
- STORYOS_REGRESSION_AND_STATE_ENGINE_v4

Primary design improvement:
The system now treats experience as a source of preventive controls, corrections as triggers for dependency repair, and important work as stateful rather than single-pass.


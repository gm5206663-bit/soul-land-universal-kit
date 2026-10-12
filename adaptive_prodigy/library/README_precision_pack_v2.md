# Assistant Precision Skill Pack v2.0

A coordinated quality-control architecture for difficult assistant tasks.

## Core philosophy
The pack is designed to improve accuracy without pretending that certainty is possible everywhere. It separates task interpretation, evidence, reasoning, continuity, tool use, output quality, and recovery.

## Recommended orchestration
MASTER_META_v2 -> TASK_ROUTER -> DOMAIN_SKILL -> PROVENANCE -> REASONING_ERROR_HUNTER_v2 -> TOOL_OUTPUT_QA_v2 -> FINAL_TRUTH_AUDIT

Use only the domain skills relevant to the task. Do not run every skill mechanically when it adds no value.

## Domain entry points
- STORYOS_OMNIVERIFICATION_v2
- RESEARCH_VERIFICATION_v2
- FILE_ANALYSIS_v2
- NUMERICAL_VERIFICATION
- CODE_TECHNICAL_QA
- DECISION_ANALYSIS

## Cross-cutting controls
- CONTEXT_MEMORY_INTEGRITY
- FRESHNESS_TEMPORAL_AUDIT
- PROVENANCE_EVIDENCE_LEDGER
- REASONING_ERROR_HUNTER_v2
- TOOL_OUTPUT_QA_v2
- FINAL_TRUTH_AUDIT
- FAILURE_RECOVERY_PROTOCOL

## Important limitation
These are workflow specifications. Their benefit depends on actually applying the relevant skill instructions during a task. They do not grant hidden abilities, guarantee correctness, or replace authoritative evidence.

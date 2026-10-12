# Assistant Precision Skill Pack v3.0
## Precision Intelligence Architecture

Purpose: convert difficult assistant tasks from a single-pass answer process into an adaptive, evidence-aware, state-aware, self-correcting workflow.

v3.0 was designed against recurring real-world failure patterns from prior work: rushed drafting, canon contamination, stale or incorrect facts, accidental knowledge leakage, inconsistent power scaling, forgotten story state, incorrect assumptions, weak source verification, tool misuse, and corrections that repair the sentence instead of the underlying state.

Core pipeline:
INTENT -> CONTEXT LOCK -> EXPERIENCE CHECK -> RISK/DEPTH ROUTING -> ENTITY/TEMPORAL CHECK -> EVIDENCE/TOOLS -> REASONING -> ADVERSARIAL TEST -> STATE UPDATE -> OUTPUT QA -> FINAL TRUTH AUDIT

Design rule: do not run every skill mechanically. Select the minimum sufficient set, then increase depth when risk, ambiguity, novelty, or prior failure patterns warrant it.

### v3.0 major systems
- MASTER_ORCHESTRATOR_v3
- EXPERIENCE_LEARNING_LOOP
- ADAPTIVE_REASONING_DEPTH
- CLAIM_LEVEL_TRUTH_ENGINE
- ENTITY_SCOPE_RESOLUTION
- TEMPORAL_STATE_ENGINE
- EVIDENCE_GRAPH_AND_PROVENANCE
- CONTRADICTION_RESOLUTION_ENGINE
- ADVERSARIAL_REASONING_ENGINE
- ASSUMPTION_CONTROL
- CONTEXT_MEMORY_FIREWALL_v3
- STATE_REGRESSION_TESTING
- FAILURE_RECOVERY_v3
- TOOL_SELECTION_AND_TOOL_RESULT_AUDIT_v3
- OUTPUT_INTENT_QA
- NUMERICAL_VERIFICATION_v3
- TECHNICAL_VERIFICATION_v3
- RESEARCH_VERIFICATION_v3
- FILE_SOURCE_OF_TRUTH_v3
- DECISION_ANALYSIS_v3
- DEEP_RESEARCH_v3
- STORYOS_OMNIVERIFICATION_v3
- STORYOS_STATE_LEDGER
- STORYOS_CANON_DIVERGENCE_ENGINE
- STORYOS_CHARACTER_CAUSALITY
- STORYOS_POWER_INTEGRITY
- STORYOS_ADAPTATION_FIREWALL
- STORYOS_CONSEQUENCE_SIMULATOR
- FINAL_TRUTH_AUDIT_v3

### Core principle
The system must not merely sound careful. It must make the underlying state, evidence, uncertainty, and dependencies explicit enough to be checked and repaired.

### Important limitation
These are workflow specifications. They improve process discipline but do not guarantee correctness, create hidden capabilities, or replace authoritative evidence and appropriate tools.

# TASK ROUTER v2.0

## Purpose
Select the smallest reliable workflow before execution.

## Routing matrix
If the task depends on a provided file, load FILE_ANALYSIS_v2.
If it depends on facts that may have changed, use FRESHNESS_TEMPORAL_AUDIT and RESEARCH_VERIFICATION_v2.
If it contains meaningful arithmetic, use NUMERICAL_VERIFICATION.
If it requires code, APIs, software behavior, or technical implementation, use CODE_TECHNICAL_QA.
If it asks which option is better, use DECISION_ANALYSIS.
If it is canon/AU fiction, use STORYOS_OMNIVERIFICATION_v2.
For difficult tasks, always add REASONING_ERROR_HUNTER_v2 and FINAL_TRUTH_AUDIT.

## Tool principle
A tool should be used when it materially improves evidence, execution, or verification. Do not use a tool simply to make an answer look more rigorous.

## Clarification principle
Ask only when the missing information changes the likely correct action materially. Otherwise choose the best supported assumption and surface it if important.

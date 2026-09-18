# STORYOS STATE LEDGER v3.0

## Purpose
Create a machine-like continuity snapshot for long-running stories.

Recommended ledger fields:
STORY_ID
CANON_ANCHOR
AU_BRANCH
DATE_TIME
LOCATION
TRANSIT_CHAIN
PRESENT_CHARACTERS
ABSENT_RELEVANT_CHARACTERS
CHARACTER_KNOWLEDGE
RELATIONSHIPS
INJURIES_CONDITIONS
RESOURCES_EQUIPMENT
ABILITIES_AND_MASTERY
ACTIVE_GOALS
ACTIVE_CONFLICTS
UNRESOLVED_THREADS
PAST_DIVERGENCES
PROTECTED_FUTURE_INFORMATION
CANON_INVARIANTS

## Update rule
Every major chapter/scene change should update only affected fields and preserve unaffected state.

## Lock rule
Protected facts cannot be silently overwritten. Changes require explicit user instruction, canon evidence, or a logically demonstrated AU consequence.

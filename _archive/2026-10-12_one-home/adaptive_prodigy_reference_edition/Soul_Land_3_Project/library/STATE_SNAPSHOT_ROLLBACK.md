# STATE SNAPSHOT & ROLLBACK v4.0

## Mission
Prevent state drift during long tasks and make corrections reversible.

## Snapshot fields
- task state
- assumptions
- verified facts
- unresolved questions
- active constraints
- key dependencies
- output target

## Before a major transformation
Create a compact snapshot.

## After transformation
Compare BEFORE vs AFTER and classify each change as INTENDED, REQUIRED CONSEQUENCE, or UNINTENDED.

## Rollback rule
When an unintended change is found, restore the affected dependency chain to the last valid state, then reapply only intended changes.

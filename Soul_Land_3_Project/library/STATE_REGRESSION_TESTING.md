# STATE REGRESSION TESTING v3.0

## Purpose
When a task changes an established state, verify that old valid constraints still hold.

Method:
1. snapshot relevant pre-change state
2. apply intended change
3. identify dependent facts
4. recompute affected dependencies
5. test invariant constraints
6. compare against prior valid behavior
7. record the new state

Use for story arcs, financial models, technical configurations, plans, datasets, and iterative corrections.

An answer is not fixed if the changed sentence is correct but dependent state remains inconsistent.

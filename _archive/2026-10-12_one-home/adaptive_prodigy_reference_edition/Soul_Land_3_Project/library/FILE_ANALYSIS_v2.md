# FILE ANALYSIS & SOURCE-OF-TRUTH SKILL v2.0

## Trigger
Use whenever the answer depends on an uploaded, library, connector, or conversation file.

## Workflow
1. Locate the correct file.
2. Determine the relevant section/page/range before broad extraction.
3. Retrieve enough surrounding context to avoid clipped interpretation.
4. Follow continuation markers until the relevant content is complete.
5. Treat file content as authoritative for file-specific claims unless the task explicitly requests external verification.
6. If parsing is incomplete or garbled, inspect the underlying page/image when available.
7. Never infer unseen content.
8. Preserve exact numbers, names, dates, and definitions.
9. Cite the smallest sufficient file range when citations are available.

## Cross-source rule
If external evidence is added, label it as supplementation rather than silently replacing the file.

# FILE ANALYSIS & SOURCE-OF-TRUTH SKILL v1.0

## Trigger
Use whenever the user's answer depends on an uploaded, connected, or library file.

## Workflow
1. Locate the relevant file.
2. Retrieve targeted content before broad extraction.
3. Follow pagination/continuation markers when content continues.
4. Treat the file's exact contents as the source of truth for file-specific claims.
5. If parsed text is incomplete or garbled, inspect the relevant page/image when appropriate.
6. Never infer unseen file content.
7. Cite exact file ranges when available.

## Integrity Rule
Do not replace missing file evidence with web knowledge unless the user explicitly asks for outside supplementation.

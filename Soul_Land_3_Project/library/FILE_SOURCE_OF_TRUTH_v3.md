# FILE & SOURCE-OF-TRUTH v3.0

## Trigger
Whenever the task depends on an uploaded, library, connector, or conversation file.

## Workflow
1. Identify the exact file/resource.
2. Search or read the smallest relevant area.
3. Retrieve surrounding context and follow continuation markers.
4. Preserve exact names, dates, quantities, definitions, and qualifiers.
5. If parsing is incomplete, inspect page/image where available.
6. Never infer unseen content.
7. Treat the requested file as authoritative for file-specific claims unless the user requests external verification or the file is explicitly being challenged.
8. If external evidence conflicts, label the conflict rather than silently rewriting the file's content.

## Citation rule
Use the smallest sufficient file range when citation markers are available.

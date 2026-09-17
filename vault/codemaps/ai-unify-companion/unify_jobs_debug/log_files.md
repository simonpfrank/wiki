# `unify_jobs_debug/log_files.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `json` (external)
- [mcp_server.constants](../mcp_server/constants.md)
- `os` (external)
- `pathlib` (external)
- `re` (external)
- `typing` (external)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.log_files._read_lines` | `def _read_lines(path: str) -> list[str]` |  |
| `unify_jobs_debug.log_files.scan_log` | `def scan_log(path: str, env: str='') -> str` | Summarise a downloaded Unify job log file. |
| `unify_jobs_debug.log_files.read_log_window` | `def read_log_window(path: str, start_line: int, end_line: int, context_before: int=0, context_after: int=0, env: str='') -> str` | Read a line range from a downloaded Unify job log file. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

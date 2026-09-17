# `unify_jobs_debug/local_dataset_files.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `csv` (external)
- `fnmatch` (external)
- `json` (external)
- [mcp_server.constants](../mcp_server/constants.md)
- `openpyxl` (external)
- `os` (external)
- `pathlib` (external)
- `re` (external)
- `typing` (external)

## Imported by (INFERRED)

- [mcp_server.tools](../mcp_server/tools/__init__.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.local_dataset_files._write_temp` | `def _write_temp(data: dict, stem: str) -> str` | Write *data* as pretty JSON to unify_storage/temp/ and return the path. |
| `unify_jobs_debug.local_dataset_files._maybe_offload` | `def _maybe_offload(data: dict, stem: str) -> str` | Always write result to temp file and return a pointer with the path and shape info. |
| `unify_jobs_debug.local_dataset_files._read_text_file` | `def _read_text_file(path: str) -> str` |  |
| `unify_jobs_debug.local_dataset_files._read_csv_file` | `def _read_csv_file(path: str, max_rows: int) -> str` |  |
| `unify_jobs_debug.local_dataset_files._read_xlsx_file` | `def _read_xlsx_file(path: str, sheet: str, max_rows: int, max_cols: int) -> str` |  |
| `unify_jobs_debug.local_dataset_files.read_local` | `def read_local(path: str, mode: str='auto', sheet: str='', max_rows: int=200, max_cols: int=50, env: str='') -> str` | Read a local file cautiously and return its contents. |
| `unify_jobs_debug.local_dataset_files.grep_local` | `def grep_local(path: str, pattern: str, glob: str='*', max_hits: int=200, context_before: int=0, context_after: int=0, env: str='') -> str` | Search for a pattern in local files (including xlsx cells via openpyxl). |
| `unify_jobs_debug.local_dataset_files._apply_path` | `def _apply_path(obj: object, parts: list[str]) -> list[object]` | Recursively walk *parts* against *obj*, expanding lists at each step. |
| `unify_jobs_debug.local_dataset_files._parse_selector` | `def _parse_selector(selector: str) -> tuple[list[str], str | None, str | None]` | Parse  'a.b[].c|field==value'  into  (path_parts, filter_field, filter_value). |
| `unify_jobs_debug.local_dataset_files._is_int` | `def _is_int(v: str) -> bool` |  |
| `unify_jobs_debug.local_dataset_files._filter_results` | `def _filter_results(results: list[Any], filter_expr: str) -> list[Any]` |  |
| `unify_jobs_debug.local_dataset_files._apply_pick_fields` | `def _apply_pick_fields(results: list[Any], fields: list[str]) -> list[Any]` |  |
| `unify_jobs_debug.local_dataset_files.query_json` | `def query_json(path: str, select: str='', filter_expr: str='', pick: str='', max_results: int=100, file_name: str='', env: str='') -> str` | Query a local JSON file using simple path expressions — no jq required. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

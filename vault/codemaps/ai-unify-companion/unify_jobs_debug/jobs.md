# `unify_jobs_debug/jobs.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `datetime` (external)
- `json` (external)
- [mcp_server.constants](../mcp_server/constants.md)
- `os` (external)
- `pathlib` (external)
- `typing` (external)
- [unify_api](../unify_api/__init__.md)
- [unify_api.constants](../unify_api/constants.md)
- [unify_api.core](../unify_api/core.md)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)
- [unify_api.core](../unify_api/core.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.jobs._utcnow` | `def _utcnow() -> datetime` |  |
| `unify_jobs_debug.jobs._parse_dt` | `def _parse_dt(value: str | None) -> datetime | None` |  |
| `unify_jobs_debug.jobs._build_status_filters` | `def _build_status_filters(status: str) -> list[int]` |  |
| `unify_jobs_debug.jobs._compute_fields` | `def _compute_fields(job: dict[str, object]) -> dict[str, object]` |  |
| `unify_jobs_debug.jobs._get_api` | `def _get_api(env: str | None=None) -> UnifyAPI` |  |
| `unify_jobs_debug.jobs.search_jobs` | `def search_jobs(status: str='', text_search: str='', only_my_jobs: bool=False, topmost_only: bool=False, min_duration_minutes: float | None=None, max_age_hours: float | None=None, max_results: int=20, order_by: str='CompletedAt', sort_descending: bool=True, file_name: str='', env: str='') -> dict[str, object]` | Search Unify jobs with pagination and post-filtering. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `unify_jobs_debug/triage.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `json` (external)
- [mcp_server.constants](../mcp_server/constants.md)
- `os` (external)
- `pathlib` (external)
- `re` (external)
- `shutil` (external)
- [unify_api](../unify_api/__init__.md)
- [unify_api.constants](../unify_api/constants.md)
- [unify_jobs_debug._challenge](_challenge.md)
- [unify_jobs_debug.summary](summary.md)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.triage._get_api` | `def _get_api(env: str | None=None)` |  |
| `unify_jobs_debug.triage._triage_recursive` | `def _triage_recursive(api, job_id: int, save_dir: pathlib.Path, visited: set[int]) -> dict` | Build a full summary for job_id, recursively triage non-completed |
| `unify_jobs_debug.triage.triage_job` | `def triage_job(job_id: int, file_name: str, env: str='', clear_downloads: bool=False, clear_temp: bool=False) -> str` | Return the job summary with first_fault populated to the deepest faulted |
| `unify_jobs_debug.triage._resolve_activity_id_by_name` | `def _resolve_activity_id_by_name(api, job_id: int, name: str) -> str | dict` | Return activity_id matching name, or an error/challenge dict. |
| `unify_jobs_debug.triage._activity_summary` | `def _activity_summary(api, job_id: int, activity_id: str) -> dict` |  |
| `unify_jobs_debug.triage._activity_errors` | `def _activity_errors(api, job_id: int, activity_id: str, grep: str, tail: int | None) -> dict` |  |
| `unify_jobs_debug.triage._activity_full` | `def _activity_full(api, job_id: int, activity_id: str, grep: str, tail: int | None) -> dict` |  |
| `unify_jobs_debug.triage.get_activity_runtime` | `def get_activity_runtime(job_id: int, activity_id: str='', name: str='', path: str='', include: str='summary', tail: int | None=None, grep: str='', env: str='') -> str` | Inspect the runtime logs for a specific activity within a job. |
| `unify_jobs_debug.triage._apply_grep_tail` | `def _apply_grep_tail(entries: list[dict], grep: str, tail: int | None) -> list[dict]` | Filter entries by an optional regex, then keep the last `tail` lines. |
| `unify_jobs_debug.triage.get_job_inputs` | `def get_job_inputs(job_id: int, download_dir: str='', env: str='') -> str` | Return the input arguments for a job, downloading any blob (file) inputs |
| `unify_jobs_debug.triage.get_activity_tree` | `def get_activity_tree(job_id: int, env: str='') -> str` | Fetch the full structured activity status tree for a job and save to temp. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

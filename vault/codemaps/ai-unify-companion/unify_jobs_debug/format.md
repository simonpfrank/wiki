# `unify_jobs_debug/format.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [unify_api.constants](../unify_api/constants.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.format.status_label` | `def status_label(status: int, names: dict=JOB_STATUS_NAMES, icons: dict=JOB_STATUS_ICONS) -> str` | Format a status int as 'icon Name'. |
| `unify_jobs_debug.format.job_status` | `def job_status(status: int) -> str` |  |
| `unify_jobs_debug.format.activity_status` | `def activity_status(status: int) -> str` |  |
| `unify_jobs_debug.format.format_size` | `def format_size(size_bytes: int) -> str` | Human-readable file size. |
| `unify_jobs_debug.format.format_job_summary` | `def format_job_summary(job: dict) -> str` | Format a Job2 object into a readable summary. |
| `unify_jobs_debug.format.format_activity_tree` | `def format_activity_tree(node: dict, indent: int=0, max_depth: int | None=None, _counter: list | None=None, max_nodes: int=200) -> str` | Recursively format a CompositeJobActivityDto tree. |
| `unify_jobs_debug.format.find_log_node` | `def find_log_node(nodes: list[dict], activity_id: str) -> dict | None` | Recursively find a log header node by ActivityId. |
| `unify_jobs_debug.format.format_log_headers` | `def format_log_headers(logs: list[dict], indent: int=0, _counter: list | None=None, max_nodes: int=200) -> str` | Format log headers tree showing activity names, types, and error/warning flags. |
| `unify_jobs_debug.format.format_log_entries` | `def format_log_entries(entries: list[dict], max_entries: int=50) -> str` | Format log entries into a readable list, truncating if too large. |
| `unify_jobs_debug.format.format_durations` | `def format_durations(dur: dict) -> str` | Format activity durations as a breakdown report. |
| `unify_jobs_debug.format.format_outputs` | `def format_outputs(outputs: list[dict]) -> str` | Format structured job outputs. |
| `unify_jobs_debug.format.format_active_jobs` | `def format_active_jobs(jobs: list) -> str` | Format active jobs list. |
| `unify_jobs_debug.format.format_job_list` | `def format_job_list(jobs: list) -> str` | Format list_jobs output. |
| `unify_jobs_debug.format.format_activity_status_flat` | `def format_activity_status_flat(job_id: int, activities: list) -> str` |  |
| `unify_jobs_debug.format.format_job_inputs` | `def format_job_inputs(job_id: int, inputs: list) -> str` |  |
| `unify_jobs_debug.format.format_hierarchy_node` | `def format_hierarchy_node(node: dict, indent: int=0) -> list` |  |
| `unify_jobs_debug.format.format_job_hierarchy` | `def format_job_hierarchy(job_id: int, hier: dict) -> str` |  |
| `unify_jobs_debug.format.format_job_velocity` | `def format_job_velocity(job_id: int, vel: dict) -> str` |  |
| `unify_jobs_debug.format.format_job_validation` | `def format_job_validation(job_id: int, flat: list) -> str` |  |
| `unify_jobs_debug.format.format_referenced_object` | `def format_referenced_object(job_id: int, activity_id: str, ref: dict) -> str` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

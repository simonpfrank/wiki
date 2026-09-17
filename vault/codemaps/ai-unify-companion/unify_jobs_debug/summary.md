# `unify_jobs_debug/summary.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `datetime` (external)
- `re` (external)
- `typing` (external)
- [unify_api.constants](../unify_api/constants.md)

## Imported by (INFERRED)

- [unify_jobs_debug.triage](triage.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.summary._activity_id` | `def _activity_id(a: dict) -> str` | Best-effort activity id across the API's field-name variants. |
| `unify_jobs_debug.summary._iter_roots` | `def _iter_roots(tree) -> list[dict]` | Normalise the structuredActivityStatus response into a list of root |
| `unify_jobs_debug.summary._find_fault_leaf` | `def _find_fault_leaf(roots: list[dict]) -> tuple[dict | None, list[dict]]` | Walk the structured activity tree and return the DEEPEST Faulted leaf |
| `unify_jobs_debug.summary._count_by_status` | `def _count_by_status(roots: list[dict]) -> dict[str, int]` | Count every activity in the tree grouped by status name. |
| `unify_jobs_debug.summary._collect_faulted` | `def _collect_faulted(roots: list[dict]) -> list[dict]` | Return a compact entry for every Faulted activity (containers + leaves). |
| `unify_jobs_debug.summary._compact_node` | `def _compact_node(node: dict) -> dict` | One compact (id, name, type, status) record for a tree node. |
| `unify_jobs_debug.summary._leaf_error` | `def _leaf_error(api, job_id: int, activity_id: str) -> tuple[str | None, int]` | Pull the terminal error message for an activity from the job's log error |
| `unify_jobs_debug.summary._duration_to_seconds` | `def _duration_to_seconds(d: str | None) -> int | None` | Parse a .NET TimeSpan string ("[d.]hh:mm:ss[.fffffff]") to seconds. |
| `unify_jobs_debug.summary._elapsed_seconds` | `def _elapsed_seconds(job: dict) -> int | None` | Compute elapsed seconds, tolerant of timestamp formats. Falls back to |
| `unify_jobs_debug.summary._find_hierarchy_node` | `def _find_hierarchy_node(node: dict, target_id: int) -> dict | None` | Recursively find the node with target_id in a job hierarchy tree. |
| `unify_jobs_debug.summary._walk_log_node` | `def _walk_log_node(node: dict, log_index: list[dict]) -> None` | Recursively collect log index entries from a log header node. |
| `unify_jobs_debug.summary._fetch_full_entries` | `def _fetch_full_entries(api, src_job_id: int, activity_id: str, instance_id: int=0) -> list[dict]` | Return all log entries for an activity. |
| `unify_jobs_debug.summary._collect_log_errors` | `def _collect_log_errors(api, src_job_id: int, log_errors: list[dict], seen_ids: set[str], instance_id_map: dict[str, int]) -> None` | Append enriched error entries for src_job_id into log_errors. |
| `unify_jobs_debug.summary._build_first_fault` | `def _build_first_fault(api, job_id: int, leaf: dict, chain: list[dict]) -> tuple[dict, list[dict]]` | Build first_fault dict and fault_chain for the deepest faulted leaf. |
| `unify_jobs_debug.summary._get_child_jobs` | `def _get_child_jobs(api, job_id: int) -> tuple[list[dict], list[int]]` | Return (child_workflow_jobs, child_job_ids) from the job hierarchy. |
| `unify_jobs_debug.summary._get_log_index` | `def _get_log_index(api, job_id: int) -> list[dict]` | Return flattened log index from job log headers. |
| `unify_jobs_debug.summary.build_job_summary` | `def build_job_summary(api, job_id: int) -> dict[str, Any]` | Build the compact job triage summary. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `unify_jobs_debug/bridge.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [mcp_server.constants](../mcp_server/constants.md)
- `os` (external)
- `typing` (external)
- [workflow_reader](../workflow_reader/__init__.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.bridge.resolve_job_workflow` | `def resolve_job_workflow(api, job_id: int) -> dict[str, Any]` | Resolve the workflow + version identifiers for a job. |
| `unify_jobs_debug.bridge._find_xaml_blob` | `def _find_xaml_blob(api, version_id: int) -> dict` | Return the .xaml blob dict ({FileName, Id, ...}) for a version. |
| `unify_jobs_debug.bridge.download_job_workflow` | `def download_job_workflow(api, job_id: int, output_dir: str | None=None) -> dict[str, Any]` | Download the workflow XAML that produced a job. |
| `unify_jobs_debug.bridge.load_job_workflow` | `def load_job_workflow(api, job_id: int)` | Download a job's workflow XAML and return a (WorkflowReader, ref) pair. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

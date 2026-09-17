# `unify_jobs_debug/operations.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `traceback` (external)
- [unify_api](../unify_api/__init__.md)
- [unify_api._mcp_helpers](../unify_api/_mcp_helpers.md)
- [unify_jobs_debug](__init__.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_jobs_debug.operations._get_api` | `def _get_api(env: str | None=None)` | Return a UnifyAPI for the given (or default) environment. |
| `unify_jobs_debug.operations._fetch_and_format_activity_logs` | `def _fetch_and_format_activity_logs(api, job_id: int, activity_id: str, instance_id: int, page_size: int, page: int, load_all: bool) -> str` |  |
| `unify_jobs_debug.operations._resolve_output_dest` | `def _resolve_output_dest(api, job_id: int, output_id: int, dest_path: str) -> str` |  |
| `unify_jobs_debug.operations.api_config` | `def api_config(url: str='', no_verify_ssl: bool=False, verify_ssl: bool=False, auth_type: str='', username: str='') -> str` | Set or display the Unify API base URL used by all job tools. |
| `unify_jobs_debug.operations.get_job` | `def get_job(job_id: int, env: str='') -> str` | Get detailed information about a specific Unify job. |
| `unify_jobs_debug.operations.get_active_jobs` | `def get_active_jobs(env: str='') -> str` | Get all currently running jobs on the Unify server. |
| `unify_jobs_debug.operations.list_jobs` | `def list_jobs(my_jobs: bool=False, running_only: bool=False, env: str='') -> str` | List recent Unify jobs. |
| `unify_jobs_debug.operations.get_activity_status` | `def get_activity_status(job_id: int, flat: bool=False, max_depth: int | None=None, env: str='') -> str` | Get the status of all activities in a job (tree by default, flat optional). |
| `unify_jobs_debug.operations.get_log_headers` | `def get_log_headers(job_id: int, env: str='') -> str` | Get a summary of activity logs for a job. |
| `unify_jobs_debug.operations.get_activity_logs` | `def get_activity_logs(job_id: int, activity_id: str, instance_id: int=0, page: int=0, page_size: int=50, load_all: bool=False, env: str='') -> str` | Get detailed log entries for a specific activity within a job. |
| `unify_jobs_debug.operations.get_log_errors` | `def get_log_errors(job_id: int, env: str='') -> str` | Get all error and warning log entries across the entire job. |
| `unify_jobs_debug.operations.get_recent_logs` | `def get_recent_logs(job_id: int, count: int=20, env: str='') -> str` | Get the N most recent log entries for a job. |
| `unify_jobs_debug.operations.download_logs` | `def download_logs(job_id: int, dest_path: str='', env: str='') -> str` | Download the full activity log file for a job. |
| `unify_jobs_debug.operations.get_activity_durations` | `def get_activity_durations(job_id: int, env: str='') -> str` | Get a timing breakdown of a job's activities. |
| `unify_jobs_debug.operations.get_job_outputs` | `def get_job_outputs(job_id: int, env: str='') -> str` | Get the output files produced by a job, grouped by activity. |
| `unify_jobs_debug.operations.get_job_inputs` | `def get_job_inputs(job_id: int, env: str='') -> str` | Get the input arguments that were passed to a job. |
| `unify_jobs_debug.operations.download_job_output` | `def download_job_output(job_id: int, output_id: int, dest_path: str='', env: str='') -> str` | Download a specific output file from a job. |
| `unify_jobs_debug.operations.get_job_hierarchy` | `def get_job_hierarchy(job_id: int, env: str='') -> str` | Get the parent/child job hierarchy for jobs that spawn sub-workflows. |
| `unify_jobs_debug.operations.get_job_velocity` | `def get_job_velocity(job_id: int, env: str='') -> str` | Get velocity/milestone information for a running or completed job. |
| `unify_jobs_debug.operations.get_job_validation` | `def get_job_validation(job_id: int, env: str='') -> str` | Get pre-run validation results for a job. |
| `unify_jobs_debug.operations.get_referenced_object` | `def get_referenced_object(job_id: int, activity_id: str, activity_instance_id: int=0, env: str='') -> str` | Get the dataset/object referenced by a specific activity in a job. |
| `unify_jobs_debug.operations.identify_workflow` | `def identify_workflow(job_id: int, env: str='') -> str` | Identify the workflow + version that produced a job (no download). |
| `unify_jobs_debug.operations.download_job_workflow` | `def download_job_workflow(job_id: int, output_dir: str='', env: str='') -> str` | Download the workflow XAML that produced a job to local disk. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

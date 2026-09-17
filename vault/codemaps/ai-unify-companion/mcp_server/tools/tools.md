# `mcp_server/tools/tools.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `json` (external)
- [mcp_server._api](../_api.md)
- [mcp_server._deploy](../_deploy.md)
- [mcp_server.constants](../constants.md)
- `os` (external)
- `pathlib` (external)
- `typing` (external)
- [unify_api](../../unify_api/__init__.md)
- [unify_api.auth](../../unify_api/auth.md)
- [unify_api.connect](../../unify_api/connect.md)
- [unify_api.constants](../../unify_api/constants.md)
- [unify_jobs_debug.jobs](../../unify_jobs_debug/jobs.md)
- [unify_jobs_debug.log_files](../../unify_jobs_debug/log_files.md)
- [unify_jobs_debug.triage](../../unify_jobs_debug/triage.md)
- [workflow_reader.inspect](../../workflow_reader/inspect.md)
- [workflow_reader.loader](../../workflow_reader/loader.md)
- [workflow_reader.tree_helpers](../../workflow_reader/tree_helpers.md)

## Imported by (INFERRED)

- [mcp_server.server](../server.md)
- [mcp_server.tools](__init__.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `mcp_server.tools.tools.clarify_arguments` | `def clarify_arguments(status: str, tool: str, *, missing: list[str] | None=None, candidates: list[dict] | None=None, schema: dict | None=None, hint: str | None=None, confirm_message: str | None=None) -> dict[str, Any]` | Build a structured clarification payload for tool follow-up. |
| `mcp_server.tools.tools.search` | `def search(query: str, kind: str | None=None, env: str='') -> str` | Search Unify for objects matching a name, with an optional kind filter. |
| `mcp_server.tools.tools.list_folder` | `def list_folder(folder_id: int, kind: str | None=None, recursive: bool=True, max_depth: int=3, env: str='') -> str` | List the contents of a Unify folder. |
| `mcp_server.tools.tools.inspect_object` | `def inspect_object(object_id: int, object_type: int, file_name: str, env: str='') -> str` | Return metadata for a known Unify object (workflow or dataset). |
| `mcp_server.tools.tools._resolve_workflow` | `def _resolve_workflow(api, workflow_id: int | None, name: str) -> tuple[int | None, str | None]` | Resolve workflow_id from name if not provided. Returns (id, error_json) or (id, None). |
| `mcp_server.tools.tools._get_required_args` | `def _get_required_args(api, workflow_id: int, args: dict) -> tuple[list[str], dict]` | Return (missing_arg_names, schema) for required args not present in args. |
| `mcp_server.tools.tools.run_job` | `def run_job(workflow_id: int | None=None, name: str='', args: dict | None=None, files: dict | None=None, env: str='') -> str` | Submit a new job for a workflow. |
| `mcp_server.tools.tools.rerun_job` | `def rerun_job(job_id: int, override_args: dict | None=None, env: str='') -> str` | Rerun a job, optionally with edited arguments. |
| `mcp_server.tools.tools.cancel_job` | `def cancel_job(job_id: int, confirm: bool=True, env: str='') -> str` | Cancel a running job. |
| `mcp_server.tools.tools.find_jobs` | `def find_jobs(scope: str='recent', workflow_id: int | None=None, status: str='', since: str='', env: str='') -> str` | List Unify jobs. |
| `mcp_server.tools.tools.search_jobs` | `def search_jobs(file_name: str, status: str='', text_search: str='', only_my_jobs: bool=False, topmost_only: bool=False, min_duration_minutes: float | None=None, max_age_hours: float | None=None, max_results: int=20, order_by: str='CompletedAt', sort_descending: bool=True, env: str='') -> str` | Search Unify jobs with pagination and post-filtering. |
| `mcp_server.tools.tools.get_job_outputs` | `def get_job_outputs(job_id: int, download_to: str | None=None, env: str='') -> str` | List job outputs, downloading all files to a local directory. |
| `mcp_server.tools.tools.download_job_logs` | `def download_job_logs(job_id: int, parent_job_id: int=0, env: str='') -> str` | Download the full activity log file for a job to the local downloads folder. |
| `mcp_server.tools.tools.scan_log` | `def scan_log(path: str, env: str='') -> str` | Summarise a downloaded Unify job log file. |
| `mcp_server.tools.tools.read_log_window` | `def read_log_window(path: str, start_line: int, end_line: int, context_before: int=0, context_after: int=0, env: str='') -> str` | Read a line range from a downloaded Unify job log file. |
| `mcp_server.tools.tools.get_job_inputs` | `def get_job_inputs(job_id: int, env: str='') -> str` | Return the input arguments for a job, downloading any blob (file) inputs |
| `mcp_server.tools.tools.get_referenced_object` | `def get_referenced_object(job_id: int, activity_id: str, activity_instance_id: int=0, env: str='') -> str` | Look up the object (dataset, model, workflow) referenced by an activity. |
| `mcp_server.tools.tools.get_activity_tree` | `def get_activity_tree(job_id: int, env: str='') -> str` | Fetch the full structured activity status tree for a job and save to temp. |
| `mcp_server.tools.tools.get_restart_points` | `def get_restart_points(job_id: int, env: str='') -> str` | List the restart points available for a job. |
| `mcp_server.tools.tools.restart_job` | `def restart_job(job_id: int, restart_point_id: int, confirm: bool=True, env: str='') -> str` | Restart a job from a specific restart point. |
| `mcp_server.tools.tools.connect` | `def connect(env: str='', interactive: bool=True) -> str` | Connect to a Unify environment and verify the connection. |
| `mcp_server.tools.tools.list_envs` | `def list_envs() -> str` | List all configured Unify environments. |
| `mcp_server.tools.tools.add_env` | `def add_env(name: str, url: str, auth_type: str='', username: str='', verify_ssl: bool | None=None, set_default: bool=False) -> str` | Add or update a named Unify environment. |
| `mcp_server.tools.tools.set_default_env` | `def set_default_env(name: str) -> str` | Set the default Unify environment. |
| `mcp_server.tools.tools.health` | `def health(env: str='') -> str` | Get Unify server health, job counts, and active environment summary. |
| `mcp_server.tools.tools.get_dataset_file` | `def get_dataset_file(dataset_id: int, file_name: str='', version_id: int | None=None, latest: bool=True, local_file_name: str='', env: str='') -> str` | Download a file from a dataset version. |
| `mcp_server.tools.tools.upload_dataset_version` | `def upload_dataset_version(dataset_id: int, changes: list, version_comment: str, env: str='') -> str` | Upload a new version to a dataset. |
| `mcp_server.tools.tools.create_folder` | `def create_folder(name: str, parent_id: int, env: str='') -> str` | Create a new folder inside an existing Unify folder. |
| `mcp_server.tools.tools.update_dataset_as_at` | `def update_dataset_as_at(dataset_id: int, as_at: bool, env: str='') -> str` | Set the AsAtProcessing flag on a dataset. |
| `mcp_server.tools.tools.validate_workflow_version` | `def validate_workflow_version(workflow_id: int, version_id: int, env: str='') -> str` | Check whether a workflow version opens correctly in the Unify designer. |
| `mcp_server.tools.tools.inspect_workflow_activity` | `def inspect_workflow_activity(xaml_path: str, activity_uid: str='', structural_path: str='') -> str` | Inspect a single activity in a downloaded XAML file by UID or structural path. |
| `mcp_server.tools.tools.restore_instructions` | `def restore_instructions() -> str` | Force-overwrite all managed .github/ instruction files with the bundled versions. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `unify_api/jobs.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [unify_api.protocol](protocol.md)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)
- [unify_api.core](core.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.jobs._coerce_arg_value` | `def _coerce_arg_value(value, type_full_name: str | None)` | Coerce a job argument value to the JSON type implied by its CLR type. |
| `unify_api.jobs._parse_submitted_job_id` | `def _parse_submitted_job_id(r) -> int | None` | Parse the new job id from a submit/resubmit response. |
| `unify_api.jobs.JobsMixin` | `class JobsMixin` |  |
| `unify_api.jobs.JobsMixin.get_job` | `def get_job(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_active_jobs` | `def get_active_jobs(self) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_recent_jobs` | `def get_recent_jobs(self, my_jobs: bool=False, running_jobs: bool=False, topmost_jobs: bool=True) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_job_activity_status` | `def get_job_activity_status(self, job_id: int) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_job_structured_activity_status` | `def get_job_structured_activity_status(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_log_headers` | `def get_log_headers(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_activity_log_entries` | `def get_activity_log_entries(self, job_id: int, activity_id: str, activity_instance_id: int=0, page_length: int=100, current_page: int=0, load_all: bool=False) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_log_errors` | `def get_log_errors(self, job_id: int, activity_name: str | None=None, activity_types: list[str] | None=None) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_recent_log_entries` | `def get_recent_log_entries(self, job_id: int, count: int=20, activity_name: str | None=None, activity_types: list[str] | None=None) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.download_job_logs` | `def download_job_logs(self, job_id: int) -> bytes` |  |
| `unify_api.jobs.JobsMixin.get_activity_durations` | `def get_activity_durations(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_job_outputs` | `def get_job_outputs(self, job_id: int) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_job_structured_outputs` | `def get_job_structured_outputs(self, job_id: int) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_job_inputs` | `def get_job_inputs(self, job_id: int) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.get_job_out_arguments` | `def get_job_out_arguments(self, job_id: int) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.download_job_output` | `def download_job_output(self, job_id: int, output_id: int) -> bytes` |  |
| `unify_api.jobs.JobsMixin.download_argument_blob` | `def download_argument_blob(self, job_id: int, blob_id: int) -> bytes` |  |
| `unify_api.jobs.JobsMixin.get_restart_points` | `def get_restart_points(self, job_id: int) -> list[dict]` |  |
| `unify_api.jobs.JobsMixin.cancel_job` | `def cancel_job(self, job_id: int) -> None` |  |
| `unify_api.jobs.JobsMixin.restart_job` | `def restart_job(self, job_id: int, instance_record_id: int) -> int` |  |
| `unify_api.jobs.JobsMixin.resubmit_job` | `def resubmit_job(self, job_id: int) -> int | None` | Clone and rerun a job verbatim (POST /api/job/{id}/resubmit). |
| `unify_api.jobs.JobsMixin.build_job_definition` | `def build_job_definition(self, workflow_id: int, version_id: int, *, job_name: str | None=None, arguments: dict | None=None, base_inputs: list[dict] | None=None, base_job: dict | None=None) -> dict` | Assemble a JobDefinition body for POST /api/job/submit. |
| `unify_api.jobs.JobsMixin.submit_job_definition` | `def submit_job_definition(self, job_definition: dict) -> int | None` | Submit a job from a full JobDefinition (POST /api/job). |
| `unify_api.jobs.JobsMixin.resubmit_job_with_args` | `def resubmit_job_with_args(self, job_id: int, arguments: dict, job_name: str | None=None) -> int | None` | Rerun a job with edited arguments via POST /api/job/submit. |
| `unify_api.jobs.JobsMixin.get_job_hierarchy` | `def get_job_hierarchy(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_job_velocity` | `def get_job_velocity(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_job_validation` | `def get_job_validation(self, job_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_referenced_object` | `def get_referenced_object(self, job_id: int, activity_id: str, activity_instance_id: int) -> dict` |  |
| `unify_api.jobs.JobsMixin.submit_job` | `def submit_job(self, workflow_id: int) -> int` |  |
| `unify_api.jobs.JobsMixin.get_job_list` | `def get_job_list(self, payload: dict) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_job_count` | `def get_job_count(self) -> dict` |  |
| `unify_api.jobs.JobsMixin.get_full_health` | `def get_full_health(self) -> dict` |  |
| `unify_api.jobs.JobsMixin.validate_workflow_version` | `def validate_workflow_version(self, workflow_id: int, version_id: int) -> dict` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

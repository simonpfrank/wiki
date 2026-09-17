# `unify_api/datasets.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `json` (external)
- `logging` (external)
- [mcp_server.constants](../mcp_server/constants.md)
- `os` (external)
- [unify_api.protocol](protocol.md)
- [workflow_reader.upload](../workflow_reader/upload.md)

## Imported by (INFERRED)

- [unify_api.core](core.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.datasets.DatasetVersionMixin` | `class DatasetVersionMixin` |  |
| `unify_api.datasets.DatasetVersionMixin.list_datasets` | `def list_datasets(self, parent_id: int | None=None) -> list[dict]` |  |
| `unify_api.datasets.DatasetVersionMixin.get_dataset` | `def get_dataset(self, dataset_id: int) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.get_dataset_details` | `def get_dataset_details(self, dataset_id: int) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.update_dataset_as_at` | `def update_dataset_as_at(self, dataset_id: int, as_at: bool) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.list_versions` | `def list_versions(self, parent_id: int) -> list[dict]` |  |
| `unify_api.datasets.DatasetVersionMixin.get_latest_version` | `def get_latest_version(self, parent_id: int) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.get_version` | `def get_version(self, version_id: int) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.get_version_details` | `def get_version_details(self, version_id: int) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.get_version_by_number` | `def get_version_by_number(self, parent_id: int, version_number: int) -> dict | None` |  |
| `unify_api.datasets.DatasetVersionMixin.list_versions_by_parent` | `def list_versions_by_parent(self, object_id: int) -> list[dict]` |  |
| `unify_api.datasets.DatasetVersionMixin.list_recent_versions_by_parent` | `def list_recent_versions_by_parent(self, object_id: int, count: int=10) -> list[dict]` |  |
| `unify_api.datasets.DatasetVersionMixin.download_version_blob` | `def download_version_blob(self, version_id: int, blob_id: int, output_path: str) -> str` |  |
| `unify_api.datasets.DatasetVersionMixin.upload_version` | `def upload_version(self, object_id: int, file_uploads: list[dict], file_paths: list[str | None] | None=None, attributes: list[dict] | None=None, version_name: str | None=None, version_comment: str | None=None) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.ping` | `def ping(self) -> bool` |  |
| `unify_api.datasets.DatasetVersionMixin.resolve_dataset` | `def resolve_dataset(self, name_or_id: str | int) -> dict` |  |
| `unify_api.datasets.DatasetVersionMixin.get_dataset_file_list` | `def get_dataset_file_list(self, dataset_id: int, version_number: int | None=None) -> list[str]` |  |
| `unify_api.datasets.DatasetVersionMixin.download_blob` | `def download_blob(self, _object_id: int, version_id: int, file_name: str) -> bytes` | Download a named blob from a version and return its raw bytes. |
| `unify_api.datasets.DatasetVersionMixin.resolve_latest_version_id` | `def resolve_latest_version_id(self, object_id: int) -> int` | Return the ID of the most recent version for an object. |
| `unify_api.datasets.DatasetVersionMixin.download_dataset_file` | `def download_dataset_file(self, dataset_id: int, file_name: str, version_id: int | None=None) -> tuple[bytes, int]` | Resolve version (latest if not given) and download a file by name. |
| `unify_api.datasets.DatasetVersionMixin.get_dataset_file_result` | `def get_dataset_file_result(self, dataset_id: int, file_name: str, version_id: int | None=None, latest: bool=True, save_to: str='') -> dict` | Download a dataset file and return a result dict ready for JSON serialisation. |
| `unify_api.datasets.DatasetVersionMixin.list_versions_with_ambiguity` | `def list_versions_with_ambiguity(self, dataset_id: int) -> list[dict]` | Return all versions for a dataset (used to detect ambiguity in tools). |
| `unify_api.datasets.DatasetVersionMixin.upload_dataset_version_from_changes` | `def upload_dataset_version_from_changes(self, dataset_id: int, changes: list[dict], version_comment: str | None=None) -> tuple[object, int]` | Build a file list from change dicts and upload a new dataset version. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

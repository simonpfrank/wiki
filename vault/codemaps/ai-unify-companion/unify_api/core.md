# `unify_api/core.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `logging` (external)
- `requests` (external)
- `typing` (external)
- [unify_api.activity_details](activity_details.md)
- [unify_api.auth](auth.md)
- [unify_api.datasets](datasets.md)
- [unify_api.explore](explore.md)
- [unify_api.jobs](jobs.md)
- [unify_api.models](models.md)
- [unify_api.workflows](workflows.md)
- `urllib3` (external)

## Imported by (INFERRED)

- [unify_jobs_debug.jobs](../unify_jobs_debug/jobs.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.core.UnifyAPI` | `class UnifyAPI` |  |
| `unify_api.core.UnifyAPI.__init__` | `def __init__(self, base_url: str, verify_ssl: bool=True)` |  |
| `unify_api.core.UnifyAPI._get` | `def _get(self, path: str, **kwargs) -> Any` |  |
| `unify_api.core.UnifyAPI._post` | `def _post(self, path: str, data: Any=None, **kwargs) -> Any` |  |
| `unify_api.core.UnifyAPI._put` | `def _put(self, path: str, data: Any=None, **kwargs) -> Any` |  |
| `unify_api.core.UnifyAPI.search` | `def search(self, query: str, page_length: int=50, page: int=0) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.search_datasets` | `def search_datasets(self, name: str) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.search_workflows` | `def search_workflows(self, name: str) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.search_models` | `def search_models(self, term: str) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.get_root_folder` | `def get_root_folder(self) -> dict` |  |
| `unify_api.core.UnifyAPI.get_root_folder_id` | `def get_root_folder_id(self) -> int` |  |
| `unify_api.core.UnifyAPI.get_child_folders` | `def get_child_folders(self, parent_id: int | None=None) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.get_folder_children` | `def get_folder_children(self, folder_id: int) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.get_folder_contents` | `def get_folder_contents(self, folder_id: int) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.get_folder` | `def get_folder(self, folder_id: int) -> dict` |  |
| `unify_api.core.UnifyAPI.find_datasets_in_folder` | `def find_datasets_in_folder(self, folder_id: int) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.find_workflows_in_folder` | `def find_workflows_in_folder(self, folder_id: int) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.list_attributes` | `def list_attributes(self) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.get_attributes_for_object` | `def get_attributes_for_object(self, object_id: int) -> list[dict]` |  |
| `unify_api.core.UnifyAPI.get_object_attribute_detail` | `def get_object_attribute_detail(self, object_id: int) -> dict` |  |
| `unify_api.core.UnifyAPISaaS` | `class UnifyAPISaaS` |  |
| `unify_api.core.UnifyAPISaaS.__init__` | `def __init__(self, base_url: str, env_name: str, username: str='', verify_ssl: bool=True, interactive: bool=True)` |  |
| `unify_api.core.UnifyAPISaaS._get` | `def _get(self, path: str, **kwargs) -> Any` |  |
| `unify_api.core.UnifyAPISaaS._post` | `def _post(self, path: str, data: Any=None, **kwargs) -> Any` |  |
| `unify_api.core.UnifyAPISaaS._apply_token` | `def _apply_token(self) -> None` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

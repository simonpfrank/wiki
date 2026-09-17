# `unify_api/protocol.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `requests` (external)
- `typing` (external)

## Imported by (INFERRED)

- [unify_api.activity_details](activity_details.md)
- [unify_api.datasets](datasets.md)
- [unify_api.explore](explore.md)
- [unify_api.jobs](jobs.md)
- [unify_api.models](models.md)
- [unify_api.workflows](workflows.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.protocol.UnifyAPIProtocol` | `class UnifyAPIProtocol` | Protocol declaring the UnifyAPI methods that mixins depend on. |
| `unify_api.protocol.UnifyAPIProtocol._get` | `def _get(self, path: str, **kwargs: Any) -> Any` |  |
| `unify_api.protocol.UnifyAPIProtocol._post` | `def _post(self, path: str, data: Any=None, **kwargs: Any) -> Any` |  |
| `unify_api.protocol.UnifyAPIProtocol._put` | `def _put(self, path: str, data: Any=None, **kwargs: Any) -> Any` |  |
| `unify_api.protocol.UnifyAPIProtocol.search` | `def search(self, query: str) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.search_datasets` | `def search_datasets(self, name: str) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.search_workflows` | `def search_workflows(self, name: str) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_dataset` | `def get_dataset(self, dataset_id: int) -> dict` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_dataset_details` | `def get_dataset_details(self, dataset_id: int) -> dict` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_dataset_file_list` | `def get_dataset_file_list(self, dataset_id: int, version_number: int | None=None) -> list[str]` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_workflow` | `def get_workflow(self, workflow_id: int) -> dict` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_workflow_details` | `def get_workflow_details(self, workflow_id: int) -> dict` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_workflow_arguments` | `def get_workflow_arguments(self, workflow_id: int, version_id: int) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_attributes_for_object` | `def get_attributes_for_object(self, object_id: int) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_object_attribute_detail` | `def get_object_attribute_detail(self, object_id: int) -> dict` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_root_folder_id` | `def get_root_folder_id(self) -> int` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_folder_children` | `def get_folder_children(self, folder_id: int) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.get_folder_contents` | `def get_folder_contents(self, folder_id: int) -> list[dict]` |  |
| `unify_api.protocol.UnifyAPIProtocol.list_versions` | `def list_versions(self, parent_id: int) -> list[dict]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

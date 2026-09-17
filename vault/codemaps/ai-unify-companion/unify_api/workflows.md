# `unify_api/workflows.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [unify_api.protocol](protocol.md)

## Imported by (INFERRED)

- [unify_api.core](core.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.workflows.WorkflowMixin` | `class WorkflowMixin` |  |
| `unify_api.workflows.WorkflowMixin.list_workflows` | `def list_workflows(self, parent_id: int | None=None) -> list[dict]` |  |
| `unify_api.workflows.WorkflowMixin.get_workflow` | `def get_workflow(self, workflow_id: int) -> dict` |  |
| `unify_api.workflows.WorkflowMixin.get_workflow_details` | `def get_workflow_details(self, workflow_id: int) -> dict` |  |
| `unify_api.workflows.WorkflowMixin.get_workflow_arguments` | `def get_workflow_arguments(self, workflow_id: int, version_id: int) -> list[dict]` |  |
| `unify_api.workflows.WorkflowMixin.resolve_workflow` | `def resolve_workflow(self, name_or_id: str | int) -> dict` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

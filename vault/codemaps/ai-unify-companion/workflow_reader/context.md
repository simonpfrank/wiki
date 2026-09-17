# `workflow_reader/context.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `re` (external)
- `typing` (external)
- [unify_api](../unify_api/__init__.md)
- `uuid` (external)

## Imported by (INFERRED)

- [activities.control_flow](../activities/control_flow.md)
- [workflow_reader.loader](loader.md)
- [workflow_reader.reader](reader.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `workflow_reader.context.generate_uid` | `def generate_uid() -> str` |  |
| `workflow_reader.context._extract_prefixes` | `def _extract_prefixes(xaml_type: str) -> set[str]` |  |
| `workflow_reader.context._resolve_xaml_type` | `def _resolve_xaml_type(type_input: str) -> tuple[str, str | None]` |  |
| `workflow_reader.context.WorkflowArgument` | `class WorkflowArgument` | An InArgument declared on the workflow root. |
| `workflow_reader.context.WorkflowArgument.__init__` | `def __init__(self, name: str, type_name: str, default: str | None=None)` |  |
| `workflow_reader.context.WorkflowArgument.from_raw_xaml` | `def from_raw_xaml(cls, name: str, xaml_type: str, default: str | None=None) -> 'WorkflowArgument'` |  |
| `workflow_reader.context.WorkflowVariable` | `class WorkflowVariable` | A Variable scoped to a specific node in the tree. |
| `workflow_reader.context.WorkflowVariable.__init__` | `def __init__(self, name: str, type_name: str, owner: 'ActivityNode | None'=None, default: str | None=None)` |  |
| `workflow_reader.context.WorkflowVariable.from_raw_xaml` | `def from_raw_xaml(cls, name: str, xaml_type: str, owner: 'ActivityNode | None'=None, default: str | None=None) -> 'WorkflowVariable'` |  |
| `workflow_reader.context.WorkflowContext` | `class WorkflowContext` | Tracks global state for a single workflow (IDs, variables, arguments, API). |
| `workflow_reader.context.WorkflowContext.__init__` | `def __init__(self, api: 'UnifyAPI | None'=None)` |  |
| `workflow_reader.context.WorkflowContext.new_uid` | `def new_uid(self) -> str` |  |
| `workflow_reader.context.WorkflowContext.add_argument` | `def add_argument(self, name: str, type_name: str, default: str | None=None) -> WorkflowArgument` |  |
| `workflow_reader.context.WorkflowContext.add_argument_raw` | `def add_argument_raw(self, name: str, xaml_type: str, default: str | None=None) -> WorkflowArgument` |  |
| `workflow_reader.context.WorkflowContext._register_type_prefixes` | `def _register_type_prefixes(self, xaml_type: str) -> None` |  |
| `workflow_reader.context.WorkflowContext.add_variable` | `def add_variable(self, name: str, type_name: str, scope: str | None=None, scope_node: 'ActivityNode | None'=None, default: str | None=None) -> WorkflowVariable` |  |
| `workflow_reader.context.WorkflowContext.add_variable_raw` | `def add_variable_raw(self, name: str, xaml_type: str, scope: str | None=None, scope_node: 'ActivityNode | None'=None, default: str | None=None) -> WorkflowVariable` |  |
| `workflow_reader.context.WorkflowContext._scope_name_to_node` | `def _scope_name_to_node(self, scope: str | None) -> 'ActivityNode | None'` |  |
| `workflow_reader.context.WorkflowContext.resolve_variable` | `def resolve_variable(self, name: str, from_node: 'ActivityNode | None'=None) -> WorkflowVariable` |  |
| `workflow_reader.context.WorkflowContext.all_variables` | `def all_variables(self) -> list[WorkflowVariable]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

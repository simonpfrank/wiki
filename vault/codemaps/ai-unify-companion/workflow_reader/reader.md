# `workflow_reader/reader.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities](../activities/__init__.md)
- [activities.control_flow](../activities/control_flow.md)
- [activities.workflow_execution](../activities/workflow_execution.md)
- [workflow_reader.context](context.md)

## Imported by (INFERRED)

- [workflow_reader.loader](loader.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `workflow_reader.reader.WorkflowReader` | `class WorkflowReader` |  |
| `workflow_reader.reader.WorkflowReader.__init__` | `def __init__(self, *, context: WorkflowContext, flow_steps: list[tuple[str, UnifySequenceNode]], xaml_text: str, path: str)` |  |
| `workflow_reader.reader.WorkflowReader.arguments` | `def arguments(self)` |  |
| `workflow_reader.reader.WorkflowReader.variables` | `def variables(self)` |  |
| `workflow_reader.reader.WorkflowReader.sequences` | `def sequences(self) -> list[UnifySequenceNode]` |  |
| `workflow_reader.reader.WorkflowReader.xaml_text` | `def xaml_text(self) -> str` |  |
| `workflow_reader.reader.WorkflowReader.path` | `def path(self) -> str` |  |
| `workflow_reader.reader._iter_node` | `def _iter_node(node)` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

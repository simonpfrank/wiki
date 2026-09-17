# `workflow_reader/inspect.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities](../activities/__init__.md)
- [activities.control_flow](../activities/control_flow.md)
- [activities.workflow_execution](../activities/workflow_execution.md)
- `typing` (external)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `workflow_reader.inspect._type_name` | `def _type_name(node: ActivityNode) -> str` |  |
| `workflow_reader.inspect._iter_with_paths` | `def _iter_with_paths(reader)` | Yield (path, node) for every node in the reader via traversal. |
| `workflow_reader.inspect._iter_node_with_paths` | `def _iter_node_with_paths(node, path: str)` |  |
| `workflow_reader.inspect._node_summary` | `def _node_summary(node: ActivityNode, path: str) -> dict` |  |
| `workflow_reader.inspect._advance_segment` | `def _advance_segment(node: ActivityNode, segments: list[str], i: int) -> tuple[ActivityNode, int]` | Advance one or two path segments from position i, returning (new_node, new_i). |
| `workflow_reader.inspect.activity_at` | `def activity_at(reader, path: str) -> ActivityNode` | Return the node at the given structural path. |
| `workflow_reader.inspect.find_by_activity_id` | `def find_by_activity_id(reader, activity_id: str) -> ActivityNode | None` | Find a node by its UniqueId attribute. Returns None if not found. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `activities/control_flow.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities._helpers](_helpers.md)
- [activities.base](base.md)
- [activities.basic](basic.md)
- [workflow_reader.activity_map](../workflow_reader/activity_map.md)
- [workflow_reader.context](../workflow_reader/context.md)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [activities.control_flow_try](control_flow_try.md)
- [activities.workflow_execution](workflow_execution.md)
- [workflow_reader.activity_map](../workflow_reader/activity_map.md)
- [workflow_reader.inspect](../workflow_reader/inspect.md)
- [workflow_reader.reader](../workflow_reader/reader.md)
- [workflow_reader.traversal](../workflow_reader/traversal.md)
- [workflow_reader.tree_helpers](../workflow_reader/tree_helpers.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.control_flow._rename_in_branch` | `def _rename_in_branch(seq, old_name: str, new_name: str) -> None` | Rename within a branch sequence and all its children. |
| `activities.control_flow._parse_sequence_branch` | `def _parse_sequence_branch(elem: ET.Element, context)` | Parse a single element inside an If.Then or If.Else container. |
| `activities.control_flow.IfNode` | `class IfNode` | If — the standard WPF conditional activity. |
| `activities.control_flow.IfNode.__init__` | `def __init__(self, context, display_name: str='If', condition: str='', then_branch=None, else_branch=None)` |  |
| `activities.control_flow.IfNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'IfNode'` |  |
| `activities.control_flow.IfNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.control_flow.ForEachNode` | `class ForEachNode` | ForEach<T> — the standard WPF ForEach activity. |
| `activities.control_flow.ForEachNode.__init__` | `def __init__(self, context, display_name: str='ForEach', item_type: str='x:String', values_expression: str='', item_name: str='item', body=None)` |  |
| `activities.control_flow.ForEachNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ForEachNode'` |  |
| `activities.control_flow.ForEachNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.control_flow.WhileNode` | `class WhileNode` | While — standard WPF while-loop activity. |
| `activities.control_flow.WhileNode.__init__` | `def __init__(self, context, display_name: str='While', condition: str='', body=None)` |  |
| `activities.control_flow.WhileNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'WhileNode'` |  |
| `activities.control_flow.WhileNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.control_flow.DoWhileNode` | `class DoWhileNode` | DoWhile — standard WPF do-while-loop activity. |
| `activities.control_flow.DoWhileNode.__init__` | `def __init__(self, context, display_name: str='DoWhile', condition: str='', body=None)` |  |
| `activities.control_flow.DoWhileNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'DoWhileNode'` |  |
| `activities.control_flow.DoWhileNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.control_flow.UnifyParallelNode` | `class UnifyParallelNode` | A UnifyParallel activity with N concurrently-executed branches. |
| `activities.control_flow.UnifyParallelNode.__init__` | `def __init__(self, display_name: str, branches: list | None=None)` |  |
| `activities.control_flow.UnifyParallelNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'UnifyParallelNode'` |  |
| `activities.control_flow.UnifyParallelNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

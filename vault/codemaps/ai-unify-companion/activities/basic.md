# `activities/basic.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.parameters](parameters.md)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [activities.control_flow](control_flow.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.basic.UnifySequenceNode` | `class UnifySequenceNode` | tuwaa:UnifySequence — the standard group/container activity. |
| `activities.basic.UnifySequenceNode.__init__` | `def __init__(self, context, display_name: str)` |  |
| `activities.basic.UnifySequenceNode.add` | `def add(self, node: ActivityNode) -> 'UnifySequenceNode'` | Add a child activity. Returns self for chaining. |
| `activities.basic.UnifySequenceNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.basic.UnifySequenceNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'UnifySequenceNode'` |  |
| `activities.basic.LogMessageNode` | `class LogMessageNode` | tuwaa:LogMessage — writes a message to the workflow log. |
| `activities.basic.LogMessageNode.__init__` | `def __init__(self, context, display_name: str, message: str, log_level: str='Info', audit_message: bool=False, active_working_directory: str='{x:Null}', from_sequence: str | None=None)` |  |
| `activities.basic.LogMessageNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'LogMessageNode'` |  |
| `activities.basic.LogMessageNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.basic.AssignNode` | `class AssignNode` | Assign — sets a variable to an expression. |
| `activities.basic.AssignNode.__init__` | `def __init__(self, context, display_name: str='Assign', variable_name: str='', expression: str='', from_sequence: str | None=None)` |  |
| `activities.basic.AssignNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'AssignNode'` |  |
| `activities.basic.AssignNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

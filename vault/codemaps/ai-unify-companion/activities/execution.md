# `activities/execution.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.parameters](parameters.md)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [workflow_reader.tree_helpers](../workflow_reader/tree_helpers.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.execution.ExpectedOutput` | `class ExpectedOutput` | Describes a named file output that an ExecuteCommand activity is expected |
| `activities.execution.ExpectedOutput.__init__` | `def __init__(self, name: str, file_name: str)` |  |
| `activities.execution.ExecuteCommandNode` | `class ExecuteCommandNode` | tuwaa:ExecuteCommand — runs an OS command or executable. |
| `activities.execution.ExecuteCommandNode.__init__` | `def __init__(self, context, display_name: str='Execute Command', command: str='', arguments: str='', activity_working_directory: str='{x:Null}', working_directory: str='{x:Null}', abort_on_nonzero: bool=False, retry_attempts: int=3, retry_on_failure: bool=False, expected_outputs: list['ExpectedOutput'] | None=None, from_sequence: str | None=None)` |  |
| `activities.execution.ExecuteCommandNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ExecuteCommandNode'` |  |
| `activities.execution.ExecuteCommandNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.execution.AssignValueNode` | `class AssignValueNode` | tuwaa:AssignValue — binds a named output from a previous ExecuteCommand |
| `activities.execution.AssignValueNode.__init__` | `def __init__(self, context, display_name: str='Assign', producer: 'ExecuteCommandNode | None'=None, output_name: str='', variable_name: str='', xaml_type: str='x:String', activity_working_directory: str='{x:Null}', retry_attempts: int=0, retry_on_failure: bool=False, from_sequence: str | None=None)` |  |
| `activities.execution.AssignValueNode._producer_uid` | `def _producer_uid(self) -> str` |  |
| `activities.execution.AssignValueNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'AssignValueNode'` |  |
| `activities.execution.AssignValueNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

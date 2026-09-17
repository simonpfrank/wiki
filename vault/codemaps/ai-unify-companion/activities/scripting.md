# `activities/scripting.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.parameters](parameters.md)
- `re` (external)
- `xml.etree.ElementTree` (external)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.scripting.ActivityParameter` | `class ActivityParameter` | Describes one parameter (argument) of a PowerShell or Python script. |
| `activities.scripting.ActivityParameter.__init__` | `def __init__(self, name: str, param_type: str='x:String', is_required: bool=True, value: ParameterValue | None=None)` |  |
| `activities.scripting.ActivityParameter.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.scripting.ActivityParameter.from_element` | `def from_element(cls, elem: ET.Element) -> 'ActivityParameter'` |  |
| `activities.scripting.ExecutePowershellNode` | `class ExecutePowershellNode` | tuwaa:ExecutePowershell — runs a PowerShell script from a Unify dataset. |
| `activities.scripting.ExecutePowershellNode.__init__` | `def __init__(self, context, display_name: str='Execute PowerShell', dataset_id: int=0, script_file_name: str='', user_properties: list[ActivityParameter] | None=None, activity_working_directory: str | None=None, is_x64: bool=True, run_on_gateway: bool=False, version_type: str='Latest', version_id: str='0', retry_attempts: int=3, retry_on_failure: bool=False)` |  |
| `activities.scripting.ExecutePowershellNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ExecutePowershellNode'` |  |
| `activities.scripting.ExecutePowershellNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

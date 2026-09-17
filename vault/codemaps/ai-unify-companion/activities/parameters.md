# `activities/parameters.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `re` (external)
- `typing` (external)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [activities.basic](basic.md)
- [activities.dataset](dataset.md)
- [activities.execute_model](execute_model.md)
- [activities.execution](execution.md)
- [activities.scripting](scripting.md)
- [activities.workflow_execution](workflow_execution.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.parameters.ParameterValue` | `class ParameterValue` | Base for all parameter value types that appear inside TextParameter.Value. |
| `activities.parameters.ParameterValue.__init__` | `def __init__(self, name: str, xaml_type: str='x:String')` |  |
| `activities.parameters.ParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` | Append a child element to *parent* and return it. |
| `activities.parameters.ParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'ParameterValue'` | Parse from a TextParameter.Value child element. |
| `activities.parameters.ParameterValue.__repr__` | `def __repr__(self) -> str` |  |
| `activities.parameters.WorkflowVariableParameterValue` | `class WorkflowVariableParameterValue` | Standard workflow variable — tuwap:WorkflowVariableParameterValue. |
| `activities.parameters.WorkflowVariableParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.WorkflowVariableParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'WorkflowVariableParameterValue'` |  |
| `activities.parameters.ActivityVariableParameterValue` | `class ActivityVariableParameterValue` | ForEach / loop iteration variable — tuwap:ActivityVariableParameterValue. |
| `activities.parameters.ActivityVariableParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.ActivityVariableParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'ActivityVariableParameterValue'` |  |
| `activities.parameters.WorkflowArgumentParameterValue` | `class WorkflowArgumentParameterValue` | Workflow argument reference — tuwap:WorkflowArgumentParameterValue. |
| `activities.parameters.WorkflowArgumentParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.WorkflowArgumentParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'WorkflowArgumentParameterValue'` |  |
| `activities.parameters.UserDefinedParameterValue` | `class UserDefinedParameterValue` | Literal user-defined value — tuwap:UserDefinedParameterValue. |
| `activities.parameters.UserDefinedParameterValue.__init__` | `def __init__(self, name: str, value_type: str | None=None)` |  |
| `activities.parameters.UserDefinedParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.UserDefinedParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'UserDefinedParameterValue'` |  |
| `activities.parameters.SystemVariableParameterValue` | `class SystemVariableParameterValue` | System-provided variable — tuwap:SystemVariableParameterValue. |
| `activities.parameters.SystemVariableParameterValue.__init__` | `def __init__(self, variable_type: str)` |  |
| `activities.parameters.SystemVariableParameterValue.variable_type` | `def variable_type(self) -> str` |  |
| `activities.parameters.SystemVariableParameterValue.argument_type` | `def argument_type(self) -> str` |  |
| `activities.parameters.SystemVariableParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.SystemVariableParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'SystemVariableParameterValue'` |  |
| `activities.parameters.ConfigVariableParameterValue` | `class ConfigVariableParameterValue` | Config variable reference — tuwap:ConfigVariableParameterValue. |
| `activities.parameters.ConfigVariableParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.ConfigVariableParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'ConfigVariableParameterValue'` |  |
| `activities.parameters.SecretConfigVariableParameterValue` | `class SecretConfigVariableParameterValue` | Secret config variable reference — tuwap:SecretConfigVariableParameterValue. |
| `activities.parameters.SecretConfigVariableParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.SecretConfigVariableParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'SecretConfigVariableParameterValue'` |  |
| `activities.parameters.DirectoryParameterValue` | `class DirectoryParameterValue` | Directory reference — tuwap:DirectoryParameterValue. |
| `activities.parameters.DirectoryParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.DirectoryParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'DirectoryParameterValue'` |  |
| `activities.parameters.FileParameterValue` | `class FileParameterValue` | File reference — tuwap:FileParameterValue. |
| `activities.parameters.FileParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.FileParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'FileParameterValue'` |  |
| `activities.parameters.ContainerParameterValue` | `class ContainerParameterValue` | Container parameter value — tuwap:ContainerParameterValue. |
| `activities.parameters.ContainerParameterValue.__init__` | `def __init__(self, name: str='', entries: list[list[tuple[str, 'ParameterValue']]] | None=None)` |  |
| `activities.parameters.ContainerParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.ContainerParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'ContainerParameterValue'` |  |
| `activities.parameters.AttributeParameterValue` | `class AttributeParameterValue` | Attribute reference — tuwap:AttributeParameterValue. |
| `activities.parameters.AttributeParameterValue.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.parameters.AttributeParameterValue.from_element` | `def from_element(cls, elem: ET.Element) -> 'AttributeParameterValue'` |  |
| `activities.parameters.parse_text_parameter_value` | `def parse_text_parameter_value(tp_val_elem: ET.Element) -> 'ParameterValue | None'` | Parse the first child of a TextParameter.Value element into the appropriate |
| `activities.parameters._parse_message_placeholders` | `def _parse_message_placeholders(context, message: str, from_node=None)` | Parse {name} placeholders in a log message. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

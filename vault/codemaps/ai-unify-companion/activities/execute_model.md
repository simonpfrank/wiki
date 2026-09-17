# `activities/execute_model.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.parameters](parameters.md)
- `xml.etree.ElementTree` (external)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.execute_model.ModelParameter` | `class ModelParameter` | One ``tuwaa:ModelParameter`` inside ``ExecuteModel.Parameters``. |
| `activities.execute_model.ModelParameter.__init__` | `def __init__(self, name: str, value: ParameterValue)` |  |
| `activities.execute_model.ModelParameter.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.execute_model.ModelParameter.from_element` | `def from_element(cls, elem: ET.Element) -> 'ModelParameter'` |  |
| `activities.execute_model.ModelParameter.__repr__` | `def __repr__(self) -> str` |  |
| `activities.execute_model.ModelExpectedOutput` | `class ModelExpectedOutput` | One ``tuwa:ExpectedOutput`` inside ``ExecuteModel.ExpectedOutputs``. |
| `activities.execute_model.ModelExpectedOutput.__init__` | `def __init__(self, name: str, file_name: str | None=None, variable: str | None=None)` |  |
| `activities.execute_model.ModelExpectedOutput.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.execute_model.ModelExpectedOutput.from_element` | `def from_element(cls, elem: ET.Element) -> 'ModelExpectedOutput'` |  |
| `activities.execute_model.ModelExpectedOutput.__repr__` | `def __repr__(self) -> str` |  |
| `activities.execute_model.ModelVersionReference` | `class ModelVersionReference` | VersionReference inside ExecuteModel.VersionReference. |
| `activities.execute_model.ModelVersionReference.__init__` | `def __init__(self, version_id: str='0', version_type: str='Latest')` |  |
| `activities.execute_model.ModelVersionReference.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.execute_model.ModelVersionReference.from_element` | `def from_element(cls, elem: ET.Element) -> 'ModelVersionReference'` |  |
| `activities.execute_model.ExecuteModelNode` | `class ExecuteModelNode` | ``tuwaa:ExecuteModel`` — executes an ASPI model (e.g. RiskAgility FM). |
| `activities.execute_model.ExecuteModelNode.__init__` | `def __init__(self, context, display_name: str='Execute Model', model_id: int=0, include_all_available_inputs: bool=True, parameters: list[ModelParameter] | None=None, expected_outputs: list[ModelExpectedOutput] | None=None, version_reference: ModelVersionReference | None=None, parameters_xml: str | None=None, requires_parameters_update: bool=False, activity_working_directory: str | None=None, retry_attempts: int=3, retry_on_failure: bool=False)` |  |
| `activities.execute_model.ExecuteModelNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ExecuteModelNode'` |  |
| `activities.execute_model.ExecuteModelNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

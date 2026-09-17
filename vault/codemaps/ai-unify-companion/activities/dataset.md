# `activities/dataset.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.parameters](parameters.md)
- `xml.etree.ElementTree` (external)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.dataset.AttributeSelector` | `class AttributeSelector` | Describes one attribute filter used in a DataSetDownload VersionReference. |
| `activities.dataset.AttributeSelector.__init__` | `def __init__(self, attribute_id: int, operator: str='Contains', value: ParameterValue | None=None)` |  |
| `activities.dataset.AttributeSelector.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.dataset.AttributeSelector.from_element` | `def from_element(cls, elem: ET.Element) -> 'AttributeSelector'` |  |
| `activities.dataset.DataSetDownloadNode` | `class DataSetDownloadNode` | tuwaa:DataSetDownload — downloads files from a Unify dataset version. |
| `activities.dataset.DataSetDownloadNode.__init__` | `def __init__(self, context, display_name: str='Download Data Set', dataset_id: int=0, file_list: list[str] | None=None, attribute_selectors: list[AttributeSelector] | None=None, overwrite_existing: bool=True, version_type: str='Latest', version_id: str='0', retry_attempts: int=3, retry_on_failure: bool=False)` |  |
| `activities.dataset.DataSetDownloadNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'DataSetDownloadNode'` |  |
| `activities.dataset.DataSetDownloadNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.dataset.FileDefinition` | `class FileDefinition` | Describes one file to upload: a target FileName in the dataset, |
| `activities.dataset.FileDefinition.__init__` | `def __init__(self, file_name: str, input_param: ParameterValue | None=None)` |  |
| `activities.dataset.FileDefinition.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.dataset.FileDefinition.from_element` | `def from_element(cls, elem: ET.Element) -> 'FileDefinition'` |  |
| `activities.dataset.AttributeIdValuePair` | `class AttributeIdValuePair` | Describes one attribute value to set on a new dataset version. |
| `activities.dataset.AttributeIdValuePair.__init__` | `def __init__(self, attribute_id: int, value: ParameterValue | None=None)` |  |
| `activities.dataset.AttributeIdValuePair.build_element` | `def build_element(self, parent: ET.Element) -> ET.Element` |  |
| `activities.dataset.AttributeIdValuePair.from_element` | `def from_element(cls, elem: ET.Element) -> 'AttributeIdValuePair'` |  |
| `activities.dataset.DataSetUploadNode` | `class DataSetUploadNode` | tuwaa:DataSetUpload — uploads files to a Unify dataset, creating a new version. |
| `activities.dataset.DataSetUploadNode.__init__` | `def __init__(self, context, display_name: str='Upload Data Set', dataset_id: int=0, file_definitions: list[FileDefinition] | None=None, attribute_values: list[AttributeIdValuePair] | None=None, new_version_name: ParameterValue | None=None, new_version_comment: ParameterValue | None=None, retry_attempts: int=3, retry_on_failure: bool=False)` |  |
| `activities.dataset.DataSetUploadNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'DataSetUploadNode'` |  |
| `activities.dataset.DataSetUploadNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `activities/workflow_execution.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.control_flow](control_flow.md)
- [activities.parameters](parameters.md)
- [workflow_reader.activity_map](../workflow_reader/activity_map.md)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [workflow_reader.activity_map](../workflow_reader/activity_map.md)
- [workflow_reader.inspect](../workflow_reader/inspect.md)
- [workflow_reader.reader](../workflow_reader/reader.md)
- [workflow_reader.tree_helpers](../workflow_reader/tree_helpers.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.workflow_execution.WorkflowArgumentBinding` | `class WorkflowArgumentBinding` | One argument passed to an ExecuteWorkflow activity. |
| `activities.workflow_execution.WorkflowArgumentBinding.__init__` | `def __init__(self, name: str, direction: str='In', is_required: bool=True, param_type: str='x:String', value: ParameterValue | None=None)` |  |
| `activities.workflow_execution.WorkflowArgumentBinding.from_element` | `def from_element(cls, elem: ET.Element) -> 'WorkflowArgumentBinding'` |  |
| `activities.workflow_execution.ExecuteWorkflowNode` | `class ExecuteWorkflowNode` | tuwaa:ExecuteWorkflow — executes another workflow inline or as a child job. |
| `activities.workflow_execution.ExecuteWorkflowNode.__init__` | `def __init__(self, context, display_name: str='Execute Workflow', workflow_id: str='0', is_sub_workflow: bool=True, output_variable: str='', has_persist: bool=False, include_persist: bool=False, retry_attempts: int=0, retry_on_failure: bool=False, run_as_job_name: str='', version_type: str='Latest', version_id: str='0', workflow_arguments: list[WorkflowArgumentBinding] | None=None)` |  |
| `activities.workflow_execution.ExecuteWorkflowNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ExecuteWorkflowNode'` |  |
| `activities.workflow_execution.ExecuteWorkflowNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.workflow_execution.ParallelForEachNode` | `class ParallelForEachNode` | tuwaa:ParallelForEach<T> — parallel iteration over a collection. |
| `activities.workflow_execution.ParallelForEachNode.__init__` | `def __init__(self, context, display_name: str='ParallelForEach', item_type: str='x:String', values_expression: str='', item_name: str='item', max_concurrent_branches: str='', completion_condition: str='', body=None)` |  |
| `activities.workflow_execution.ParallelForEachNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ParallelForEachNode'` |  |
| `activities.workflow_execution.ParallelForEachNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.workflow_execution.AwaitedFile` | `class AwaitedFile` | One file awaited by an ExecuteAwaitFiles activity. |
| `activities.workflow_execution.AwaitedFile.__init__` | `def __init__(self, output_name: str, input_value: ParameterValue | None=None)` |  |
| `activities.workflow_execution.AwaitedFile.from_element` | `def from_element(cls, elem: ET.Element) -> 'AwaitedFile'` |  |
| `activities.workflow_execution.ExecuteAwaitFilesNode` | `class ExecuteAwaitFilesNode` | tuwaa:ExecuteAwaitFiles — waits for external files to appear. |
| `activities.workflow_execution.ExecuteAwaitFilesNode.__init__` | `def __init__(self, context, display_name: str='Await Files', timeout: str='00:05:00', awaited_files: list[AwaitedFile] | None=None, has_persist: bool=False, retry_attempts: int=0, retry_on_failure: bool=False)` |  |
| `activities.workflow_execution.ExecuteAwaitFilesNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ExecuteAwaitFilesNode'` |  |
| `activities.workflow_execution.ExecuteAwaitFilesNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.workflow_execution.TerminateWorkflowNode` | `class TerminateWorkflowNode` | TerminateWorkflow — deliberately terminates the workflow with a reason. |
| `activities.workflow_execution.TerminateWorkflowNode.__init__` | `def __init__(self, context, display_name: str='Terminate Workflow', reason: str='')` |  |
| `activities.workflow_execution.TerminateWorkflowNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'TerminateWorkflowNode'` |  |
| `activities.workflow_execution.TerminateWorkflowNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.workflow_execution.SwitchNode` | `class SwitchNode` | Switch<T> — routes execution based on a keyed expression. |
| `activities.workflow_execution.SwitchNode.__init__` | `def __init__(self, context, display_name: str='Switch', type_arguments: str='x:String', expression: str='', cases: dict | None=None, default_branch=None)` |  |
| `activities.workflow_execution.SwitchNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'SwitchNode'` |  |
| `activities.workflow_execution.SwitchNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

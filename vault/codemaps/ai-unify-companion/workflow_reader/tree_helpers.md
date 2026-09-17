# `workflow_reader/tree_helpers.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities](../activities/__init__.md)
- [activities.control_flow](../activities/control_flow.md)
- [activities.execution](../activities/execution.md)
- [activities.workflow_execution](../activities/workflow_execution.md)
- `io` (external)
- `typing` (external)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `workflow_reader.tree_helpers._node_type_name` | `def _node_type_name(node: ActivityNode) -> str` | Friendly type name for a node. |
| `workflow_reader.tree_helpers._summary_sequence_children` | `def _summary_sequence_children(node: UnifySequenceNode, path: str, allow_raw: bool) -> list[dict]` |  |
| `workflow_reader.tree_helpers._summary_branch_entry` | `def _summary_branch_entry(seq: UnifySequenceNode, path: str, allow_raw: bool) -> dict` |  |
| `workflow_reader.tree_helpers._summary_if` | `def _summary_if(node: IfNode, path: str, allow_raw: bool) -> dict` |  |
| `workflow_reader.tree_helpers._summary_trycatch` | `def _summary_trycatch(node: TryCatchNode, path: str, allow_raw: bool) -> dict` |  |
| `workflow_reader.tree_helpers._summary_switch` | `def _summary_switch(node: SwitchNode, path: str, allow_raw: bool) -> dict` |  |
| `workflow_reader.tree_helpers._node_summary` | `def _node_summary(node: ActivityNode, path: str, allow_raw: bool) -> dict` | Build a summary dict for a single node (recursive for containers). |
| `workflow_reader.tree_helpers._param_to_dict` | `def _param_to_dict(p: ParameterValue) -> dict` | Serialize a ParameterValue to a JSON-friendly dict. |
| `workflow_reader.tree_helpers._detail_body_branch` | `def _detail_body_branch(node: Any, path: str, allow_raw: bool) -> dict | None` |  |
| `workflow_reader.tree_helpers._detail_seq_branch` | `def _detail_seq_branch(seq: UnifySequenceNode, path: str, allow_raw: bool) -> dict` |  |
| `workflow_reader.tree_helpers._detail_log_message` | `def _detail_log_message(node: LogMessageNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_assign` | `def _detail_assign(node: AssignNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_execute_command` | `def _detail_execute_command(node: ExecuteCommandNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_if` | `def _detail_if(node: IfNode, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_foreach` | `def _detail_foreach(node: ForEachNode, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_while` | `def _detail_while(node: Any, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_trycatch` | `def _detail_trycatch(node: TryCatchNode, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_dataset_download` | `def _detail_dataset_download(node: DataSetDownloadNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_dataset_upload` | `def _detail_dataset_upload(node: DataSetUploadNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_execute_model` | `def _detail_execute_model(node: ExecuteModelNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_execute_powershell` | `def _detail_execute_powershell(node: ExecutePowershellNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_execute_workflow` | `def _detail_execute_workflow(node: ExecuteWorkflowNode, _path: str, _allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_parallel_foreach` | `def _detail_parallel_foreach(node: ParallelForEachNode, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_switch` | `def _detail_switch(node: SwitchNode, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_parallel` | `def _detail_parallel(node: UnifyParallelNode, path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._detail_raw` | `def _detail_raw(node: RawActivityNode, _path: str, allow_raw: bool, info: dict) -> None` |  |
| `workflow_reader.tree_helpers._activity_detail` | `def _activity_detail(node: ActivityNode, path: str, allow_raw: bool) -> dict` | Build a detailed dict for a single activity node. |
| `workflow_reader.tree_helpers._iter_subnodes` | `def _iter_subnodes(node: ActivityNode)` | Yield sub-nodes that need to be recursively checked for raw activities. |
| `workflow_reader.tree_helpers._contains_raw_activity` | `def _contains_raw_activity(node: ActivityNode) -> bool` | Recursively check if a node or its descendants contain any RawActivityNode. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

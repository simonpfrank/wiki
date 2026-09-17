# `workflow_reader/loader.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities](../activities/__init__.md)
- [workflow_reader.activity_map](activity_map.md)
- [workflow_reader.context](context.md)
- [workflow_reader.reader](reader.md)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `workflow_reader.loader.load` | `def load(path: str) -> WorkflowReader` |  |
| `workflow_reader.loader._collect_flow_steps` | `def _collect_flow_steps(flowchart_elem: ET.Element) -> list[ET.Element]` |  |
| `workflow_reader.loader._parse_flow_step` | `def _parse_flow_step(step: ET.Element, context: WorkflowContext, flow_steps: list[tuple[str, UnifySequenceNode]]) -> None` |  |
| `workflow_reader.loader._parse_activity` | `def _parse_activity(elem: ET.Element, context: WorkflowContext) -> ActivityNode` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `activities/base.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `re` (external)
- `typing` (external)
- `xml.etree.ElementTree` (external)

## Imported by (INFERRED)

- [activities._helpers](_helpers.md)
- [activities.basic](basic.md)
- [activities.collections](collections.md)
- [activities.control_flow](control_flow.md)
- [activities.control_flow_try](control_flow_try.md)
- [activities.dataset](dataset.md)
- [activities.execute_model](execute_model.md)
- [activities.execution](execution.md)
- [activities.scripting](scripting.md)
- [activities.workflow_execution](workflow_execution.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.base.scan_expression_refs` | `def scan_expression_refs(expression: str, context) -> list[str]` | Scan a VB.NET expression string and return the names of any workflow |
| `activities.base.ActivityNode` | `class ActivityNode` | Base class for all activity nodes. |
| `activities.base.ActivityNode.__init__` | `def __init__(self)` |  |
| `activities.base.ActivityNode.ancestors` | `def ancestors(self) -> list['ActivityNode']` | Walk up the parent chain, returning [parent, grandparent, ...]. |
| `activities.base.ActivityNode.referenced_variables` | `def referenced_variables(self) -> list[str]` | Return the names of all variables/arguments this node reads. |
| `activities.base.RawActivityNode` | `class RawActivityNode` | Catch-all node for activity types we haven't implemented yet. |
| `activities.base.RawActivityNode.__init__` | `def __init__(self, elem: ET.Element, context=None)` |  |
| `activities.base.RawActivityNode.__repr__` | `def __repr__(self) -> str` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

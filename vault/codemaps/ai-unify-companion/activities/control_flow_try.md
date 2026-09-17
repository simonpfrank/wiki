# `activities/control_flow_try.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- [activities.control_flow](control_flow.md)
- `xml.etree.ElementTree` (external)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.control_flow_try.CatchClause` | `class CatchClause` | A single Catch clause inside a TryCatch activity. |
| `activities.control_flow_try.CatchClause.__init__` | `def __init__(self, exception_type: str='s:Exception', exception_name: str='exception', handler=None)` |  |
| `activities.control_flow_try.TryCatchNode` | `class TryCatchNode` | TryCatch — standard WPF try/catch/finally activity. |
| `activities.control_flow_try.TryCatchNode.__init__` | `def __init__(self, context, display_name: str='TryCatch', try_branch=None, catches=None, finally_branch=None)` |  |
| `activities.control_flow_try.TryCatchNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'TryCatchNode'` |  |
| `activities.control_flow_try.TryCatchNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

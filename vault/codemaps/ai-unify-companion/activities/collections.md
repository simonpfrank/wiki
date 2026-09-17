# `activities/collections.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [activities.base](base.md)
- `xml.etree.ElementTree` (external)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `activities.collections.AddToCollectionNode` | `class AddToCollectionNode` | AddToCollection<T> — appends an item to a collection variable. |
| `activities.collections.AddToCollectionNode.__init__` | `def __init__(self, context, display_name: str='AddToCollection', item_type: str='x:String', collection: str='', item: str='')` |  |
| `activities.collections.AddToCollectionNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'AddToCollectionNode'` |  |
| `activities.collections.AddToCollectionNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.collections.RemoveFromCollectionNode` | `class RemoveFromCollectionNode` | RemoveFromCollection<T> — removes the first matching item from a collection. |
| `activities.collections.RemoveFromCollectionNode.__init__` | `def __init__(self, context, display_name: str='RemoveFromCollection', item_type: str='x:String', collection: str='', item: str='')` |  |
| `activities.collections.RemoveFromCollectionNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'RemoveFromCollectionNode'` |  |
| `activities.collections.RemoveFromCollectionNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.collections.ExistsInCollectionNode` | `class ExistsInCollectionNode` | ExistsInCollection<T> — checks whether an item exists in a collection. |
| `activities.collections.ExistsInCollectionNode.__init__` | `def __init__(self, context, display_name: str='ExistsInCollection', item_type: str='x:String', collection: str='', item: str='', result: str='')` |  |
| `activities.collections.ExistsInCollectionNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ExistsInCollectionNode'` |  |
| `activities.collections.ExistsInCollectionNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |
| `activities.collections.ClearCollectionNode` | `class ClearCollectionNode` | ClearCollection<T> — removes all items from a collection variable. |
| `activities.collections.ClearCollectionNode.__init__` | `def __init__(self, context, display_name: str='ClearCollection', item_type: str='x:String', collection: str='')` |  |
| `activities.collections.ClearCollectionNode.from_element` | `def from_element(cls, elem: ET.Element, context) -> 'ClearCollectionNode'` |  |
| `activities.collections.ClearCollectionNode.referenced_variables` | `def referenced_variables(self) -> list[str]` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

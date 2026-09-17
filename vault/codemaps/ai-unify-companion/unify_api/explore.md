# `unify_api/explore.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [unify_api.protocol](protocol.md)

## Imported by (INFERRED)

- [unify_api.core](core.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.explore._kind_of` | `def _kind_of(object_type: int) -> str` |  |
| `unify_api.explore.ExploreMixin` | `class ExploreMixin` | Mixin providing high-level search, browse, and inspect methods. |
| `unify_api.explore.ExploreMixin.search_all` | `def search_all(self, query: str, kind: str | None=None) -> list[dict]` | Search Unify for objects matching query, with optional kind filter. |
| `unify_api.explore.ExploreMixin.browse_folder` | `def browse_folder(self, folder_id: int, kind: str | None=None, recursive: bool=True, max_depth: int=DEFAULT_BROWSE_DEPTH) -> list[dict]` | List folder contents, optionally recursing into sub-folders. |
| `unify_api.explore.ExploreMixin._collect_folder` | `def _collect_folder(self, folder_id: int, items: list[dict], recursive: bool, max_depth: int, current_depth: int) -> None` |  |
| `unify_api.explore.ExploreMixin.inspect_object` | `def inspect_object(self, object_id: int, object_type: int) -> dict` | Return composite detail for a known Unify object. |
| `unify_api.explore.ExploreMixin._inspect_workflow` | `def _inspect_workflow(self, object_id: int, kind: str) -> dict` |  |
| `unify_api.explore.ExploreMixin._inspect_dataset` | `def _inspect_dataset(self, object_id: int, kind: str) -> dict` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

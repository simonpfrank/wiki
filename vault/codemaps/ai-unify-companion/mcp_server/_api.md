# `mcp_server/_api.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- [unify_api](../unify_api/__init__.md)

## Imported by (INFERRED)

- [mcp_server.tools.tools](tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `mcp_server._api.get_api` | `def get_api(env: str | None=None, interactive: bool=False)` | Return a UnifyAPI instance for the given (or default) environment. |
| `mcp_server._api.resolve_workflow` | `def resolve_workflow(api, workflow_id_or_name: int | str) -> dict` | Resolve a workflow by id or name. Raises ValueError if ambiguous. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

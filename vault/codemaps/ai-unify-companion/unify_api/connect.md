# `unify_api/connect.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `re` (external)
- `typing` (external)
- [unify_api](__init__.md)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.connect.resolve_or_register_url` | `def resolve_or_register_url(url: str, envs: dict, config: dict) -> str` | Find an existing env by URL or auto-register a new one. |
| `unify_api.connect.connect_to_env` | `def connect_to_env(env: str, envs: dict, _config: dict, api: Any) -> dict[str, Any]` | Perform health probe and build the connection result dict. |
| `unify_api.connect.list_environments` | `def list_environments() -> dict[str, Any]` | Return environments and default from config. |
| `unify_api.connect.add_environment` | `def add_environment(name: str, url: str, auth_type: str='', username: str | None=None, verify_ssl: bool | None=None, set_default: bool=False) -> dict[str, Any]` | Add or update a named environment. Returns config dict. |
| `unify_api.connect.set_default_environment` | `def set_default_environment(name: str) -> dict[str, Any]` | Set the default environment. Returns config dict. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

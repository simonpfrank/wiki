# `unify_api/config.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `getpass` (external)
- `json` (external)
- `keyring` (external)
- `msvcrt` (external)
- `os` (external)
- `sys` (external)
- `threading` (external)
- `typing` (external)
- [unify_api](__init__.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.config._read_config` | `def _read_config() -> dict` | Read the shared config file.  Returns empty structure if missing. |
| `unify_api.config._write_config` | `def _write_config(config: dict) -> None` | Write the shared config file (creates directory if needed). |
| `unify_api.config.list_environments` | `def list_environments() -> dict` | Return the full config: environments dict + default name. |
| `unify_api.config.add_environment` | `def add_environment(name: str, url: str, verify_ssl: bool | None=None, set_default: bool=False, auth_type: str='', username: str | None=None) -> dict` | Add or update a named environment.  Returns the updated config. |
| `unify_api.config.remove_environment` | `def remove_environment(name: str) -> dict` | Remove a named environment.  Returns the updated config. |
| `unify_api.config.set_default_environment` | `def set_default_environment(name: str) -> dict` | Set the default environment.  Returns the updated config. |
| `unify_api.config.get_api` | `def get_api(env: str | None=None, interactive: bool=True)` | Return a UnifyAPI instance for the given (or default) environment. |
| `unify_api.config._invalidate_cache` | `def _invalidate_cache(name: str) -> None` | Remove a cached API instance (e.g. after config change). |
| `unify_api.config.format_config` | `def format_config(config: dict | None=None) -> str` | Format the config for display to the agent. |
| `unify_api.config.cmd_api_config` | `def cmd_api_config(url: str='', name: str='', no_verify_ssl: bool=False, verify_ssl: bool=False, set_default: bool=False, remove: str='', auth_type: str='sso', username: str='') -> str` | Manage environments.  Called by MCP tool wrappers. |
| `unify_api.config._read_password` | `def _read_password(prompt: str) -> str` | Read a password from the terminal without echoing, using msvcrt on Windows. |
| `unify_api.config.set_credentials` | `def set_credentials(env_name: str, username: str | None=None, password: str | None=None) -> str` | Store SaaS credentials in the OS keyring. |
| `unify_api.config._cli` | `def _cli() -> None` | Simple CLI for credential management. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

# `unify_api/auth.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `keyring` (external)
- `logging` (external)
- `msal` (external)
- `os` (external)
- `requests` (external)
- `requests_negotiate_sspi` (external)
- `threading` (external)
- `time` (external)
- `typing` (external)

## Imported by (INFERRED)

- [mcp_server.tools.tools](../mcp_server/tools/tools.md)
- [unify_api.core](core.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `unify_api.auth.get_negotiate_auth` | `def get_negotiate_auth()` |  |
| `unify_api.auth.detect_auth_type` | `def detect_auth_type(url: str, verify_ssl: bool=False) -> str` |  |
| `unify_api.auth.SaaSAuthRequired` | `class SaaSAuthRequired` |  |
| `unify_api.auth.SaaSAuthRequired.__init__` | `def __init__(self, message: str, user_code: str, verification_uri: str)` |  |
| `unify_api.auth.SaaSTokenManager` | `class SaaSTokenManager` |  |
| `unify_api.auth.SaaSTokenManager.__init__` | `def __init__(self, base_url: str, env_name: str, username: str='', verify_ssl: bool=True, interactive: bool=True)` |  |
| `unify_api.auth.SaaSTokenManager.get_token` | `def get_token(self) -> str` |  |
| `unify_api.auth.SaaSTokenManager._initiate_device_flow` | `def _initiate_device_flow(self, app) -> NoReturn` | Step 1: Start device flow and raise with the code for the caller. |
| `unify_api.auth.SaaSTokenManager._complete_device_flow` | `def _complete_device_flow(self, app) -> str` | Step 2: Poll for completion. User should have signed in by now. |
| `unify_api.auth.SaaSTokenManager._get_app` | `def _get_app(self)` |  |
| `unify_api.auth.SaaSTokenManager._get_scopes` | `def _get_scopes(self) -> list[str]` |  |
| `unify_api.auth.SaaSTokenManager._fetch_aad_params` | `def _fetch_aad_params(self) -> dict` |  |
| `unify_api.auth.SaaSTokenManager._cache_path` | `def _cache_path(self) -> str` |  |
| `unify_api.auth.SaaSTokenManager._build_cache` | `def _build_cache(self)` |  |
| `unify_api.auth.SaaSTokenManager._save_cache` | `def _save_cache(self) -> None` |  |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

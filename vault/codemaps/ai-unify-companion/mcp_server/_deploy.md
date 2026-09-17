# `mcp_server/_deploy.py`

Generated codemap page — do not hand-edit above this line.

## Imports

- `hashlib` (external)
- `json` (external)
- `logging` (external)
- `pathlib` (external)
- `shutil` (external)

## Imported by (INFERRED)

- [mcp_server.server](server.md)
- [mcp_server.tools.tools](tools/tools.md)

## Symbols

| Anchor | Signature | Summary |
|---|---|---|
| `mcp_server._deploy._instructions_root` | `def _instructions_root() -> pathlib.Path` | Return the path to mcp_server/instructions/ inside the installed package. |
| `mcp_server._deploy._github_bundle_root` | `def _github_bundle_root() -> pathlib.Path` | Return the .github/ subtree bundled inside the package. |
| `mcp_server._deploy._python_coding_template` | `def _python_coding_template() -> pathlib.Path` | Return the template python-coding.instructions.md path in the package. |
| `mcp_server._deploy._manifest_path` | `def _manifest_path(workspace_root: pathlib.Path) -> pathlib.Path` |  |
| `mcp_server._deploy._sha256` | `def _sha256(path: pathlib.Path) -> str` |  |
| `mcp_server._deploy._load_manifest` | `def _load_manifest(workspace_root: pathlib.Path) -> dict[str, str]` |  |
| `mcp_server._deploy._save_manifest` | `def _save_manifest(workspace_root: pathlib.Path, manifest: dict[str, str]) -> None` |  |
| `mcp_server._deploy.deploy_instructions` | `def deploy_instructions(workspace_root: pathlib.Path) -> list[str]` | Deploy bundled instruction files to workspace_root/.github/. |
| `mcp_server._deploy.restore_instructions` | `def restore_instructions(workspace_root: pathlib.Path) -> list[str]` | Force-overwrite all managed instruction files and reset the manifest. |

<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->

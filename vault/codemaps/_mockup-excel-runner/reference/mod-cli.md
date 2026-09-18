---
type: module
layer: 0
status: mockup
source: generated-simulated
lines: 168
---

# cli

`excel_runner/cli.py` · 168 lines · **live** · [start here](../start-here.md)

> CLI entrypoint: run a workflow YAML file.

Appears in the route at [step 1](../route-run-a-workflow/r1-you-run-the-command.md).

## What's in here

| Line | Symbol | Kind | Reached | One-liner |
|---|---|---|---|---|
| 31 | `_BelowWarningFilter` | class | live | Lets only DEBUG/INFO through; WARNING+ goes to stderr instead |
| 38 | `configure_logging` | function | live | Attaches the CLI's stdout/stderr console handlers |
| 66 | `_parse_env_override` | function | live | Parses one `--env KEY=VALUE` |
| 88 | `main` | function | **entry** | Run a workflow YAML file |

## Depends on

- [core](mod-core.md) — for `ExcelRunnerError`
- [runner](mod-runner.md) — for `run_workflow`
- _external:_ `argparse`, `logging`, `sys`

## Used by

Nothing in the source. Reached from outside via the `excel-runner` console
script and `python -m excel_runner`.

## Symbols

### main

`def main(argv: list[str] | None = None) -> int`

Run a workflow YAML file. Returns 0 if every step succeeded or was skipped, 1
otherwise.

- **Calls:** `configure_logging`, `_parse_env_override`, [runner.run_workflow](mod-runner.md)
- **Called by:** nothing in source — this is an entry point
- **Called by tests:** 6 test symbols

### configure_logging

`def configure_logging(level_name: str) -> None`

The only place in the project that attaches logging handlers. Clears existing
handlers first, so calling `main()` twice in one process (as tests do) doesn't
duplicate output.

- **Calls:** `_BelowWarningFilter`
- **Called by:** `main`

<!-- ── hand-written below, preserved on regeneration ─────────────── -->

## Notes

Don't add behaviour here. The rule in this project is that the CLI is a wrapper
and `run_workflow` is the API — anything you're tempted to put in `main` almost
certainly belongs in [runner](mod-runner.md), or it won't exist for library
callers.

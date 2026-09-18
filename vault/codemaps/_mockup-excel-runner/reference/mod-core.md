---
type: module
layer: 2
status: mockup
source: generated-simulated
lines: 538
---

# core

`excel_runner/core.py` · 538 lines · **live** · [start here](../start-here.md)

> Core layer: the workflow data model, error types, and the loading/templating
> pipeline.

Appears in the route at [step 2](../route-run-a-workflow/r2-load-the-workflow.md).

## What's in here

Three groups. Read them in this order.

**The model** — what a workflow *is*

| Symbol | One-liner |
|---|---|
| `WorkbookRef` | A logical workbook declared in `workbooks:` |
| `Step` | A single step: action name, workbook, params, optional `if:` |
| `Workflow` | Environment + workbook registry + ordered steps |

**Loading** — YAML to model

| Symbol | One-liner |
|---|---|
| `load` | Load and parse a workflow YAML file |
| `_build_step` | One `steps:` entry into a `Step` |
| `resolve_value` | Expand `{{ }}` recursively through dicts and lists |
| `_resolve_string`, `_whole_expression`, `_evaluate_expression` | Templating internals |
| `evaluate_condition` | Evaluate a step's `if:` to a bool |

**Errors** — the exception hierarchy everything else raises

| Symbol | One-liner |
|---|---|
| `ExcelRunnerError` | Base. Catch this at the boundary |
| `ValidationError` | Failed before any workbook was touched |
| `ActionExecutionError` | An action failed mid-run |
| `ErrorDetail` | Plain-English message plus technical cause |

## Depends on

- _external only:_ `dataclasses`, `pathlib`, `yaml`, `jinja2`

**Nothing in this project.** `core` is the bottom of the dependency graph —
which is why 5 of the 6 source modules import it.

## Used by

- [cli](mod-cli.md), [runner](mod-runner.md), [engine](mod-engine.md), [actions](mod-actions.md)
- _47 test modules_

<!-- ── hand-written below, preserved on regeneration ─────────────── -->

## Notes

The high import count makes this look like the most important file. It isn't —
it's the most *depended on*, which is different. It's important in the way a
vocabulary is important. The behaviour lives in
[runner](mod-runner.md) and [engine](mod-engine.md).

The one genuinely subtle thing here is that templating happens at **load**
time, not execution time. See
[step 2](../route-run-a-workflow/r2-load-the-workflow.md).

---
type: module
layer: 3
status: mockup
source: generated-simulated
lines: 825
---

# actions

`excel_runner/actions.py` · 825 lines · **live** · [start here](../start-here.md)

> Action functions — the 21 things a workflow step can actually do.

Every function here is one `action:` value in a YAML step. They are never
called by name from anywhere; see
[the action registry](../concepts/concept-action-registry.md).

Appears in the route at [step 5](../route-run-a-workflow/r5-execute-each-step.md).

## The catalogue

| Capability | Actions |
|---|---|
| Workbook lifecycle | `open`, `save`, `close`, `create_sheet`, `delete_sheet`, `rename_sheet` |
| Reading | `read_range`, `read_metadata`, `dump` |
| Writing | `write_cell`, `write_range`, `write_row`, `insert_range`, `set_column_width` |
| Finding | `find_row`, `find_column`, `find_columns`, `find_headers_row` |
| Cross-workbook | `copy` |
| Live Excel only | `recalculate` |
| Control | `stop` |

## Anatomy of an action

Every one has the same shape, which is what makes discovery possible:

```python
@action(capability="write")
def write_range(session, sheet, start_cell, values) -> ActionResult:
    """Write a 2-D block of values starting at start_cell."""
```

- First parameter is always `session` — injected, never written in YAML.
- Remaining parameters become the step's `params:` schema, derived from the
  signature by `discover_actions`.
- The docstring's first line becomes the description in `list_actions`.

So **adding an action is: write the function, tag it, done.** No registration
list to update. That's the design win, and the navigability cost.

## Depends on

- [backends](mod-backends.md), [core](mod-core.md)

## Used by

- [engine](mod-engine.md) — by scanning, not by importing names
- _26 test modules — one per action, which is a good map of expected behaviour_

<!-- ── hand-written below, preserved on regeneration ─────────────── -->

## Notes

`copy` is the odd one out: it's the only action needing two sessions, which is
why [runner](mod-runner.md) has a separate `_dispatch_copy`. If you add another
cross-workbook action, that's the code you'll need to generalise.

`recalculate` is the other odd one — the only action that forces a live Excel
process, and therefore the only one that changes a session's backend as a side
effect.

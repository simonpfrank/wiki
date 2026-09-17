# Note to self: graph-view edge semantics still fuzzy

**Context:** picking this up on another machine — read this before touching
`tools/codemap_gen/generate.py` or the import-resolution logic again.

## What's actually working

The last fix (collapsing trailing `__init__` segments when deriving a dotted
module name from a file path) is confirmed correct for the example chain:

```
mcp_server/server.py -> mcp_server/tools/__init__.py -> mcp_server/tools/tools.py -> mcp_server/_api.py
```

This now resolves as real Obsidian links:
`server.py` → `tools/__init__.md` → `tools/tools.md` → `_api.md`
(see [prd_knowledge_system.md §10](../vault/project/docs/prd_knowledge_system.md#L363)).

Usage-based import filtering (an import only counts as an edge if the name is
actually referenced, not just declared) is also implemented and verified.

## What we're actually struggling with

I keep explaining the desired graph edges via **one-off hand-drawn examples**
("mcp_server -> server.py -> tools -> __init__.py -> ...") rather than a
precise, general rule. Each example exposes a real bug (good), but we've been
fixing them one at a time instead of writing down the actual semantics we want
for **when an import should produce an edge, and what the edge should point
to**. Specifically still unclear/undocumented:

- **Package vs. symbol imports**: `from mcp_server.tools import _TOOLS` (a
  package-level import resolving through `__init__.py`) vs.
  `from mcp_server._api import get_api` (importing a **function**, not a
  module). The second case "stops" at `_api.py` — we want the file-level edge,
  never a per-function node — but we haven't written down *why* that's always
  correct, or whether there's a case where it shouldn't be.
- No formal statement of the resolution algorithm exists outside the code
  itself (`generate.py`) and scattered PRD §10 log entries. If a new edge case
  breaks it, we're back to "here's a diagram, guess what's wrong."

## Open next step (not started)

Function-level call-hierarchy ("who calls this function") is still phase 2,
not started. See [prd_knowledge_system.md §13](../vault/project/docs/prd_knowledge_system.md)
for the terminology we settled on:

- Module-level = **dependency/import graph** (done, mostly working)
- Function-level "who calls it" = **call hierarchy** (incoming callers) — not built

## Suggested next action

Before adding more edge cases, write a short **formal spec** (few bullet
rules, not prose) for import-edge resolution in the PRD or a new
`docs/import_edge_rules.md`, covering: package imports, symbol/function
imports, aliased imports, re-exports through `__init__.py`, and relative
imports. Then treat every future bug as "which rule did we violate" instead of
"here's a new diagram."

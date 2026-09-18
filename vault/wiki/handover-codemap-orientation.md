---
type: note
status: active
source: hand-written
updated: 2026-09-18
---

# Handover: codemap orientation experiments

Session state as of 2026-09-18, written to survive a machine change. Covers
the "how does a newcomer navigate an unfamiliar Python repo" thread — the
`orient.py` experiment, the Obsidian graph-shape experiments, and the
hand-built mockup that replaced further coding.

Related: [prd_knowledge_system.md](../project/docs/prd_knowledge_system.md)
(partly superseded — see [Open questions](#open-questions)),
[decision-plain-markdown-links.md](decision-plain-markdown-links.md).

## The problem being solved

> "Imagine I get given a reasonable repo to maintain, where do I start? That
> is a horrible feeling."

Navigate the hierarchy of a Python codebase as a newcomer — start at the top
and follow one path down, or start in the middle and orient outwards. Not
"list every symbol". The existing `tools/codemap_gen/generate.py` answers
*what symbols exist*; that is not the question.

**Working method agreed:** try something, look at it, refine it, and only when
we hit the "aha — that's it (or that's all that's possible)" do we spec it and
build it properly. The PRD is not dogma; it was written before we knew this.

## Three-phase model (agreed)

1. **Orientation** — what is this thing, how do I run it, what are the big pieces
2. **Localization** — which file/function do I care about for my task
3. **Comprehension** — what does this code actually do

## Six newcomer questions

1. How do I run it?
2. What happens when I do? (the flow)
3. What are the major pieces and how do they layer?
4. What's alive and what's dead?
5. This file is 1,700 lines — what's in it and which part do I want?
6. **What do I touch to change X?** ← still unaddressed by anything built

## What was built

### `tools/orient/orient.py` (~750 lines, disposable v0)

```powershell
python tools\orient\orient.py --repo C:\Dev\projects\excel-runner --out vault\codemaps\excel-runner
```

Emits module pages, a start-here page, a liveness page, and JSONL.
`--include-tests` off by default.

Key parts:

- `Symbol` / `Module` dataclasses carrying `calls`, `call_order`,
  `ambiguous_calls`, `called_by`, `called_by_tests`, `status`, `is_data_type`
- `call_targets()` — **source-ordered** (sorted by `lineno`, `col_offset`)
- `looks_like_data_type()` — dataclass decorator, or bases matching
  `Error|Exception|Enum|BaseModel|TypedDict|NamedTuple|Protocol`
- `resolve_calls()` — 5-step ladder: local name → `self.method()` →
  `imported_module.attr()` → local class instance → globally-unique short name
  (marked AMBIGUOUS)
- `find_entry_points()` — pyproject `[project.scripts]`, `__main__.py`,
  `if __name__ == "__main__"`, top-level `__all__`
- `cli_arguments()` — pulls `parser.add_argument(...)` flags + help
- `classify()` — BFS reachability → `entry | live | registered | test-only | unreached`
- `build_trace()` — `MAX_TRACE_DEPTH=4`, `MAX_CHILDREN_PER_NODE=6`

Verified on `excel-runner`: 9 module pages, 209 symbols, 58 test modules
parsed-not-written, 760 links / 0 broken. Liveness: entry 9, live 106,
registered 53, test-only 15, unreached 26.

### `vault/codemaps/_graph-experiments/` (23 files, complete)

Three link topologies, built to test what Obsidian's graph view can show:

- `1-chain/` — 6 pages, each links only forward (sequence)
- `2-tree/` — 1 root → 3 branches → 6 leaves (decomposition)
- `3-hub/` — same 6 pages plus an index, every page carrying a breadcrumb
  back to it (the control, showing hub pollution)

### `vault/codemaps/_mockup-excel-runner/` (16 files, complete)

Hand-written, no script, labelled plausible-not-accurate. Built to make the
requirement visible instead of coding another guess.

| Family | Folder | Shape | Job |
|---|---|---|---|
| Spine | `route-run-a-workflow/` | 6 pages, mostly one link forward | sequence, end to end |
| Ribs | `reference/` | 6 dense generated-looking pages | facts per file |
| Concepts | `concepts/` | 3 pages | the "why" |

Entry point: [_mockup-excel-runner/start-here.md](../codemaps/_mockup-excel-runner/start-here.md).
123 links, 0 broken.

Mermaid deliberately used five ways, to judge which earn their place:

1. layered system overview (start-here) — subgraphs as layers, `==>` calls,
   `-.->` secondary
2. per-step flow (route pages) — 5–8 nodes
3. decision flow (`r3`, `r5`) — branches and failure paths
4. `sequenceDiagram` (`concept-session`) — backend switch over time
5. "what's inside this 1,766-line file" (`mod-engine`) — subgraphs by
   responsibility plus a *which part do you want?* table

Front-matter carries `type`, `layer`/`step`, `status`, `source`. Reference
pages carry an explicit `<!-- hand-written below, preserved on regeneration -->`
marker, so the machine/human boundary is machine-checkable.

## Durable findings

- **Obsidian's graph view cannot show hierarchy, order or direction. Ever.**
  Force-directed and undirected. No folder layout or link arrangement changes
  this.
- **The hairball is caused by our own link density, not by Obsidian.** Degree
  decides shape. Breadcrumbs and index links are good for clicking and poison
  for the graph.
- **Sequence and decomposition are different relations that render
  identically** in the graph. Mermaid *can* distinguish them (solid vs dotted,
  subgraphs); the graph view cannot. A capability gap, not cosmetics.
- **AST tells you structure; it cannot tell you significance.** Significance
  needs ranking signals (entry points, fan-in, churn, size) plus a curated top
  layer.
- **"How do I run it" is question one and is not in the call graph** — it comes
  from pyproject, `__main__`, argparse, launch.json, CI, README.
- **Dead-code reachability is the significance handle** — live / registered /
  test-only / unreached.
- **Decorator registration defeats call-following.** 53 of `excel-runner`'s
  symbols are reachable only via a decorator registry. Surfaced honestly in
  output rather than hidden.
- **Anti-overload is a design constraint** — bounded depth, capped children,
  breadcrumbs. Less is the feature.
- **Unique filenames matter for graph legibility**, not just link correctness.
- **Call traces must be source-ordered.** Alphabetical order destroys the
  meaning of "what happens when it runs".
- **Data types pollute traces.** `Step`, `ErrorDetail`, `ValidationError` are
  *things*, not *steps* — footnote them.
- **Tests swamp output.** Parse them for `called_by_tests` counts; don't emit
  pages for them.

## The uncomfortable finding

Roughly: tables, symbol lists, imports, line counts and the route *skeleton*
are generatable. The prose, the layer assignments, the "which part do you
want" table and **all three concept pages** are not — they are judgement.

The mockup was only writable because `excel-runner` has excellent docstrings
and a detailed README changelog. **On the nightmare repo, the concept pages
would be blank.** That is the significance problem made concrete.

If the concept pages are worth keeping, the tool's job becomes *generate the
skeleton, then prompt an agent to write the judgement* — a different product
from a code generator.

## Where it was left

Mockup finished and awaiting a verdict. The three questions put to the user:

1. **Which pages did you actually use, and which did you skip?** If the
   reference pages went unopened, that changes what gets built first.
2. **Is the route the primary artefact**, with start-here as the door — or is
   start-here enough on its own?
3. **Are the concept pages worth the fact they can't be generated?**

## Open questions

- Is the graph earning its place, or is it *orientation theatre* with routes +
  front door being the real product?
- Does an honest 12-wide fan-out (`run_workflow`) survive mermaid? Proposed
  three-way test: graph neighbourhood vs scoped mermaid vs nested bullets.
- PRD §13.5 (rejected one-file-per-function) and §13 point 2 (usage-based
  edges) need revisiting — declared "wrong now we know".
  [docs/note_graph_view_edge_semantics.md](../../docs/note_graph_view_edge_semantics.md)
  and its "never a per-function node" stance is likewise obsolete.
- Question 6 — "what do I touch to change X" — untouched.
- Significance/ranking (git churn, fan-in) still deferred.
- Obsidian deep links: heading anchors match literally in Obsidian
  (`#AuditLogger.record_step`) but GitHub slugifies
  (`#auditloggerrecord_step`). Deep links break on GitHub.

## Housekeeping

- `vault/codemaps/excel-runner/` (the generated output) — a delete was
  proposed and **cancelled**; decide whether to keep it as a before/after
  comparison against the mockup.
- `tools/codemap_gen/generate.py` untouched, kept as reference.

## Reference facts (excel-runner)

`C:\Dev\projects\excel-runner` — 8 Python files, ~4,500 lines. Console script
`excel-runner = excel_runner.cli:main`. 58 test modules.

Flow: `cli.main` → argparse, `configure_logging` → `runner.run_workflow` →
`core.load` → `engine.discover_actions` → `validate_static` → `plan` →
optional `validate_existence` → `ScratchManager` → `SessionManager` → step
loop via `_dispatch` / `_dispatch_copy` → `compute_link_commit_order` → close
sessions → `AuditLogger`.

Public API: `ActionSpec, RunResult, Step, StepResult, Workflow, WorkbookRef,
list_actions, run_workflow`.

Sharp edges: `recalculate` forces a backend switch to xlwings; a `close`
action must call `forget_session()`; `.xlsm` needs `keep_vba` or macros are
silently dropped.

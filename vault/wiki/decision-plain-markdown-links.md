---
type: decision
status: active
source: hand-written
---

# Decision: plain Markdown links, not Obsidian wikilinks

Migrated from the original `codemap_notes.md` design notes (now retired —
superseded by [prd_knowledge_system.md](../project/docs/prd_knowledge_system.md)
and [spec_summary.md](../project/docs/spec_summary.md)).

## Decision

- **Format: plain Markdown, relative file links** (`[foo.py](../src/foo.py)`),
  not Obsidian wikilinks (`[[foo]]`).
- **Obsidian is a viewer/editor only** — a vault is just a repo (or a folder
  within it) opened in Obsidian for the graph view / backlinks / nicer
  editing experience. Nothing in generated docs depends on Obsidian-only
  syntax.

## Why

Plain relative links render everywhere (GitHub, any editor, an agent's file
tools) with zero resolver logic. Wikilinks only render inside Obsidian and
require name-to-path resolution, which is a liability for tooling and for
anyone reading the repo outside Obsidian.

## Why a codemap at all

An AST-derived map is a graph (modules → classes/functions → calls/imports →
symbols). Its value is as a **router**, not a second source of truth:

- Fast "what does this call / get called by" without re-parsing.
- Stable, human-scannable summaries (signatures + one-line purpose) instead of
  full bodies.
- A place to write *why* the code is shaped this way — which a generator can
  never infer, so that part stays hand-written.

Risk if hand-maintained: it drifts from the code and becomes actively
misleading. Mitigation: generate the structural parts from a script, and check
it into CI as a diff-check — never hand-edit the generated sections.

## Keeping it from going stale

- Generate from an AST walk at build/pre-commit time.
- Add a CI/lint check: regenerate into a temp location and diff against the
  committed file; fail if they differ — same pattern as a formatter check.
- Hand-written prose (architecture narrative, task index framing, "why")
  stays separate from the generated tables, since a script can't infer intent.

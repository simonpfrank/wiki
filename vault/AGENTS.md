# Vault schema — how to maintain this vault

This file is the schema doc for this vault (Karpathy LLM-wiki pattern):
inject it into every session that reads or writes here. It's about the
general knowledge side (`wiki/`, `sources/`, `queue/`); code-specific
generation rules for a codemap live in that repo's own generated docs, not
here — see [project/docs/prd_knowledge_system.md](project/docs/prd_knowledge_system.md).

## Layers

- **`sources/`** — raw ingested material. Immutable once added: read it,
  summarize it, cite it, never edit it. Cite by filename.
- **`wiki/`** — AI-maintained pages. One concept per page, backlinked to
  related pages, one-line summary at the top. This is what you write to.
- **`queue/`** — actionable tickets, not knowledge pages (see Task queue below).
- This file — the schema. Read it, don't need to be told twice per session,
  but re-read if it's been a while or something here seems to have changed.

## Navigation files

- **`index.md`** — catalog: one line per page (link + one-line summary).
  Update it whenever a page is added or removed. Entry point for a human or
  agent orienting for the first time.
- **`log.md`** — append-only, newest-first, fixed-prefix entries:
  `## [YYYY-MM-DD] <verb> | <short title>`, so `grep "^## \[" log.md` finds
  recent activity without reading the whole file. Verbs so far: `scaffold`,
  `decision`, `ingest`, `sync`, `lint`. Add new ones as needed, keep them short.

## Front-matter (required on every `wiki/` and `queue/` page)

```yaml
---
type: module | concept | decision | source | task | project
status: draft | active | deprecated | stale
source: generated | hand-written | mixed
---
```

Full definitions of each `type` value:
[project/docs/spec_summary.md](project/docs/spec_summary.md#type-enum--one-definition-per-value-with-purpose-and-an-example).
Add `tags:`, `repo:`, `aliases:` only once there's an actual need for them
(see that same doc) — don't front-load taxonomy that isn't earning its keep.

## Operations

- **`/capture <source>`** — ingest a source into `sources/`, then create or
  update the `wiki/` page(s) it informs, then update `index.md`.
- **`/sync`** — re-check `wiki/` pages against any `sources/` material that's
  newer than the page, refresh what's stale.
- **`/lint`** — check for: broken links, orphan pages (nothing links to
  them and they're not in `index.md`), pages with `status: stale` past a
  reasonable age, contradictions between pages covering the same topic.
- **`/digest`** — summarize recent activity from `log.md` (e.g. last N
  entries) into a short recap.

These are conventions to follow when asked to do the equivalent action, not
literal slash-commands that exist yet — implement them as real tooling later
if that's worth doing (see [project/docs/prd_knowledge_system.md](project/docs/prd_knowledge_system.md) §5).

## Task queue (`queue/`)

- One file per ticket: `queue/000N-short-name.md`.
- Front-matter: `type: task`, `status: todo | in-progress | done | blocked`,
  optional `priority`, optional `depends_on: [other-ticket-filenames]`.
- To work through the queue: list `queue/`, filter `status: todo`, take the
  next by `priority` then filename order (unless told otherwise), set it to
  `in-progress`, execute the body as instructions, then set `status: done`
  (or `blocked` with a reason) and append a short completion note to the
  ticket file. Log the outcome in `log.md`.
- Follow-up work discovered mid-ticket becomes a new ticket file, not a note
  left only in chat.

## Persistent memory — the rule that makes any of this worth doing

A chat session is not durable storage. Before considering a session's work
"done": any non-trivial agreement gets written to either a `decision` page
(standalone/structural) or a `log.md` entry (smaller/incremental) — never
left only in the conversation transcript. If in doubt, write the smaller
`log.md` entry; it's cheap and better than nothing.

## What NOT to do here

- Don't use Obsidian wikilinks (`[[foo]]`) — plain relative Markdown links
  only, so everything still renders on GitHub and is readable by any agent's
  file tools without a resolver. See
  [wiki/decision-plain-markdown-links.md](wiki/decision-plain-markdown-links.md).
- Don't edit `sources/` — it's immutable.
- Don't stand up a vector DB / embeddings pipeline as the default retrieval
  path — grep + these structured files is the default; only reconsider if it
  demonstrably doesn't scale.

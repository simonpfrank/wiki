# Codemap + Knowledge Wiki — Feature & Practice Summary

Terse, as-if-finalized reference derived from [prd_knowledge_system.md](prd_knowledge_system.md).
Not a spec — a working checklist of what to build and what to follow, until
practices and functionality get split into separate docs.

## Principles

- Plain markdown, relative links only. No wikilinks, no proprietary format.
- Obsidian is a viewer, never a dependency — everything still works on GitHub
  and via an agent's file tools with zero resolver logic.
- Generated content and hand-written prose are never mixed in a way that lets
  one silently overwrite the other.
- Text files only — no vector DB, no graph DB, as the primary path. Grep +
  a lightweight generated index is the default; revisit only if it doesn't
  scale.
- Agent path and human path are separate outputs from one shared extraction,
  not one format compromising for both.
- A chat session is not durable storage: any non-trivial agreement gets
  flushed to a `decision` page or a `log.md` entry before the session ends —
  never left only in conversation.

## Features to build

### Codemap generator (code)
- AST walk (Python via `ast`/Pylance first).
- `--out <path>` parameter — never hardcodes destination. Default recommendation:
  `<repo>/docs/` opened as that repo's Obsidian vault; alternative: a separate
  shared vault folder (e.g. `codemaps/<repo-name>/`).
- Output structure: **mirrored** — one generated page per source file,
  `<out>/<path-mirrors-src>/foo.md`.
- Emits two projections from one pass:
  - Agent-facing dense index (JSONL-style, one record per symbol: path,
    symbol, signature, one-line summary, imports, imported_by, stable anchor).
    No full bodies, no control flow.
  - Human-facing markdown: module responsibility table, symbol index,
    cross-module edges, "follow the data" walkthrough, glossary — with a
    hand-written section left for prose/"why" that the generator never touches.
- Cross-module edges tagged `EXTRACTED` / `INFERRED` / `AMBIGUOUS` (borrowed
  from graphify) so agent/human know what's fact vs. derived.
- Regeneration keyed to stable anchors — only needed on interface changes,
  not every edit.
- Kept from drifting via a CI diff-check (regenerate to temp, diff against
  committed) — consider a git-hook-based auto-rebuild (graphify pattern:
  rebuild on commit/branch-switch, `update` after pull) as an alternative or
  complement later.

### Codemap query tool (agent-facing)
- Thin CLI over the dense index, not markdown-reading. Verbs: symbol lookup,
  callers/callees, imports, task-description → candidate file(s).
- Interface shape borrowed from graphify's `query` / `path` / `explain` —
  worth using as the starting verb set regardless of implementation.
- Agent index format: **decided — JSONL**. One record per line, fast to
  grep/parse, appendable, diffable, no DB. Two record kinds: `module`
  (file-level: path, doc_ref, imports/imported_by) and `function`/`class`/
  `method` (symbol-level: anchor, signature, summary, calls/called_by).
  Per-edge `confidence: EXTRACTED | INFERRED | AMBIGUOUS`. Regen keyed to a
  signature hash, not line numbers. Full schema:
  [prd_knowledge_system.md §11](prd_knowledge_system.md#11-jsonl-codemap-index-schema-decided).

### Task queue (tickets the agent executes)
- Files under `queue/`, one per ticket, e.g. `queue/0001-add-export-backend.md`.
- Front-matter: `type: task`, `status: todo | in-progress | done | blocked`,
  optional `priority`, optional `depends_on:`. Body = the instruction/prompt.
- Agent picks the next `status: todo` (priority, then filename order),
  executes it, updates `status` + adds a completion note, logs it in `log.md`.
- Follow-up work discovered mid-task becomes a new ticket file, not a buried
  chat TODO.
- Deliberately simple: files + a status field, no workflow engine.

### Knowledge ingest (general wiki, Karpathy pattern)
- `sources/` — raw ingested material, immutable, cited by filename.
- `wiki/` — AI-maintained pages, one concept per page, backlinked, summary at top.
- `index.md` — catalog: link + one-line summary per page, updated on every ingest.
- `log.md` — append-only, newest-first, fixed-prefix entries (`## [date] ...`)
  so `grep "^## \[" log.md` works.
- A schema doc (`AGENTS.md`-style) telling the agent how to maintain the wiki,
  injected every session.
- Operations: `/capture` (ingest → update wiki), `/sync` (refresh from new
  sources), `/lint` (broken links, orphan pages, staleness, contradictions),
  `/digest` (recap from the log).
- Population driven by a documented prompt/workflow, not manual per-file
  authoring — this is the "just via a prompt" requirement.

### Vault folder layout (minimal, grow as needed)
```
vault/
  index.md
  log.md
  wiki/
  sources/
  codemaps/<repo-name>/   # only when a repo's --out target is this shared vault
  project/                # this project's own design docs
```

## Front-matter / tagging (decided)

Minimum viable, applied from day one:

| Field | Values / shape | Purpose |
|---|---|---|
| `type` | closed enum, defined below | page kind, drives Bases grouping |
| `status` | `draft \| active \| deprecated \| stale` | lifecycle, feeds `/lint` staleness checks |
| `source` | `generated \| hand-written \| mixed` | machine-checkable generated-vs-hand-written boundary |

### `type` enum — one definition per value, with purpose and an example

Every page gets exactly one. If a page doesn't cleanly fit one of these,
that's a signal the taxonomy is missing something — raise it rather than
force-fitting.

| `type` | What it is | Who authors it | Lives in | Example |
|---|---|---|---|---|
| `module` | One generated page per source file/symbol group — signature-level summary, not prose | Generated | `<out>/<mirrors-src>/` | `render_diagram` in `mermaid_render.py` → `mermaid_render.md` |
| `concept` | An explainer for an idea, term, or pattern that isn't tied to one file — the "what is X" pages other pages link out to | Human or AI-maintained (Karpathy `/capture`/`/sync`) | `wiki/` | "What is an AST", "RAG vs. wiki-as-memory" |
| `decision` | A point-in-time design choice: context → options considered → what was picked → why. Distinct from `concept` because it's a specific call, not a general explainer, and it's expected to eventually go `stale`/`deprecated` if superseded | Hand-written (agent can draft, human confirms) | `wiki/` or `project/` | [wiki/decision-plain-markdown-links.md](../../wiki/decision-plain-markdown-links.md) |
| `source` | A wiki-side pointer/summary for one raw ingested item — title, origin, date, one-line summary, links to the `concept`/`decision` pages it informed. **Not** the raw material itself (that's the immutable file under `sources/`) | Generated on ingest (`/capture`) | `wiki/` (points at `sources/`) | Summary page for an ingested article or repo README |
| `task` | **Redefined, narrowly: an actionable ticket with a status** (todo/in-progress/done/blocked) — a thing to be executed, not a reference doc. See Task queue below. Recurring "how to do X" reference write-ups now live under `concept` instead (they're read, not executed) | Human-authored, agent-executed | `queue/` | `queue/0001-add-export-backend.md` |
| `project` | Meta: pages *about this tooling/system itself* — PRDs, this summary, process notes. Distinct from everything else because it describes the system, not content the system manages | Hand-written | `project/` | This PRD, [spec_summary.md](spec_summary.md) |

**Not page types** — two things removed from the original draft because they're
single special files, not a page kind that varies per-page:
- `index.md` and `log.md` are exempt from `type` front-matter entirely; they're
  fixed-format navigation files (catalog / append-only ledger), not content pages.
- A glossary is not its own type — glossary terms are just short `concept` pages
  (or a glossary section linking out to them), so they stay covered by `concept`
  rather than adding a parallel mechanism.

Added opportunistically, not upfront:

| Field | When |
|---|---|
| `tags:` (freeform) | once enough `wiki/` pages exist to need topical filtering |
| `repo:` | once a shared-vault destination is actually in use |
| `aliases:` (Obsidian built-in) | when a concept has more than one name worth merging in the graph |

Edge-level (not page front-matter): `EXTRACTED` / `INFERRED` / `AMBIGUOUS`
confidence tags on codemap cross-module edges.

## Explicit non-goals

- No vector DB / embeddings as the primary retrieval path.
- No Obsidian plugin.
- No replacing hand-written architecture prose with generated content.
- Not adopting graphify wholesale — mining it for ideas, not depending on it.

## When discussing a new feature

Before designing it from scratch, check whether graphify already solved it —
call it out explicitly so it can be considered (borrow, adapt, or consciously
reject), rather than reinventing silently.

## Open / not yet decided

- Obsidian Bases usage — spike once real front-matter exists across enough
  pages to be worth querying.
- Scope split: this doc mixes practices (conventions, tagging, folder rules)
  and functionality (generator, query tool, ingest pipeline) deliberately for
  now; separate them once both stabilize.

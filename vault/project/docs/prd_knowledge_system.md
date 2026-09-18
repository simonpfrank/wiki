# PRD — Codemap + Knowledge Wiki System

Status: draft, for discussion. No code written yet.
## 1. Problem

Two related but distinct needs:

- **Code navigation**: an agent working in a codebase burns context re-discovering
  structure (what calls what, where a symbol lives) every session; a human new
  to a codebase has the same problem but wants prose/diagrams, not a symbol dump.
- **General knowledge**: notes, decisions, external material accumulate with no
  durable, cross-linked structure — hard to retrieve later, by human or agent,
  without re-reading everything or standing up a vector DB.

Both need: **plain markdown, relative links, no proprietary format**, so the
same content works in Obsidian (graph view, backlinks, Bases) *and* renders
natively on GitHub *and* is directly readable by an agent's file tools — no
resolver, no DB, no lock-in.

Some people talk about having a 'Brain' e.g. all their knowledge which is an interesting concept

## 2. Prior art we're building on

- [wiki/decision-plain-markdown-links.md](../../wiki/decision-plain-markdown-links.md) — existing decisions for the code-AST
  side: plain relative links not wikilinks, Obsidian is viewer-only, generated
  content is diff-checked in CI so it can't silently drift, hand-written prose
  (the "why") stays separate from generated tables. (Migrated here from the
  now-retired `codemap_notes.md` — see §7.b.)
- **Karpathy's LLM Wiki pattern** (gist, Apr 2026) — for the general-knowledge
  side: three layers —
  - `sources/` — raw ingested material, immutable, cite by filename.
  - `wiki/` — AI-maintained pages, one concept per page, backlinked, summary at
    top.
  - a schema doc (`AGENTS.md`-style) injected into every session telling the
    agent *how* to maintain the wiki.
  - Two navigation files: `index.md` (catalog: link + one-line summary per
    page, updated on every ingest) and `log.md` (append-only, newest-first,
    fixed-prefix entries so `grep "^## \[" log.md` works).
  - Four operations: `/capture` (ingest a source, update wiki), `/sync`
    (refresh wiki from new sources), `/lint` (broken links, orphan pages,
    staleness, contradictions), `/digest` (recap from the log).
  - Core reframe: RAG re-derives relationships on every query; a wiki
    compounds — each ingest/query refines what's already there instead of
    starting from scratch.
- **graphify** ([Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)) —
  a real, actively-developed CLI (118k★), not a toy. Directly relevant, see
  §11 for a full breakdown of what to borrow.

## 3. Non-goals

- No vector database, no embeddings-based retrieval as the primary path
  (grep/graph-traversal over structured markdown + a lightweight generated
  index is the primary path; embeddings could be an *optional* accelerant
  later, not a dependency).
- Not an Obsidian plugin — Obsidian is one viewer among several, never a
  requirement for the content to be useful.
- Not trying to replace hand-written architecture prose — generated content
  augments it, never overwrites it.

## 4. Two consumers, explicitly separate modules

The same underlying facts (symbols, files, relationships, notes) get surfaced
differently, and the two paths should be **separate modules/functions**, not
one format serving both badly.

### 4a. Agent path — optimized for speed / low context

- Goal: fewest tokens to find *where* to make a change and *what else touches
  it*, with high confidence.
- Primary artifact: a **dense structured index**, not prose — e.g. JSONL or
  similar, one record per symbol: `{path, symbol, signature, one_line_summary,
  imports, imported_by, anchor}`. Machine-first format, not meant to be read
  top-to-bottom by a human.
- Access is via a **specialized query tool** ("codemap grep"), not by an agent
  reading generated markdown directly:
  - lookup by symbol name / fuzzy task description → candidate file(s)
  - "what calls X" / "what does X call" / "what imports X"
  - stable anchors (`module.symbol`) so regen is only needed on interface
    changes, not every edit
- Explicitly excluded: full function bodies, control flow, prose — that's what
  reading the actual file is for.
- For the general-knowledge side, the equivalent agent-facing surface is the
  Karpathy `index.md` + `log.md` pair plus grep over `wiki/`: cheap to scan,
  no DB required.

### 4b. Human path — optimized for orientation / understanding

- Goal: build a mental model of how something works or how it relates to
  other things, browsing rather than querying for one fact.
- Primary artifact: **markdown pages meant to be read**, per the existing
  codemap notes style — architecture narrative, module responsibility table,
  "follow the data" walkthrough, glossary.
- Consumed via Obsidian (or plain markdown viewer): graph view for
  orientation ("what connects to what"), backlinks, and potentially
  **Obsidian Bases** — a table/database view over front-matter properties
  (e.g. all pages with `type: module`, sortable by responsibility) — worth a
  small spike once real front-matter exists, not committed to yet.
- Front-matter/tags needed to make Bases and graph clustering useful: at
  minimum `type` (module/concept/decision/task), and enough tags to cluster
  meaningfully — exact taxonomy TBD, see open questions.

### 4d. Graph navigation is usage-driven, not folder-driven (§13)

Correction from the original framing: the human path's graph view isn't
meant to mirror the physical folder tree — it's meant to let you follow
*usage* (what calls/imports what), which is a different shape than the
directory structure. Full design in §13; summarized here since it changes
what "human-facing markdown" actually needs to contain.

### 4c. Shared substrate

Both paths are generated/maintained from the **same underlying extraction**
(AST walk for code, ingest step for general knowledge) so there is one source
of truth on disk; the two artifacts (dense index vs. prose pages) are two
projections of it, not independently maintained.

## 5. Proposed modules

1. **Codemap generator** (code-specific)
   - AST walk (language-appropriate; Python via `ast`/Pylance to start).
   - Emits: (a) the agent-facing dense index, (b) human-facing generated
     markdown (module table, symbol index, cross-module edges), leaving a
     hand-written section for prose/"why".
   - CI diff-check so generated content can't silently drift (per existing
     codemap notes).

2. **Codemap query tool** (agent-facing)
   - Thin CLI/tool over the dense index: symbol lookup, callers/callees,
     task-description → candidate file. This is the "specialist grep" you
     mentioned — scoped now as its own module rather than folded into the
     generator.

3. **Knowledge ingest** (general, Karpathy-pattern)
   - `sources/` (raw, immutable) → `wiki/` (maintained pages) pipeline.
   - Schema doc defining how pages are structured, linked, tagged.
   - `index.md` + `log.md` maintenance.

4. **Wiki maintenance conventions**
   - Page template(s), front-matter schema, tag taxonomy.
   - `/lint`-equivalent: broken links, orphan pages, staleness.
   - Where code-codemap pages and general-knowledge pages live relative to
     each other (folder convention) — see open questions.

5. **Population workflow**
   - You want to drive this "just via a prompt" — i.e. a documented
     prompt/workflow that takes a source (repo, article, note) and runs
     ingest → wiki update → index/log update, so populating the vault doesn't
     require manual file-by-file authoring.

## 6. Open questions (need your input before design goes further)

1. **Folder layout**: mirror code structure (`vault/code/<path>/foo.md` next
   to `src/foo.py`) vs. flat per-package `CODEMAP.md` — probably decided
   per-repo-size rather than globally; agree? 
2. **Where does the general wiki live relative to a given codebase's
   codemap?** Same vault, different subfolder? Separate vault entirely,
   cross-linked? 
3. **Tag/front-matter taxonomy** for `type:` clustering (module, concept,
   decision, task, source, ...) — start minimal and grow, or design taxonomy
   upfront?
4. **Agent index format** — **decided: JSONL.** One record per line = fast
   line-by-line grep/parse without loading a whole file or standing up a DB,
   trivially appendable, diffable in git, and openable in any editor — the
   fastest option for both an agent's tools and your "stay text-based, no DB"
   answer in 6.a-Q4. Revisit only if a real corpus proves this too slow to
   scan, per that same answer.
5. **graphify** — link needed to evaluate as prior art.
6. Confirm scope: this repo stays tooling-design-only (per your answer) —
   actual vault/codemap output happens in target repos when the tooling is
   applied there, not here?
### 6.a Answers
1. Yes
2. a sub directory of the repo root possibly docs, but actually could be sucked into a vault in a separate folder structure there is no 'live' link between the two, it is updated via a script. Also need some recommendations for folders for non code 
3. need recommendations/options
4. let's stay with text based (openable in anything for now), if we have a massive code base and it doesn't scale then we dal with that then
5. https://github.com/Graphify-Labs/graphify also conceptually it may not be relevant but there may be some functional ideas which could be useful
6. We can dogfood this project in it so it becomes where we make the tooling and where we test concepts - another repo might be used for the AST stuff

### 6.b Destination vs. structure — two separate decisions

Correction from the first pass at this: "where generated files go" and "how
they're laid out once there" are independent, and conflating them into one
options table was confusing. Splitting them:

**Destination — a generator parameter, not a fixed choice**

The generator takes an output-root path (`--out <path>`, or config) and
writes there; it never hardcodes "the repo" or "the vault". This gives the
flexibility you want: point it at a project's `docs/` folder, or at an
entirely separate vault folder, per repo, without changing the tool.

- **Recommended default**: `<repo>/docs/` (or `docs/codemap/` within it),
  opened directly in Obsidian as that repo's vault. Not the repo root —
  even though Obsidian's graph only ever shows `.md` files (it doesn't
  "ingest" source code regardless of vault root), scoping to `docs/` keeps
  the vault folder (and its `.obsidian/` config) separate from source, and
  avoids stray unrelated `.md` files elsewhere in the repo (READMEs, license
  notes, etc.) cluttering the graph.
- **Alternative**: point `--out` at a wholly separate vault folder (e.g. this
  notes vault's `codemaps/<repo-name>/`) instead of the project's `docs/`.
  Same generator, different destination argument — this is how one repo's
  codemap ends up aggregated alongside others in a shared vault, still with
  no live link (just re-running the generator against a different path,
  on demand).
- Both are valid uses of the same tool; which one you pick per-repo is a
  runtime choice, not a design fork.

**Structure — decided: mirrored**

Once a destination is chosen, the layout within it mirrors the source tree:
`<out>/<path-mirrors-src>/foo.md` next to a conceptual `src/foo.py`. One
generated page per source file — gives one graph node per file for a
meaningful Obsidian graph, and is simple to diff-check in CI (one generated
file changed ⇒ one source file changed). This replaces the earlier flat vs.
mirrored options table — going with mirrored outright rather than deciding
per-repo-size, since destination flexibility already handles the "small repo,
don't want much generated output" case (point `--out` at a single throwaway
folder, or just don't run it).

**Non-code vault folders (recommendation, minimal to start):**

```
vault/
  index.md          # catalog: link + one-line summary per page (Karpathy pattern)
  log.md            # append-only, newest-first, fixed-prefix entries
  wiki/              # AI-maintained concept pages, one concept per page, backlinked
  sources/           # raw ingested material, immutable, cited by filename
  codemaps/
    <repo-name>/     # only used when a repo's --out target is this shared vault
                     # rather than its own docs/ folder
  project/           # this project's own design docs (already in use — this PRD lives here)
```

Start with just these; add folders only when a real need shows up rather than
designing the full tree upfront.

### 6.c Front-matter / tag taxonomy — options, recommendation

| Option | Description | Pros | Cons |
|---|---|---|---|
| 1. Minimal closed `type` | Single front-matter field, small fixed enum (see [spec_summary.md](spec_summary.md) for the full definition of each value: `module, concept, decision, source, task, project`) | Cheap, consistent, enough for Obsidian Bases to group/filter by type immediately | Coarse — can't slice by topic |
| 2. `type` + freeform `tags:` | Add an open list of topical tags on top of option 1 | Flexible topical clustering in graph view | Tag sprawl/inconsistency without discipline; needs periodic cleanup (a `/lint`-equivalent) |
| 3. Confidence tagging (borrowed from graphify) | Tag *relationships/links* (not pages) as `EXTRACTED` (explicit in source) vs `INFERRED` (derived) vs `AMBIGUOUS` | Lets agent/human know what's fact vs. derived — valuable for the codemap's cross-module edges specifically | Only applies to generated edges, not general wiki pages; extra generator complexity |

**Recommendation:** start with **option 1** everywhere (cheap, unblocks Bases),
layer **option 2** on only once you're actually writing enough `wiki/` pages to
need topical filtering (don't design the tag vocabulary speculatively), and
adopt **option 3** specifically for the codemap generator's cross-module edges
since it directly improves agent trust in generated relationships at low cost.

**More than topical tagging — other front-matter dimensions this PRD actually needs:**

The options above only cover "what kind of page/edge is this" and "what topic
does it belong to." Separate concerns, easy to miss, all cheap to add now
rather than retrofit later:

| Field | Purpose | Why it's needed here specifically |
|---|---|---|
| `status: draft \| active \| deprecated \| stale` | Lifecycle state | Enables a `/lint`-equivalent (§5.4, Karpathy's `/lint`) to flag staleness — without it there's no cheap way to ask "what hasn't been touched in a while" |
| `source: generated \| hand-written \| mixed` | Provenance | This whole PRD's core principle is generated content must never silently overwrite hand-written prose (§2, §5.1). Without a machine-checkable field, that boundary lives only in folder convention/comments, which is weaker |
| `repo: <name>` | Which codebase a page came from | Only matters once a shared vault aggregates codemaps from multiple repos (§6.b's "separate vault" destination option) — lets a Bases view scope/filter to one repo |
| `aliases:` (Obsidian's own built-in field, not custom) | Alternate names for the same concept | Lets differently-named references (e.g. a class name vs. its file name) resolve to one graph node instead of splitting backlinks across near-duplicate pages |

**Revised recommendation:** minimum viable front-matter from day one is
`type` + `status` + `source`, since `status`/`source` are structural (they
gate lint and generated/hand-written safety, not cosmetic), with `repo` added
only once a shared-vault destination is actually in use, and free-form
`tags:`/`aliases:` added opportunistically as pages accumulate rather than
mandated upfront.

## 7. Next steps once open questions are answered

- Lock folder layout + front-matter schema (small decision, unblocks
  everything else).
- Spec the dense agent-index format precisely (fields, anchors, regen
  triggers).
- Prototype the codemap generator against a small real repo.
- Draft the wiki schema doc (Karpathy-pattern `AGENTS.md`-equivalent) and one
  example `/capture` → `wiki/` page round-trip.
### 7.a comments on 7
* Folder layout: need some options, pros and cons for each and recommendation so I can see the art of the possible and decide
* Prototype: Yes lets keep his agile we can rebuild it decently if we need to
* Yes there is also a chrome obsidian web capture tool I can try
* I also want to delete the original codemap doc soon so make sure we have what we need from it in here (but I suspect we have everything)

### 7.b coverage check before deleting codemap_notes.md — done

Everything in the original doc is represented here: the plain-relative-links
decision and rationale (§1, §2), Obsidian-as-viewer-only (§2, §4b), the
agent/human split with its exact content lists — task index, one-line
symbol summaries, stable anchors, excluded full bodies for the agent;
architecture narrative, module table, "follow the data" walkthrough, glossary
for the human (§4a/§4b, carried over near-verbatim), the drift risk + CI
diff-check mitigation (§2, §5.1), and the "generator script next" step
(§5.1/§7). Nothing identified as missing.

**Done**: `project/codemap_notes.md` deleted. Its one durable decision (plain
links over wikilinks, plus the drift/CI-check rationale) migrated to
[wiki/decision-plain-markdown-links.md](../../wiki/decision-plain-markdown-links.md)
rather than disappearing outright — flagged as a `decision` page per the
type taxonomy (§6.c) instead of a design note that would otherwise dangle.
The Obsidian web-capture tool you mentioned is a new input to fold into the
**Population workflow** (§5.5) rather than something the old doc covered.

## 8. Task queue — tickets the agent executes one by one

New capability, prompted by re-reading the `task` type: you want to be able
to drop work items in as files and have an agent pick them up and execute
them one at a time, like a lightweight issue tracker that lives entirely as
text files — no GitHub Issues, no DB, consistent with everything else here.

This means splitting what was previously one fuzzy `task` type into two
clearer things:

- **`concept` pages** now cover reference "how do I do X" write-ups (moved out
  of `task` — those are read, not executed, so they belong with the other
  explainer pages).
- **`task` is redefined, narrowly: an actionable ticket with a status**, not a
  reference doc.

**Shape:**

- One file per ticket under `queue/` (vault-level, or per-repo if scoped to a
  project), e.g. `queue/0001-add-export-backend.md`. A numeric/date prefix
  gives stable default ordering without relying on front-matter alone.
- Front-matter: `type: task`, `status: todo | in-progress | done | blocked`,
  optional `priority`, optional `depends_on: [...]` (other ticket filenames).
  Body is the instruction itself, written like you'd write a prompt.
- **Execution model**: agent lists `queue/`, filters `status: todo`, takes the
  next one (by priority, then filename order, unless told otherwise),
  executes it, then updates that file's `status` to `done` (or `blocked` with
  a reason) and appends a short completion note. A `log.md` entry gets added
  either way — this is the mechanism, not a separate one (§9).
- Follow-up work discovered mid-execution becomes a new ticket file, not a
  buried TODO comment in chat — keeps the queue as the single place work is
  tracked.
- This is deliberately simple (files + front-matter status), not a workflow
  engine — no automatic dependency resolution, no scheduling; you and/or the
  agent read the queue and decide what runs next.

## 9. Persistent memory — flushing agreed decisions to disk

Direct consequence of the whole premise of this system (Karpathy's core
reframe in §2): a chat session is not durable storage. Anything agreed in
conversation that isn't written to a file by the end of the session is lost
the moment context resets — so "we agreed X" has to become a practice, not
an afterthought.

**Rule: after any non-trivial agreement in a session, it gets flushed to one
of two places before the session is considered done:**

- A **`decision` page** (§6.c type enum) if it's a standalone, structural
  choice worth its own page (e.g. everything already captured in this PRD).
- A **`log.md` entry** if it's smaller/incremental — doesn't warrant a full
  page, but still needs to exist as a fact on disk (e.g. "decided agent index
  is JSONL" is exactly this kind of item, now captured in §6 above rather
  than only living in chat).

This PRD itself has been operating this way already (every answered open
question gets written back into the doc rather than left in conversation) —
this section just makes that an explicit, named practice rather than an
implicit habit, so it carries over to the actual wiki/codemap once built.

## 10. Prototype status

`tools/codemap_gen/generate.py` — first working prototype of the codemap
generator (§5.1), built and smoke-tested self-hosted (ran against its own
source). Implements the §12 JSONL schema (`module`/`function`/`class`/`method`
records, anchors, signature-hash regen trigger, `EXTRACTED`/`INFERRED`
confidence tags) plus mirrored markdown output (§6.b structure decision).

Lives in this repo per your answer: build the tool here, run it from here
against whatever target repo's `--src` you point it at (`--out` stays a
parameter, per §6.b — not hardcoded to this repo).

**Tested against a real repo** (`ai-unify-companion`, `src/` — 55 files, 624
JSONL records, 5 sub-packages): ran clean. Found and fixed a real bug in the
process — `doc_ref` was written as an absolute host path
(`C:/Dev/projects/notes/...`) instead of relative to `--out`, which broke the
portability/diffability that was the whole point of choosing JSONL (§6.a-Q4,
§12). Fixed: `doc_ref` is now relative to `--out` (e.g. `activities/__init__.md`).
Output was a scratch folder in this repo, not written into the target repo,
and was deleted after verifying — no lasting changes to `ai-unify-companion`.

**Second bug found/fixed**: generated markdown never contained real markdown
links for imports/imported-by, just plain backticked text — so Obsidian's
graph view had nothing to draw edges from (every generated page showed as an
isolated dot). Fixed: `write_markdown` now builds a dotted-module-name →
`doc_ref` lookup and emits real relative links (e.g. `[activities.base](base.md)`)
for any import that resolves to another generated page; external
(stdlib/third-party) imports are still shown as plain text, tagged `(external)`.

**Third fix, implementing §13 point 2**: import edges are now usage-based,
not declaration-based. Verified with a synthetic test file: an unused
`from collections import OrderedDict` was correctly dropped from the
generated page's Imports list, while a used, aliased import (`import sys as
system`) and a used `from typing import Optional` were correctly kept.
Re-ran against `ai-unify-companion` afterward to confirm no regressions
(still 55 files, index regenerates cleanly).

**Fourth bug found/fixed** (found by you, walking `mcp_server/server.py` →
`mcp_server/tools/__init__.py` → `mcp_server/tools/tools.py` →
`mcp_server/_api.py` by hand in the real repo): package-level imports that
resolve to an `__init__.py` were showing as `(external)` instead of linking.
`from mcp_server.tools import _TOOLS` imports the dotted name
`mcp_server.tools`, but the file is `mcp_server/tools/__init__.py`, and the
lookup was keying it as `mcp_server.tools.__init__` — one segment too long,
so it never matched. Fixed: `_module_anchor` (and the two places deriving a
dotted module name from a path) now collapse a trailing `__init__` segment,
matching real Python import semantics. Confirmed fixed: `server.py`'s
`mcp_server.tools` import now links to `tools/__init__.md`; the rest of that
chain (`tools/__init__.py` → `tools/tools.py` → `mcp_server._api.py`) was
already correct since none of those are `__init__.py` files.

Known prototype limitations (not yet addressed):
- Python only (no tree-sitter multi-language support yet).
- Call resolution is same-file-only for `calls`; cross-file `called_by` is
  not yet implemented (only cross-file `imported_by` is, and only via a
  simple name match — genuinely `INFERRED`, sometimes wrong).
- No CI diff-check yet (§5.1) — regeneration is manual only.
- No hand-written-section preservation on regen yet (the markdown template
  has a placeholder comment for it, not implemented).
- No `queue/` or `wiki/` tooling yet (§8, §5.3) — codemap generator only.
- Function-level call-hierarchy layer (§13, points 5–6) not started — current
  Symbols table is still a flat per-file list, not caller-focused.

## 11. graphify — functional takeaways

Not adopting graphify wholesale (this PRD is explicitly about building our own
tooling to learn from / control), but it's a working implementation of almost
every idea here, so worth stealing from directly:

- **Confidence tags on edges** (`EXTRACTED` / `INFERRED` / `AMBIGUOUS`) —
  adopt this in our own agent-index format (§4a, §6.c option 3). Cheap and
  directly useful.
- **Separate output modes from one extraction pass**: graphify produces
  `graph.json` (machine query), `GRAPH_REPORT.md` (human overview), and
  optional `--wiki` ("agent-crawlable markdown wiki") / `--obsidian` (writes
  into an existing vault, never overwriting your own notes) as separate
  exporters off the same underlying graph — validates our "one extraction,
  two projections" design (§4c) and the vault-push pattern in §6.b option D.
- **query / path / explain** as the three core query verbs ("what connects
  to X", "shortest path between X and Y", "summarize X") — a good starting
  shape for our own codemap query tool's interface (§5.2), regardless of
  implementation.
- **Git-hook-driven regeneration** (rebuild on commit/branch-switch, `update`
  after pull, a merge driver so `graph.json` never gets conflict markers) —
  an alternative or complement to the CI-diff-check approach in
  [wiki/decision-plain-markdown-links.md](../../wiki/decision-plain-markdown-links.md): hooks keep it current automatically
  instead of only failing a check after the fact. Worth considering for our
  generator once it exists.
- **God nodes / community detection** for human orientation — a nice-to-have
  for the human path (§4b), not needed for v1.
- **Work-memory** (`save-result` / `reflect`, building a `LESSONS.md` from
  which past queries were actually useful) — an interesting future idea for
  the agent path (learning what worked across sessions), explicitly out of
  scope for now.
- **MCP server** exposing `query_graph`/`get_node`/`get_neighbors`/
  `shortest_path` — one candidate interface for our codemap query tool
  (§5.2), as an alternative to a plain CLI.
- Confirms staying **text-based / no forced vector DB or graph DB** is a
  reasonable default: graphify's core mode is exactly that (tree-sitter AST,
  no LLM, no embeddings for code); Neo4j/FalkorDB export exists but is opt-in,
  not required.

## 12. JSONL codemap-index schema (decided)

One file per repo: `codemap-index.jsonl`, one JSON object per line, two
record kinds distinguished by `kind`.

**File-level record** (one per source file):

```json
{"kind": "module", "path": "src/foo/bar.py", "doc_ref": "docs/codemap/foo/bar.md",
 "imports": ["foo.constants", "os"], "imported_by": ["foo.main"],
 "confidence": {"imported_by": "INFERRED"}, "hash": "sha1:..."}
```

**Symbol-level record** (one per function/class/method):

```json
{"kind": "function", "anchor": "foo.bar.render_diagram",
 "path": "src/foo/bar.py", "line": 42,
 "signature": "def render_diagram(spec: str, out: Path) -> None",
 "summary": "Renders a mermaid spec to a PNG at out.",
 "calls": ["foo.bar._invoke_mmdc"], "called_by": ["foo.main.convert"],
 "confidence": {"calls": "EXTRACTED", "called_by": "INFERRED"},
 "hash": "sha1:..."}
```

**Fields, in both record kinds:**

| Field | Meaning |
|---|---|
| `kind` | `module` (file-level) or `function` / `class` / `method` (symbol-level) |
| `path` | Repo-relative source file path |
| `anchor` | Stable id (`module.symbol`, dotted) — symbol-level only; this is what the query tool looks up, not `line` |
| `line` | Current line number — informational, not the anchor; not a regen trigger |
| `doc_ref` | Path to the corresponding generated human-facing markdown page (bridges agent index → human doc) |
| `signature` | Full signature, no body |
| `summary` | One-line docstring summary |
| `imports` / `calls` | Outgoing edges (module-level imports, symbol-level calls) |
| `imported_by` / `called_by` | Incoming edges — computed/derived, always `INFERRED` |
| `confidence` | Per-edge-field map of `EXTRACTED` (explicit in source, e.g. a direct `import` statement or direct call) vs. `INFERRED` (derived by resolving names) vs. `AMBIGUOUS` (couldn't resolve confidently) — borrowed from graphify (§11) |
| `hash` | Hash of the signature (not the body) — **the regen trigger**: only regenerate a record when this changes, so line-number-only edits don't cause churn |

**Query tool implication (§5.2)**: `query`/`path`/`explain` verbs operate over
this file by `anchor`, not `path`+`line`, so results stay valid across
unrelated edits elsewhere in the file.

## 13. Graph navigation — usage-driven, not folder-driven

Correction to the original design (§4b originally implied the graph mirrors
the folder structure). It doesn't — the point of the graph view is to
**navigate by usage**, following what actually calls/imports what, which is
a different shape than the directory tree. Worked through with you turn by
turn; final shape below.

**Terminology** (so this doesn't stay "dependency view" informally):
- **Dependency graph / import graph** — module-level: nodes are files,
  edges are "imports from."
- **Call hierarchy** — function-level: for one function, its **incoming
  calls / callers** (what you asked for — "who calls it") vs. **outgoing
  calls / callees** (what it calls). This is the same concept as VS Code's
  own "Call Hierarchy" feature, just for one function.
- The combination — always following usage rather than physical layout — is
  **usage-driven navigation**.

**Decisions:**

1. **Phased: module-level dependency graph first, function-level call
   hierarchy layer added after.** Not attempting both at once.
2. **Edges reflect actual usage, not just declared imports.** An import that
   is never referenced in the file must not create an edge — this needed a
   real change to the generator: after collecting `import`/`from...import`
   statements, scan the rest of the module for actual references to each
   imported name; only emit an edge for names that are genuinely used.
   Everything built so far (§10) was import-based only — this is a known gap
   to close, not yet implemented.
3. **No separate "folder" abstraction.** In Python the package path already
   *is* the dotted module name (`unify_api.datasets.upload_dataset`) — the
   hierarchy is baked into naming, so there's no need to invent folder/group
   nodes on top of it.
4. **No custom graph renderer.** The generator's only job is to emit correct
   relative markdown links; Obsidian's built-in graph view does the
   visualization. This was already close to working (§10's bug fix made
   links real) but needs the usage-based filtering from point 2 to stop
   showing edges for unused imports.
5. **Function-level nodes: anchors, not separate files** — go as far as
   Obsidian natively supports, no more. Obsidian's graph view only ever
   nodes on **files**, never on headings/sections within a file — a link to
   `bar.md#render_diagram` is fully clickable (works in Obsidian, and on
   GitHub) but still only draws a file-to-file edge in the graph view, not a
   function-to-function dot. Making functions actual separate graph dots
   would mean one `.md` file per function — rejected as disproportionate
   (would reopen the mirrored-per-file decision, §6.b, at a much finer grain
   than intended). So: functions get **anchors within their module's page**
   for click-through browsing and eventual "who calls this" call-hierarchy
   info, but the module/file stays the unit of graph-node granularity.
6. Consequence for the human-facing markdown page: the current flat "table
   of every function in the file" (§10's prototype output) isn't the end
   state for the function-level layer — once built, each function's entry
   should show **callers** (who calls it), not just its own signature, so
   the click-through story is "land on a function, see who uses it," not
   "see a symbol dump."

**Not yet implemented** (this section is a design decision, not a build
report): usage-based edge filtering (point 2), and the function-level
call-hierarchy layer (points 5–6) at all. §10's prototype only has the
old import-based, flat-symbol-table behavior.

[start-here](codemaps/excel-runner/start-here.md)
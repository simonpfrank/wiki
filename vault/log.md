# Log

Append-only, newest-first. Fixed prefix per entry so `grep "^## \[" log.md` works.

## [2026-09-17] decision | JSONL codemap-index schema specced

Locked the exact record shape: `module` (file-level) and `function/class/method`
(symbol-level) records, `anchor` as the stable query key (not path+line),
per-edge `confidence` (EXTRACTED/INFERRED/AMBIGUOUS), regen keyed to a
signature hash. Full schema in
[project/docs/prd_knowledge_system.md](project/docs/prd_knowledge_system.md) §11.

## [2026-09-17] decision | Vault schema doc drafted (AGENTS.md)

Added `AGENTS.md` at vault root — the Karpathy-pattern schema doc: layers,
navigation files, required front-matter, `/capture /sync /lint /digest`
conventions, task-queue execution rules, and the persistent-memory rule.
Linked from `index.md`.

## [2026-09-17] scaffold | Vault structure created

Created `index.md`, `log.md`, `wiki/`, `sources/`, `queue/` per the folder
layout decided in [project/docs/prd_knowledge_system.md](project/docs/prd_knowledge_system.md#6b-destination-vs-structure--two-separate-decisions).
Retired `project/codemap_notes.md` — its one durable decision (plain Markdown
links over wikilinks) migrated to [wiki/decision-plain-markdown-links.md](wiki/decision-plain-markdown-links.md);
everything else was already folded into the PRD (§7.b coverage check).

## [2026-09-17] decision | Agent index format locked to JSONL

One record per line — fast to grep/parse, appendable, diffable, no DB. See
[project/docs/prd_knowledge_system.md](project/docs/prd_knowledge_system.md), §6 item 4.

## [2026-09-17] decision | Task queue + persistent-memory practice added

`task` type redefined narrowly as an executable ticket (`queue/`, status
todo/in-progress/done/blocked); `concept` absorbed the old "how-to" write-up
use. Added the practice that any non-trivial agreement in a session gets
flushed to a `decision` page or here in `log.md` before the session ends. See
[project/docs/prd_knowledge_system.md](project/docs/prd_knowledge_system.md), §9–§10.

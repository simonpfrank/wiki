# Graph-shape experiments

Three small sets of hand-written documents, built to answer one question:

> Does Obsidian's graph view show a sequence if the links *are* a sequence?

Short answer: **yes, mostly.** The hairball in the generated codemap is caused by
our own link density, not by Obsidian. Degree (how many links a node has) is what
decides the shape.

Read these in graph view, **one folder at a time**, using the graph's search
filter so the other two don't interfere:

| Experiment | Filter to type into graph view | What it should show |
|---|---|---|
| 1. Pure chain | `path:1-chain` | A readable line: 6 nodes, one after another |
| 2. Branching tree | `path:2-tree` | A splayed tree: one root, three branches, two leaves each |
| 3. Chain + a hub | `path:3-hub` | The same chain as #1, wrecked by one index page |

Also turn on **Arrows** in graph view: Settings (gear) -> Display -> Arrows.
Without it the links are undirected and you lose the "which way does it flow"
information even when the shape is right.

## What each experiment is testing

**1-chain** — every page links to exactly one next page and nothing else. No
breadcrumbs, no back-links, no index. This is the minimum-degree case.

**2-tree** — a root that fans out to three children, each with two leaves.
Still no back-links. Tests whether branching survives (real call flows branch).

**3-hub** — identical to the chain, except every page also links back to an
index page, and the index links to all of them. One extra link per page. This
is what the generated codemap pages currently do with their `[Start here]`
breadcrumb.

## The point

If 3-hub looks materially worse than 1-chain, then the design rule is:

- **Navigational links (breadcrumbs, indexes, "back to top") destroy graph shape.**
  They are useful for clicking and poisonous for the graph.
- The two purposes conflict, so they may need to be separated: sparse,
  sequence-only link sets for the graph, with navigation handled some other way
  (front-matter, folder structure, or links that Obsidian doesn't count).

Nothing in this folder links out to the rest of the vault, on purpose — that
would re-create the hub problem across the whole thing.

_Note: this README deliberately uses plain code-formatted paths, not links,
so that it doesn't become a hub itself._

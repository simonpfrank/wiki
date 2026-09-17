#!/usr/bin/env python3
"""Codemap generator prototype.

Walks a Python source tree with the stdlib `ast` module and emits:

- `<out>/codemap-index.jsonl` — the agent-facing dense index (one JSON
  object per line; `module` records and `function`/`class`/`method` records),
  per docs/prd_knowledge_system.md §11.
- `<out>/<path-mirrors-src>/<file>.md` — one human-facing markdown page per
  source file (module responsibility + symbol table), mirroring the source
  tree per §6.b.

Usage:
    python generate.py --src <path-to-source-root> --out <path-to-output-root>

Scope (prototype): Python only, best-effort call resolution limited to
same-file top-level calls. Cross-file `imported_by`/`called_by` resolution is
a second pass done after all files are parsed.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SymbolRecord:
    kind: str  # "function" | "class" | "method"
    anchor: str
    path: str
    line: int
    signature: str
    summary: str
    calls: list[str] = field(default_factory=list)
    called_by: list[str] = field(default_factory=list)


@dataclass
class ModuleRecord:
    path: str
    doc_ref: str
    imports: list[str] = field(default_factory=list)
    imported_by: list[str] = field(default_factory=list)
    symbols: list[SymbolRecord] = field(default_factory=list)


def _one_line_summary(node: ast.AST) -> str:
    doc = ast.get_docstring(node, clean=True)
    if not doc:
        return ""
    return doc.strip().splitlines()[0].strip()


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
    try:
        args = ast.unparse(node.args)
    except Exception:
        args = ""
    returns = f" -> {ast.unparse(node.returns)}" if node.returns else ""
    return f"{prefix} {node.name}({args}){returns}"


def _hash(signature: str) -> str:
    return "sha1:" + hashlib.sha1(signature.encode("utf-8")).hexdigest()[:12]


def _module_anchor(rel_path: Path) -> str:
    # Python imports `pkg.sub`, not `pkg.sub.__init__`, even though the file
    # on disk is pkg/sub/__init__.py — collapse the trailing __init__ so
    # anchors/lookups match what actually appears in import statements.
    parts = list(rel_path.with_suffix("").parts)
    if len(parts) > 1 and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _collect_calls(node: ast.AST) -> list[str]:
    calls: list[str] = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call):
            fn = sub.func
            if isinstance(fn, ast.Name):
                calls.append(fn.id)
            elif isinstance(fn, ast.Attribute):
                calls.append(fn.attr)
    # de-dup, keep order
    seen: set[str] = set()
    out = []
    for c in calls:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


def parse_module(src_root: Path, out_root: Path, file_path: Path) -> ModuleRecord:
    rel_path = file_path.relative_to(src_root)
    module_anchor = _module_anchor(rel_path)
    # doc_ref is relative to out_root, not an absolute host path — keeps the
    # index portable/diffable regardless of where --out was run from.
    doc_ref = str(rel_path.with_suffix(".md").as_posix())

    text = file_path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(file_path))

    # (bound_name, target_module) for every import — bound_name is the name
    # that actually appears in code (respecting `as` aliases); target_module
    # is what we'd draw an edge to. Collected separately from usage so an
    # import that's declared but never referenced doesn't produce an edge
    # (PRD §13, point 2 — usage-based, not declaration-based).
    bindings: list[tuple[str, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                bound = alias.asname or alias.name.split(".")[0]
                bindings.append((bound, alias.name))
        elif isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                bound = alias.asname or alias.name
                bindings.append((bound, node.module))

    used_names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    imports = sorted({target for bound, target in bindings if bound in used_names})

    module_rec = ModuleRecord(path=str(rel_path.as_posix()), doc_ref=doc_ref, imports=imports)

    # top-level function name -> anchor, for same-file call resolution
    top_level_funcs = {
        node.name: f"{module_anchor}.{node.name}"
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            anchor = f"{module_anchor}.{node.name}"
            raw_calls = _collect_calls(node)
            resolved_calls = [top_level_funcs[c] for c in raw_calls if c in top_level_funcs and c != node.name]
            module_rec.symbols.append(
                SymbolRecord(
                    kind="function",
                    anchor=anchor,
                    path=module_rec.path,
                    line=node.lineno,
                    signature=_signature(node),
                    summary=_one_line_summary(node),
                    calls=resolved_calls,
                )
            )
        elif isinstance(node, ast.ClassDef):
            class_anchor = f"{module_anchor}.{node.name}"
            module_rec.symbols.append(
                SymbolRecord(
                    kind="class",
                    anchor=class_anchor,
                    path=module_rec.path,
                    line=node.lineno,
                    signature=f"class {node.name}",
                    summary=_one_line_summary(node),
                )
            )
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method_anchor = f"{class_anchor}.{sub.name}"
                    module_rec.symbols.append(
                        SymbolRecord(
                            kind="method",
                            anchor=method_anchor,
                            path=module_rec.path,
                            line=sub.lineno,
                            signature=_signature(sub),
                            summary=_one_line_summary(sub),
                        )
                    )

    return module_rec


def resolve_cross_file_edges(modules: list[ModuleRecord]) -> None:
    """Second pass: fill in imported_by (module-level) — INFERRED, best-effort."""
    for m in modules:
        m_name = _module_anchor(Path(m.path))
        for other in modules:
            if other is m:
                continue
            if any(imp == m_name or imp.endswith("." + m_name.split(".")[-1]) for imp in other.imports):
                m.imported_by.append(_module_anchor(Path(other.path)))


def write_jsonl(modules: list[ModuleRecord], out_root: Path) -> None:
    out_root.mkdir(parents=True, exist_ok=True)
    index_path = out_root / "codemap-index.jsonl"
    with index_path.open("w", encoding="utf-8") as f:
        for m in modules:
            rec = {
                "kind": "module",
                "path": m.path,
                "doc_ref": m.doc_ref,
                "imports": m.imports,
                "imported_by": sorted(set(m.imported_by)),
                "confidence": {"imported_by": "INFERRED"} if m.imported_by else {},
                "hash": _hash(",".join(m.imports)),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            for s in m.symbols:
                srec = {
                    "kind": s.kind,
                    "anchor": s.anchor,
                    "path": s.path,
                    "line": s.line,
                    "signature": s.signature,
                    "summary": s.summary,
                    "calls": s.calls,
                    "called_by": s.called_by,
                    "confidence": {"calls": "EXTRACTED"} if s.calls else {},
                    "hash": _hash(s.signature),
                }
                f.write(json.dumps(srec, ensure_ascii=False) + "\n")
    print(f"wrote {index_path}")


def _module_name(m: ModuleRecord) -> str:
    return _module_anchor(Path(m.path))


def _relative_link(from_doc: Path, to_doc: Path) -> str:
    """Relative markdown link href from one generated page to another."""
    return to_doc.relative_to(from_doc.parent, walk_up=True).as_posix()


def write_markdown(modules: list[ModuleRecord], out_root: Path) -> None:
    # dotted module name -> its ModuleRecord, so imports/imported_by that refer
    # to another generated page become real markdown links, not plain text —
    # without this, Obsidian's graph has nothing to draw edges from.
    by_name = {_module_name(m): m for m in modules}

    for m in modules:
        doc_path = out_root / m.doc_ref
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# `{m.path}`", "", "Generated codemap page — do not hand-edit above this line.", ""]
        if m.imports:
            lines += ["## Imports", ""]
            for i in m.imports:
                target = by_name.get(i)
                if target is not None:
                    href = _relative_link(doc_path, out_root / target.doc_ref)
                    lines.append(f"- [{i}]({href})")
                else:
                    lines.append(f"- `{i}` (external)")
            lines.append("")
        if m.imported_by:
            lines += ["## Imported by (INFERRED)", ""]
            for i in sorted(set(m.imported_by)):
                target = by_name.get(i)
                if target is not None:
                    href = _relative_link(doc_path, out_root / target.doc_ref)
                    lines.append(f"- [{i}]({href})")
                else:
                    lines.append(f"- `{i}`")
            lines.append("")
        if m.symbols:
            lines += ["## Symbols", "", "| Anchor | Signature | Summary |", "|---|---|---|"]
            for s in m.symbols:
                lines.append(f"| `{s.anchor}` | `{s.signature}` | {s.summary} |")
            lines.append("")
        lines += ["<!-- hand-written notes below this line are preserved on regen (not yet implemented in this prototype) -->", ""]
        doc_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {len(modules)} markdown page(s) under {out_root}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", required=True, type=Path, help="Source root to walk (Python files)")
    parser.add_argument("--out", required=True, type=Path, help="Output root for codemap-index.jsonl + mirrored markdown")
    args = parser.parse_args()

    src_root = args.src.resolve()
    out_root = args.out.resolve()

    py_files = sorted(src_root.rglob("*.py"))
    modules = [parse_module(src_root, out_root, f) for f in py_files]
    resolve_cross_file_edges(modules)

    write_jsonl(modules, out_root)
    write_markdown(modules, out_root)


if __name__ == "__main__":
    main()

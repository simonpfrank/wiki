#!/usr/bin/env python3
"""Orientation-map generator — EXPERIMENT v0. Disposable.

Not the codemap generator (`tools/codemap_gen/generate.py`). That one answers
"what symbols exist". This one tries to answer the six newcomer questions:

  1. How do I actually run this?
  2. Which parts are real (vs. dead/stale/superseded)?
  3. What are the handful of things that matter, and what is each for?
  4. What happens between "I run it" and "output appears"?
  5. This file is huge — what's in it and where do I start reading?
  6. If I want to change X, what do I touch?

Deliberately bounded: depth limits and per-node caps everywhere, because the
failure mode being designed against is cognitive overload, not incompleteness.

Usage:
    python orient.py --repo <path-to-repo-root> --out <path-to-output-root>
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import tomllib
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "build",
    "dist",
    "node_modules",
    ".tox",
    "site-packages",
}

MAX_TRACE_DEPTH = 4
MAX_CHILDREN_PER_NODE = 6
TOP_FILES_SHOWN = 8


# --------------------------------------------------------------------------
# model
# --------------------------------------------------------------------------


@dataclass
class Symbol:
    kind: str  # function | class | method
    name: str
    anchor: str
    module: str
    path: str
    line: int
    signature: str
    summary: str
    decorators: list[str] = field(default_factory=list)
    calls: set[str] = field(default_factory=set)
    call_order: list[str] = field(default_factory=list)
    ambiguous_calls: set[str] = field(default_factory=set)
    called_by: set[str] = field(default_factory=set)
    called_by_tests: set[str] = field(default_factory=set)
    status: str = "unknown"
    is_data_type: bool = False


@dataclass
class Module:
    path: str
    name: str
    role: str
    line_count: int
    is_test: bool
    symbols: list[Symbol] = field(default_factory=list)
    internal_imports: set[str] = field(default_factory=set)
    external_imports: set[str] = field(default_factory=set)
    imported_by: set[str] = field(default_factory=set)
    imported_by_tests: set[str] = field(default_factory=set)
    exports: list[str] = field(default_factory=list)
    module_calls: set[str] = field(default_factory=set)
    module_call_order: list[str] = field(default_factory=list)
    has_main_guard: bool = False
    status: str = "unknown"

    @property
    def doc_name(self) -> str:
        return f"{self.name}.md"


@dataclass
class EntryPoint:
    label: str  # how you invoke it
    anchor: str  # symbol/module anchor it lands on ("" if unresolved)
    evidence: str  # where we learned this


# --------------------------------------------------------------------------
# discovery
# --------------------------------------------------------------------------


def find_python_files(repo: Path) -> list[Path]:
    out: list[Path] = []
    for p in repo.rglob("*.py"):
        parts = set(p.relative_to(repo).parts)
        if parts & SKIP_DIRS or any(s.endswith(".egg-info") for s in parts):
            continue
        out.append(p)
    return sorted(out)


def dotted_name(rel: Path) -> str:
    parts = list(rel.with_suffix("").parts)
    if len(parts) > 1 and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def first_line(doc: str | None) -> str:
    if not doc:
        return ""
    # First sentence-ish: first non-empty line, trimmed.
    for ln in doc.strip().splitlines():
        if ln.strip():
            return ln.strip()
    return ""


def signature_of(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
    try:
        args = ast.unparse(node.args)
    except Exception:
        args = "..."
    returns = f" -> {ast.unparse(node.returns)}" if node.returns else ""
    return f"{prefix} {node.name}({args}){returns}"


def decorator_names(
    node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef,
) -> list[str]:
    names = []
    for d in node.decorator_list:
        try:
            names.append(ast.unparse(d))
        except Exception:
            pass
    return names


# --------------------------------------------------------------------------
# parse
# --------------------------------------------------------------------------


def parse_module(repo: Path, file_path: Path) -> Module:
    rel = file_path.relative_to(repo)
    name = dotted_name(rel)
    text = file_path.read_text(encoding="utf-8", errors="replace")
    tree = ast.parse(text, filename=str(file_path))

    mod = Module(
        path=rel.as_posix(),
        name=name,
        role=first_line(ast.get_docstring(tree, clean=True)),
        line_count=text.count("\n") + 1,
        is_test=(
            "tests" in rel.parts
            or "test" in rel.parts
            or rel.name.startswith("test_")
            or rel.name == "conftest.py"
        ),
    )

    # --- imports: bound name -> target ------------------------------------
    # module_bindings: bound name refers to a whole module (attribute calls)
    # symbol_bindings: bound name refers to a symbol inside a module
    module_bindings: dict[str, str] = {}
    symbol_bindings: dict[str, str] = {}
    all_targets: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                bound = alias.asname or alias.name.split(".")[0]
                module_bindings[bound] = alias.name
                all_targets.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level and node.level > 0:
                base = ".".join(
                    name.split(".")[: max(0, len(name.split(".")) - node.level + 1)]
                )
                target_mod = f"{base}.{node.module}" if node.module else base
            else:
                target_mod = node.module or ""
            if not target_mod:
                continue
            all_targets.add(target_mod)
            for alias in node.names:
                bound = alias.asname or alias.name
                symbol_bindings[bound] = f"{target_mod}.{alias.name}"
                module_bindings.setdefault(bound, f"{target_mod}.{alias.name}")

    used = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    used |= {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    mod._raw_import_targets = {  # type: ignore[attr-defined]
        t for b, t in list(module_bindings.items()) if b in used
    } | {t.rsplit(".", 1)[0] for b, t in symbol_bindings.items() if b in used}
    mod._module_bindings = module_bindings  # type: ignore[attr-defined]
    mod._symbol_bindings = symbol_bindings  # type: ignore[attr-defined]

    # --- __all__ ----------------------------------------------------------
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "__all__":
                    try:
                        mod.exports = [str(v) for v in ast.literal_eval(node.value)]
                    except Exception:
                        pass

    # --- symbols ----------------------------------------------------------
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            mod.symbols.append(
                Symbol(
                    kind="function",
                    name=node.name,
                    anchor=f"{name}.{node.name}",
                    module=name,
                    path=mod.path,
                    line=node.lineno,
                    signature=signature_of(node),
                    summary=first_line(ast.get_docstring(node, clean=True)),
                    decorators=decorator_names(node),
                )
            )
            mod.symbols[-1]._node = node  # type: ignore[attr-defined]
        elif isinstance(node, ast.ClassDef):
            cls_anchor = f"{name}.{node.name}"
            bases = ", ".join(ast.unparse(b) for b in node.bases) if node.bases else ""
            mod.symbols.append(
                Symbol(
                    kind="class",
                    name=node.name,
                    anchor=cls_anchor,
                    module=name,
                    path=mod.path,
                    line=node.lineno,
                    signature=(
                        f"class {node.name}({bases})" if bases else f"class {node.name}"
                    ),
                    summary=first_line(ast.get_docstring(node, clean=True)),
                    decorators=decorator_names(node),
                    is_data_type=looks_like_data_type(node),
                )
            )
            mod.symbols[-1]._node = node  # type: ignore[attr-defined]
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    mod.symbols.append(
                        Symbol(
                            kind="method",
                            name=f"{node.name}.{sub.name}",
                            anchor=f"{cls_anchor}.{sub.name}",
                            module=name,
                            path=mod.path,
                            line=sub.lineno,
                            signature=signature_of(sub),
                            summary=first_line(ast.get_docstring(sub, clean=True)),
                            decorators=decorator_names(sub),
                        )
                    )
                    mod.symbols[-1]._node = sub  # type: ignore[attr-defined]
                    mod.symbols[-1]._class = node.name  # type: ignore[attr-defined]
        else:
            if isinstance(node, ast.If):
                test = node.test
                if (
                    isinstance(test, ast.Compare)
                    and isinstance(test.left, ast.Name)
                    and test.left.id == "__name__"
                ):
                    mod.has_main_guard = True

    mod._tree = tree  # type: ignore[attr-defined]
    return mod


# --------------------------------------------------------------------------
# call resolution
# --------------------------------------------------------------------------


def call_targets(node: ast.AST) -> list[tuple[str | None, str]]:
    """(receiver, attr_or_name) for every call in a node's body, in source order.

    Source order matters: question 4 is "what happens when it runs", which is a
    *sequence*. Sorting these alphabetically (the first version did) turns a
    readable route into a meaningless list.
    """
    found: list[tuple[int, int, str | None, str]] = []
    for sub in ast.walk(node):
        if not isinstance(sub, ast.Call):
            continue
        fn = sub.func
        pos = (getattr(fn, "lineno", 0), getattr(fn, "col_offset", 0))
        if isinstance(fn, ast.Name):
            found.append((pos[0], pos[1], None, fn.id))
        elif isinstance(fn, ast.Attribute):
            recv = fn.value
            if isinstance(recv, ast.Name):
                found.append((pos[0], pos[1], recv.id, fn.attr))
            else:
                found.append((pos[0], pos[1], "?", fn.attr))
    found.sort(key=lambda t: (t[0], t[1]))
    return [(r, a) for _, _, r, a in found]


DATA_BASE_HINTS = (
    "Error",
    "Exception",
    "Enum",
    "BaseModel",
    "TypedDict",
    "NamedTuple",
    "Protocol",
)


def looks_like_data_type(node: ast.ClassDef) -> bool:
    """Dataclasses, exceptions and enums are *things*, not *steps*. Keeping them
    in the call trace buries the actual flow under type construction noise."""
    for d in node.decorator_list:
        try:
            if "dataclass" in ast.unparse(d):
                return True
        except Exception:
            pass
    for b in node.bases:
        try:
            txt = ast.unparse(b)
        except Exception:
            continue
        if any(h in txt for h in DATA_BASE_HINTS):
            return True
    return False


def resolve_calls(modules: dict[str, Module]) -> None:
    all_anchors = {s.anchor for m in modules.values() for s in m.symbols}
    # unique short-name index, used only as a last-resort AMBIGUOUS fallback
    by_short: dict[str, list[str]] = {}
    for m in modules.values():
        if m.is_test:
            continue
        for s in m.symbols:
            by_short.setdefault(s.name.split(".")[-1], []).append(s.anchor)

    for mod in modules.values():
        local: dict[str, str] = {}
        for s in mod.symbols:
            if s.kind in ("function", "class"):
                local[s.name] = s.anchor
        mbind = mod._module_bindings  # type: ignore[attr-defined]
        sbind = mod._symbol_bindings  # type: ignore[attr-defined]

        def resolve(
            recv: str | None, attr: str, owner_class: str | None
        ) -> tuple[str | None, bool]:
            # 1. plain name, defined in this file
            if recv is None:
                if attr in local:
                    return local[attr], False
                if attr in sbind and sbind[attr] in all_anchors:
                    return sbind[attr], False
                return None, False
            # 2. self.method() inside a class
            if recv == "self" and owner_class:
                cand = f"{mod.name}.{owner_class}.{attr}"
                if cand in all_anchors:
                    return cand, False
            # 3. imported_module.attr()
            if recv in mbind:
                cand = f"{mbind[recv]}.{attr}"
                if cand in all_anchors:
                    return cand, False
            # 4. local class instance: Foo().bar() where Foo is in this file
            if recv in local:
                cand = f"{local[recv]}.{attr}"
                if cand in all_anchors:
                    return cand, False
            # 5. last resort: globally-unique method name
            cands = by_short.get(attr, [])
            if len(cands) == 1 and cands[0] != attr:
                return cands[0], True
            return None, False

        for s in mod.symbols:
            node = getattr(s, "_node", None)
            if node is None:
                continue
            owner = getattr(s, "_class", None)
            for recv, attr in call_targets(node):
                target, ambiguous = resolve(recv, attr, owner)
                if target and target != s.anchor:
                    (s.ambiguous_calls if ambiguous else s.calls).add(target)
                    if not ambiguous and target not in s.call_order:
                        s.call_order.append(target)

        # module-level (top-of-file / __main__ guard) calls
        body_only = ast.Module(
            body=[
                n
                for n in mod._tree.body  # type: ignore[attr-defined]
                if not isinstance(
                    n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
                )
            ],
            type_ignores=[],
        )
        for recv, attr in call_targets(body_only):
            target, _ = resolve(recv, attr, None)
            if target:
                mod.module_calls.add(target)
                if target not in mod.module_call_order:
                    mod.module_call_order.append(target)

    # reverse edges — test callers are kept as a count, not as links, so a
    # source page never points at a test page that may not be generated.
    index = {s.anchor: s for m in modules.values() for s in m.symbols}
    for m in modules.values():
        bucket = "called_by_tests" if m.is_test else "called_by"
        for s in m.symbols:
            for t in s.calls | s.ambiguous_calls:
                if t in index:
                    getattr(index[t], bucket).add(s.anchor)
        for t in m.module_calls:
            if t in index:
                getattr(index[t], bucket).add(m.name)

    # module import edges
    for m in modules.values():
        for t in m._raw_import_targets:  # type: ignore[attr-defined]
            target = t if t in modules else t.rsplit(".", 1)[0]
            if target in modules:
                m.internal_imports.add(target)
                if m.is_test:
                    modules[target].imported_by_tests.add(m.name)
                else:
                    modules[target].imported_by.add(m.name)
            else:
                m.external_imports.add(t.split(".")[0])


# --------------------------------------------------------------------------
# entry points — question 1
# --------------------------------------------------------------------------


def find_entry_points(repo: Path, modules: dict[str, Module]) -> list[EntryPoint]:
    eps: list[EntryPoint] = []

    pyproject = repo / "pyproject.toml"
    if pyproject.exists():
        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        scripts = data.get("project", {}).get("scripts", {})
        for cmd, target in scripts.items():
            mod_part, _, fn = target.partition(":")
            anchor = f"{mod_part}.{fn}" if fn else mod_part
            eps.append(
                EntryPoint(
                    label=f"{cmd} ...",
                    anchor=anchor,
                    evidence="pyproject.toml [project.scripts]",
                )
            )

    for name, mod in modules.items():
        if mod.path.endswith("__main__.py"):
            pkg = name.rsplit(".", 1)[0] if "." in name else name
            anchor = next(iter(mod.module_calls), name)
            eps.append(
                EntryPoint(
                    label=f"python -m {pkg}",
                    anchor=anchor,
                    evidence=f"{mod.path} exists",
                )
            )
        elif mod.has_main_guard and not mod.is_test:
            eps.append(
                EntryPoint(
                    label=f"python {mod.path}",
                    anchor=next(iter(mod.module_calls), name),
                    evidence=f'`if __name__ == "__main__":` in {mod.path}',
                )
            )

    # library entry: top-level package __all__
    pkgs = [
        m
        for m in modules.values()
        if m.path.endswith("__init__.py") and "." not in m.name
    ]
    for pkg in pkgs:
        for exported in pkg.exports:
            anchor = None
            for cand in modules.values():
                for s in cand.symbols:
                    if s.name == exported and s.module.startswith(pkg.name):
                        anchor = s.anchor
                        break
                if anchor:
                    break
            eps.append(
                EntryPoint(
                    label=f"from {pkg.name} import {exported}",
                    anchor=anchor or "",
                    evidence=f"__all__ in {pkg.path}",
                )
            )
    return eps


def cli_arguments(
    repo: Path, modules: dict[str, Module], anchor: str
) -> list[tuple[str, str]]:
    """Pull `parser.add_argument(...)` out of the entry module, so the
    'how do I run it' answer includes the actual arguments, not just a command."""
    mod_name = anchor.rsplit(".", 1)[0]
    mod = modules.get(mod_name)
    if mod is None:
        return []
    args: list[tuple[str, str]] = []
    for node in ast.walk(mod._tree):  # type: ignore[attr-defined]
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "add_argument"
        ):
            flag = ""
            if node.args and isinstance(node.args[0], ast.Constant):
                flag = str(node.args[0].value)
            help_text = ""
            for kw in node.keywords:
                if kw.arg == "help":
                    try:
                        val = ast.literal_eval(kw.value)
                        help_text = " ".join(str(val).split())
                    except Exception:
                        help_text = "(dynamic)"
            if flag:
                args.append((flag, help_text))
    return args


def readme_commands(repo: Path) -> list[str]:
    readme = repo / "README.md"
    if not readme.exists():
        return []
    text = readme.read_text(encoding="utf-8", errors="replace")
    cmds: list[str] = []
    for block in re.findall(
        r"```(?:bash|sh|shell|console|powershell)?\n(.*?)```", text, re.S
    ):
        for ln in block.splitlines():
            ln = ln.strip().lstrip("$ ").strip()
            if ln.startswith(("python", "pip", "uv ", "poetry")) or "-runner" in ln:
                cmds.append(ln)
    seen, out = set(), []
    for c in cmds:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out[:6]


# --------------------------------------------------------------------------
# reachability — question 2
# --------------------------------------------------------------------------


def classify(
    modules: dict[str, Module], entries: list[EntryPoint]
) -> dict[str, set[str]]:
    edges: dict[str, set[str]] = {}
    for m in modules.values():
        edges[m.name] = set(m.module_calls)
        for s in m.symbols:
            edges[s.anchor] = s.calls | s.ambiguous_calls
            # a class being reachable makes its methods reachable
            if s.kind == "class":
                edges[s.anchor] |= {
                    o.anchor
                    for o in m.symbols
                    if o.kind == "method" and o.anchor.startswith(s.anchor + ".")
                }

    def reach(seeds: set[str]) -> set[str]:
        seen = set()
        q = deque(s for s in seeds if s)
        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            for nxt in edges.get(cur, ()):
                if nxt not in seen:
                    q.append(nxt)
        return seen

    entry_seeds = {e.anchor for e in entries if e.anchor}
    live = reach(entry_seeds)
    test_seeds = {m.name for m in modules.values() if m.is_test}
    test_seeds |= {s.anchor for m in modules.values() if m.is_test for s in m.symbols}
    test_reached = reach(test_seeds)

    registered: set[str] = set()
    for m in modules.values():
        if m.is_test:
            continue
        for s in m.symbols:
            if s.decorators and any(
                not d.startswith(
                    (
                        "property",
                        "staticmethod",
                        "classmethod",
                        "abstractmethod",
                        "dataclass",
                        "override",
                        "functools",
                        "cached_property",
                    )
                )
                for d in s.decorators
            ):
                registered.add(s.anchor)
    registered_reach = reach(registered)

    for m in modules.values():
        for s in m.symbols:
            if s.anchor in entry_seeds:
                s.status = "entry"
            elif s.anchor in live:
                s.status = "live"
            elif s.anchor in registered_reach:
                s.status = "registered"
            elif s.anchor in test_reached:
                s.status = "test-only"
            else:
                s.status = "unreached"
        if m.is_test:
            m.status = "test"
        else:
            kinds = {s.status for s in m.symbols}
            if {"entry", "live"} & kinds:
                m.status = "live"
            elif "registered" in kinds:
                m.status = "registered"
            elif "test-only" in kinds:
                m.status = "test-only"
            elif not m.symbols:
                m.status = "no-symbols"
            else:
                m.status = "unreached"

    return {"live": live, "test": test_reached, "registered": registered_reach}


# --------------------------------------------------------------------------
# markdown emit
# --------------------------------------------------------------------------


def anchor_link(
    target: str, modules: dict[str, Module], from_module: str | None
) -> str:
    """Markdown link to a symbol anchor, as seen from a module page (or root)."""
    mod_name = target
    while mod_name and mod_name not in modules:
        if "." not in mod_name:
            return f"`{target}`"
        mod_name = mod_name.rsplit(".", 1)[0]
    if not mod_name:
        return f"`{target}`"
    heading = target[len(mod_name) + 1 :]
    short = heading or mod_name
    if from_module == mod_name and heading:
        return f"[{short}](#{heading})"
    prefix = "" if from_module else "modules/"
    frag = f"#{heading}" if heading else ""
    return f"[{target}]({prefix}{mod_name}.md{frag})"


def build_trace(root: str, modules: dict[str, Module]) -> list[str]:
    index = {s.anchor: s for m in modules.values() for s in m.symbols}
    lines: list[str] = []
    visited: set[str] = set()
    skipped_types: set[str] = set()

    def children_of(anchor: str) -> list[str]:
        sym = index.get(anchor)
        raw = (
            sym.call_order
            if sym
            else modules[anchor].module_call_order if anchor in modules else []
        )
        out = []
        for c in raw:
            target = index.get(c)
            if target is not None and target.is_data_type:
                skipped_types.add(c)
                continue
            out.append(c)
        return out

    def walk(anchor: str, depth: int) -> None:
        sym = index.get(anchor)
        label = anchor_link(anchor, modules, None)
        note = f" — {sym.summary}" if sym and sym.summary else ""
        if anchor in visited:
            lines.append("  " * depth + f"- {label} _(shown earlier)_")
            return
        visited.add(anchor)
        lines.append("  " * depth + f"- {label}{note}")
        children = children_of(anchor)
        if depth >= MAX_TRACE_DEPTH:
            if children:
                lines.append(
                    "  " * (depth + 1)
                    + f"- _\u2026 {len(children)} more level(s) below — open the page to continue_"
                )
            return
        for child in children[:MAX_CHILDREN_PER_NODE]:
            walk(child, depth + 1)
        if len(children) > MAX_CHILDREN_PER_NODE:
            lines.append(
                "  " * (depth + 1)
                + f"- _(+{len(children) - MAX_CHILDREN_PER_NODE} more, not shown)_"
            )

    walk(root, 0)
    if skipped_types:
        lines += [
            "",
            f"_Data types / exceptions constructed along the way (omitted from the route): "
            + ", ".join(f"`{t.rsplit('.', 1)[-1]}`" for t in sorted(skipped_types))
            + "._",
        ]
    return lines


def write_start_here(
    out: Path,
    repo: Path,
    modules: dict[str, Module],
    entries: list[EntryPoint],
    traces: list[tuple[str, str]],
    test_count: int = 0,
) -> None:
    pyproject = repo / "pyproject.toml"
    desc = ""
    if pyproject.exists():
        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        desc = data.get("project", {}).get("description", "")

    L: list[str] = [f"# Start here — `{repo.name}`", ""]
    if desc:
        L += [f"> {desc}", ""]
    L += [
        "_Generated orientation map (experiment v0). Everything below is derived from the "
        "source — treat `INFERRED`/`ambiguous` markings as hints, not facts._",
        "",
    ]

    # Q1
    L += ["## 1. How do I run it", ""]
    runnable = [e for e in entries if not e.label.startswith("from ")]
    if runnable:
        L += ["| Command | Lands on | How we know |", "|---|---|---|"]
        for e in runnable:
            L.append(
                f"| `{e.label}` | {anchor_link(e.anchor, modules, None) if e.anchor else '—'} | {e.evidence} |"
            )
        L.append("")
    for e in runnable:
        args = cli_arguments(repo, modules, e.anchor) if e.anchor else []
        if args:
            L += [f"**Arguments for `{e.label}`**", ""]
            L += ["| Argument | Purpose |", "|---|---|"]
            for flag, help_text in args:
                L.append(f"| `{flag}` | {help_text} |")
            L.append("")
            break
    cmds = readme_commands(repo)
    if cmds:
        L += (
            ["**Commands found in the README:**", ""]
            + [f"- `{c}`" for c in cmds]
            + [""]
        )

    lib = [e for e in entries if e.label.startswith("from ")]
    if lib:
        L += [
            "**Or use it as a library** (public API — the only names the package promises):",
            "",
        ]
        for e in lib:
            L.append(
                f"- `{e.label}` → {anchor_link(e.anchor, modules, None) if e.anchor else '_unresolved_'}"
            )
        L.append("")

    # Q4
    if traces:
        L += ["## 2. What happens when it runs", ""]
        for label, fname in traces:
            L.append(
                f"- [{label}]({fname}) — bounded call trace, depth {MAX_TRACE_DEPTH}"
            )
        L.append("")

    # Q3
    src = [m for m in modules.values() if not m.is_test]
    ranked = sorted(
        src,
        key=lambda m: (
            0 if m.status in ("live",) else 1,
            -len(m.imported_by),
            -m.line_count,
        ),
    )
    L += [
        "## 3. The files that matter",
        "",
        "Ranked by: reachable from an entry point, then how many *other source* modules "
        "import it (test importers counted separately — they inflate everything), then "
        "size. Blunt on purpose — it is a starting order, not a truth.",
        "",
        "| # | Module | Lines | Used by (src) | Used by (tests) | Status | What it's for |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, m in enumerate(ranked[:TOP_FILES_SHOWN], 1):
        role = m.role or "_(no module docstring)_"
        if len(role) > 110:
            role = role[:107] + "..."
        L.append(
            f"| {i} | [{m.name}](modules/{m.doc_name}) | {m.line_count} | "
            f"{len(m.imported_by)} | {len(m.imported_by_tests)} | {m.status} | {role} |"
        )
    L.append("")
    if len(ranked) > TOP_FILES_SHOWN:
        L += [
            f"<details><summary>The other {len(ranked) - TOP_FILES_SHOWN} module(s)</summary>",
            "",
        ]
        for m in ranked[TOP_FILES_SHOWN:]:
            L.append(
                f"- [{m.name}](modules/{m.doc_name}) — {m.line_count} lines, {m.status}"
            )
        L += ["", "</details>", ""]

    # Q2
    counts: dict[str, int] = {}
    for m in src:
        counts[m.status] = counts.get(m.status, 0) + 1
    L += [
        "## 4. What's real and what can I ignore",
        "",
        "  ".join(f"**{k}**: {v}" for k, v in sorted(counts.items())),
        "",
        "See [liveness](liveness.md) for the per-symbol breakdown and the caveats "
        "(this is the least trustworthy page here — read the caveats).",
        "",
    ]
    if test_count:
        L += [
            f'_{test_count} test module(s) were read (so "only tests call this" is still '
            f"detected) but deliberately not given pages — rerun with `--include-tests` "
            f"if you want them._",
            "",
        ]

    # Q5
    biggest = sorted(src, key=lambda m: -m.line_count)[:3]
    L += ["## 5. The big files (start inside them, not at the top)", ""]
    for m in biggest:
        live_syms = sum(
            1 for s in m.symbols if s.status in ("live", "entry", "registered")
        )
        L.append(
            f"- [{m.name}](modules/{m.doc_name}) — {m.line_count} lines, "
            f"{len(m.symbols)} symbols ({live_syms} reached). "
            f"Its page opens with a what's-in-here map."
        )
    L.append("")

    (out / "start-here.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def write_liveness(out: Path, modules: dict[str, Module]) -> None:
    L = [
        "# Liveness — what's actually used",
        "",
        "[Start here](start-here.md)",
        "",
        "> **Caveats, read these first.** This is computed by following calls from the "
        "entry points, and Python defeats that in normal, non-suspicious ways: decorator "
        "registration, dynamic dispatch, callbacks held in dicts, `getattr`, plugin loading. "
        "`unreached` means *we could not find a caller*, **not** *it is dead*. Treat it as "
        "a list of things worth asking about.",
        "",
    ]
    buckets: dict[str, list[Symbol]] = {}
    for m in modules.values():
        if m.is_test:
            continue
        for s in m.symbols:
            buckets.setdefault(s.status, []).append(s)

    order = ["entry", "live", "registered", "test-only", "unreached"]
    blurb = {
        "entry": "Where execution starts.",
        "live": "Reachable by following calls from an entry point.",
        "registered": "Reached only via a decorator — almost certainly a registration/plugin "
        "mechanism. Real, but invisible to call-following.",
        "test-only": "No caller in the source; only tests reach it. Could be genuinely "
        "internal, could be leftover.",
        "unreached": "No caller found anywhere. Worth asking about — see caveats.",
    }
    for status in order:
        items = sorted(buckets.get(status, []), key=lambda s: s.anchor)
        if not items:
            continue
        L += [f"## {status} ({len(items)})", "", blurb[status], ""]
        for s in items:
            L.append(f"- {anchor_link(s.anchor, modules, None)} — `{s.path}:{s.line}`")
        L.append("")
    (out / "liveness.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def write_module_page(out: Path, mod: Module, modules: dict[str, Module]) -> None:
    L = [
        f"# {mod.name}",
        "",
        f"[Start here](../start-here.md) › `{mod.path}` · {mod.line_count} lines · "
        f"**{mod.status}**",
        "",
    ]
    if mod.role:
        L += [f"> {mod.role}", ""]

    if mod.symbols:
        L += [
            "## What's in here",
            "",
            "| Line | Symbol | Kind | Status | One-liner |",
            "|---|---|---|---|---|",
        ]
        for s in mod.symbols:
            heading = s.anchor[len(mod.name) + 1 :]
            summary = s.summary if len(s.summary) <= 90 else s.summary[:87] + "..."
            L.append(
                f"| {s.line} | [{s.name}](#{heading}) | {s.kind} | {s.status} | {summary} |"
            )
        L.append("")

    if mod.internal_imports or mod.external_imports:
        L += ["## Depends on", ""]
        for t in sorted(mod.internal_imports):
            L.append(f"- [{t}]({t}.md)")
        if mod.external_imports:
            L.append(
                f"- _external:_ "
                + ", ".join(f"`{e}`" for e in sorted(mod.external_imports))
            )
        L.append("")
    if mod.imported_by or mod.imported_by_tests:
        L += ["## Used by", ""]
        for t in sorted(mod.imported_by):
            L.append(f"- [{t}]({t}.md)" if t in modules else f"- `{t}`")
        if mod.imported_by_tests:
            L.append(f"- _{len(mod.imported_by_tests)} test module(s)_")
        L.append("")

    L += ["## Symbols", ""]
    for s in mod.symbols:
        heading = s.anchor[len(mod.name) + 1 :]
        L += [f"### {heading}", "", f"`{s.signature}`", ""]
        if s.summary:
            L += [s.summary, ""]
        facts = [f"`{mod.path}:{s.line}`", f"status: **{s.status}**"]
        if s.decorators:
            facts.append("decorated: " + ", ".join(f"`@{d}`" for d in s.decorators))
        L += ["  ·  ".join(facts), ""]
        if s.calls:
            L.append(
                "**Calls:** "
                + ", ".join(anchor_link(t, modules, mod.name) for t in sorted(s.calls))
            )
        if s.ambiguous_calls:
            L.append(
                "**Calls (ambiguous — name-matched only):** "
                + ", ".join(
                    anchor_link(t, modules, mod.name) for t in sorted(s.ambiguous_calls)
                )
            )
        if s.called_by:
            L.append(
                "**Called by:** "
                + ", ".join(
                    anchor_link(t, modules, mod.name) for t in sorted(s.called_by)
                )
            )
        if s.called_by_tests:
            L.append(f"**Called by tests:** {len(s.called_by_tests)} test symbol(s)")
        if not (s.calls or s.called_by or s.ambiguous_calls or s.called_by_tests):
            L.append("_No call edges found._")
        L.append("")

    L += ["---", "", "[Start here](../start-here.md) · [Liveness](../liveness.md)", ""]
    (out / "modules" / mod.doc_name).write_text("\n".join(L) + "\n", encoding="utf-8")


def write_jsonl(out: Path, modules: dict[str, Module], include_tests: bool) -> None:
    with (out / "codemap-index.jsonl").open("w", encoding="utf-8") as f:
        for m in sorted(modules.values(), key=lambda x: x.name):
            if m.is_test and not include_tests:
                continue
            f.write(
                json.dumps(
                    {
                        "kind": "module",
                        "name": m.name,
                        "path": m.path,
                        "doc_ref": f"modules/{m.doc_name}",
                        "role": m.role,
                        "status": m.status,
                        "lines": m.line_count,
                        "imports": sorted(m.internal_imports),
                        "imported_by": sorted(m.imported_by),
                        "imported_by_test_count": len(m.imported_by_tests),
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            for s in m.symbols:
                f.write(
                    json.dumps(
                        {
                            "kind": s.kind,
                            "anchor": s.anchor,
                            "path": s.path,
                            "line": s.line,
                            "signature": s.signature,
                            "summary": s.summary,
                            "status": s.status,
                            "calls": sorted(s.calls),
                            "ambiguous_calls": sorted(s.ambiguous_calls),
                            "called_by": sorted(s.called_by),
                            "called_by_test_count": len(s.called_by_tests),
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument(
        "--include-tests",
        action="store_true",
        help="Also emit a page per test module. Off by default: tests are still parsed "
        "(they're needed for the 'test-only' liveness signal), they just don't get "
        "pages, because they swamp the graph and aren't what you're trying to read.",
    )
    args = ap.parse_args()

    repo = args.repo.resolve()
    out = args.out.resolve()
    (out / "modules").mkdir(parents=True, exist_ok=True)

    files = find_python_files(repo)
    modules: dict[str, Module] = {}
    for f in files:
        try:
            m = parse_module(repo, f)
        except SyntaxError as exc:
            print(f"  skip {f}: {exc}", file=sys.stderr)
            continue
        modules[m.name] = m

    resolve_calls(modules)
    entries = find_entry_points(repo, modules)
    classify(modules, entries)

    # Everything above needs the tests (reachability). Everything below is what
    # gets written, so tests drop out here unless asked for.
    test_count = sum(1 for m in modules.values() if m.is_test)
    emitted = {k: v for k, v in modules.items() if args.include_tests or not v.is_test}

    traces: list[tuple[str, str]] = []
    for e in entries:
        if e.label.startswith("from ") or not e.anchor:
            continue
        slug = "flow-" + re.sub(r"[^a-z0-9]+", "-", e.label.lower()).strip("-") + ".md"
        body = [
            "# Flow — `" + e.label + "`",
            "",
            "[Start here](start-here.md)",
            "",
            f"Call trace from {anchor_link(e.anchor, emitted, None)}, "
            f"max depth {MAX_TRACE_DEPTH}, max {MAX_CHILDREN_PER_NODE} children shown per "
            "step. Truncated on purpose — this is a route, not an inventory.",
            "",
        ]
        body += build_trace(e.anchor, emitted)
        body += ["", "---", "", "[Start here](start-here.md)", ""]
        (out / slug).write_text("\n".join(body) + "\n", encoding="utf-8")
        traces.append((e.label, slug))

    write_start_here(out, repo, emitted, entries, traces, test_count)
    write_liveness(out, emitted)
    for m in emitted.values():
        write_module_page(out, m, emitted)
    write_jsonl(out, emitted, args.include_tests)

    print(
        f"{len(emitted)} module page(s), "
        f"{sum(len(m.symbols) for m in emitted.values())} symbols -> {out}"
        + (
            f"  ({test_count} test module(s) parsed but not written)"
            if not args.include_tests
            else ""
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

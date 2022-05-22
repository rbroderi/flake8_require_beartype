from __future__ import annotations

import ast
import sys
from typing import Any
from typing import Generator

if sys.version_info >= (3, 8):  # pragma: >=3.8 cover
    import importlib.metadata as importlib_metadata
else:  # pragma: <3.8 cover
    import importlib_metadata

RBT001 = 'RBT001 Function missing @beartype'  # noqa: E501
RBT002 = 'RBT002 Method missing @beartype'  # noqa: E501


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: list[tuple[int, int, str]] = []
        self._from_imports: dict[str, str] = {}

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        for node_ in ast.walk(node):
            for child in ast.iter_child_nodes(node_):
                if isinstance(child, ast.FunctionDef):
                    setattr(child, 'parent', node_)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        is_method = False
        parent = getattr(node, 'parent', None)
        if parent is not None:
            is_method = True
        has_beartype = False
        for obj in node.decorator_list:
            if isinstance(obj, ast.Name) and obj.id == 'beartype':
                has_beartype = True
        if not has_beartype:
            for arg in node.args.args:
                if arg.arg not in {'self', 'cls', 'mcls'}:
                    if is_method:
                        self.errors.append(
                            (node.lineno, node.col_offset, RBT002),
                        )
                    else:
                        self.errors.append(
                            (node.lineno, node.col_offset, RBT001),
                        )
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(name)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)

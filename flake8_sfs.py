"""Check Python code String Formatting Style (SFS).

This is a plugin for the tool flake8 tool for checking Python source code.
"""

import ast

from flake8 import utils as stdin_utils

__version__ = "0.0.3"

plugin_prefix = "SFS"


class StringFormatStyleChecker:
    """Checker of Python code for string formatting style."""

    name = "flake8-sfs"
    version = __version__

    def __init__(self, tree, filename):
        """Initialise the plugin for a new Python file."""
        self.filename = filename
        self.tree = tree

    def run(self):
        """Check the string formatting style of this file."""
        if self.filename == "stdin":
            lines = stdin_utils.stdin_get_value()
            tree = ast.parse(lines)
        elif self.tree:
            tree = self.tree
        else:
            with open(self.filename) as f:
                tree = ast.parse(f.read())

        percent_bytes = set()
        percent_strings = set()
        format_method = set()
        str_format = set()
        f_strings = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.JoinedStr):
                # Might this be an f-string?
                if True or any(isinstance(_, ast.FormattedValue) for _ in node.values):
                    f_strings.add((node.lineno, node.col_offset))
            elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
                # Percent operator - could be string formatting
                if isinstance(node.left, ast.Num):
                    # Numerical modulo
                    continue
                elif isinstance(node.left, ast.Str):
                    # String!
                    percent_strings.add((node.lineno, node.col_offset))
                elif isinstance(node.left, ast.Bytes):
                    percent_bytes.add((node.lineno, node.col_offset))
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "format"
            ):
                if isinstance(node.func.value, ast.Str):
                    # String with a .format attribute...
                    format_method.add((node.lineno, node.col_offset))
                elif (
                    isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "str"
                    and isinstance(node.args[0], ast.Str)
                ):
                    # str.format("...", ...)
                    str_format.add((node.lineno, node.col_offset))

        # Avoid duplicate messages
        for msg_str, msg_values in (
            ("101 String literal formatting using percent operator.", percent_strings),
            ("102 Bytes literal formatting using percent operator.", percent_bytes),
            ("201 String literal formatting using format method.", format_method),
            ("202 String formatting with str.format('...', ...) directly.", str_format),
            ("301 String literal formatting using f-string.", f_strings),
        ):
            for line, col in sorted(msg_values):
                yield (line, col, plugin_prefix + msg_str, type(self))

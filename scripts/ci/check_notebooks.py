#!/usr/bin/env python3
"""Validate and execute every notebook in the repo, according to its
declared `content_status` notebook metadata:

  template    - a student-facing file with intentional blank/incomplete
                exercise cells. Only checked for valid notebook JSON;
                Python syntax and execution are not enforced, since a
                blank cell (or a deliberately incomplete one, e.g.
                `def foo():` with no body) is expected and not a bug.
  complete    - a fully worked file. Every code cell must parse as valid
                Python and the whole notebook must execute top-to-bottom
                without error.
  interactive - a fully worked file that calls input() by design (meant
                to be run interactively by a student). Code cells must
                parse as valid Python, but execution is skipped, since a
                headless kernel with no stdin can't satisfy input().

Every notebook must declare one of these three via
`metadata.content_status` - a missing or unrecognised value is a CI
failure, so new uploads can't silently skip being checked.
"""
import ast
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

REPO_ROOT = Path(__file__).resolve().parents[2]
EXECUTION_TIMEOUT_SECONDS = 180
MAGIC_OR_SHELL_LINE = re.compile(r"^\s*[!%]")
VALID_STATUSES = {"template", "complete", "interactive"}


def find_notebooks():
    return sorted(
        p for p in REPO_ROOT.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts
    )


def strip_non_python_lines(source: str) -> str:
    return "\n".join(
        "" if MAGIC_OR_SHELL_LINE.match(line) else line for line in source.splitlines()
    )


def check_syntax(nb) -> list[str]:
    errors = []
    for i, cell in enumerate(nb.cells):
        if cell.get("cell_type") != "code":
            continue
        source = strip_non_python_lines(cell.get("source", ""))
        try:
            ast.parse(source)
        except SyntaxError as exc:
            errors.append(f"cell {i}: SyntaxError: {exc}")
    return errors


def execute_notebook(nb) -> str | None:
    """Returns an error string on failure, None on success."""
    client = NotebookClient(
        nb,
        timeout=EXECUTION_TIMEOUT_SECONDS,
        kernel_name="python3",
        allow_errors=False,
    )
    try:
        client.execute()
    except CellExecutionError as exc:
        return str(exc).splitlines()[0]
    except Exception as exc:  # noqa: BLE001 - surface any kernel failure as a CI failure
        return f"{type(exc).__name__}: {exc}"
    return None


def main() -> int:
    notebooks = find_notebooks()
    if not notebooks:
        print("No notebooks found.")
        return 0

    failures = []
    counts = {"template": 0, "complete": 0, "interactive": 0}

    for path in notebooks:
        rel = path.relative_to(REPO_ROOT)
        try:
            nb = nbformat.read(path, as_version=4)
        except Exception as exc:  # noqa: BLE001
            failures.append((rel, [f"could not parse notebook JSON: {exc}"]))
            continue

        try:
            nbformat.validate(nb)
        except nbformat.ValidationError as exc:
            failures.append((rel, [f"nbformat validation failed: {exc}"]))
            continue

        status = nb.metadata.get("content_status")
        if status not in VALID_STATUSES:
            failures.append((
                rel,
                [
                    f"missing or invalid metadata.content_status ({status!r}); "
                    f"must be one of {sorted(VALID_STATUSES)}"
                ],
            ))
            continue
        counts[status] += 1

        if status == "template":
            continue  # JSON/nbformat validity is all that's required

        errors = check_syntax(nb)
        if errors:
            failures.append((rel, errors))
            continue

        if status == "interactive":
            continue  # syntax-checked, execution skipped by design

        error = execute_notebook(nb)
        if error:
            failures.append((rel, [error]))

    print(
        f"Checked {len(notebooks)} notebook(s): "
        f"{counts['template']} template, {counts['complete']} complete, "
        f"{counts['interactive']} interactive."
    )

    if failures:
        print("\nFAILURES:")
        for rel, errors in failures:
            print(f"  {rel}")
            for err in errors:
                print(f"    - {err}")
        return 1

    print("\nAll notebooks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

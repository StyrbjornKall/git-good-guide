# Copilot instructions

These are general conventions for this repository. They apply to all code, regardless of the specific project. Project- or domain-specific instructions (data sources, APIs, scientific context, etc.) should be added in a separate section below or in a project README that Copilot is pointed to.

## Project layout

- Source code lives under `src/<package_name>/`. Reusable logic goes here, not in `scripts/` or `notebooks/`.
- `scripts/` is for thin, runnable entry points (CLI-style). They should import from `src/`, not contain business logic themselves.
- `notebooks/` is for exploration only. Don't add logic here that should be reused — move it to `src/` and import it instead.
- `tests/` mirrors the structure of `src/`. New functions/classes should come with at least a basic test.
- Every package and subpackage under `src/` should have an `__init__.py`.

## Environment & dependencies

- Use **uv** for all dependency and environment management. Add new dependencies with `uv add <package>` (or `uv add --dev <package>` for dev-only tools) so `pyproject.toml` and `uv.lock` stay in sync. Don't call `pip install` directly.
- Never hardcode absolute file paths, credentials, or machine-specific config. Use the `.env` file loaded with `python-dotenv` (`load_dotenv()` + `os.getenv("VAR_NAME")`). If you introduce a new environment variable, add a placeholder entry to `.env.example` as well.
- Assume the package is installed as an editable install (`uv sync` / `pip install -e .`), so imports like `from <package_name>.module import thing` should work from scripts, tests, and notebooks.

## Code style

- All new functions and methods must have type hints for arguments and return values.
- All new functions, classes, and modules must have docstrings (one-line summary is fine for simple helpers; describe args/returns for anything non-trivial).
- Follow the formatting and linting rules in `ruff.toml`. Code should be ruff-clean — if you add a dependency or pattern that ruff flags, fix it rather than disabling the rule, unless there's a clear reason to ignore it (and if so, add an inline `# noqa: <rule>` with a short comment why).
- Prefer small, composable functions over long ones. If a function is doing several distinct things, split it.
- Comments should explain *why*, not *what* — the code should already make "what" clear via naming, types, and structure. Use these tags where relevant, as they're highlighted by the Better Comments extension:
  - `# TODO:` for planned work
  - `# FIXME:` for known issues / bugs
  - `# NOTE:` for important context or caveats
  - `# ?` for open questions

## Logging

- Use `loguru` for all logging — prefer to not use `print()` or the standard `logging` module in new code. If you encounter existing `print()` calls in code you're editing, consider replacing them with `logger` calls as part of the change.
- Use appropriate log levels (`debug` for verbose internals, `info` for normal progress, `warning`/`error` for problems).

## Data handling

- If using databases or polars, be explicit about dtypes/schemas where it matters (e.g. when reading CSVs), rather than relying on inference, to avoid silent type-coercion bugs.

## Testing & verification

- For new functions with non-trivial logic, add a small test in `tests/` covering at least the typical case and one edge case.
- If a change can't be verified automatically (e.g. it depends on external data or services), say so explicitly rather than assuming it works.

## General working style

- Make minimal, focused changes that match the existing structure and conventions of the repo rather than introducing a new pattern alongside an existing one.
- When adding a new dependency, prefer well-established, actively maintained packages, and explain briefly why it's needed.
- If a request is ambiguous or could be implemented in more than one reasonable way, briefly state the assumption you're making rather than silently picking one.
- Always update this instructions file when you notice something is missing or when making large updates to the repository. If making large edits with important changes, consider adding a brief summary of the changes in a separate .md file and notify the user to review it before adding its contents to this file.
- Always ask follow up questions if anything is unclear or you need more info to implement a request, rather than making assumptions or leaving it half-done.

---

## Project-specific notes

<!--
Add anything specific to this repository below: domain context, key
data sources, important business logic, naming conventions for this project,
things Copilot should never touch, etc.
-->
# Git good guide - from noob to ai bro

## If you just cloned this for using for a personal project
Then you should probably rename the venvs name and write a description in the `pyproject.toml` file.

```toml
[project]
name = "git-good-guide" # Rename this (it will be the name of your venv)
version = "0.1.0"
description = "Add your description here" # Write something meaningful here
...
```

## Background

you are noob. wanna git good? yeah, me too. Agent mode may be here to stay and help you with your daily work, but how can we help copilot do its best? And how can we at the same time become better coders?

A lot boils down to **good coding practice**!

## A good repo structure

**bad practice:** all files in a single dir, no subdirs, no structure --> you and copilot confused
**good practice:** this repo!

## Use vscode to your advantage

vscode is a fantastic editor and can help you fix typical problems and nicer ways of working by using settings and extensions! Every pro should have a .vscode dir in their repo!

Why? python is great because you can write a bunch of your own modules, but importing modules can be a hassle because of relative paths. You can cofigure better intellisence from vscode by adding ptyhon module paths in vscode's settings.

## Use editable installs with src layout

If your package code lives under `src/`, your editor can resolve imports, but Python at runtime still needs to know where that package is.

The clean, tool-agnostic way is an editable install.

**Pro note:** The pro explicitly says what is a package and not by adding a `__init__.py` file in each package. This tells python that "this is a package" and was necessary up to python 3.3 to make editable installs resolve easily. As of 3.4 this is not really necessary anymore but for good coding practices, we keep it!

### One-time setup per environment

Add this to pyptoject.toml

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

From the repository root:

```bash
# uv
uv sync

# pip (venv, system python, pyenv, etc.)
pip install -e .

# conda
conda activate <your-env>
pip install -e .
```

After this, imports like `from my_cool_package.logger.setup_logger import setup_logger` work from scripts, tests, and notebooks.

### Do I need to reinstall after every code change?

Usually no.

With editable install, changes in files under `src/` are picked up immediately.

Re-run install/sync only when you change packaging metadata, such as:

- dependencies in `pyproject.toml`
- package discovery/build config in `pyproject.toml`
- added console scripts/entry points

## Logging

Stop using print and start using a logger. Python's own logging module is quite complicated to use so we use loguru (a package) instead. You can use this out of the box, but to styalize things and keep track of log files we build a small wrapper to also catch print statements!

**benefits:** you will never have to rerun stuff because you forgot to check what a print said one year ago, just read the logs.

## .env file

hardcoded paths suck and it sucks having to run code on multiple machines like mithra, saga, and alvis where project directories are different. That's where .env files come in! A .env file is basically a file that keeps track of stuff that you need to run code but that changes across machines. Prime examples are paths!

A .env file's variables can be loaded into python using the `dotenv` package. Then variables can be loaded using os.getenv() which gives you access to paths (or other variables directly in the script)!

**benefit:** no need for hardcoded paths anymore, just keep a .env file on each machine and you're good!

## Code formatters

Code is great if it is formatted correctly. Dictionaries, newlines, tabs, etc all should follow rules to help you and your copilot understand and overview code quickly. A code formatter helps with this and is standard for good coding practice.

**Pro-tip:** use ruff and configure how to use it in the vscode settings. (currently it is formatting upon save of a file!)

## Specific tips for data scientists

### Pandas is slow

Pandas is pretty standard in our field, but it is not built for huge dataframes and big data. Enter Polars! Polars is almost a dropin replacement for pandas but extremely fast (even with millions of rows). Polars also integrates much better with databases, like SQL and duckdb and has better dtype control (more rigid - less forgiving - less chances for slip ups - better coding practice). Syntax is a bit wierd moving from pandas though.

**Pro-tip:** if pandas operations are taking up time, polars will likely get the job done way faster. Just run polars.from_pandas(df) and run the same thing!

### Duckdb

Databases are scary, but quite good. They are also quite convenient ways to store all data you need for a repo since it only requires moving a single .db file rather than hundreds of files...

A new kid on the block i duckdb which integrates super well into python and polars/pandas. It is basically SQL but easier to work with and copilot has a very good understanding of how to use it. I use it in preprocessing pipelines to keep track of steps in the pipe and inspect changes. I keep convient tables, like mappings, settings etc in there as well.

**Pro-tip:** Try out duckdb if you work with big datasets that might require joining with other files. Then try out the polars integration and one converted to polars just run `to_pandas()` to get back into familiar territory.

### DBCode extension

Databases are har to overview (many different tables, large tables, complex indices). Try DBCode! A VScode extension that let's you inspect like any kind of database visually in vscode! Integrates very well with SQL and duckdb. E.g., try to inspect ncbi taxonomy!
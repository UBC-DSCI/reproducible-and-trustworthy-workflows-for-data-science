# Building a data analysis pipeline using GNU Make

Adapted from [Software Carpentry](http://software-carpentry.org/).

This example data analysis project counts the words in 4 novels.
It reports the 10 most frequent words in each book
in a [report](report/count_report.qmd).

## Set-up (first time only)

You need [uv](https://docs.astral.sh/uv/), [Quarto](https://quarto.org/) and GNU Make.
From the root of this project,
create the Python environment from `uv.lock`:

```bash
uv sync
```

## Run the analysis

Run the whole analysis, from counting the words to rendering the report:

```bash
uv run make all
```

`uv run` puts the project's environment first on the `PATH`,
so the `python` in the `Makefile` is the project's Python.
You can instead activate the environment
(`source .venv/bin/activate`, or `source .venv/Scripts/activate` in Git Bash on Windows)
and run `make all`.

Other targets in the `Makefile`:

- `make dats` counts the words and writes the `.dat` files.
- `make figs` makes the figures.
- `make clean-dats` and `make clean-figs` delete those files.
- `make clean-all` deletes every output, back to the starting point.

The shell script from the previous lesson, `run_all.sh`, still works too
(`uv run bash run_all.sh`).

## Dependencies

- GNU Make
- Quarto
- Python and the Python packages in `pyproject.toml` (locked in `uv.lock`):
    - `click`
    - `matplotlib`
    - `pandas`

# Building a data analysis pipeline using a shell script

Adapted from [Software Carpentry](http://software-carpentry.org/).

This example data analysis project counts the words in 4 novels.
It reports the 10 most frequent words in each book
in a [report](report/count_report.qmd).

## Set-up (first time only)

You need [uv](https://docs.astral.sh/uv/) and [Quarto](https://quarto.org/).
From the root of this project,
create the Python environment from `uv.lock`:

```bash
uv sync
```

## Run the analysis

The driver script `run_all.sh` runs every step,
from counting the words to rendering the report:

```bash
uv run bash run_all.sh
```

`uv run` puts the project's environment first on the `PATH`,
so the `python` in `run_all.sh` is the project's Python.
You can instead activate the environment
(`source .venv/bin/activate`, or `source .venv/Scripts/activate` in Git Bash on Windows)
and run `bash run_all.sh`.

## Dependencies

- Quarto
- Python and the Python packages in `pyproject.toml` (locked in `uv.lock`):
    - `click`
    - `matplotlib`
    - `pandas`

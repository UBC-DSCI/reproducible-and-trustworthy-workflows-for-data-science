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

The driver script `run_all.sh` runs every step,
from counting the words to rendering the report:

```bash
uv run bash run_all.sh
```

## Exercise

Add a "smarter" data analysis pipeline using GNU Make.
It should do the same as `run_all.sh` when you type:

```bash
uv run make all
```

It should reset the analysis to the starting point
(the state when you first copied this repository)
when you type:

```bash
uv run make clean-all
```

## Dependencies

- GNU Make
- Quarto
- Python and the Python packages in `pyproject.toml` (locked in `uv.lock`):
    - `click`
    - `matplotlib`
    - `pandas`

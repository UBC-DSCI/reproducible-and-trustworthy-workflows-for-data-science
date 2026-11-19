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

Prefix each command with `uv run`,
or activate the environment first
(`source .venv/bin/activate`, or `source .venv/Scripts/activate` in Git Bash on Windows)
and leave `uv run` off.

Count the words:

```bash
uv run python scripts/wordcount.py \
    --input_file=data/isles.txt \
    --output_file=results/isles.dat
uv run python scripts/wordcount.py \
    --input_file=data/abyss.txt \
    --output_file=results/abyss.dat
uv run python scripts/wordcount.py \
    --input_file=data/last.txt \
    --output_file=results/last.dat
uv run python scripts/wordcount.py \
    --input_file=data/sierra.txt \
    --output_file=results/sierra.dat
```

Create the plots:

```bash
uv run python scripts/plotcount.py \
    --input_file=results/isles.dat \
    --output_file=results/figure/isles.png
uv run python scripts/plotcount.py \
    --input_file=results/abyss.dat \
    --output_file=results/figure/abyss.png
uv run python scripts/plotcount.py \
    --input_file=results/last.dat \
    --output_file=results/figure/last.png
uv run python scripts/plotcount.py \
    --input_file=results/sierra.dat \
    --output_file=results/figure/sierra.png
```

Render the report:

```bash
quarto render report/count_report.qmd
```

## Exercise

Add a data analysis pipeline using a shell script, called `run_all.sh`.
It should do everything above when you type:

```bash
uv run bash run_all.sh
```

## Dependencies

- Quarto
- Python and the Python packages in `pyproject.toml` (locked in `uv.lock`):
    - `click`
    - `matplotlib`
    - `pandas`

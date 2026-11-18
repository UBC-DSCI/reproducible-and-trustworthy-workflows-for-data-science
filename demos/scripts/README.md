# Scripts demo: non-interactive R and Python scripts

First pass, to be reviewed when taught.

This demo shows how to write R and Python scripts
and run them from the command line,
instead of running code interactively.
It covers:

- a `main()` function and script structure,
- saving results to a file instead of printing them,
- command-line arguments with `docopt` (R) and `click` (Python),
  first positional, then as named options,
- a YAML configuration file read by an R script and a Python script.

It is used in the chapter
[Non-interactive scripts](../../book/lectures/0810-scripts.qmd).

## Where it came from

Adapted from the DSCI 310 live-coding repository
<https://github.com/DSCI-310/2024-02-13-scripts>
(Daniel Chen, February 2024, MIT licence, kept in `LICENSE`).
The scripts themselves follow the chapter,
whose examples are by Tiffany Timbers,
so they have the chapter's file names rather than the repository's
(`01-print_mean_hp.R`, `cli.py` and so on).

## What is here

- `start/` is what the class starts from:
  the two data files in `data/`,
  and the R and Python environments
  (`DESCRIPTION` and `renv.lock` for docopt, readr, tidyverse and yaml;
  `pyproject.toml` and `uv.lock` for click, pandas and PyYAML).
  It has no `src/` and no `results/` folder.
  Making `results/` is part of the lesson
  (the chapter points out that a script cannot write to a folder that does not exist).
- `end/` has every script from the chapter in `src/`,
  a `config.yaml`, and an empty `results/` folder (kept by a `README.md`).
  When the chapter changes a script but keeps its name,
  `end/` keeps both versions under different names
  (`save_mean_hp.R`, `quick_csv_col_mean_options.R`, `sum_options.py`),
  so every example can be run.

## Live coding, from `start/` to `end/`

Copy `start/` somewhere outside this repository and run `git init` in it.
Then, from its root:

1. Restore the environments
   (`Rscript -e 'renv::restore()'` and `uv sync`).
2. Write `src/print_mean_hp.R` and run it with `Rscript src/print_mean_hp.R`.
3. Write `src/quick_titanic_fare_mean.R`, with a `main()` function.
4. Write `src/save_mean_hp.R`, which writes `results/mean_hp_col.csv`.
   Run it once before making `results/` to see it fail, then `mkdir results`.
5. Write `src/demo-docopt.R` and run `Rscript src/demo-docopt.R I LOVE MDS`
   to see the list that `docopt` returns.
6. Write `src/quick_titanic_col_mean.R`, which takes the column as an argument.
7. Write `src/quick_csv_col_mean.R`, which also takes the file,
   and run it on both data files.
8. Change it to named options (`src/quick_csv_col_mean_options.R`)
   and run it with the options in either order.
9. Write `src/sum.py` with `click` positional arguments,
   then `src/sum_options.py` with options,
   and run them with `uv run python`.
10. Write `config.yaml`, then `src/clean_data.R` and `src/clean_data.py`,
    which read it.

## Run `end/`

```bash
cd end
Rscript -e 'renv::restore(prompt = FALSE)'
uv sync --locked
Rscript src/print_mean_hp.R
Rscript src/quick_titanic_fare_mean.R
Rscript src/save_mean_hp.R
Rscript src/demo-docopt.R I LOVE MDS
Rscript src/quick_titanic_col_mean.R fare
Rscript src/quick_csv_col_mean.R data/gapminder.csv lifeExp
Rscript src/quick_csv_col_mean_options.R --var=fare --file_path=data/titanic.csv
Rscript src/clean_data.R --config=config.yaml
uv run python src/sum.py 5 7
uv run python src/sum_options.py --num1=5 --num2=7
uv run python src/clean_data.py --config=config.yaml
```

The scripts write `results/mean_hp_col.csv` and `results/titanic_clean.csv`.
Delete them afterwards with `rm results/*.csv`.

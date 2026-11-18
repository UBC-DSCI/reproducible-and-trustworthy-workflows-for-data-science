# Non-interactive scripts

In-class live coding: writing R and Python scripts
and running them from the command line.

## Set-up (first time only)

From the root of this project,
install the R packages locked in `renv.lock`
(opening `scripts-end.Rproj` in RStudio activates `renv` too):

```bash
Rscript -e 'renv::restore()'
```

and create the Python environment locked in `uv.lock`:

```bash
uv sync
```

## Data

- `data/titanic.csv` is the Titanic data set,
  from <https://raw.githubusercontent.com/ttimbers/rscript-demo/main/data/titanic.csv>
  (original source <https://biostat.app.vumc.org/wiki/Main/DataSets>).
- `data/gapminder.csv` is the Gapminder data,
  from <https://swcarpentry.github.io/r-novice-gapminder/data/gapminder-FiveYearData.csv>.

## Running the scripts

Run every script from the root of this project.

R scripts:

```bash
Rscript src/print_mean_hp.R
Rscript src/quick_titanic_fare_mean.R
Rscript src/save_mean_hp.R
Rscript src/demo-docopt.R I LOVE MDS
Rscript src/quick_titanic_col_mean.R fare
Rscript src/quick_csv_col_mean.R data/titanic.csv fare
Rscript src/quick_csv_col_mean.R data/gapminder.csv lifeExp
Rscript src/quick_csv_col_mean_options.R --file_path=data/titanic.csv --var=fare
Rscript src/quick_csv_col_mean_options.R --var=fare --file_path=data/titanic.csv
Rscript src/clean_data.R --config=config.yaml
```

Python scripts:

```bash
uv run python src/sum.py 5 7
uv run python src/sum_options.py --num1=5 --num2=7
uv run python src/clean_data.py --config=config.yaml
```

`save_mean_hp.R` writes `results/mean_hp_col.csv`,
and both `clean_data` scripts write `results/titanic_clean.csv`,
the path set in `config.yaml`.

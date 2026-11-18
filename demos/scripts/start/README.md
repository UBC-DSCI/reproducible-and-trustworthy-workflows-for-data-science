# Non-interactive scripts

In-class live coding: writing R and Python scripts
and running them from the command line.

## Set-up (first time only)

From the root of this project,
install the R packages locked in `renv.lock`
(opening `scripts-start.Rproj` in RStudio activates `renv` too):

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

## Running scripts

Put the scripts in `src/` and run them from the root of this project:

```bash
Rscript src/print_mean_hp.R
uv run python src/sum.py 5 7
```

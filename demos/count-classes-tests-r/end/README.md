# Demo of tests for functions used in data analysis

This repository shows how to set up unit tests
for functions that are used in a data analysis.
This is one step away from making an R package.

The demo data analysis is in `notebooks/eda.qmd`.
It calls a function, `count_classes()`,
which lives in `R/count_classes.R`
and calculates the number of observations in each class of a data set.

The tests for `count_classes()` live in `tests/testthat/test-count_classes.R`,
and the helper data for the tests lives in `tests/testthat/helper-count_classes.R`.
`testthat::test_dir("tests/testthat")` first runs any files that begin with `helper`
and then any files that begin with `test`.

Outside an R package, `testthat::test_dir()` uses testthat's 2nd edition,
so the test file turns on the 3rd edition with `local_edition(3)`.

## Run the tests

Restore the R packages with renv, then run the tests:

```bash
Rscript -e 'renv::restore(prompt = FALSE)'
Rscript -e 'testthat::test_dir("tests/testthat")'
```

To render the analysis
(it needs the Quarto CLI, and internet access to download the data):

```bash
quarto render notebooks/eda.qmd
```

This writes `notebooks/eda.html`.

## How the files were set up

Several `usethis` functions set up the files and folders:

- `usethis::use_r("count_classes")` creates `R/count_classes.R`.
- `usethis::use_testthat()` creates `tests/testthat/`.
  It also writes `tests/testthat.R`, which is only for packages,
  so we deleted it.
- `usethis::use_test("count_classes")` creates `tests/testthat/test-count_classes.R`.

`tests/testthat/helper-count_classes.R` was created by hand,
as there is no `usethis` function for it.

## Dependencies

R and the packages in `DESCRIPTION`
(dplyr, rmarkdown, testthat and tidyverse;
Quarto renders R code through knitr and rmarkdown),
locked in `renv.lock`.

# count-classes-tests-r

First pass, to be reviewed when taught.

This demo walks through the test-driven workflow for a function
that a data analysis uses,
without making an R package.
The function, `count_classes()`, counts the observations in each class of a data frame.
It lives in `R/`,
its tests and their helper data live in `tests/testthat/`,
`testthat::test_dir("tests/testthat")` runs the tests,
and the analysis document calls the function with `source()`.

It is used by
[Testing: R (testthat)](../../book/lectures/1020-testing-r-testthat.qmd),
in the section "Where do the function and test files go?".
The Python version is [count-classes-tests-python](../count-classes-tests-python/).

Adapted from Tiffany Timbers' <https://github.com/ttimbers/demo-tests-ds-analysis>
(the same files are also in <https://github.com/ttimbers/demo-tests-ds-analysis-r>).
The function, test data and tests here follow the chapter,
which has moved on from that repository.

## What is in it

- `start/` is an renv project with the Quarto analysis document `notebooks/eda.qmd`,
  which counts the classes inline with dplyr.
  It has no `R/` or `tests/` folder yet.
- `end/` adds the function in `R/count_classes.R`,
  the test data in `tests/testthat/helper-count_classes.R`,
  and the tests in `tests/testthat/test-count_classes.R`.
  The document sources the function instead of counting inline.

## Live coding from `start/` to `end/`

Copy `start/` out of this repository and run `git init` in it.
The numbered steps match the chapter's five steps.

0. Run `renv::restore()`, then `renv::install(c("testthat", "usethis"))`.
   `usethis::use_testthat()` needs testthat installed.
   usethis is a development tool, so it stays out of `DESCRIPTION` and the lockfile.
1. Run `usethis::use_r("count_classes")`
   and write the function's specification and roxygen documentation
   with an empty body.
2. Run `usethis::use_testthat()`
   and delete the `tests/testthat.R` it writes,
   because that file is only for packages.
   Run `usethis::use_test("count_classes")`
   and replace the example test with three empty `test_that()` blocks
   (expected use, edge cases, errors).
   At the top of the test file add
   `library(testthat)`, `local_edition(3)` and `source("../../R/count_classes.R")`.
3. Create `tests/testthat/helper-count_classes.R` by hand
   and write the code that makes the test data.
4. Fill in the `expect_*()` calls
   and run `testthat::test_dir("tests/testthat")`.
   All six expectations fail.
5. Write the function body and run the tests again.
   All six pass.
6. In `notebooks/eda.qmd`, add `source("../R/count_classes.R")`
   and replace the inline counting with `count_classes(cancer, Class)`.
7. Add `dplyr` and `testthat` to `Imports:` in `DESCRIPTION`
   and run `renv::snapshot()`.
   The project uses explicit snapshots (set in `renv/settings.json`),
   so the lockfile records only what `DESCRIPTION` lists, and what those packages need.

## Run `end/`

From this folder:

```bash
cd end
Rscript -e 'renv::restore(prompt = FALSE)'
Rscript -e 'testthat::test_dir("tests/testthat")'
```

The last line of the test output is `[ FAIL 0 | WARN 0 | SKIP 0 | PASS 6 ]`.

To render the analysis
(it needs the Quarto CLI, and internet access to download the data):

```bash
quarto render notebooks/eda.qmd
```

This writes `notebooks/eda.html`.

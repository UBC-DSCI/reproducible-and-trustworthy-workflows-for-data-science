# `vdiffr` demo: testing a pretty scatter plot

First pass, to be reviewed when taught.

This demo shows visual regression testing in R with
[`vdiffr`](https://vdiffr.r-lib.org/) and [`testthat`](https://testthat.r-lib.org/).
A function, `pretty_scatter()`, draws a styled `ggplot2` scatter plot of the
`palmerpenguins` data.
A test saves a snapshot of that plot as an SVG file,
and later runs fail if the plot changes.

It is used in the chapter
[Testing images](../../book/lectures/1040-testing-images.qmd),
in the sections "Visual regression testing with `vdiffr`" and "`vdiffr` demo"
(including the exercise).

## Where it came from

Adapted from Tiffany Timbers' <https://github.com/ttimbers/vdiffr-demo>
(last commit March 2022).
That repository has no licence file,
so the code and the snapshot here are credited to Tiffany Timbers.

## What is here

- `start/` is what the class starts from:
  `R/pretty_scatter.R`, an empty `tests/testthat/` folder
  (kept in git by `.gitkeep`) and an RStudio project file.
  It has no `renv`, so it uses the packages installed in your own R library.
- `end/` is the finished project:
  the same function, the test `tests/testthat/test-pretty_scatter.R`,
  the committed snapshot `tests/testthat/_snaps/pretty_scatter/pretty-scatter.svg`,
  and a `DESCRIPTION` and `renv.lock` that pin
  ggplot2 4.0.4, palmerpenguins 0.1.1, testthat 3.3.2 and vdiffr 1.0.9 on R 4.6.2.

## Live coding, from `start/` to `end/`

Before class, make sure ggplot2, palmerpenguins, testthat and vdiffr are installed,
plus shiny and diffviewer for `testthat::snapshot_review()`:

```r
install.packages(c("ggplot2", "palmerpenguins", "testthat", "vdiffr", "shiny", "diffviewer"))
```

1. Copy `start/` out of this repository, run `git init` in the copy,
   and open `vdiffr-pretty-scatter-start.Rproj` in RStudio or Positron.
2. Show `R/pretty_scatter.R`, then source it and draw the plot in the console:

   ```r
   source("R/pretty_scatter.R")
   library(palmerpenguins)
   library(ggplot2)
   pretty_scatter(penguins, bill_length_mm, bill_depth_mm) +
       labs(x = "Bill length (mm)", y = "Bill depth (mm)")
   ```

3. Create `tests/testthat/test-pretty_scatter.R`,
   either by hand or with `usethis::use_test("pretty_scatter")`
   (which writes a placeholder test to replace),
   and type the test from the chapter
   (copy it from [`end/tests/testthat/test-pretty_scatter.R`](end/tests/testthat/test-pretty_scatter.R)).
4. Run `testthat::test_dir("tests/testthat")` in the console.
   The first run records the snapshot and warns
   "Adding new file snapshot: 'tests/testthat/_snaps/pretty_scatter/pretty-scatter.svg'".
   Open the SVG to show what was saved.
5. Run `testthat::test_dir("tests/testthat")` again.
   It passes, because the plot matches the snapshot.
6. Remove `alpha = 0.8` from `R/pretty_scatter.R` and run the tests again.
   They fail with "Snapshot of `testcase` has changed".
   Run `testthat::snapshot_review()` to compare the old and new plots side by side,
   then either accept the new snapshot or put `alpha = 0.8` back.
7. Commit the function, the test and `tests/testthat/_snaps/`.

## The chapter's exercise

Students work on their own copy of `end/`
(copy it out, `git init`, open `vdiffr-pretty-scatter-end.Rproj`, run `renv::restore()`).

1. Run `testthat::test_dir("tests/testthat")` and check that the test passes.
2. Change something in `R/pretty_scatter.R` that changes the plot,
   such as the text size, the point colour, or `alpha = 0.8`.
3. Run `testthat::test_dir("tests/testthat")` again and see it fail
   with "Snapshot of `testcase` has changed".
   Run `testthat::snapshot_review()` to compare the two snapshots.
   It needs shiny and diffviewer, which `end/` does not lock,
   so it may ask to install them.
4. Add another plot function to `R/` and test it with `vdiffr::expect_doppelganger()`.
   There is no solution for this step here.

## Running `end/`

From a terminal, in `end/`:

```bash
Rscript -e "renv::restore(prompt = FALSE)"
Rscript -e "Sys.setenv(NOT_CRAN = 'true'); testthat::test_dir('tests/testthat')"
```

The last line of output should be `[ FAIL 0 | WARN 1 | SKIP 0 | PASS 1 ]`.
The warning is ggplot2's "Removed 2 rows containing missing values",
from the two penguins with no bill measurements.

In RStudio or Positron, open `vdiffr-pretty-scatter-end.Rproj`,
then run `renv::restore()` and `testthat::test_dir("tests/testthat")` in the console.

### Why `NOT_CRAN`

`vdiffr` snapshot tests are skipped on CRAN.
`testthat` decides it is "on CRAN" when R is not interactive
and the environment variable `NOT_CRAN` is not `"true"`.
So in a console the test runs,
but `Rscript -e 'testthat::test_dir("tests/testthat")'` from a terminal
skips the test with `Reason: On CRAN` and ends `[ FAIL 0 | WARN 1 | SKIP 1 | PASS 0 ]`,
even when the plot has changed.
Setting `NOT_CRAN` to `"true"` makes the test run.

## Changes from the source repository

- The snapshot was regenerated on 2026-11-18 with the versions above.
  It came out byte-identical to the 2022 snapshot in the source repository,
  which still passes with ggplot2 4.0.4 and vdiffr 1.0.9.
- `end/` has a `DESCRIPTION` and `renv` lockfile; the source had neither.
- `tests/testthat.R` is left out.
  The source's copy (`library(vdiffr-demo)` and `test_check("vdiffr-demo")`)
  is what `usethis::use_testthat()` writes outside an R package, and it does not run.
  `testthat::test_dir("tests/testthat")` does not need it.
  `start/` already has `tests/testthat/` so that `usethis::use_test()` does not write that file.
- `*.new.svg` is in `.gitignore`.
  `testthat` writes `pretty-scatter.new.svg` next to the snapshot when the test fails,
  and removes it when you accept the change or the test passes again.
- Not copied: the rendered `README.md` and `README_files/`,
  `img/snapshot-reviewer.png` (the book has it as `book/img/snapshot-reviewer.png`),
  and `tests/vdiffr.Rout.fail`.

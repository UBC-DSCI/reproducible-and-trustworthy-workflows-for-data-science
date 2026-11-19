# foofactors: start here

This folder is nearly empty on purpose.
In this demo you build the `foofactors` R package from nothing,
and `usethis::create_package()` writes the package skeleton for you.
The only files here are this README,
an RStudio project file,
a `.gitignore`,
and a `.Rbuildignore` that keeps the project file out of the built package.

## Before you start

Install the development tools once, outside any project:

```r
install.packages("devtools")  # also installs usethis, roxygen2 and testthat
```

## Set up

1. Copy this folder somewhere outside any other R project or git repository,
   and name the copy `foofactors`.
   `create_package()` uses the folder's name as the package's name.
2. Make it a git repository:

   ```bash
   cd foofactors
   git init
   ```

3. Open the folder in RStudio or Positron, and in the R console run:

   ```r
   usethis::create_package(".")
   ```

   This writes `DESCRIPTION`, `NAMESPACE`, `R/` and `.Rbuildignore`.
   In RStudio it also writes `foofactors.Rproj` and offers to reopen the folder as a package project.
   Say yes, so the Build pane appears.

## The code you are given

The function, for `R/fbind.R` (create it with `usethis::use_r("fbind")`):

```r
fbind <- function(a, b) {
  factor(c(as.character(a), as.character(b)))
}
```

Its test, for `tests/testthat/test-fbind.R` (create it with `usethis::use_test("fbind")`):

```r
test_that("fbind() binds factor (or character)", {
  x <- c("a", "b")
  x_fact <- factor(x)
  y <- c("c", "d")
  z <- factor(c("a", "b", "c", "d"))

  expect_identical(fbind(x, y), z)
  expect_identical(fbind(x_fact, y), z)
})
```

The second function, for `R/fcount.R`, uses forcats:

```r
fcount <- function(x) {
  forcats::fct_count(x, sort = TRUE)
}
```

The steps that turn these into a package,
and the finished package,
are in the course repository under `demos/foofactors/`.

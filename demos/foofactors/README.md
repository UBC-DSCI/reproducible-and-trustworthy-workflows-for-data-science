# foofactors: build a small R package with usethis and devtools

First pass, to be reviewed when taught.

## What it teaches

Building a small R package from nothing with `usethis` and `devtools`,
and what each of the essential package files does:
`DESCRIPTION`, `NAMESPACE`, `R/`, `man/*.Rd` and `tests/testthat/`.
The package has two functions,
`fbind()` (bind two factors) and `fcount()` (a sorted frequency table, using forcats).

Chapters that use it:

- [Packaging: R](../../book/lectures/1160-packaging-r.qmd)
  shows this package's `DESCRIPTION`, `R/fbind.R` and `man/fbind.Rd`.
- [Introduction to R & Python packages](../../book/lectures/1110-packaging.qmd)
  lists foofactors in its tour of R packages,
  and its learning objective "use `devtools` and `usethis` to create a small and simple R package".

## Where it came from

Adapted from Tiffany Timbers' <https://github.com/ttimbers/foofactors>,
which is Jenny Bryan's <https://github.com/jennybc/foofactors>
with Tiffany as author, URLs, and a GitHub Actions workflow.
Jenny's repository is the end product of the "Whole Game" chapter
in a draft of the second edition of [R Packages](https://r-pkgs.org).
The published [Whole Game](https://r-pkgs.org/whole-game.html) chapter
now builds a different package, regexcite, with the same workflow.

## Folders

- `start/`: nearly empty (a README with the given code, an `.Rproj`, `.gitignore` and `.Rbuildignore`).
  Copy it out to a folder named `foofactors` and `git init` it.
  It has no renv on purpose, since the class installs devtools globally and creates the package from nothing.
- `end/`: the finished package,
  with renv locking forcats (the package's dependency)
  and the development tools (devtools, usethis, roxygen2, testthat, covr, rmarkdown).

## Live-coding steps

Run these in the R console from the copied `foofactors` folder.
The code to paste is in `start/README.md`.

1. `usethis::create_package(".")` writes `DESCRIPTION`, `NAMESPACE`, `R/` and `.Rbuildignore`.
2. `usethis::use_r("fbind")`, paste `fbind()`, then `devtools::load_all()` and try it.
3. Run `devtools::check()`, which warns about the placeholder license ("Non-standard license specification").
4. Fill in `DESCRIPTION` (`Title`, `Description`, `Authors@R`),
   then `usethis::use_mit_license("Your Name")`.
5. Add the roxygen comment to `fbind()` (in RStudio: Code > Insert Roxygen Skeleton),
   then `devtools::document()` writes `man/fbind.Rd` and `export(fbind)` in `NAMESPACE`.
   Look at `?fbind`.
6. Run `devtools::check()` again, which now gives 0 errors, 0 warnings and 0 notes.
   `devtools::install()` and `library(foofactors)` in a fresh session.
7. `usethis::use_testthat()`, `usethis::use_test("fbind")`, paste the test, `devtools::test()`.
8. `usethis::use_package("forcats")` adds forcats to `Imports`.
   `usethis::use_r("fcount")`, paste `fcount()` and its roxygen comment, `devtools::document()`.
9. `usethis::use_readme_qmd()`, write the README, `devtools::build_readme()`
   (see [Run `end/`](#run-end) for running it inside renv).
10. `devtools::check()` one last time.

Steps 1 to 8 were replayed non-interactively on a copy of `start/`,
and the result passed `devtools::check()` with 0 errors, 0 warnings, 0 notes.

What the current tools write differs from `end/` in two places,
because `end/` keeps the `DESCRIPTION` the chapter shows:

- `usethis::use_testthat()` writes `testthat (>= 3.0.0)` and `Config/testthat/edition: 3`;
  `end/` has `testthat (>= 2.1.0)`.
- `create_package()` does not add `LazyData: true`; `end/` has it.

## Run `end/`

From the repository root:

```bash
cd demos/foofactors/end
Rscript -e 'renv::restore(prompt = FALSE)'
Rscript -e 'devtools::test()'
Rscript -e 'devtools::check()'
```

`devtools::check()` ends with `0 errors ✔ | 0 warnings ✔ | 0 notes ✔`.

To re-render the package's `README.md` from `README.qmd`,
which needs the Quarto CLI:

```bash
Rscript -e 'renv::install("quarto")'
Rscript -e 'Sys.setenv(RENV_CONFIG_AUTOLOADER_ENABLED = "FALSE"); devtools::build_readme()'
```

`devtools::build_readme()` renders a `README.qmd` with the quarto R package,
which renv does not record because no code in the package calls it.
It installs foofactors into a temporary library
and starts Quarto with that library on `R_LIBS_USER`.
Quarto then starts a new R session in this folder,
where `.Rprofile` would activate renv and drop the temporary library,
so `library(foofactors)` would fail.
Turning off renv's autoloader for that session keeps the temporary library.

The renv settings are `snapshot.type: implicit` and `snapshot.dev: true`,
so `renv::snapshot()` keeps the development tools.
renv finds devtools and roxygen2 through `foofactors-end.Rproj`
(`PackageUseDevtools`, `PackageRoxygenize`),
testthat and covr through `Suggests`,
and rmarkdown and knitr through `README.qmd`.
An explicit snapshot reads only `DESCRIPTION` and would drop devtools.

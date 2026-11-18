
<!-- README.md is generated from README.Rmd. Please edit that file -->

**NOTE: This is a toy package created for expository purposes, for the
Whole Game chapter of a draft of the second edition of [R
Packages](https://r-pkgs.org) (the published chapter now builds a
package called regexcite). It is not meant to actually be useful. If you
want a package for factor handling, please see
[forcats](https://forcats.tidyverse.org).**

### foofactors

Factors are a very useful type of variable in R, but they can also be
very aggravating. This package provides some helper functions for the
care and feeding of factors.

### Installation

``` r
devtools::install_github(
  "UBC-DSCI/reproducible-and-trustworthy-workflows-for-data-science",
  subdir = "demos/foofactors/end"
)
```

### Quick demo

Binding two factors via `fbind()`:

``` r
library(foofactors)
a <- factor(c("character", "hits", "your", "eyeballs"))
b <- factor(c("but", "integer", "where it", "counts"))
```

Before R 4.1.0, simply catenating two factors returned their integer
codes, a result most people didn’t expect. Since R 4.1.0, `c()` returns
a factor, with the levels of `a` followed by the levels of `b`:

``` r
c(a, b)
#> [1] character hits      your      eyeballs  but       integer   where it 
#> [8] counts   
#> Levels: character eyeballs hits your but counts integer where it
```

The `fbind()` function glues two factors together and returns a factor
whose levels are sorted.

``` r
fbind(a, b)
#> [1] character hits      your      eyeballs  but       integer   where it 
#> [8] counts   
#> Levels: but character counts eyeballs hits integer where it your
```

Often we want a table of frequencies for the levels of a factor. The
base `table()` function returns an object of class `table`, which can be
inconvenient for downstream work.

``` r
set.seed(1234)
x <- factor(sample(letters[1:5], size = 100, replace = TRUE))
table(x)
#> x
#>  a  b  c  d  e 
#> 19 19 21 22 19
```

The `fcount()` function returns a frequency table as a tibble with a
column of factor levels and another of frequencies:

``` r
fcount(x)
#> # A tibble: 5 × 2
#>   f         n
#>   <fct> <int>
#> 1 d        22
#> 2 c        21
#> 3 a        19
#> 4 b        19
#> 5 e        19
```

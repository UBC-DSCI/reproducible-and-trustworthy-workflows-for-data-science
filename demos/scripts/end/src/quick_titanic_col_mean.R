# author: Tiffany Timbers
# date: 2020-01-15

"This script calculates the mean for a specified column
from titanic.csv.

Usage: quick_titanic_col_mean.R <var>
" -> doc


library(tidyverse)
library(docopt)

opt <- docopt(doc)

main <- function(var) {

  # read in data
  data <- read_csv('data/titanic.csv')

  # print out statistic of variable of interest
  out <- data |>
    pull(.data[[var]]) |>
    mean(na.rm = TRUE)
  print(out)
}

main(opt$var)

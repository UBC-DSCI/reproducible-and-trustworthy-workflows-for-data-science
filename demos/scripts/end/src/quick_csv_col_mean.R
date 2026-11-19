# author: Tiffany Timbers
# date: 2020-01-15

"This script calculates the mean for a specified column
from titanic.csv.

Usage: quick_csv_col_mean.R <file_path> <var>
" -> doc


library(tidyverse)
library(docopt)

opt <- docopt(doc)

main <- function(file_path, var) {

  # read in data
  data <- read_csv(file_path)

  # print out statistic of variable of interest
  out <- data |>
    pull(.data[[var]]) |>
    mean(na.rm = TRUE)
  print(out)
}

main(opt$file_path, opt$var)

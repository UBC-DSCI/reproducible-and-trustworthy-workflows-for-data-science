# author: Tiffany Timbers
# date: 2020-01-15

"This script calculates the mean for a specified column
from titanic.csv.

Usage: quick_csv_col_mean_options.R --file_path=<file_path> --var=<var>

Options:
--file_path=<file_path>   Path to the data file
--var=<var>               Unquoted column name of the numerical vector for which to calculate the mean
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

# author: Tiffany Timbers
# date: 2020-01-15
#
# This script calculates the mean horsepower of the cars from the built-in
# R data frame `mtcars` and saves it to `results/mean_hp_col.csv`.
# This script takes no arguments.
#
# Usage: Rscript src/save_mean_hp.R

library(readr)

main <- function() {
  mean_hp <- mean(mtcars$hp)
  mean_hp <- data.frame(value = mean_hp)
  write_csv(mean_hp, "results/mean_hp_col.csv")
}

main()

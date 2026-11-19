# author: Tiffany Timbers
# date: 2020-01-15
#
# This script calculates the mean horsepower of the cars from the built-in
# R data frame `mtcars`. This script takes no arguments.
#
# Usage: Rscript src/print_mean_hp.R

mean_hp <- mean(mtcars$hp)
print(mean_hp)

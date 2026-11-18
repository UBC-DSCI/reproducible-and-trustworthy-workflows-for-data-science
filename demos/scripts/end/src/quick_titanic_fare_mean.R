# author: Tiffany Timbers
# date: 2020-01-15
#
# This script calculates the mean for the fare (ticket price)
# from titanic.csv. This script takes no arguments.
#
# Usage: Rscript src/quick_titanic_fare_mean.R

library(tidyverse)

main <- function() {
  data <- read_csv('data/titanic.csv')
  out <- data %>%
         pull(fare) %>%
         mean(na.rm = TRUE)
  print(out)
}

main()

# Limit output of data frame output to 10 lines
options(repr.matrix.max.rows = 10)

add_two_numbers <- function(x, y) {
  x + y
}

add_two_numbers(1, 4)

math_two_numbers <- function(x, y, operation) {
  if (operation == "add") {
    return(x + y)
  } 
  x - y
}

math_two_numbers (1, 4, "add")

math_two_numbers (1, 4, "subtract")

math_two_numbers <- function(x, y, operation = "add") {
  if (operation == "add") {
    return(x + y)
  } 
  x - y
}

math_two_numbers (1, 4)

math_two_numbers (1, 4, "subtract")

add <- function(x, y, ...) {
    print(list(...))
}
add(1, 3, 5, 6)

x <- 10

add_to_x <- function(to_add) {
    x <- 5
    to_add + x
}

add_to_x(2)

x <- 10

add_to_x <- function(to_add) {
    to_add + x
}

add_to_x(2)

add_to_x <- function(to_add) {
    to_add + x
}

x <- 10
add_to_x(2)

x <- 20
add_to_x(2)

x <- 10

add_to_x <- function(to_add) {
    x <- to_add + x
    x
}

add_to_x(2)
add_to_x(2)
add_to_x(2)

dplyr::select(mtcars, mpg, cyl, hp, qsec)

fahr_to_celsius <- function(temp) {
  (temp - 32) * 5/9
}

fahr_to_celsius <- function(temp) {
  if(!is.numeric(temp)) {    
    stop("`fahr_to_celsius` expects a vector of numeric values")
  }
  (temp - 32) * 5/9
}

library(tidyverse)
library(gapminder)

gapminder |>
  filter(country == "Canada", year == 1952)

gapminder[gapminder$country == "Canada" & gapminder$year == 1952, ]

filter_gap <- function(col, val) {
  filter(gapminder, {{col}} == val)
}

filter_gap(country, "Canada")

group_summary <- function(data, group, col, fun) {
  data |>
    group_by({{ group }}) |>
    summarise( {{ col }} := fun({{ col }}))
}

group_summary(gapminder, continent, gdpPercap, mean)

#' Converts temperatures from Fahrenheit to Celsius.
#'    
#' @param temp a vector of temperatures in Fahrenheit
#' 
#' @return a vector of temperatures in Celsius
#' 
#' @examples
#' fahr_to_celcius(-20)
fahr_to_celsius <- function(temp) {
    (temp - 32) * 5/9
}



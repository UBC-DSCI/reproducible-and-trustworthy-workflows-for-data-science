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

#' Count class observations
#'
#' Creates a new data frame with two columns, 
#' listing the classes present in the input data frame,
#' and the number of observations for each class.
#'
#' @param data_frame A data frame or data frame extension (e.g. a tibble).
#' @param class_col unquoted column name of column containing class labels
#'
#' @return A data frame with two columns. 
#'   The first column (named class) lists the classes from the input data frame.
#'   The second column (named count) lists the number of observations for each class from the input data frame.
#'   It will have one row for each class present in input data frame.
#'
#' @export
#'
#' @examples
#' count_classes(mtcars, am)
count_classes <- function(data_frame, class_col) {
  # returns a data frame with two columns: class and count
}

library(testthat)

test_that("`count_classes` should return a data frame or data frame extension", {
  # tests to be added here
})

test_that("`count_classes` should return a data frame, or data frame extension, 
with the number of rows that corresponds to the number of unique classes 
in the column passed to `class_col`", {
  # tests to be added here
})

test_that("`count_classes` should return a data frame, or data frame extension, 
whose values in the `count` column correspond to the number of observations 
for the group in the `class` column from the original data frame", {
  # tests to be added here
})

test_that("`count_classes` should throw an error when incorrect types 
are passed to `data_frame` and `class_col` arguments", {
  # tests to be added here
})

# function input for tests
five_classes_3_obs <- data.frame(class_lables = rep(c("class1", "class2", "class3", "class4", "class5"), 3))
two_classes_3_obs <- data.frame(class_lables = rep(c("class1", "class2"), 3))
two_classes_3_and_2_obs <- data.frame(class_lables = c(rep(c("class1", "class2"), 2), "class1"))
two_classes_3_and_1_obs <- data.frame(class_lables = c(rep("class1", 3), "class2"))
one_class_3_obs <- data.frame(class_lables = rep("class1", 3))
empty_df  <- data.frame(class_lables = character(0))
vector_class_labels <- rep(c("class1", "class2"), 3)
two_classes_3_obs_as_list <- list(class_lables = rep(c("class1", "class2"), 3))

# expected function output
five_classes_3_obs_output <- data.frame(class = c("class1", "class2", "class3", "class4", "class5"),
                                        count = rep(3, 5))
two_classes_3_obs_output <- data.frame(class = c("class1", "class2"),
                                count = c(3, 3))
two_classes_3_and_2_obs_output <- data.frame(class = c("class1", "class2"),
                                      count = c(3, 2))
two_classes_3_and_1_obs_output <- data.frame(class = c("class1", "class2"),
                                      count = c(3, 1))
one_class_3_obs_output <- data.frame(class = "class1",
                              count = 3)
empty_df_output <- data.frame(class = character(0),
                              count = numeric(0))

test_that("`count_classes` should return a tibble", {
  expect_s3_class(count_classes(two_classes_3_obs, class_lables), "tibble")
})

test_that("`count_classes` should return a data frame, or data frame extension, 
with the number of rows that corresponds to the number of unique classes 
in the column passed to `class_col`", {
  expect_equivalent(count_classes(five_classes_3_obs, class_lables), five_classes_3_obs_output)
  expect_equivalent(count_classes(two_classes_3_obs, class_lables), two_classes_3_obs_output)
  expect_equivalent(count_classes(one_class_3_obs, class_lables), one_class_3_obs_output)
  expect_equivalent(count_classes(empty_df, class_lables), empty_df_output)
})

test_that("`count_classes` should return a data frame, or data frame extension, 
whose values in the `count` column correspond to the number of observations 
for the group in the `class` column from the original data frame", {
  expect_equivalent(count_classes(two_classes_3_and_2_obs, class_lables), two_classes_3_and_2_obs_output)
  expect_equivalent(count_classes(two_classes_3_and_1_obs, class_lables), two_classes_3_and_1_obs_output)
})

test_that("`count_classes` should throw an error when incorrect types 
are passed to `data_frame` and `class_col` arguments", {
  expect_error(count_classes(two_classes_3_obs, vector_class_labels))
  expect_error(count_classes(two_classes_3_obs_as_list, class_lables))
})

#' Count class observations
#'
#' Creates a new data frame with two columns, 
#' listing the classes present in the input data frame,
#' and the number of observations for each class.
#'
#' @param data_frame A data frame or data frame extension (e.g. a tibble).
#' @param class_col unquoted column name of column containing class labels
#'
#' @return A data frame with two columns. 
#'   The first column (named class) lists the classes from the input data frame.
#'   The second column (named count) lists the number of observations for each class from the input data frame.
#'   It will have one row for each class present in input data frame.
#'
#' @export
#'
#' @examples
#' count_classes(mtcars, am)
count_classes <- function(data_frame, class_col) {
  if (!is.data.frame(data_frame)) {
    stop("`data_frame` should be a data frame or data frame extension (e.g. a tibble)")
  }

  data_frame |>
    dplyr::group_by({{ class_col }}) |>
    dplyr::summarize(count = dplyr::n()) |>
    dplyr::rename_at(1, ~ "class")
}

test_that("`count_classes` should return a tibble", {
  expect_s3_class(count_classes(two_classes_3_obs, class_lables), "data.frame")
})

test_that("`count_classes` should return a data frame, or data frame extension, 
with the number of rows that corresponds to the number of unique classes 
in the column passed to `class_col`", {
  expect_equivalent(count_classes(five_classes_3_obs, class_lables), five_classes_3_obs_output)
  expect_equivalent(count_classes(two_classes_3_obs, class_lables), two_classes_3_obs_output)
  expect_equivalent(count_classes(one_class_3_obs, class_lables), one_class_3_obs_output)
  expect_equivalent(count_classes(empty_df, class_lables), empty_df_output)
})

test_that("`count_classes` should return a data frame, or data frame extension, 
whose values in the `count` column correspond to the number of observations 
for the group in the `class` column from the original data frame", {
  expect_equivalent(count_classes(two_classes_3_and_2_obs, class_lables), two_classes_3_and_2_obs_output)
  expect_equivalent(count_classes(two_classes_3_and_1_obs, class_lables), two_classes_3_and_1_obs_output)
})

test_that("`count_classes` should throw an error when incorrect types 
are passed to `data_frame` and `class_col` arguments", {
  expect_error(count_classes(two_classes_3_obs, vector_class_labels))
  expect_error(count_classes(two_classes_3_obs_as_list, class_lables))
})

options(repr.plot.width = 4, repr.plot.height = 4)

cars_ggplot_scatter <- ggplot2::ggplot(mtcars, ggplot2::aes(hp, mpg)) + 
    ggplot2::geom_point()

cars_ggplot_scatter

cars_ggplot_scatter$layers[[1]]$geom

cars_ggplot_scatter$mapping$x

#' scatter2d 
#'
#' A short-cut function for creating 2 dimensional scatterplots via ggplot2.
#'
#' @param data data.frame or tibble
#' @param x unquoted column name to plot on the x-axis from data data.frame or tibble
#' @param y unquoted column name to plot on the y-axis from data data.frame or tibble
#'
#' @return
#' @export
#'
#' @examples
#' scatter2d(mtcars, hp, mpg)
scatter2d <- function(data, x, y) {
    ggplot2::ggplot(data, ggplot2::aes(x = {{x}}, y = {{y}})) +
        ggplot2::geom_point()
}

helper_data <- dplyr::tibble(x_vals = c(2, 4, 6),
                   y_vals = c(2, 4, 6))

helper_plot2d <- scatter2d(helper_data, x_vals, y_vals)

test_that('Plot should use geom_point and map x to x-axis, and y to y-axis.', {
    expect_true("GeomPoint" %in% c(class(helper_plot2d$layers[[1]]$geom)))
    expect_true("x_vals"  == rlang::get_expr(helper_plot2d$mapping$x))
    expect_true("y_vals" == rlang::get_expr(helper_plot2d$mapping$y))
})

cars_scatter <- plot(mtcars$hp, mtcars$mpg)

typeof(cars_scatter)
class(cars_scatter)

pretty_scatter <- function(.data, x_axis_col, y_axis_col) {
    ggplot2::ggplot(data = .data, 
                    ggplot2::aes(x = {{ x_axis_col }}, y = {{ y_axis_col }})) +
        ggplot2::geom_point(alpha = 0.8, colour = "steelblue", size = 3) +
        ggplot2::theme_bw() +
        ggplot2::theme(text = ggplot2::element_text(size = 14))
}

library(palmerpenguins)
library(ggplot2)
penguins_scatter <- pretty_scatter(penguins, bill_length_mm, bill_depth_mm) + 
    labs(x = "Bill length (mm)", y = "Bill depth (mm)")
penguins_scatter

library(testthat)

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

test_data <- dplyr::tibble(x_vals = c(2, 4, 6),
                   y_vals = c(2, 4, 6))

plot2d <- scatter2d(test_data, x_vals, y_vals)
plot2d

plot2d$layers

plot2d$layers[[1]]$geom

plot2d$layers[[1]]$geom

class(plot2d$layers[[1]]$geom)

plot2d$mapping$x

rlang::get_expr(plot2d$mapping$x)

test_that('Plot should use geom_point and map x to x-axis, and y to y-axis.', {
    expect_true("GeomPoint" %in% c(class(plot2d$layers[[1]]$geom)))
    expect_true("x_vals"  == rlang::get_expr(plot2d$mapping$x))
    expect_true("y_vals" == rlang::get_expr(plot2d$mapping$y))
})

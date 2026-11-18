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
        dplyr::rename("class" = {{ class_col }})
}

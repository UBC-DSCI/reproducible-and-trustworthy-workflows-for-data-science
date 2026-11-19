library(testthat)
# `ignore_attr` needs testthat's 3rd edition. Outside an R package,
# testthat::test_dir() defaults to the 2nd edition, so we turn on the 3rd here.
local_edition(3)
source("../../R/count_classes.R")

test_that("`count_classes` should return a data frame, or tibble,
with the number of rows corresponding to the number of unique classes
in the `class_col` from the original dataframe. The new dataframe
will have a `class column` whose values are the unique classes,
and a `count` column, whose values will be the number of observations
for each  class", {
  expect_s3_class(count_classes(two_classes_2_obs, class_labels),
                  "data.frame")
  expect_equal(count_classes(two_classes_2_obs, class_labels),
               two_classes_2_obs_output, ignore_attr = TRUE)
  expect_equal(count_classes(two_classes_2_and_1_obs, class_labels),
               two_classes_2_and_1_obs_output, ignore_attr = TRUE)
})

test_that("`count_classes` should return a data frame, or tibble,
with one row if there is only one class,
and an empty data frame, or tibble, if the input data frame is empty", {
  expect_equal(count_classes(one_class_2_obs, class_labels),
               one_class_2_obs_output, ignore_attr = TRUE)
  expect_equal(count_classes(empty_df, class_labels),
               empty_df_output, ignore_attr = TRUE)
})

test_that("`count_classes` should throw an error when incorrect types
are passed to the `data_frame` argument", {
  expect_error(count_classes(two_classes_two_obs_as_list, class_labels))
})

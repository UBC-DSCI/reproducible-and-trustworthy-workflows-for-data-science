library(palmerpenguins)
library(ggplot2)
library(vdiffr)
source("../../R/pretty_scatter.R")

penguins_scatter <- pretty_scatter(penguins, bill_length_mm, bill_depth_mm) +
    labs(x = "Bill length (mm)", y = "Bill depth (mm)")
penguins_scatter

test_that("refactoring our code should not change our plot", {
    expect_doppelganger("pretty scatter", penguins_scatter)
})

options(repr.matrix.max.rows = 10)

add <- function(x, y) {
  x + y
}

add(5, 10)

add <- function(x, y) {
    if (!is.numeric(x) | !is.numeric(y)) {
        return(NA)
    }
    x + y
}

add(5, "a")

repeat_string <- function(x, n = 2) {
    repeated <- ""
    for (i in seq_along(1:n)) {
        repeated <- paste0(repeated, x)
    }
    repeated
}

repeat_string("MDS")

add <- function(x, y, ...) {
    total = x + y
    for (value in list(...)) {
        total <- total + value
    }
    total
    print(list(...))
}
add(1, 3, 5, 6)

x <- 1
g04 <- function() {
  y <- 2
  i <- function() {
    z <- 3
    c(x, y, z)
  }
  i()
}
g04()

g12 <- function() x + 1
x <- 15
g12()

x <- 20
g12()

g11 <- function() {
  if (!exists("a")) {
    a <- 1
  } else {
    a <- a + 1
  }
  a
}

g11()
g11()
g11()

head(mtcars, n = 2)

dplyr::select(mtcars, mpg, cyl, hp, qsec)

library(testthat)

x <- c(3.5, 3.5, 3.5)
y <- c(3.5, 3.5, 3.5)
test_that("x and y should contain the same values", {
    expect_equal(x, y)
})

x <- c(3.5, 3.5, 3.5)
y <- c(3.5, 3.5, 3.49999)
test_that("x and y should contain the same values", {
    expect_equal(x, y, tolerance = 0.00001)
})

celsius_to_fahr <- function(temp) {
  (temp * (9 / 5)) + 32
}

test_that("Temperature should be the same in Celcius and Fahrenheit at -40", {
        expect_identical(celsius_to_fahr(-40), -40)
    })
test_that("Room temperature should be about 23 degrees in Celcius and 73 degrees Fahrenheit", {
        expect_equal(celsius_to_fahr(23), 73, tolerance = 1)
    })

test_fahr_to_celsius <- function() {
    test_that("Temperature should be the same in Celcius and Fahrenheit at -40", {
        expect_identical(fahr_to_celsius(-40), -40)
    })
    test_that("Room temperature should be about 73 degrees Fahrenheit and 23 degrees in Celcius", {
        expect_equal(fahr_to_celsius(73), 23, tolerance = 1)
    })
}

fahr_to_celsius <- function(temp) {
    (temp + 32) * 5/9
}

fahr_to_celsius <- function(temp) {
    (temp - 32) * 5/9
}

test_fahr_to_celsius()

fahr_to_celsius <- function(temp) {
    if(!is.numeric(temp)){
        stop("Cannot calculate temperature in Farenheit for non-numerical values")
    }
    (temp - 32) * 5/9
}

test_that("Non-numeric values for temp should throw an error", {
    expect_error(fahr_to_celsius("thirty"))
    expect_error(fahr_to_celsius(list(4)))
    })

try({x <- data.frame(col1 = c(1, 2, 3, 2, 1), 
                     col2 = c(0, 1, 0, 0 , 1))
     x[3]
})
dim(x)

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

source("src/kelvin_to_celsius.R")

kelvin_to_celsius(273.15)

library(convertemp)

?celsius_to_kelvin

celsius_to_kelvin(0)

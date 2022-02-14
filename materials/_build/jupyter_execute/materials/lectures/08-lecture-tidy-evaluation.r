library(gapminder)
library(tidyverse)
options(repr.matrix.max.rows = 5)

gapminder

gapminder[gapminder$country == "Canada" & gapminder$year == 1952, ]

filter(gapminder, country == "Canada", year == 1952)

filter(gapminder, country == "Canada", year == 1952)

filter_gap <- function(col, val) {
    col <- enquo(col)
    filter(gapminder, !!col == val)
}

filter_gap(country, "Canada")

filter_gap <- function(col, val) {
    filter(gapminder, {{col}} == val)
}

filter_gap(country, "Canada")

# example of what we want to wrap: filter(gapminder, country == "Canada")
filter_gap <- function(col, val) {
    col <- sym(col)
    filter(gapminder, !!col == val)
}

filter_gap("country", "Canada")

group_summary <- function(data, group, col, fun) {
    data %>% 
        group_by({{ group }}) %>% 
        summarise( {{ col }} := fun({{ col }}))
}

group_summary(gapminder, continent, gdpPercap, mean)

sort_gap <- function(...) {
    arrange(gapminder, ...)
}

sort_gap(year)

sort_gap <- function(x, ...) {
    print(x + 1)
    arrange(gapminder, ...)
}

sort_gap(1, year, continent, country)

square_diff_n_select <- function(data, col_to_change, col_range) {
    data %>% 
        mutate({{ col_to_change }} := ({{ col_to_change }} - mean({{ col_to_change }}))^2) %>% 
        select({{col_range}})
}

square_diff_n_select(mtcars, mpg, mpg:hp)

square_diff_n_select <- function(data, col_to_change, ...) {
    data %>% 
        mutate({{ col_to_change }} := ({{ col_to_change }} - mean({{ col_to_change }}))^2) %>% 
        select(..., {{ col_to_change }})
}

square_diff_n_select(mtcars, mpg, drat, carb)

check_if_numeric <- function(data, col) {
    is.numeric(data %>% pull({{ col }}))
}

check_if_numeric(gapminder, pop)

square_diff_n_select <- function(data, col_to_change, ...) {
    if (!is.numeric(data %>% pull({{ col_to_change }}))) {
        stop('col_to_change must be numeric')
    }
    
    data %>% 
        mutate({{ col_to_change }} := ({{ col_to_change }} - mean({{ col_to_change }}))^2) %>% 
        select(..., {{ col_to_change }})
}

square_diff_n_select(gapminder, lifeExp, country, year)

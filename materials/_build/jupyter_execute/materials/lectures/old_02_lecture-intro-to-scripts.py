#!/usr/bin/env python
# coding: utf-8

# # Lecture 2 - Scaling up: read-eval-print-loop (REPL) processes versus non-interactive scripts

# ## Learning Objectives:
# 
# By the end of the lecture, students should be able to:
# 
# - Explain when it is optimal to work in a read-eval-print-loop (REPL) framework and when it is optimal to shift to using non-interactive scripts
# - Be able to create simple scripts in Python and R that can take input and be executed from the command line

# #### Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode) versus Scripts
# 
# - Up until now, we have primarily been using R and Python in an Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode)
# - Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode) is when we run our code in the console in R/Python, or in cells/chunks in the RStudio/Juptyer notebooks
# - A Read-eval-print-loop (REPL) framework (*i.e.,* interactive mode) is very useful for:
#     - solving small problems
#     - developing code that will be knit to an analytic report
#     - developing code that will be run as a script (i.e., in "batch" mode)

# ## What is a script?
# 
# An R/Python script is simply a plain text file containing (almost) the same commands that you would enter into R/Python's console or in cells/chunks in the RStudio/Juptyer notebooks. We often run these from top to bottom from the command line/unix shell.

# #### Why write scripts?
# 
# - Efficiency!
# - Automation!
# - Reusable!
# - Record of what you have done!

# ### Scripts in R

# Let's start with a small, simple example to demonstrate how we write and run scripts in R (it is very similar in Python and we will get to this later in the lesson).
# 
# Our script will be called `print_mean_hp.R`, and it will calculate the mean horsepower of the cars from the built-in R data frame `mtcars`. 
# 
# We will develop this script inside RStudio, make sure it works, and then run it from the command line/terminal/Git bash.
# 
# ##### Our first R script:
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# #
# # This script calculates the mean horsepower of the cars from the built-in 
# # R data frame `mtcars`. This script takes no arguments.
# #
# # Usage: Rscript print_mean_hp.R
# 
# mean_hp <- mean(mtcars$hp)
# print(mean_hp)
# ```
# 

# ##### Running our first R script
# 
# To run our R script, we need to open the command line/terminal/Git bash, and either navigate to the directory that houses the script OR point to it when we call it. We will do the former.
# 
# Then to run the R script, we use the `Rscript` command, followed by the name/path to the file:
# 
# ```
# Rscript print_mean_hp.R
# ```
# 
# The output should be:
# 
# ```
# [1] 146.6875
# ```

# #### A couple notes about scripts
# 
# - If you want something to be output to the command line/terminal/Git bash, you **should** explicitly ask for it to be print. *This is not an absolute requirement in R, but it is in Python!*
# - Similar with figures, they need to be saved! You will never see a figure created in a script unless you write it to a file.
# - From a reproducibility perspective, if we want input from the user, usually we will design the scripts to take command line arguments, and not use keyboard/user prompts.
# 

# ### Script structure and organization
# 
# Although not necessary in R or Python, it is still good practice and advised to organize the code in your script into a main function and other functions. This practice keeps your code readable and organized, this has some additional benefits we will discuss later.
# 
# ##### Example R script organization:
# ```
# # documentation comments
# 
# # import libraries/packages
# 
# # parse/define command line arguments here
# 
# # define main function
# main <- function(){
#     # code for "guts" of script goes here
# }
# 
# # code for other functions & tests goes here
# 
# # call main function
# main()
# ```
# 
# 
# 
# 

# ##### Example Python script organization:
# ```
# # documentation comments
# 
# # import libraries/packages
# 
# # parse/define command line arguments here
# 
# # define main function
# def main():
#     # code for "guts" of script goes here
# 
# # code for other functions & tests goes here
# 
# # call main function
# if __name__ == "__main__":
#     main()
# ```

# *You can see that R and Python scripts should have roughly the same style. There is the difference of `if __name__ == "__main__":` in Python scripts, and R does not really have an equivalent. The benefit of some control flow around `main`, as is done in Python, is so that you could import or source the other functions in the script without running the `main` function.* 
# 
# *You can do something like this in R (although I am not sure how commonly it is done - I more often see folks instead typically abstract the other functions into another script and source that, or create an R package):*
# 
# ```
# if (getOption('run.main', default = FALSE)) {
#   main()
# }
# ```
# 
# *I made a demo and you can find it here: [https://github.com/ttimbers/if_name_equals_main](https://github.com/ttimbers/if_name_equals_main)*

# ## Scripts in R:

# Here we write a script called `quick_titanic_fare_se.R` which reads in the [titanic dataset](https://github.ubc.ca/ubc-mds-2016/datasets/raw/master/data/titanic.csv) and calculates the standard error for the fare (ticket price) variable.
# 
# Our script has two functions, a function we defined to calculate the standard error of the mean (such a function does not exist in R) and a `main` function which runs the "body" of our code.
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# #
# # This script calculates the standard error for the fare (ticket price)
# # from titanic.csv. This script takes no arguments.
# #
# # Usage: quick_titanic_fare_se.R
# 
# library(tidyverse)
# library(testthat)
# 
# main <- function() {
# 
#   # read in data
#   data <- read_csv('data/titanic.csv')
# 
#   # print out statistic of variable of interest
#   out <- data %>%
#     pull(fare) %>%
#     sterror()
#   print(out)
# }
# 
# #' calculate standard error
# #'
# #' @param x a vector of numeric values
# #' @return the standard error of x as a numeric vector of length one
# #' @examples
# #' sterror(mtcars$hp)
# sterror <- function(x) {
#   sd(x, na.rm = TRUE) / sqrt(length(x))
# }
# 
# test_that("sterror should return 0 if vector values are all the same", {
#     expect_equal(sterror(c(1, 1, 1)), 0)
# })
# 
# main()
# ```

# #### Note on functions and tests in scripts
# 
# There are different levels of abstraction, that also scale with project complexity and importance. For now, its OK to put our functions and tests inside the scripts we call to "run" our analysis. However, as these grow in size and complexity we will want to abstract these to their own `.R` and `.py` files and take advantage of testing software that can automate the running of tests. This can also be paired with version control so that the tests are run everytime code is pushed to GitHub (we call this continuous integration). We will learn more about this later in this and follow-on courses.

# ### Using command line arguments in R
# Let's make our script more flexible, and let us specify when we call the script, what variable we want to calculate the standard error for.
# 
# To do this, we use the `docopt` R package. This will allow us to collect the text we enter at the command line when we call the script, and make it available to us when we run the script. 
# 
# When we run `docopt` it takes the text we entered at the command line and gives it to us as a named list of the text provided after the script name. The names of the items in the list come from the documentation. Whitespace at the command line is what is used to parse the text into separate items in the vector.
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# 
# "This script calculates the standard error for the fare (ticket price)
# from titanic.csv. This script takes no arguments.
# 
# Usage: quick_titanic_fare_se.R <var>
# " -> doc
# 
# library(tidyverse)
# library(testthat)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# main <- function(var) {
# 
#   # read in data
#   data <- read_csv('data/titanic.csv')
# 
#   # print out statistic of variable of interest
#   out <- data %>%
#     pull({{var}}) %>%
#     sterror()
#   print(out)
# }
# 
# #' calculate standard error
# #'
# #' @param x a vector of numeric values
# #' @return the standard error of x as a numeric vector of length one
# #' @examples
# #' sterror(mtcars$hp)
# sterror <- function(x) {
#   sd(x, na.rm = TRUE) / sqrt(length(x))
# }
# 
# test_that("sterror should return 0 if vector values are all the same", {
#     expect_equal(sterror(c(1, 1, 1)), 0)
# })
# 
# main(opt$var)
# ```
# 
# And we would run a script like this from the command line as follows: 
# 
# ```
# Rscript src/quick_csv_stat.R fare
# ```

# Let's make our script even more flexible, and let us specify that dataset as well (we could then use it more generally on other files, such as the Gapminder `.csv`'s we saw in Block 1).
# 
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# 
# "This script calculates the standard error for any numerical vector
# from a csv file. This script takes an unquoted column name and a data file path.
# 
# Usage: quick_titanic_fare_se.R <file_path> <var>
# " -> doc
# 
# library(tidyverse)
# library(testthat)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# main <- function(file_path, var) {
# 
#   # read in data
#   data <- read_csv(file_path)
# 
#   # print out statistic of variable of interest
#   out <- data %>%
#     pull({{var}}) %>%
#     sterror()
#   print(out)
# }
# 
# #' calculate standard error
# #'
# #' @param x a vector of numeric values
# #' @return the standard error of x as a numeric vector of length one
# #' @examples
# #' sterror(mtcars$hp)
# sterror <- function(x) {
#   sd(x, na.rm = TRUE) / sqrt(length(x))
# }
# 
# test_that("sterror should return 0 if vector values are all the same", {
#     expect_equal(sterror(c(1, 1, 1)), 0)
# })
# 
# main(opt$file_path, opt$var)
# 
# ```

# ### Positional arguments vs options
# 
# In the examples above, we used `docopt` to specify positional arguments. This means that the order matters! If we change the order of the values of the arguments at the command line, our script will likely throw an error, because it will try to perform the wrong operations on the wrong values. 
# 
# Another downside to positional arguments, is that without good documentation, they can be less readable. And certainly the call to the script to is less readable. We can instead give the arguments names using `--ARGUMENT_NAME` syntax. We call these "options". Below is the same script but specified using options as opposed to positional arguments:
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# 
# "This script calculates the standard error for any numerical vector
# from a csv file. This script takes an unquoted column name and a data file path.
# 
# Usage: quick_titanic_fare_se.R --file_path=<file_path> --var=<var>
# 
# Options:
# --file_path=<file_path>   Path to the data file
# --var=<var>               Unquoted column name of the numerical vector for which to calculate the se
# " -> doc
# 
# library(tidyverse)
# library(testthat)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# main <- function(file_path, var) {
# 
#   # read in data
#   data <- read_csv(file_path)
# 
#   # print out statistic of variable of interest
#   out <- data %>%
#     pull({{var}}) %>%
#     sterror()
#   print(out)
# }
# 
# #' calculate standard error
# #'
# #' @param x a vector of numeric values
# #' @return the standard error of x as a numeric vector of length one
# #' @examples
# #' sterror(mtcars$hp)
# sterror <- function(x) {
#   sd(x, na.rm = TRUE) / sqrt(length(x))
# }
# 
# test_that("sterror should return 0 if vector values are all the same", {
#     expect_equal(sterror(c(1, 1, 1)), 0)
# })
# 
# main(opt$file_path, opt$var)
# 
# ```

# And we would run a script like this that uses options like this: 
# 
# ```
# Rscript src/quick_csv_stat.R --file_path=data/titanic.csv --var=fare
# ```
# 
# or like this: 
# 
# ```
# Rscript src/quick_csv_stat.R --var=fare --file_path=data/titanic.csv
# ```
# 
# because we gave the arguments names, and thus their position no longer matters!

# ### Optional elements (arguments or options)
# 
# If you would like an argument or option to be "optional" (i.e., not required!) enclose them with the square brackets "[ ]"  in the documentation.

# #### Improving our docs
# 
# We can improve our docs further by adding an "Options" section with {docopt}:
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# 
# "This script calculates the standard error for any numerical vector
# from a csv file. This script takes an unquoted column name and a data file path.
# 
# Usage: quick_titanic_fare_se.R --file_path=<file_path> --var=<var>
# 
# Options:
# --file_path=<file_path>   Path to the data file
# --var=<var>               Unquoted column name of the numerical vector for which to calculate the se
# " -> doc
# 
# library(tidyverse)
# library(testthat)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# main <- function(file_path, var) {
# 
#   # read in data
#   data <- read_csv(file_path)
# 
#   # print out statistic of variable of interest
#   out <- data %>%
#     pull({{var}}) %>%
#     sterror()
#   print(out)
# }
# 
# #' calculate standard error
# #'
# #' @param x a vector of numeric values
# #' @return the standard error of x as a numeric vector of length one
# #' @examples
# #' sterror(mtcars$hp)
# sterror <- function(x) {
#   sd(x, na.rm = TRUE) / sqrt(length(x))
# }
# 
# test_that("sterror should return 0 if vector values are all the same", {
#     expect_equal(sterror(c(1, 1, 1)), 0)
# })
# 
# main(opt$file_path, opt$var)
# 
# ```

# And then the user can see these docs by calling the script from the command line and using the `--help` to get this information:
# 
# ```
# This script calculates the standard error for any numerical vector
# from a csv file. This script takes an unquoted column name and a data file path.
# 
# Usage: quick_titanic_fare_se.R --file_path=<file_path> --var=<var>
# 
# Options:
# --file_path=<file_path>   Path to the data file
# --var=<var>               Unquoted column name of the numerical vector for which to calculate the se 
# ```

# ## Scripts in Python
# 
# Reminder of what they typically look like:
# 
# ```
# # documentation comments
# 
# # import libraries/packages
# 
# # parse/define command line arguments here
# 
# # define main function
# def main():
#     # code for "guts" of script goes here
# 
# # code for other functions & tests goes here
# 
# # call main function
# if __name__ == "__main__":
#     main()
# ```

# ### Where to develop scripts in Python
# 
# #### In a integrated development environment (IDE):
# 
# Or use an IDE, such as:
# - RStudio (gasp! 😱) via [`reticulate`](https://rstudio.github.io/reticulate/)
# - VS Code
# - [Spyder](https://www.spyder-ide.org/) (I think this comes with Anaconda, so you should have it installed)
# - Atom text editor + [`hydrogen`](https://atom.io/packages/hydrogen) (highly recommended by Mike Yuan, an MDS Alumni)
# - [PyCharm](https://www.jetbrains.com/pycharm/)
# 
# #### In a Jupyter notebook:
# 
# Jupyter + [`nbconvert`](https://nbconvert.readthedocs.io/en/latest/) (install via `conda install nbconvert`):
# 
# Convert a notebook to a script at the command line via:
# ```jupyter nbconvert --to script <input notebook>```
# 
# #### TLDR;
# 
# I recommend using an IDE over Jupyter. True, you may want to abstract code the originally was developed in a Jupyter notebook, but as soon as you switch the filename from `.ipynb` to `.py` you should change developing environments.

# ### Command line arguments in Python explained
# 
# `docopt` was originally written in and for Python! There are other packages you can use, but `docopt` is extremely elegant and powerful. I've used `sys` and `argparse` previously, and now that I've tried `docopt`, there's no turning back for me. Key features I like are:
# - writing the code for the command line arguments in docopt forces you to write the documentation (because it parses the documentation!)
# - it gives you the command line arguments as simple dictionary
# - you have to write very few lines of code to parse a complicated command line input
# - it provides a consistent framework between R and Python

# Here we rewrite the script above in Python using `docopt`:
# 
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# 
# '''This script calculates the standard error for any numerical vector
# from a csv file. This script takes an unquoted column name and a data file path.
# 
# Usage: quick_titanic_fare_se.py --file_path=<file_path> --var=<var>
# 
# Options:
# --file_path=<file_path>   Path to the data file
# --var=<var>               Unquoted column name of the numerical vector for which to calculate the se
# '''
# 
# import pandas as pd
# import numpy as np
# from docopt import docopt
# 
# opt = docopt(__doc__)
# 
# def main(file_path, var):
#   # read in data
#   data = pd.read_csv(file_path)
# 
#   # print out statistic of variable of interest
#   out = sterror(data[var])
#   print(out)
# 
# # standard error function
# 
# def sterror(x):
#   """
#   calculate standard error
#     
#   Parameters
#   ----------
#   numpy.ndarray : x
#     A numpy array of numeric values.
#         
#   Returns
#   -------
#   se
#     The standard error of x. 
#         
#   Examples
#   --------
#   >>> sterror(numpy.array([2, 2, 2]))
#   0
#   """
#   se = x.std()/np.sqrt(x.size)
#   return se
#   
# def test_sterror():
#   assert sterror(np.array([1, 1, 1])) == 0, "sterror should return 0 if vector values are all the same"
# 
# test_sterror()
#   
# if __name__ == "__main__":
#     main(opt["--file_path"], opt["--var"])
# 
# ```

# ## Some tips for RStudio IDE:
# 
# - To indent a block of text, highlight and use tab
# - To fix indenting in general to R code standards, use Command/Cntrl + I 
# - To get multiple cursors, hold alt/option and highlight lines using cursor
# - To get multiple cursors to the beginning of the line, use control A
# - To get multiple cursors to the end of the line, use control E

# ## What we covered:
# 
# - When to work in a read-eval-print-loop (REPL) framework versus when to use scripts
# - Scripts in R
# - Scripts in Python
# - Command line arguments in R & Python

# ## What's next?
# 
# - running literate code documents interactively
# - more advanced R Markdown (figure and table formatting, citation)
# - flexible R Markdown reports with parameterization

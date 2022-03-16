#!/usr/bin/env python
# coding: utf-8

# # Packaging and documenting code

# ## Topic learning objectives
# 
# By the end of this topic, students will be able to:
# 
# 1. Explain the circumstances in which one should consider creating a package for their code
# 
# 2. Name the key files and directories in R software packages and describe the function of each
# 
# 3. Use available package development tools (e.g., `usethis` and `devtools` in R) to create a small, simple software package
# 
# 4. Generate well formatted function and package-level documentation for software packages using available tools (e.g., `Roxygen2` and `pkgdown` in R)

# ## When to start writing an R or Python package
# 
# When your DRY radar goes off:
# 
# > It depends on your level of patience for violating the DRY principle, for me the magic number is about 3. If I repeat writing code within a single script or notebook, on the third try hair starts to stand up on the back of my neck and I am irritated sufficiently to either write a funciton or a loop. The same goes with copying files containing functions that I would like to re-use. The third time that I do this, I am convinced that I will likely want to use this code again on another project and thus I should package it to make my life easier. 
# 
# When you think your code has general usefulness others could benefit from:
# 
# > Another reason to package your code is that you think that it is a general enough solution that other people would find it useful. Doing this can be viewed as an act of altruism that also provides you professional gain by putting your data science skills on display (and padding your CV!).
# 
# When you want to share data:
# 
# > The R package ecosystem has found great use in packaging data in addition to Software. Packaging data is beyond the scope of this course, but you should know that it is widely done in R and that you can do it if you want or need to.
# 
# Let's watch a video from rstudio::conf 2020, called RMarkdown Driven Development by Emily Riederer, because I think it is such a nice narrative on how analysis code can evolve into packages: 
# 
# [https://rstudio.com/resources/rstudioconf-2020/rmarkdown-driven-development/](https://rstudio.com/resources/rstudioconf-2020/rmarkdown-driven-development/)

# ## Tour de packages
# 
# We will spend some time now exploring GitHub repositories of some Python and R packages to get more familiar with their internals. As we do this, fill out the missing data in the table below (which tries to match up the corresponding R and Python package key files and directories):
# 
# | Description                                            | Python        | R            |
# |--------------------------------------------------------|---------------|--------------|
# | Online package repository or index                     |               |              |
# | Directory for user-facing package functions            |               |              |
# | Directory for tests for user-facing package functions  |               |              |
# | Directory for documentation                            |               |              |
# | Package metadata                                       |               |              |
# | File(s) that define the Namespace                      |               |              | 
# | Tool(s) for easy package creation                      |               |              |
# 
# > Note: at the end of lecture I will review the answers to this table.

# ## Tour de R packages
# 
# Some R packages you may want to explore:
# 
# 1. [`foofactors`](https://github.com/jennybc/foofactors) - the end product of [the Whole Game Chapter](https://r-pkgs.org/whole-game.html) from the R Packages book.
# 
# 1. [`convertempr`](https://github.com/ttimbers/convertempr) - a simple example package I built as a demo for this course 
# 
# 1. [`broom`](https://github.com/tidymodels/broom) - a tidyverse R package
# 
# 1. [`tidyhydat`](https://github.com/ropensci/tidyhydat) - a reviewed ROpenSci R package
# 
# ### {usethis} and the evolution of R packaging
# 
# What constitutes an R package or its configuration files, has not changed in a long time. However the tools commonly used to build them have. Currently, the most straight forward, and easy way to build R packages now involves the use of two developer packages called {usethis} and {devtools}.
# 
# 
# ```{figure} img/usethis-devtools.png
# ---
# height: 400px
# name: usethis-devtools
# ---
# `usethis` and `devtools` R packages
# ```
# 
# These packages automate repetitive tasks that arise during project setup and development. It prevents you from having to do things like manually create boiler plate file and directory structures needed for building your R package structure, as well as simplifies the checking, installation and building of your package from source code. 
# 
# Packages created via {usethis} and {devtools} can be shared so that they can be installed via source from GitHub, or as package binaries on CRAN. For a package to be shared on CRAN, there is a check and gatekeeping system (in contrast to PyPI). We will learn more about this in later parts of the course.
# 
# > Fun fact! Jenny Bryan, a past UBC Statistics Professor UBC MDS founder, is the maintainer for the `usethis` R package!
# 
# ### Learn more by building a toy R package
# 
# For invidividual assignment 5, you will build a toy R package using a tutorial Jenny Bryan put together: [The Whole Game](https://r-pkgs.org/whole-game.html)
# 
# After building the toy package, read [Package structure and state](https://r-pkgs.org/package-structure-state.html) to deepen your understanding of what packaging means in R and what packages actually are.

# ## Tour de Python packages
# 
# Some Python packages you may want to explore:
# 
# 1. [`pycounts_tb`](https://github.com/TomasBeuzen/pycounts_tb) - the end product of [How to Package a Python](https://py-pkgs.org/03-how-to-package-a-python) from the Python Packages book
# 
# 1. [`convertempPy`](https://github.com/ttimbers/convertempPy) - a simple example package I built as a demo for this course 
# 
# 1. [`PyWebCAT`](https://github.com/UNCG-DAISY/PyWebCAT) - a Pythonic way to interface with the NOAA National Ocean Service Web Camera Applications Testbed (WebCAT)
# 
# 2. [`laserembeddings`](https://github.com/yannvgn/laserembeddings) - a Python package (uses the Poetry approach to creating Python packages)
# 
# 3. [`pandera`](https://github.com/pandera-dev/pandera) - a reviewed PyOpenSci Python package (uses more traditional approach to creating Python packages)
# 
# ### Poetry and the evolution of Python packaging
# 
# If you want to package your Python code and distribute for ease of use by others on the Python Packaging Index (PyPI) you need to convert it to a standard format called Wheel. 
# 
# Previously, to do this it was standard to have 4 configuration files in your package repository:
# 
# - `setup.py`
# - `requirements.txt`
# - `setup.cfg`
# - `MANIFEST.in`
# 
# In 2016, a new PEP ([518](https://www.python.org/dev/peps/pep-0518/)) was made. This PEP defined a new configuration format, `pyproject.toml`, so that now a single file can be used in place of those previous four. This file must have at least two sections, `[build-system]` and `[tool]`.
# 
# This new single configuration file has inspired some new tools to be created in the package building and management ecosystem in Python. One of the most recent and simplest to use is Poetry (created in 2018). When used to build packages, Poetry roughly does two things:
# 
# 1. Uses the `pyproject.toml` to manage and solve package configurations via the Poetry commands `init`, `add`, `config`, etc
# 
# 2. Creates a lock file (`poetry.lock`) which automatically creates and activates a virtual environment (if none are activated) where the Poetry commands such as `install`, `build`, `run`, etc are executed.
# 
# Cookiecutter templates are also useful to help setup the biolerplate project and directory structure needed for packages. We will use these in this course as well.
# 
# ### Learn more by building a toy Python package
# 
# For an optional/bonus part of invidividual assignment 5, you can choose to build a toy Python package using a tutorial we have put together for you: [How to package a Python](https://py-pkgs.org/03-how-to-package-a-python)
# 
# After building the toy package, read [Package structure and state](https://py-pkgs.org/04-package-structure) to deepen your understanding of what packaging means in Python and what packages actually are.

# ## Key package things for Python and R packages
# 
# | Description                                            | Python        | R            |
# |--------------------------------------------------------|---------------|--------------|
# | Online package repository or index                     | PyPI          | CRAN         |
# | Directory for user-facing package functions            | Package directory (a named directory within the project root that contians `.py` files and a `__init__.py` file) | `R` directory 
# | Directory for tests for user-facing package functions   | `tests`      | `tests/testthat` |
# | Directory for documentation                             | `docs`       | `man` and `vignettes` |
# | Package metadata                                        | `pyproject.toml` | `DESCRIPTION` |
# | File(s) that define the Namespace                      | `__init__.py`     | `NAMESPACE`         | 
# | Tool(s) for easy package creation                      |  Cookiecutter & Poetry | `usethis` & `devtools` |

# ## Dealing with other package dependencies in your package
# 
# ### Dealing with package dependencies in R
# 
# - When we write code in our package that uses functions from other packages we need to import those functions from the namespace of their packages.
# 
# - In R, we do this via `use_package`, which adds that package to the “Imports” section of DESCRIPTION
# 
# - We also need to refer to that package in our function code, there are two ways to do this:
#   1. refer the function by `package::fun_name` (e.g., `dplyer::filter`) whenever you use the function in your code
#   2. add the function to your packages namespace so that you can just refer to it as your normally would. To do this add `@importFrom <package_name> <function_or_operator>` to the Roxygen documentation of the function that you would like to use the function from the other package in and then use `document()` to update the DESCRIPTION and NAMESPACE file. 
#   
# *It is recommended to use method 1 (`pkg::fun_name`) because it is more explicit on what external functions your package code depends on (making it easier to read for collaborators, including future you). The trade off is that it’s a little more work to write.*
# 
# ### The pipe, `%>%`, a special dependency
# 
# - Given the ubiquity of the pipe operator, `%>%`, in R, there is a function that automates exposing to your entire package: `usethis::use_pipe()`
# 
# - Note, in general, the tidyverse team does not recommend using the pipe in packages unless they are personal, low use packages, or “pro” packages with a lot of data wrangling because:
#   - In most cases it is really an unnecessary dependency 
#   - It is not that readable for folks who do not typically use the pipe
#   - makes debugging more challenging 
#   
# So, should you use the pipe in your package? The answer is, it depends on your package's scope, aims and goals. Also, this is probably your first package, so it doesn't have to be perfect. If using the pipe helps you get the job done this time around, go for it. Just know that if you aim to ever build a widely used package, you probably do not want to depend on it.

# ## Package documentation for R
# 
# There are several levels of documentation possible for R packages:
# - code-level documentation (Roxygen-style comments)
# - vignettes
# - package websites (via `pkgdown`)
# 
# ### Code-level documentation (Roxygen-style comments)
# 
# - We learned the basics of how to write Roxygen-style comments in DSCI 511
# - In the package context, there are Namespace tags you should know about:
#     - `@export` - this should be added to all package functions you want your user to know about
#     - `@NoRd` - this should be added to helper/internal helper functions that you don't want your user to know about
#     
# ### Vignettes
# It is common for packages to have vignettes (think demos with narratives) showing how to use the package in a more real-world scenario than the documentation examples show. Think of your vignette as a demonstration of how someone would use your function to solve a problem. 
# 
# - It should demonstrate how the individual functions in your package work, as well as how they can be integrated together.
# 
# - To create a template for your vignette, run:
#     ```
#     usethis::use_vignette("package_name-vignette")
#     ```
#     
# - Add content to that file and knit it when done.
# 
# As an example, here's the `dplyr` vignette: <https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html>
# 
# ### Package websites (via [`pkgdown`](https://pkgdown.r-lib.org/))
# 
# - Vignettes are very helpful, however they are not that discoverable by others, websites are a much easier way to share your package with others.
# 
# - The `pkgdown` R package let's you build a beautiful website for your R package in 4 steps!
# 
#     1. Turn on GitHub pages in your package repository, setting `main branch / docs folder` as the source.
# 
#     2. Install `pkgdown`: `install.packages("pkgdown")
# 
#     3. Run `pkgdown::build_site()` from the root of your project, and commit and push the changes made by this.
# 
#     4. Push your code, including the `docs` directory to GitHub.com
# 
#     
# In addition to the beautiful website, `pkgdown` automatically links to your vignette under the articles section of the website!!! 🎉🎉🎉
# 
# > Note you can also configure a GitHub Actions workflow to automate the rebuilding of the `pkgdown` site 
# > anytime changes are pushed to your package's GitHub repository. 
# > We will discuss this later in the course under the topic of continuous deployment.

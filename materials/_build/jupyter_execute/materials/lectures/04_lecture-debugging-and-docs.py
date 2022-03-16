#!/usr/bin/env python
# coding: utf-8

# # Lecture 4: Code coverage & package dependencies

# ## Learning objectives:
# By the end of this lecture, students should be able to:
# 
# - Define code, test and branch coverage, and explain why high coverage in each of these metrics is desired.
# - Calculate code coverage in R and Python
# - Manage package dependencies in R and Python packages

# ## Coverage
# 
# **Definition:** Proportion of system being executed by the test suite.
# 
# - usually reported as a percentage: $$Coverage = \frac{covered}{(covered + uncovered)} * 100$$
# 
# 

# ### Coverage metrics:
# 
# There are many, but here are the ones our automated tools in this course will calculate for you:
# 
# | Metric | Description                           | Dependent upon control flow |
# |--------|---------------------------------------|-----------------------------|
# | line   | lines of code that tests execute      | No                          |
# | branch | number of branches (independent code segments) that tests execute | Yes                         |
# 

# ### What exactly is a branch?
# 
# ```
# def my_function(x):
#     # Branch 1
#     if condition_met:
#         y = function_a(x)
#         z = function_b(y)
#     # Branch 2
#     else: 
#         y = function_b(x)
#         z = function_c(y)
#     return z
# ```
# 
# *Adapted from: <http://www.ncover.com/blog/code-coverage-metrics-branch-coverage/>*

# ## How are line and branch coverage different?
# 
# Consider the same example we just saw and the unit test below, let's manually calculate the coverage using line and branch coverage metrics:
# 
# ```
# def my_function(x):
#     # Branch 1
#     if x == "pony":
#         y = function_a(x)
#         z = function_b(y)
#     # Branch 2
#     else: 
#         y = function_c(x)
#         w = function_d(y)
#         z = function_e(y)
#     return z
# ```
# 
# ```
# def test_my_function():
#     assert my_function("pony") == ("Actually a unicorn")
# ```
# 
# *Note: function definitions are not counted as lines when calculating coverage*

# #### Using branch as the coverage metric:
# 
# $Coverage = \frac{covered}{(covered + uncovered)} * 100$
# 
# $Coverage = \frac{1}{(1 + 1)} * 100$
# 
# $Coverage = 50\%$

# #### Using line as the coverage metric:
# 
# $Coverage = \frac{covered}{(covered + uncovered)} * 100$
# 
# $Coverage = \frac{4}{(4 + 4)} * 100$
# 
# $Coverage = 50\%$

# ### But wait, line coverage can be misleading... 
# 
# Let's alter our function and re-calculate line and branch coverage:
# 
# ```
# def my_function(x):
#     # Branch 1
#     if x == "pony":
#         y = function_a(x)
#         z = function_b(y)
#         print(z)
#         print("some important message")
#         print("another important message")
#         print("a less important message")
#         print("just makin' stuff up here...")
#         print("out of things to say...")
#         print("how creative can I be...")
#         print("I guess not very...")
#     # Branch 2
#     else: 
#         y = function_c(x)
#         w = function_d(y)
#         z = function_e(y)
#     return z
# ```
# 
# ```
# def test_my_function():
#     assert my_function("pony") == ("Actually a unicorn")
# ```

# #### Using branch as the coverage metric:
# 
# $Coverage = \frac{covered}{(covered + uncovered)} * 100$
# 
# $Coverage = \frac{1}{(1 + 1)} * 100$
# 
# $Coverage = 50\%$

# #### Using line as the coverage metric:
# 
# $Coverage = \frac{covered}{(covered + uncovered)} * 100$
# 
# $Coverage = \frac{12}{(12 + 4)} * 100$
# 
# $Coverage = 75\%$
# 
# 🤯

# ### Take home message:
# 
# Use branch coverage when you can, especially if your code uses control flow!

# ### Calculating coverage in Python
# 
# We use the plugin  tool [`pytest-cov`](https://github.com/pytest-dev/pytest-cov) to do this. 
# 
# Install as a package dependency via poetry:
# ```
# poetry add --dev pytest-cov
# ```

# ### Calculating coverage in Python
# 
# To calculate line coverage and print it to the terminal:
# ```
# poetry run pytest --cov=<project_slug> 
# ```
# 
# To calculate line coverage and print it to the terminal:
# ```
# poetry run pytest --cov-branch --cov=<project_slug>
# ```
# 
# Next week we will learn to use GitHub actions to link this to [codecov.io](https://codecov.io/) to get a shiny button ✨ that advertises your code coverage!

# ### Exercise: Calculate coverage in Python
# 
# Let's practice calculating coverage in Python!
# 
# #### Steps:
# 
# 1. Fork & clone this GitHub repository: <https://github.com/ttimbers/big_abs> 
# 
# 2. Using a command line, navigate to the root of this repository and run `poetry install`
# 
# 3. Calculate the line coverage and print it to the terminal via `poetry run pytest --cov=big_abs`
# 
# 4. Calculate the branch coverage and print it to the terminal via `poetry run pytest --cov-branch --cov=big_abs`
# 
# 

# ### How does `coverage` in Python actually count line coverage?
# 
# - the output from `poetry run pytest --cov=big_abs` gives a table that looks like this:
# 
# ```
# ---------- coverage: platform darwin, python 3.7.6-final-0 -----------
# Name                  Stmts   Miss  Cover
# -----------------------------------------
# big_abs/__init__.py       1      0   100%
# big_abs/big_abs.py        8      2    75%
# -----------------------------------------
# TOTAL                     9      2    78%
# ```
# 
# In the column labelled as "Stmts", coverage is calculating all possible line jumps that could have been executed (these line jumps are sometimes called arcs). 
# 
# > Note - this leads coverage to count two statements on one line that are separated by a ";" (e.g., print("hello"); print("there")) as one statement, as well as calculating a single statement that is spread across two lines as one statement. 
# 
# In the column labelled as "Miss", this is the number of line jumps not executed by the tests. 
# 
# The coverage percentage in this scenario is calculated by:
# $$Coverage = \frac{(Stmts - Miss)}{Stmts}$$
# $$Coverage = \frac{8 - 2}{8} * 100 = 75\%$$

# ### How does `coverage` in Python actually branch coverage?
# 
# - the output from `poetry run pytest --cov-branch --cov=big_abs` gives a table that looks like this:
# 
# ```
# ---------- coverage: platform darwin, python 3.7.6-final-0 -----------
# Name                  Stmts   Miss Branch BrPart  Cover
# -------------------------------------------------------
# big_abs/__init__.py       1      0      0      0   100%
# big_abs/big_abs.py        8      2      6      3    64%
# -------------------------------------------------------
# TOTAL                     9      2      6      3    67%
# ```
# 
# In the column labelled as "Branch", coverage is actually counting the number of possible jumps from branch points.
# 
# > Note: because coverage is using line jumps to count branches, each `if` inherently has an `else` even if its not explicitly written in the code.
# 
# In the column labelled as "BrPart", this is the number of of possible jumps from branch points executed by the tests.
# 
# The branch coverage percentage in this tool is calculated by:
# 
# $$Coverage = \frac{(Stmts\:executed + BrPart)}{(Stmts + Branch)}$$
# 
# $$Coverage = \frac{((Stmts - Miss) + BrPart)}{(Stmts + Branch)}$$
# 
# So for `big_abs/big_abs.py` 64% was calculated from:
# $$Coverage = \frac{((8 - 2) + 3)}{(8 + 6)} * 100 = 64\%$$

# #### Want more details on the execution of Coverage?
# 
# **Documentation**
# 
# https://coverage.readthedocs.io/en/coverage-4.0.3/howitworks.html#execution
# 
# **Source code:**
# 
# https://github.com/nedbat/coveragepy/blob/4ce893437c9e777216cac981c5909572fa10d9df/coverage/results.py#L240
# 
# ```
# def ratio_covered(self):
#         """Return a numerator and denominator for the coverage ratio."""
#         numerator = self.n_executed + self.n_executed_branches
#         denominator = self.n_statements + self.n_branches
#         return numerator, denominator
# ```

# ### Coverage reports
# 
# There is a very cool html report you can generate that will give you some more information about what lines and branches have been executed or not for each file. You can generate it via `poetry run pytest --cov-branch --cov=big_abs --cov-report html` and you will get a folder called `htmlcov` in the root directory of your project. 
# 
# From there you will see a table like we generated in the terminal, but you can click on the file to see more info that looks like this:
# 
# 
# ```{figure} img/covr_html.png
# ---
# width: 500px
# name: covr_html
# ---
# ```

# ### Exercise: Improve branch coverage
# 
# Let's add some additional test cases to improve the branch coverage for the `big_abs` Python package!
# 
# #### Steps:
# 1. Open `big_abs/big_abs.py` and `tests/test_big_abs.py` and identify the branch(es) that the current test case covers
# 
# 2. Add at least one new test case that will improve branch coverage. Prove this to yourself by calculating the branch coverage and print it to the terminal via `poetry run pytest --cov-branch --cov=big_abs`
# 

# ## Calculating coverage in R
# 
# We use the [`covr`](https://covr.r-lib.org/) R package to do this. 
# 
# Install via R console:
# ```
# install.packages("covr")
# ```

# To calculate line coverage and have it show in the viewer pane in RStudio:
# ```
# covr::report()
# ```
# 
# Currently `covr` does not have the functionality to calculate branch coverage. Thus this is up to you in R to calculate this by hand if you really want to know. 
# 
# > Why has this not been implemented? It has been in an now unsupported package (see [here](https://github.com/MangoTheCat/testCoverage)), but its implementation was too complicated for others to understand. Automating the calculation of branch coverage is non-trivial, and this is a perfect demonstration of that.

# ## Dealing with other package dependencies in your package

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

# ### Dealing with package dependencies in Python
# 
# - Given that we are using Poetry to manage our Python packages, we can take advantage of Poetry to manage our package dependencies. 
# 
# - To add a package dependency (one that our package functions depend on), we use `poetry add <package_name>`.
# 
# - When we do this Poetry adds this depenedency to the `pyproject.toml` file under the `[tool.poetry.dependencies]` table as well as to the `poetry.lock` file.
# 
# - Then we need to import these dependencies in our `.py` files where our functions live. Given that [PEP 08](https://www.python.org/dev/peps/pep-0008/) states that: _"Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants."_ we typically do this at the very top of the file, even when we are writing code that will end up in a package.
# 
#   > It is possible to import packages inside a function, and there is sound reasoning in doing so to make your code more readable, however, it goes against convention and so you need to get your whole team to agree to this if you want to do things this way.

# ### How does Poetry `install` use `pyproject.toml` & `poetry.lock`
# 
# - The install command reads the `pyproject.toml` file from the current project, resolves the dependencies, and installs them.
# 
# - If there is a `poetry.lock` file in the current directory, it will use the exact versions from there instead of resolving them. This ensures that everyone using the library will get the same versions of the dependencies.
# 
# - If there is no `poetry.lock` file, Poetry will create one after dependency resolution.
# 
# *Source: [Poetry install documentation](https://python-poetry.org/docs/cli/#install)*
# 

# ## Where are we headed next?
# 
# - Package bells & whistles! Including
#     - Continuous integration
#     - Documentation
#     - Package versioning
#     - Package publishing

# ## Extra materials
# 
# ### Helper/internal functions in R
# - [Helper/internal functions in R](https://www.r-bloggers.com/internal-functions-in-r-packages/)
# - [Testing helper/internal functions in R](https://github.com/r-lib/covr/issues/301)

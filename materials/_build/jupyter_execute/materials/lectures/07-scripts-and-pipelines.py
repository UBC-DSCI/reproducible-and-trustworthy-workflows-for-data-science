#!/usr/bin/env python
# coding: utf-8

# # Non-interactive scripts and data analysis pipelines

# ## Topic learning objectives
# 
# By the end of this topic, students should be able to:
# 
# 1. Explain when it is optimal to work in a read-eval-print-loop (REPL) framework and
# when it is optimal to shift to using non-interactive scripts.
# 2. Be able to create simple scripts in R that can take input and be executed
# from the command line.
# 3. Decide when to move from using command line arguments to pass variables into a
# script to passing variables in via a configuration file, and create scripts that can read
# configuration files.
# 4. Justify why analysis pipelines should be used over a single long script in data analysis
# projects, specifically in regards to how this affects reproducibility, maintainability and
# future derivatives of the work.
# 5. Write a simple automated analysis pipeline using workflow tool (e.g., GNU Make)
# 6. Discuss the advantage of using software that has a dependency graph for analysis
# pipelines compared to software that does not.

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
# Although not necessary in R or Python, it is still good practice and advised to organize the code in your script into related sections. This practice keeps your code readable and organized. Below we outline how we typically organize R scripts:
# 
# ##### Example R script organization:
# ```
# # documentation comments
# 
# # load libraries/packages or source functions from other scripts
# 
# # parse/define command line arguments here
# 
# # code for "guts" of script goes here
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

# Here we write a script called `quick_titanic_fare_mean.R` which reads in the [titanic dataset](https://github.ubc.ca/ubc-mds-2016/datasets/raw/master/data/titanic.csv) and calculates the standard error for the fare (ticket price) variable.
# 
# Our script has two functions, a function we defined to calculate the standard error of the mean (such a function does not exist in R) and a `main` function which runs the "body" of our code.
# 
# ```
# # author: Tiffany Timbers
# # date: 2020-01-15
# #
# # This script calculates the mean for the fare (ticket price)
# # from titanic.csv. This script takes no arguments.
# #
# # Usage: quick_titanic_fare_mean.R
# 
# library(tidyverse)
# 
# data <- read_csv('data/titanic.csv')
# 
# out <- data %>%
#          pull(fare) %>%
#          mean()
# 
# print(out)
# ```
# 
# Wait! Other languages use a `main` function (so you can, for example, import and access parts of the code into other code docs) - why are we not doing this here? I truly do not know the answer (yet) to why not, however, it is not commonly done. Perhaps this is due to historical origins and culture of the R programming language and it's user base. A question is, can you do this if you want? That question I can answer with a yes, see here for an example: <https://github.com/ttimbers/if_name_equals_main>

# ### Using command line arguments in R
# Let's make our script more flexible, and let us specify when we call the script, what variable we want to calculate the standard error for.
# 
# To do this, we use the `docopt` R package. This will allow us to collect the text we enter at the command line when we call the script, and make it available to us when we run the script. 
# 
# When we run `docopt` it takes the text we entered at the command line and gives it to us as a named list of the text provided after the script name. The names of the items in the list come from the documentation. Whitespace at the command line is what is used to parse the text into separate items in the vector.
# 
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
# 
# library(tidyverse)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# data <- read_csv('data/titanic.csv')
# 
# out <- data %>%
#          pull({{ opt$var }}) %>%
#          mean()
# 
# print(out)
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
# 
# library(tidyverse)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# data <- read_csv(opt$file_path)
# 
# out <- data %>%
#          pull({{ opt$var }}) %>%
#          mean()
# 
# print(out)
# ```
# 
# Now we would run a script like this from the command line as follows: 
# 
# ```
# Rscript src/quick_csv_stat.R data/titanic.csv fare
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
# 
# library(tidyverse)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# data <- read_csv(opt$file_path)
# 
# out <- data %>%
#          pull({{ opt$var }}) %>%
#          mean()
# 
# print(out)
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
# 
# library(tidyverse)
# library(docopt)
# 
# opt <- docopt(doc)
# 
# data <- read_csv(opt$file_path)
# 
# out <- data %>%
#          pull({{ opt$var }}) %>%
#          mean()
# 
# print(out)
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

# #### Some tips for RStudio IDE:
# 
# - To indent a block of text, highlight and use tab
# - To fix indenting in general to R code standards, use Command/Cntrl + I 
# - To get multiple cursors, hold alt/option and highlight lines using cursor
# - To get multiple cursors to the beginning of the line, use control A
# - To get multiple cursors to the end of the line, use control E

# ## Data analysis pipelines
# 
# - As analysis grows in length and complexity, one literate code document generally is not enough
# 
# - To improve code report readability (and code reproducibility and modularity) it is better to abstract at least parts of the code away (e.g, to scripts)
# 
# - These scripts save figures and tables that will be imported into the final report
# 
# <img src="img/scripts.png" width=600>

# ### Demo: building a Data Analysis pipeline using a Shell script tutorial
# adapted from [Software Carpentry](http://software-carpentry.org/)
# 
# To illustrate how to make a data analysis pipeline using a shell script to drive other scripts, we will work through an example together. Here are some set-up instructions so that we can do this together:
# 
# #### Set-up instructions
# 
# - Download [data_analysis_pipeline_eg-1.0.zip](https://github.com/ttimbers/data_analysis_pipeline_eg/archive/v1.0.zip)
# - Unzip it and change into the `data_analysis_pipeline_eg-1.0` directory.
# 
# #### Let's do some analysis!
# 
# Suppose we have a script, `wordcount.py`, that reads in a text file,
# counts the words in this text file, and outputs a data file:
# 
# ~~~
# $ python src/wordcount.py data/isles.txt results/isles.dat
# ~~~
# 
# If we view the first 5 rows of the data file using `head`,
# 
# ~~~
# $ head -5 results/isles.dat
# ~~~
# 
# we can see that the file consists of one row per word. Each row shows the word itself,
# the number of occurrences of that word, and the number of occurrences as a percentage of
# the total number of words in the text file.
# 
# ~~~
# the 3822 6.7371760973
# of 2460 4.33632998414
# and 1723 3.03719372466
# to 1479 2.60708619778
# a 1308 2.30565838181
# ~~~
# 
# Suppose we also have a script, `plotcount.py`, that reads in a data
# file and save a plot of the 10 most frequently occurring words:
# 
# ~~~
# $ python src/plotcount.py results/isles.dat results/figure/isles.png
# ~~~
# 
# Together these scripts implement a data analysis pipeline:
# 
# 1. Read a data file.
# 2. Perform an analysis on this data file.
# 3. Write the analysis results to a new file.
# 4. Plot a graph of the analysis results.
# 
# To document how we'd like the analysis to be run, so we (and others) have a record and
# can replicate it, we will build a shell script called `run_all.sh`. Let's work to try
# to build this pipeline so it does all that!
# 
# ```
# # run_all.sh
# # Tiffany Timbers, Nov 2017
# #
# # This driver script completes the textual analysis of
# # 3 novels and creates figures on the 10 most frequently
# # occuring words from each of the 3 novels. This script
# # takes no arguments.
# #
# # Usage: bash run_all.sh
# 
# # perform wordcout on novels
# python src/wordcount.py data/isles.txt results/isles.dat
# 
# # create plots
# python src/plotcount.py results/isles.dat results/figure/isles.png
# ```
# 
# We actually have 4 books that we want to analyze, and then put the figures in a report. 
# 
# 1. Read a data file.
# 2. Perform an analysis on this data file.
# 3. Write the analysis results to a new file.
# 4. Plot a graph of the analysis results.
# 5. Save the graph as an image, so we can put it in a paper.
# 
# Let's extend our shell script to do that!
# 
# ```
# # run_all.sh
# # Tiffany Timbers, Nov 2018
# 
# # This driver script completes the textual analysis of
# # 3 novels and creates figures on the 10 most frequently
# # occuring words from each of the 3 novels. This script
# # takes no arguments.
# 
# # example usage:
# # bash run_all.sh
# 
# # count the words
# python src/wordcount.py data/isles.txt results/isles.dat
# python src/wordcount.py data/abyss.txt results/abyss.dat
# python src/wordcount.py data/last.txt results/last.dat
# python src/wordcount.py data/sierra.txt results/sierra.dat
# 
# # create the plots
# python src/plotcount.py results/isles.dat results/figure/isles.png
# python src/plotcount.py results/abyss.dat results/figure/abyss.png
# python src/plotcount.py results/last.dat results/figure/last.png
# python src/plotcount.py results/sierra.dat results/figure/sierra.png
# 
# # write the report
# Rscript -e "rmarkdown::render('doc/count_report.Rmd')"
# ```
# 
# ### Another example:
# 
# From the [breast cancer prediction example analysis repo](https://github.com/ttimbers/breast_cancer_predictor), here is a data analysis pipeline using a shell script:
# 
# ```
# # run_all.sh
# # Tiffany Timbers, Jan 2020
# 
# # download data
# python src/download_data.py --out_type=feather --url=https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wpbc.data --out_file=data/raw/wdbc.feather
# 
# # run eda report
# Rscript -e "rmarkdown::render('src/breast_cancer_eda.Rmd')"
# 
# # pre-process data 
# Rscript src/pre_process_wisc.r --input=data/raw/wdbc.feather --out_dir=data/processed 
# 
# # create exploratory data analysis figure and write to file 
# Rscript src/eda_wisc.r --train=data/processed/training.feather --out_dir=results
# 
# # tune model
# Rscript src/fit_breast_cancer_predict_model.r --train=data/processed/training.feather --out_dir=results
# 
# # test model
# Rscript src/breast_cancer_test_results.r --test=data/processed/test.feather --out_dir=results
# 
# # render final report
# Rscript -e "rmarkdown::render('doc/breast_cancer_predict_report.Rmd', output_format = 'github_document')"
# ```

# ### Discussion
# 
# - What are the advantages to using a data analysis pipeline?
# 
# - How "good" is a shell script as a data analysis pipeline? What might not be ideal about this?

# ## GNU Make as a data analysis pipeline tool
# 
# We previously built a data analysis pipeline by using a shell script (we called it `run_all.sh`) to piece together and create a record of all the scripts and arguments we used in our analysis. That is a step in the right direction, but there were a few unsatisfactory things about this strategy:
# 
#   1. It takes time to manually erase all intermediate and final files generated by analysis to do a complete test to see that everything is working from top to bottom
#   2. It runs every step every time. This can be problematic if some steps take a long time and you have only changed other, smaller parts of the analysis
# 
# Thus, to improve on this we are going to use the build and automation tool, Make, to make a smarter
# data analysis pipeline.
# 

# ### Makefile Structure
# 
# Each block of code in a Makefile is called a rule, it looks something like this:
# 
# ~~~
# file_to_create.png : data_it_depends_on.dat script_it_depends_on.py
# 	python script_it_depends_on.py data_it_depends_on.dat file_to_create.png
# ~~~
# 
# * `file_to_create.png` is a target, a file to be created, or built.
# * `data_it_depends_on.dat` and `script_it_depends_on.py` are dependencies, files which are needed to build or update the target. Targets can have zero or more dependencies.
# * `:` separates targets from dependencies.
# * `python script_it_depends_on.py data_it_depends_on.dat file_to_create.png` is an action, a command to run to build or update the target using the dependencies. Targets can have zero or more actions. Actions are indented using the TAB character, not 8 spaces.
# * Together, the target, dependencies, and actions form a rule.

# ### Structure if you have multiple targets from a scripts
# 
# ~~~
# file_to_create_1.png file_to_create_2.png : data_it_depends_on.dat script_it_depends_on.py
# 	python script_it_depends_on.py data_it_depends_on.dat file_to_create
# ~~~

# ### Demo: building a Data Analysis pipeline using Make, a tutorial
# adapted from [Software Carpentry](http://software-carpentry.org/)
# 
# #### Set-up instructions
# 
# - Download [data_analysis_pipeline_eg-2.0.zip](https://github.com/ttimbers/data_analysis_pipeline_eg/archive/v2.0.zip)
# - Unzip it and change into the `data_analysis_pipeline_eg-2.0` directory.
# - note - the tutorial in [lecture 4](lecture/04_lecture-shell-driver-scripts.md) is a prerequisite
# 
# 
# Good reference: http://swcarpentry.github.io/make-novice/reference
# 
# Create a file, called `Makefile`, with the following content:
# 
# ~~~
# # Count words.
# results/isles.dat : data/isles.txt src/wordcount.py
# 	python src/wordcount.py data/isles.txt results/isles.dat
# ~~~
# 
# This is a simple build file, which for
# Make is called a Makefile - a file executed
# by Make. Let us go through each line in turn:
# 
# * `#` denotes a *comment*. Any text from `#` to the end of the line is
#   ignored by Make.
# * `results/isles.dat` is a [target](http://swcarpentry.github.io/make-novice/reference#target), a file to be
#   created, or built.
# * `data/isles.txt` and `src/wordcount.py` are [dependencies](http://swcarpentry.github.io/make-novice/reference#dependency), a
#   file that is needed to build or update the target. Targets can have
#   zero or more dependencies.
# * `:` separates targets from dependencies.
# * `python src/wordcount.py data/isles.txt isles.dat` is an
#   [action](http://swcarpentry.github.io/make-novice/reference#action), a command to run to build or update
#   the target using the dependencies. Targets can have zero or more
#   actions.
# * Actions are indented using the TAB character, *not* 8 spaces. This
#   is a legacy of Make's 1970's origins.
# * Together, the target, dependencies, and actions form a
#   [rule](http://swcarpentry.github.io/make-novice/reference#rule).
# 
# Our rule above describes how to build the target `results/isles.dat` using the
# action `python src/wordcount.py` and the dependency `data/isles.txt`.
# 
# By default, Make looks for a Makefile, called `Makefile`, and we can
# run Make as follows:
# 
# ~~~
# $ make
# ~~~
# 
# Make prints out the actions it executes:
# 
# ~~~
# python src/wordcount.py data/isles.txt results/isles.dat
# ~~~
# 
# If we see,
# 
# ~~~
# Makefile:3: *** missing separator.  Stop.
# ~~~
# 
# then we have used a space instead of a TAB characters to indent one of
# our actions.
# 
# We don't have to call our Makefile `Makefile`. However, if we call it
# something else we need to tell Make where to find it. This we can do
# using `-f` flag. For example:
# 
# ~~~
# $ make -f Makefile
# ~~~
# 
# As we have re-run our Makefile, Make now informs us that:
# 
# ~~~
# make: `results/isles.dat' is up to date.
# ~~~
# 
# This is because our target, `results/isles.dat`, has now been created, and
# Make will not create it again. To see how this works, let's pretend to
# update one of the text files. Rather than opening the file in an
# editor, we can use the shell `touch` command to update its timestamp
# (which would happen if we did edit the file):
# 
# ~~~
# $ touch data/isles.txt
# ~~~
# 
# If we compare the timestamps of `data/isles.txt` and `results/isles.dat`,
# 
# ~~~
# $ ls -l data/isles.txt results/isles.dat
# ~~~
# 
# then we see that `results/isles.dat`, the target, is now older
# than`data/isles.txt`, its dependency:
# 
# ~~~
# -rw-r--r--    1 mjj      Administ   323972 Jun 12 10:35 books/isles.txt
# -rw-r--r--    1 mjj      Administ   182273 Jun 12 09:58 isles.dat
# ~~~
# 
# If we run Make again,
# 
# ~~~
# $ make
# ~~~
# 
# then it recreates `results/isles.dat`:
# 
# ~~~
# python src/wordcount.py data/isles.txt results/isles.dat
# ~~~
# 
# When it is asked to build a target, Make checks the 'last modification
# time' of both the target and its dependencies. If any dependency has
# been updated since the target, then the actions are re-run to update
# the target.
# 
# We may want to remove all our data files so we can explicitly recreate
# them all. We can introduce a new target, and associated rule, `clean`:
# 
# ~~~
# results/isles.dat : data/isles.txt
# 	python src/wordcount.py data/isles.txt results/isles.dat
# 
# clean :
# 	rm -f results/*.dat
# ~~~
# 
# This is an example of a rule that has no dependencies. `clean` has no
# dependencies on any `.dat` file as it makes no sense to create these
# just to remove them. We just want to remove the data files whether or
# not they exist. If we run Make and specify this target,
# 
# ~~~
# $ make clean
# ~~~
# 
# then we get:
# 
# ~~~
# rm -f *.dat
# ~~~
# 
# There is no actual thing built called `clean`. Rather, it is a
# short-hand that we can use to execute a useful sequence of
# actions. Such targets, though very useful, can lead to problems. For
# example, let us recreate our data files, create a directory called
# `clean`, then run Make:
# 
# ~~~
# $ make results/isles.dat
# $ mkdir clean
# $ make clean
# ~~~
# 
# We get:
# 
# ~~~
# make: `clean' is up to date.
# ~~~

# Let's add another rule to the end of `Makefile`:
# 
# ~~~
# results/isles.dat : data/isles.txt src/wordcount.py
# 	python src/wordcount.py data/isles.txt results/isles.dat
# 
# results/figure/isles.png : results/isles.dat src/plotcount.py
# 	python src/plotcount.py results/isles.dat results/figure/isles.png
# 
# clean :
# 	rm -f results/*.dat
# 	rm -f results/figure/*.png
# ~~~
# 
# the new target isles.png depends on the target isles.dat. So to make both, we can simply
# type:
# 
# ~~~
# $ make isles.dat
# $ ls
# ~~~
# 
# Let's add another book:
# 
# ~~~
# results/isles.dat : data/isles.txt src/wordcount.py
# 	python src/wordcount.py data/isles.txt results/isles.dat
# 
# results/abyss.dat : data/abyss.txt src/wordcount.py
#   python src/wordcount.py data/abyss.txt results/abyss.dat
# 
# results/figure/isles.png : results/isles.dat src/plotcount.py
# 	python src/plotcount.py results/isles.dat results/figure/isles.png
# 
# results/figure/abyss.png : results/abyss.dat src/plotcount.py
#   python src/plotcount.py results/abyss.dat results/figure/abyss.png
# 
# clean :
# 	rm -f results/*.dat
# 	rm -f results/figure/*.png
# ~~~
# 
# To run all of the commands, we need to type make <TARGET> for each one:
# ~~~
# $ make isles.png
# $ make abyss.png
# ~~~
# 
# OR we can add a target `all` which will build the last of the dependencies.
# 
# ~~~
# all: results/figure/isles.png results/figure/abyss.png
# 
# # count words
# results/isles.dat : data/isles.txt src/wordcount.py
# 	python src/wordcount.py data/isles.txt results/isles.dat
# 	
# results/abyss.dat : data/abyss.txt src/wordcount.py
# 	python src/wordcount.py data/abyss.txt results/abyss.dat
# 
# # plot word count
# results/figure/isles.png : results/isles.dat src/plotcount.py
# 	python src/plotcount.py results/isles.dat isles.png
# 
# results/figure/abyss.png : results/abyss.dat src/plotcount.py
# 	python src/plotcount.py results/abyss.dat abyss.png
# 
# clean :
# 	rm -f results/*.dat
# 	rm -f results/figure/*.png
# 
# ~~~
# 
# ### Finish off the Makefile!
# 
# ```
# # Makefile
# # Tiffany Timbers, Nov 2018
# 
# # This driver script completes the textual analysis of
# # 3 novels and creates figures on the 10 most frequently
# # occuring words from each of the 3 novels. This script
# # takes no arguments.
# 
# # example usage:
# # make all
# 
# all : doc/count_report.md
# 
# # count the words
# results/isles.dat : data/isles.txt src/wordcount.py
# 	python src/wordcount.py data/isles.txt results/isles.dat
# results/abyss.dat : data/abyss.txt src/wordcount.py
# 	python src/wordcount.py data/abyss.txt results/abyss.dat
# results/last.dat : data/last.txt src/wordcount.py
# 	python src/wordcount.py data/last.txt results/last.dat
# results/sierra.dat : data/sierra.txt src/wordcount.py
# 	python src/wordcount.py data/sierra.txt results/sierra.dat
# 	
# # create the plots
# results/figure/isles.png : results/isles.dat src/plotcount.py
# 	python src/plotcount.py results/isles.dat results/figure/isles.png
# results/figure/abyss.png : results/abyss.dat src/plotcount.py	
# 	python src/plotcount.py results/abyss.dat results/figure/abyss.png
# results/figure/last.png : results/last.dat src/plotcount.py	
# 	python src/plotcount.py results/last.dat results/figure/last.png
# results/figure/sierra.png : results/sierra.dat src/plotcount.py	
# 	python src/plotcount.py results/sierra.dat results/figure/sierra.png
# 	
# # write the report
# doc/count_report.md : doc/count_report.Rmd results/figure/isles.png results/figure/abyss.png results/figure/last.png results/figure/sierra.png
# 	Rscript -e "rmarkdown::render('doc/count_report.Rmd')"
# 	
# clean :
# 	rm -rf results/isles.dat results/abyss.dat results/last.dat results/sierra.dat
# 	rm -rf results/figure/isles.png results/figure/abyss.png results/figure/last.png results/figure/sierra.png
# 	rm -rf doc/count_report.md doc/count_report.html
# ```

# ### Pattern matching and variables in a Makefile
# 
# It is possible to DRY out a Makefile and use variables.
# 
# Using wild cards and pattern matching in a makefile is possible, but the syntax is not very readable. So if you choose to do this proceed with caution. Example of how to do this are here: http://swcarpentry.github.io/make-novice/05-patterns/index.html
# 
# As for variables in a Makefile, in most cases we actually do not want to do this. The reason is that we want this file to be a record of what we did to run our analysis (e.g., what files were used, what settings were used, etc). If you start using variables with your Makefile, then you are shifting the problem of recording how your analysis was done to another file. There needs to be some file in your repo that captures what variables were called so that you can replicate your analysis. Examples of using variables in a Makefile are here: http://swcarpentry.github.io/make-novice/06-variables/index.html

# ## What's next?
# 
# - Advanced use of reproducible reports

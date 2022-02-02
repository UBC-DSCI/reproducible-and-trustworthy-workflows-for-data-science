#!/usr/bin/env python
# coding: utf-8

# # Filenames and data science project organization, Integrated development environments
# 
# **Attribution:** much of these notes come from [Jenny Bryan](https://en.wikipedia.org/wiki/Jenny_Bryan)'s talk "Naming things" ([original slides](http://www2.stat.duke.edu/~rcs46/lectures_2015/01-markdown-git/slides/naming-slides/naming-slides.pdf) and [source code](https://github.com/jennybc/organization-and-naming))

# ## Topic learning objectives
# 
# By the end of this topic, students should be able to:
# 
# 1. Explain how project organization and file naming contribute to reproducible data science
# 2. Organize projects and name files in a sound manner
# 3. Use an integrated development environment (IDE) to create, edit and run a script (e.g., VScode in Python, or RStudio in R)
# 4. Use the IDE to access documentation/help, environment variables and efficiently navigate directories
# 5. Extend and customize an IDE with useful extensions/add-ons/tools such as linters and formatters
# 

# ## Filenames - best practices
# 
# ### Names matter
# 
# <img src="img/cheers.png" width=600>
# 
# ### What works, what doesn't?
# 
# **NO**
# 
# ~~~
# myabstract.docx
# Joe’s Filenames Use Spaces and Punctuation.xlsx
# figure 1.png
# fig 2.png
# JW7d^(2sl@deletethisandyourcareerisoverWx2*.txt
# ~~~
# 
# **YES**
# 
# ~~~
# 2014-06-08_abstract-for-sla.docx
# joes-filenames-are-getting-better.xlsx
# fig01_talk-scatterplot-length-vs-interest.png
# fig02_talk-histogram-attendance.png
# 1986-01-28_raw-data-from-challenger-o-rings.txt
# ~~~
# 
# ### Three principles for (file) names
# 
# 1. Machine readable
# 
# 2. Human readable
# 
# 3. Plays well with default ordering
# 
# #### Awesome file names :)
# 
# ```{figure} img/awesome_names.png
# :width: 600px
# :align: center
# ```
# ### Machine readable
# 
# #### Machine readable
# 
# - Regular expression and globbing friendly
#     + Avoid spaces, punctuation, accented characters, case sensitivity
# 
# - Easy to compute on
#     + Deliberate use of delimiters
#     
# #### Globbing
# 
# **Excerpt of complete file listing:**
# 
# 
# ```{figure} img/plasmid_names.png
# :width: 600px
# :align: center
# ```
# <hr>
# 
# **Example of globbing to narrow file listing:**
# 
# ```{figure} img/plasmid_glob.png
# :width: 600px
# :align: center
# ```
# 
# #### Same using Mac OS Finder search facilities
# 
# 
# ```{figure} img/plasmid_mac_os_search.png
# :width: 600px
# :align: center
# ```
# 
# 
# #### Same using regex in R
# 
# 
# ```{figure} img/plasmid_regex.png
# :width: 600px
# :align: center
# ```
# 
# 
# #### Punctuation {.smaller}
# 
# Deliberate use of `"-"` and `"_"` allows recovery of meta-data from the filenames:
# 
# - `"_"` underscore used to delimit units of meta-data I want later
# - `"-"` hyphen used to delimit words so my eyes don't bleed
# 
# 
# ```{figure} img/plasmid_delimiters.png
# :width: 600px
# :align: center
# 
# 
# <hr>
# 
# ```{figure} img/plasmid_delimiters_code.png
# :width: 600px
# :align: center
# ```
# 
# 
# This happens to be R but also possible in the shell, Python, etc.
# 
# #### Recap: machine readable
# 
# - Easy to search for files later
# 
# - Easy to narrow file lists based on names
# 
# - Easy to extract info from file names, e.g. by splitting
# 
# - New to regular expressions and globbing? be kind to yourself and avoid
#     + Spaces in file names
#     + Punctuation
#     + Accented characters
#     + Different files named `foo` and `Foo`
#     
# ### Human readable
# 
# #### Human readable
# 
# - Name contains info on content
# 
# - Connects to concept of a *slug* from semantic URLs
# 
# #### Example
# 
# **Which set of file(name)s do you want at 3 a.m. before a deadline?**
# 
# ```{figure} img/human_readable_not_options.png
# :width: 600px
# :align: center
# ```
# 
# #### Embrace the slug
# 
# <div class="columns-2">
# slug filenames
# ![](img/slug_filenames.png)
# 
# slug
# ```{figure} img/slug.jpg
# :width: 600px
# :align: center
# ```
# </div>
# 
# #### Recap: Human readable
# 
# Easy to figure out what the heck something is, based on its name
# 
# ### Plays well with default ordering
# 
# #### Plays well with default ordering
# 
# - Put something numeric first
# 
# - Use the ISO 8601 standard for dates
# 
# - Left pad other numbers with zeros
# 
# #### Examples
# 
# **Chronological order:**
# 
# ![chronological_order](img/chronological_order.png)
# ```{figure} img/chronological_order.png
# :width: 600px
# :align: center
# ```
# <hr>
# 
# **Logical order:** Put something numeric first
# 
# ```{figure} img/logical_order.png
# :width: 600px
# :align: center
# ```
# #### Dates
# 
# Use the ISO 8601 standard for dates: YYYY-MM-DD
# 
# ```{figure} img/chronological_order.png
# :width: 600px
# :align: center
# ```
# 
# 
# ```{figure} img/iso_8601.png
# :width: 600px
# :align: center
# ```
# 
# 
# #### Comprehensive map of all countries in the world that use the MM-DD-YYYY format
# 
# 
# ```{figure} img/map_mmddyyy.png
# :width: 600px
# :align: center
# ```
# 
# 
# <br>
# 
# From https://twitter.com/donohoe/status/597876118688026624.
# 
# #### Left pad other numbers with zeros
# 
# 
# ```{figure} img/logical_order.png
# :width: 600px
# :align: center
# ```
# 
# 
# <br>
# 
# If you don’t left pad, you get this:
# 
# ~~~
# 10_final-figs-for-publication.R
# 1_data-cleaning.R
# 2_fit-model.R
# ~~~
# 
# which is just sad :(
# 
# #### Recap: Plays well with default ordering
# 
# - Put something numeric first
# 
# - Use the ISO 8601 standard for dates
# 
# - Left pad other numbers with zeros
# 
# #### Recap
# 
# #### Three principles for (file) names
# 
# 1. Machine readable
# 
# 2. Human readable
# 
# 3. Plays well with default ordering
# 
# #### Pros
# 
# - Easy to implement NOW
# 
# - Payoffs accumulate as your skills evolve and projects get more complex
# 
# #### Go forth and use awesome file names :)
# 
# 
# ```{figure} img/chronological_order.png
# :width: 600px
# :align: center
# ```
# 
# <br>
# 
# 
# ```{figure} img/logical_order.png
# :width: 600px
# :align: center
# ```
# 

# ## Project organization
# 
# A good project structure looks similar to this:
# 
# ```
# project/          
# ├── data/              *.csv        
# │   ├── processed/
# │   └── raw/     
# ├── reports/           *.ipynb *.Rmd
# ├── src/               *.py *.R
# ├── doc/               *.md
# ├── README.md
# └── environment.yaml (or renv.lock)
# ```
# 
# This can differ slightly between projects
# and for R the `src` directory is often just called `R/`,
# whereas for Python is has the same name as the project (`project`).
# You will learn more about project hierarchy when making packages.
# 
# <!--
# A place for everything, everything in its place.
# 
# Benjamin Franklin
# 
# 
# 
# ---
# 
# ![beer_messy_tidy](img/beer_messy_tidy.png)
# 
# ---
# 
# ![files_messy_tidy](img/files_messy_tidy.png)
# 
# ## Face it...
# 
# - There are going to be files
# 
# - LOTS of files
# 
# - The files will change over time
# 
# - The files will have relationships to each other
# 
# - It'll probably get complicated
# 
# ## Mighty weapon
# 
# - File organization and naming is a mighty weapon against chaos
# 
# - Make a file's name and location VERY INFORMATIVE about what it is, why it exists, how it relates to other things
# 
# - The more things are self-explanatory, the better
# 
# - READMEs are great, but don't document something if you could just make that thing self-documenting by definition
# 
# 
# ## Attribution:
# 
# - Slides borrowed from the [Data Carpentry](https://datacarpentry.org/) [Reproducible Science Workshop](https://datacarpentry.org/rr-organization1/)
# 
# -->

# ### A tour de data science project organization
# 
# Below we link to three different data science projects shared via GitHub repositories. The first is a data analysis project, while the latter two are data science tools (an R and a Python package, respectively).
# 
# As you explore these projects, note the following similarities:
# - Files related generally to the project are found in the project root (e.g., `README`, `CODE_OF_CONDUCT.md`, computational environment files, etc)
# - Code files are generally found in the `src` or `R` directory
# - `data` houses raw and processed data
# - `doc` houses documentation files and or documents related to the project (sometimes there is both a `doc` and `reports` directory when there are two kinds of writing in a project).
# - Other directories can be added as needed to group files with like/similar functions. Most important is that they have descriptive and obvious names related to the directory contents.
# 
# ##### Example projects
# - [a data analysis project](https://github.com/ttimbers/breast_cancer_predictor)
# - [a R package](https://github.com/ttimbers/canlang)
# - [a Python package](https://github.com/ttimbers/pycounts_tat)

# ## Integrated development environments
# 
# Integrated development environments (IDEs) are software that provide comprehensive tools for programming in one place. 
# 
# The classic Jupyter notebook interface is typically not considered an IDE, however the newer, JupyterLab interface is. 
# 
# <img src="img/jupyternotebook.png" width=800>
# 
# <img src="img/jupyterlab.png" width=800>
# 
# Other very popular IDEs for data science include RStudio and VSCode. We will now explore these and look for similarities to identify key IDE features important for developing code for data science.
# 
# <img src="img/rstudio.png" width=800>
# 
# > **Note:** RStudio was originally developed to work with the R programming language, but now it can work with Python well too! If you would like to use RStudio with Python, please follow the instructions here on how to configure this: <https://ttimbers.github.io/intro-to-reticulate/setup-instructions/setup-after-installing-python.html>
# 
# <img src="img/vscode.png" width=800>
# 
# > **Note 1:** If you would like to use VS Code with Python, then please follow the instructions below on how to configure this: 
# > 1. Install the VSCode [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) in your VSCode application
# > 2. Code can be sent line-by-line to the Python console via `Shift` + `Enter`. The first time you do this, an interactive iPython console will open up. Future `Shift` + `Enter` keystrokes during that work session will send code to that console.
# > 3. A bash command line terminal console can be added by clicking the **Terminal** > **New Terminal** menu item, and then the "+" symbol and selecting "bash".
# 
# > **Note 2:** If you would like to use VS Code with R, please follow the instructions below on how to configure this: 
# > 
# > 1. Install the VSCode [R Extension](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r) in your VSCode application
# > 2. In the R console, install `languageserver` R package via `install.packages("languageserver")`
# > 3. Install the `radian` Python package (which gives an improved R console in VS Code) via `conda install radian`
# > 4. In the VS Code settings (found by clicking the **Code** > **Preferences** > **Settings** menu item) search for "r.path" and paste the path to `radian` under the textbox for your operating system (you can find the path to `radian` by typing `which radian` in the terminal). For example, on my Mac x86 laptop, the path is `/Users/tiffany/opt/miniconda3/bin/radian`
# > 5. In the VS Code settings (Code > Preferences > Settings) search for "R: Bracketed Paste" and select the checkbox for this setting (this allows you to send code to the R console when it is split across lines without it breaking).
# > 6. An interactive R console can be added by clicking the **Terminal** > **New Terminal** menu item, and then the "+" symbol and selecting "R Terminal". Code can be sent line-by-line to the R console via `Cmd` + `Enter` (Mac) or `Control` + `Enter` (Windows).
# 
# #### Key features of all of these IDEs includes:
# - screen split into panes
# - file browser
# - convenient access to R/Python console and a terminal
# - editor for code writing
# - code autocompletion
# - code/syntax highlighting

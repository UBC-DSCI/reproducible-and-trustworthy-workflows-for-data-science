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
# ```{figure} ../img/awesome_names.png
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
# ```{figure} ../img/plasmid_names.png
# :width: 600px
# :align: center
# ```
# <hr>
# 
# **Example of globbing to narrow file listing:**
# 
# ```{figure} ../img/plasmid_glob.png
# :width: 600px
# :align: center
# ```
# 
# #### Same using Mac OS Finder search facilities
# 
# 
# ```{figure} ../img/plasmid_mac_os_search.png
# :width: 600px
# :align: center
# ```
# 
# 
# #### Same using regex in R
# 
# 
# ```{figure} ../img/plasmid_regex.png
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
# ```{figure} ../img/plasmid_delimiters.png
# :width: 600px
# :align: center
# 
# 
# <hr>
# 
# ```{figure} ../img/plasmid_delimiters_code.png
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
# ```{figure} ../img/human_readable_not_options.png
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
# ```{figure} ../img/slug.jpg
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
# ```{figure} ../img/chronological_order.png
# :width: 600px
# :align: center
# ```
# <hr>
# 
# **Logical order:** Put something numeric first
# 
# ```{figure} ../img/logical_order.png
# :width: 600px
# :align: center
# ```
# #### Dates
# 
# Use the ISO 8601 standard for dates: YYYY-MM-DD
# 
# ```{figure} ../img/chronological_order.png
# :width: 600px
# :align: center
# ```
# 
# 
# ```{figure} ../img/iso_8601.png
# :width: 600px
# :align: center
# ```
# 
# 
# #### Comprehensive map of all countries in the world that use the MM-DD-YYYY format
# 
# 
# ```{figure} ../img/map_mmddyyy.png
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
# ```{figure} ../img/logical_order.png
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
# ```{figure} ../img/chronological_order.png
# :width: 600px
# :align: center
# ```
# 
# <br>
# 
# 
# ```{figure} ../img/logical_order.png
# :width: 600px
# :align: center
# ```
# 

# #  Tell Git to ignore irrelevant files using a `.gitignore` file
# 
# You may have encountered this before:
# 
# ```
# git status
# ```
# 
# ```
# On branch timberst-master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
# 
# 	.ipynb_checkpoints/
# 	.DS_Store
# 
# no changes added to commit (use "git add" and/or "git commit -a")
# ```
# 
# Git is letting us know about untracked files (ones we have never committed before). We don't care about these files. We'd prefer not to have them clutter our view (so we can pay attention to files we do want to track). What do we do?

# ## Create a `.gitignore` file
# 
# Using the plain text editor of your choice (mine is VS Code) create a file called `.gitignore` inside your Git repo. To do this with VS Code, I would type:
# 
# ```
# code .gitignore
# ```
# 
# Inside the text file, list the files and folders you would like to ignore, one per line. For example:
# 
# ```
# .ipynb_checkpoints/
# .DS_Store
# ```
# 
# Save the file, and `add` and `commit` it with Git. Then try `git status` again. You should see:
# 
# ```
# On branch timberst-master
# nothing to commit, working tree clean
# ```

# ## `.gitignore` tips and tricks
# 
# - append `**/` to the beginning of any file/folder names listed in the `.gitignore` file to have them ignored in subdirectories within the repo as well
# - create a [global `.gitignore` file](https://help.github.com/articles/ignoring-files/#create-a-global-gitignore) so that you do not have to create the same `.gitignore` for all your homework repos

# Let's create a `gitignore` file in our 521 lab 2 repo. 
# 
# ### Steps to follow: 
# 1. Use a text editor (e.g., VS Code, nano, Jupyter) to create a file called `.gitignore` in your 521 lab 2 repo
# 2. Add `**/.ipynb_checkpoints/` to that file and save it
# 3. `add` and `commit` it with Git
# 4. Type `git status` and see if you no longer see `.ipynb_checkpoints/` as a untracked file

# # Project organization
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

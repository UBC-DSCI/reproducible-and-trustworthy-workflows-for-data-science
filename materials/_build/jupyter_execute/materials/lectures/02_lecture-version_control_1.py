#!/usr/bin/env python
# coding: utf-8

# # Version control for transparency and collaboration

# ## Week learning objectives
# 
# By the end of the lecture, students should be able to:
# 
# 1. Explain why and how data analysis projects benefit from both local and remote version control
# 2. Use Git's basic functions to save changes to local and remote version control, as well as view and restore older versions of files
# 3. Use Git and GitHub to successfully collaborate with others (e.g., handle merge conflicts, use a fork-pull-request and branch-pull-request workflow to contribute to a project, organize tasks through issue milestones and project boards)

# ## Version control
# 
# > *"Version control is the process of keeping a record of changes to documents, including when the changes were made and who made them, throughout the history of their development. It also provides the means both to view earlier versions of the project and to revert changes."*
# >
# > -- [*Data Science: A First Introduction*](https://ubc-dsci.github.io/introduction-to-datascience/Getting-started-with-version-control.html)
# 
# In this course we will learn to use the most popular version control software tools, Git and GitHub. A schematic of local and remote version control repositories using these tools is shown below:
# 
# <img src="https://ubc-dsci.github.io/introduction-to-datascience/_main_files/figure-html/vc1-no-changes-1.png" width=800>
# 
# Source: [*Data Science: A First Introduction*](https://ubc-dsci.github.io/introduction-to-datascience/Getting-started-with-version-control.html)

# ### A Zoom poll!
# 
# Before this class, you were asked to read [Chapter 12: Collaboration with version control](https://ubc-dsci.github.io/introduction-to-datascience/Getting-started-with-version-control.html) from Data Science: A First Introduction. We're goig to do a Zoom poll with the following questions to check your knowledge!
# 
# **1. Which of these is untrue about the Git and GitHub version control software?**
# 
# *a. Allows you to view and/or retrieve older snapshots of the files and directories in a project.*
# 
# *b. Automatically snapshots your work every 2 minutes.*
# 
# *c. Provides transparency on who made what changes to files and directories in a document.*
# 
# *d. Can act as a way to back-up your work.*
# 
# 
# **2. GitHub is the software you use locally on your computer (i.e., your laptop) to commit changes to the version control history. True or False?**
# 
# *a. True*
# 
# *b. False*
# 
# *c. Neither true or false.*
# 
# 
# **3. You changed two files (`notes.txt` and `eda.ipynb`) but you only want to commit changes to one of them (`eda.ipynb`) to the version control history. Which Git command allows you to specify this?**
# 
# *a. Add*
# 
# *b. Commit*
# 
# *c. Push*
# 
# *d. Push*
# 
# **4. At a minimum, how often should you push your work to GitHub?**
# 
# *a. Every 5 min.*
# 
# *b. Every 30 min.*
# 
# *c. At the end of every work session.*
# 
# *d. Once a week.*
# 
# 
# **5. You try to push your most recent commit from your locale version control repository to your remote repository on GitHub and it fails because Git says the `remote contains work that you have locally`. What do should you do next?**
# 
# *a. Commit the changes you made recently in your working directory.*
# 
# *b. Force push your changes.*
# 
# *c. Pull the changes from the remote repository that you do not have locally.*
# 
# 
# **6. You pull changes that exist in your remote version control repository on GitHub that you do not have in your local version control repository, and you get the message `Auto-merging in <FILENAME> CONFLICT (content): Merge conflict in <FILENAME> Automatic merge failed; fix conflicts and then commit the result`. What do you need to do?**
# 
# *a. Push the changes from the local repository that you do not have remotely.*
# 
# *b. Force pull the changes.*
# 
# *c. Manually open the file with the conflict and edit it to have the desired version of the changes, as well as remove the special Git syntax used to identify the merge conflict.*

# ## Hands on practice with merge conflicts!
# 
# One of the major blockers getting used to using version control is dealing with merge conflicts! 😱
# 
# Git can automatically handle merging two versions of a file if each collaborator changes different lines, however when two collaborators change the same line, Git throws up its hands and says, I cannot handle this responsbility, I need help from a human!
# 
# <img src="https://media.giphy.com/media/4SZxcPTtlGAZa/giphy.gif">

# When this happens, your human task is to find the merge conflict markers, remove them, and settle on which version of the line(s) where the conflict occurred should remain.
# 
# > ### Merge conflict markers:
# > 
# > - the beginning of the merge conflict is preceded by `<<<<<<< HEAD` 
# > - the end of the merge conflict is marked by `>>>>>>>`
# > - between the markings mentioned above, Git also inserts a separator (`=======`). The version of the change before the separator is your > change, and the version that follows the separator was the change that existed on GitHub. 

# We are going to now generate and resolve merge conflicts.I have set-up a template GitHub repository for you so that you can easily generate a merge conflict to resolve. We will do this twice, once with a simple plain text file (*e.g.*, an R script) and once with a more complex text file (*e.g.*, a Jupyter notebook).
# 
# #### Resolving merge conflicts in a simple text file:
# 
# **Steps:**
# 
# 1. Click the green “Use this template” button from [this GitHub repository](https://github.com/ttimbers/r-cube) to obtain a copy of it for yourself (do not fork it).
# 
# 2. Clone this repository to your computer.
# 
# 3. Create a remote branch named `make-conflict` (this will use GitHub Actions to create a commit in your remote repository).
# 
# 4. Fix the second line in `cube.r` so that it calculates the cube, not the square (e.g., change `x^2` to `x^3`). Commit your changes to version control via Git and push your changes to GitHub.
# 
# 5. Resolve the merge conflict them so that you can see your changes on GitHub.
# 
# 
# #### Resolving merge conflicts in a more complex text file:
# 
# **Steps:**
# 
# 1. Click the green “Use this template” button from [this GitHub repository](https://github.com/ttimbers/r-cube-notebook) to obtain a copy of it for yourself (do not fork it).
# 
# 2. Clone this repository to your computer.
# 
# 3. Create a remote branch named `make-conflict` (this will use GitHub Actions to create a commit in your remote repository).
# 
# 4. Fix the second line in the code cell in `cube.ipynb` so that it calculates the cube, not the square (e.g., change `x^2` to `x^3`). Commit your changes to version control via Git and push your changes to GitHub.
# 
# 5. Resolve the merge conflict them so that you can see your changes on GitHub.

# ## Going back in time!
# 
# ### Just going for a look:
# 
# The easiest way to go back in time in your version control repository is to use the GitHub.com website. To do this, we click the commits link:
# 
# <img src="img/releases.png" width=800>
# 
# Then we can view the history, along with the commit messages. To view the state of a repository at that time, we click on the "**<>**" button:
# 
# <img src="img/commits_eg.png" width=800>

# ### Travelling in time or bringing something something from the back from the past:
# 
# Sometimes you want to be able to explore and run the files from the past, or bring a past version of a file to the future. When we need to do either of those things, we should be working with Git in our local repository. 

# Here's the same history as viewed above, but using the JupyterLab Git extension:
# 
# <img src="img/jupyter-git-history.png" width=800>

# To see what was changed at a given point in history, click the down arrow associated with the commit. You can then diff the file (see what was changed for a particular file by clicking the file icon beside it.
# 
# <img src="img/jupyter-view-changes.png">

# #### Travelling in time to the past
# 
# If you wanted to move your project's file and directories (so entire state) back to this point in time you can do that by clicking the clock icon. **NOTE: If you do this, be sure you pushed your changes, as it will discard anything more recent than this commit on your local computer (i.e., this is a hard reset).**
# 
# <img src="img/jupyter-hard-reset.png" width=500>
# 
# Again, because this is a hard reset, Git will warn you about the consequences:
# 
# <img src="img/jupyter-hard-reset-warning.png" width=500>
# 
# Once, you have done this, you will see the more recent commits in your history are GONE!
# 
# <img src="img/jupyter-after-hard-reset.png" width=500>

# #### Exercise:
# 
# 1. Clone [this GitHub repository](https://github.com/ttimbers/data_analysis_pipeline_eg) to your computer.
# 
# 2. View the names of the files that were changed in commit `44c17be`, and the specific changes made to the file `doc/count_report.Rmd`.
# 
# 3. Do a hard reset to the state of the repository as it was in commit `44c17be`.
# 
# 4. Then pull the Git remote repository to go back to where you started.
# 
# *Question - could you have gone back to where you started if the work was not stored in the remote repository?*
# 

# #### Bringing something something from the back from the past
# 
# There is not a nice and easy way (that I am aware of) of cherry-picking a version of single file from the past using the JupyterLab Git extension. To do this, I resort to the Git command line tool in the terminal. The general command is:
# 
# ```
# git checkout <HASH> <FILE>
# ```
# 
# For example, to checkout the version of the `doc/count_report.Rmd` from the commit whose hash starts with `5837143`, we would type: 
# 
# ```
# git checkout 5837143 doc/count_report.Rmd
# ```
# 
# That will bring that version of the `doc/count_report.Rmd` into our working directory. We can view it, run it or use it, et cetera. If we want to keep that version going forward for our project, we would have to then add and commit that version of the file to do so.
# 
# > ##### What Git tool to use?
# >
# > There are many many many different tools for using Git. We have so far discussed two in this class (the JupyterLab Git extension,
# > and the Git command line). Others include GitHub Desktop, GitKraken, Source Tree, RStudio's Git GUI, and VSCode's Git GUI.
# > Which one should you use? Anyone that fits you best! I recommend experimenting with a few and then settling in with the one
# > that you find easiest to use. One note is that some commands are limited in some tools (e.g., the example above with the
# > JupyterLab Git extension). If you hit that case in your favorite tool, you can use the Git command line tool to get around it
# > and then go back to primarily using your tool of choice.

# ## Git Branches
# 
# Branches allow you to have a playground 
# for developing and testing new additions to your code,
# as well as fixes.
# This playground lets your explore, experiment and test 
# in a safe place - away from others that might be using 
# or depending on the current version of your code.
# This is perhaps more obviously useful if your project
# is deployed and has users (e.g., a data visualization dashboard, 
# an R or Python package, a phone app, etc),
# but this can also be useful for code that make up a data analyses.
# As, in addition to the reasons stated above for branching,
# branching also lets you organize units of work into smaller, 
# more manageable chunks that are easier for collaborators to check over and review.
# 
# Once the new code additions or fixes have been 
# finalized in their branch playground,
# they can be merged back to the main code-base.
# Several branch playgrounds can co-exist, 
# one for each new code addition or fix being worked on.
# This allows for parallelization of work!
# 
# We can use a construction of a house
# as a metaphor for this kind of development.
# First,
# you need to build the foundation.
# Since everything depends on the foundation being built,
# this would be developed on the main branch.
# When the foundation is finished,
# the construction of other parts of the house that don't depend on each other
# could take place in parallel,
# e.g. some contributors might start working on the walls and others on the floor.
# When either of these features is finished, 
# it can be added back to the house
# (merged into main).
# When depicted graphically,
# this process would look something like this
# (each dot is a commit).
# 
# <img src="img/branches-house-analogy.png" width=400>

# A more realistic Git branching example for a data analysis project might look something like this:
# 
# <img src="img/git-branch-diagrams.png" width=400>

# ### Creating a branch
# 
# Using the JupyterLab Git extension, you create a new branch on your local computer by clicking on the up arrow in the "Current Branch" tab, and clicking the blue "New Branch" button.
# 
# <img src="img/create-new-branch.png" width=500>
# 
# A dialogue box will open, and ask you to name the branch. After you do this, click on the blue "Create Branch" button. Remember to name it after the work you plan to do. Here we plan to fix the documentation a bit, so we will call it `patch-docs`.
# 
# <img src="img/name-new-branch.png" width=300>
# 
# To finally switch to the new playground (i.e., your new branch) click on the branch name of the new branch you just created in the Branches section of the "Current Branch" tab.
# 
# <img src="img/switch-to-new-branch.png" width=500>
# 
# As you work here, you can commit your changes to version control locally, and even push your changes to the remote repository. All the changes however will live only on that branch until you do something to move them to another branch. When you want to start discussing your changes with your collaborators to start the process of bringing these changes into the main branch (main code-base) you typically create what is called a pull request. A pull request is a like an asking your collaborators "is it OK to merge my code?" Usually there will be some discussion and a few more revisions to the code, but eventually they will give you the thumbs up when everything looks good and the code can then be merged. We will discuss this more next.

# #### Exercise
# 
# 1. Make your own copy of [this GitHub repository](https://github.com/ttimbers/sqrt) by clicking the green "Use this template" button.
# 
# 2. Create a new branch named `better_error_msg` in the local repository using the JupyterLab Git extension.
# 
# 3. On that branch, fix the `sqrt.py` so that if you run this script with a negative number as an argument you do not get an difficult to understand error, but instead throw a helpful exception informing the user that the number should be positive. Fix to add to `sqrt.py`:
#   
#   ```
#   if number < 0:
#     raise Exception("n should not a positive number")
#   ```
# 
# 4. Switch back to the `main` branch and look at the `README.md` file - do you see the change there?
# 
# 5. Switch back to the `better_error_msg` branch - do you see the change there?
# 
# 6. Push your change to the remote GitHub repository, and see where you can find it there!

# ## Creating a pull request
# 
# To create a pull request,
# go to the remote GitHub repository,
# and usually GitHub will should show you a yellow banner listing any recently pushed branches.
# 
# <img src="img/create-pr.png" width=700>
# 
# To create a pull request,
# you click the green button "Compare & pull request".
# In the new page,
# add a message to describe the changes you have made,
# scroll down to review the changed files,
# and the click the green button that reads "Create pull request".
# If you are working together in a team,
# you could also designate certain team members to review your work
# and assign relevant labels,
# via the right hand side panel.
# 
# The next step is for a collaborator to review your work
# and merge it in if they approve it.

# #### Exercise
# 
# 1. Use the green "Compare & pull request" button on the yellow banner to open a pull request.
# 
# 2. Go to the "Pull requests" tab on the remote GitHub repository and explore the "Conversation" and "Files changed" sub-tabs there.

# ## Next class: 
# 
# - pull request reviews
# - GitHub tools for project management

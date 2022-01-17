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

# ## A Zoom poll!
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

# 

# 

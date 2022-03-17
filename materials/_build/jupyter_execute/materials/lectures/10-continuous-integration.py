#!/usr/bin/env python
# coding: utf-8

# # Automated testing and continuous integration

# ## Topic learning objectives
# 
# By the end of this topic, students should be able to:
# 
# 1. Argue the costs and benefits of using automated test infrastructure
# 2. Use a testing framework (e.g., `testhat`) to automate the running of a
# project's entire test suite
# 3. Use a continuous integration (e.g., GitHub Actions) to automate the running of the
# test suite using the testing framework
# 4. Incorporate non-code-functionality tests such as style/format checkers into a testing
# pipeline

# ## Continuous Integration (CI)
# 
# Defined as the practice of **frequently** integrating code (*e.g.*, several times a day) changes from contributors to a shared repository. Often the submission of code to the shared repository is combined with automated testing (and other things, such as style checking) to increase code dependability and quality.
# 
# ### Why use CI + automated testing
# 
# - detects errors sooner
# - reduces the amount of code to be examined when debugging
# - facilitates merging
# - ensures new code additions do not introduce errors

# ## GitHub actions
# 
# A tool and service for automating software development tasks, located in the same place where you already store your code.
# 
# ### Key concepts:
# **Actions:** Individual tasks you want to perform.
# 
# **Workflow:** A collection of actions (specified together in one file).
# 
# **Event:** Something that triggers the running of a workflow.
# 
# **Runner**: A machine that can run the Github Action(s).
# 
# **Job**: A set of steps executed on the same runner.
# 
# **Step**: A set of commands or actions which a job executes.

# ### Examples of GitHub Actions
#  
# You have already interacted with GitHub Actions in this class! We used it to:
# 
# 1. Generate the issues in the [`mds-homework` repo](https://github.com/ubc-mds/mds-homework) upon push to the "create" branch: <https://github.com/UBC-MDS/mds-homework/blob/master/.github/workflows/create_issues.yml>
# 
# 2. Generate a pull request in the [`review-my-pull-request` repo](https://github.com/ttimbers/review-my-pull-request) upon push to the "pr" branch: : <https://github.com/ttimbers/review-my-pull-request/blob/master/.github/workflows/pr.yml>

# ### Exercise: Getting to know GitHub Actions workflows
# 
# We are going to each create our own GitHub Actions workflow. This workflow is a very simple toy example where we run some `echo` shell commands to print things to the runner's terminal.
# 
# #### Steps:
# 
# 1. Create a new public **GitHub.com** repository with a `README`.
# 
# 2. Click on the "Actions" tab
# 
# 3. Click on the first "Set up this workflow" button
#     
#     <img src="img/gh-actions-setup.png" width=600>
# 
# 4. Click on the two green commit buttons to add this workflow file
# 
# 5. Go to the "Actions" tab and look at the build logs by following these instructions:
# 
#     Click on the message associated with the event that created the action:
#     
#     <img src="img/check-logs1.png" width=600>
#     
#     Click on the build link:
#     
#     <img src="img/check-logs2.png" width=600>
#     
#     Click on the arrow inside the build logs to expand a section and see the output of the action:
# 
#     <img src="img/check-logs3.png" width=600>
#     
#   
# ### GitHub Actions workflow file:
# 
# A `YAML` file that lives in the `.github/workflows` directory or your repository which speciies your workflow. 
# 
# ```
# # This is a basic workflow to help you get started with Actions
# 
# name: CI
# 
# # Controls when the workflow will run
# on:
#   # Triggers the workflow on push or pull request events but only for the main branch
#   push:
#     branches: [ main ]
#   pull_request:
#     branches: [ main ]
# 
#   # Allows you to run this workflow manually from the Actions tab
#   workflow_dispatch:
# 
# # A workflow run is made up of one or more jobs that can run sequentially or in parallel
# jobs:
#   # This workflow contains a single job called "build"
#   build:
#     # The type of runner that the job will run on
#     runs-on: ubuntu-latest
# 
#     # Steps represent a sequence of tasks that will be executed as part of the job
#     steps:
#       # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
#       - uses: actions/checkout@v2
# 
#       # Runs a single command using the runners shell
#       - name: Run a one-line script
#         run: echo Hello, world!
# 
#       # Runs a set of commands using the runners shell
#       - name: Run a multi-line script
#         run: |
#           echo Add other actions to build,
#           echo test, and deploy your project.
# 
# ```
# 
# The file above has:
# - 3 possible event triggers (push to main, pull request to main, or manual dispatch through the Actions tab)
# - runs on an Ubuntu OS
# - one job called "build"
# - 3 steps
# - the type of runner is ubuntu
# - the first step uses an action, and the following two steps run commands

# ### Commands vs actions
# 
# Steps can consist commands or actions. Let's spend some time to discuss what each of these are and how they differ.
# 
# ### Commands
# 
# Steps that use commands look like the one shown below. They consist of a `name` and a `run` parameter. The commands listed after `run` are run in the runner's shell:
# 
# ```
# - name: Run a one-line script
#       run: echo Hello, world!
# ```
# 
# As shown in the file above, we can run multiple commands in a step using the `|` character:
# ```
# - name: Run a multi-line script
#       run: |
#         echo Add other actions to build,
#         echo test, and deploy your project.
# ```
# 
# ### Actions
# 
# Steps that use actions look like the one shown below (which builds and publishes Docker containers). They always have a `uses` parameter, and often also have `name` and `with` parameters. The `uses` parameter specifies which action to use, and the `with` parameters provide arguments to those actions. The `@master` at the name of the `uses` line, specifies whether to use the version at the head of the actions default branch, or a specific version (*e.g.,* `@v2`).
# 
# ```
# - name: Publish to Registry
#       uses: elgohr/Publish-Docker-Github-Action@master
#       with:
#         name: myDocker/repository
#         username: ${{ secrets.DOCKER_USERNAME }}
#         password: ${{ secrets.DOCKER_PASSWORD }}
# ```
# 
# Actions commonly perform one task in a workflow. There are two ways to build actions, either using JavaScript or by creating a Docker container that runs a shell script. For the latter such actions are defined by:
# - a Dockerfile
# - a shell script to run inside the Docker container
# 
# > In this course we will use actions built by others, but not build our own. That is beyond the scope of this course. However, if you are intersted in learning more, I point you to the documentation below.

# #### Optional:
# 
# For example, for the action above see its:
# - [Dockerfile](https://github.com/elgohr/Publish-Docker-Github-Action/blob/master/Dockerfile)
# - [endpoint.sh script](https://github.com/elgohr/Publish-Docker-Github-Action/blob/master/entrypoint.sh)
# - [GitHub repo](https://github.com/elgohr/Publish-Docker-Github-Action)
# 
# Read the docs here to learn how to build your own Docker container GitHub action: <https://help.github.com/en/actions/building-actions/creating-a-docker-container-action>
# 
# Read the docs here to learn how to build your own JavaScript GitHub action:
# <https://help.github.com/en/actions/building-actions/creating-a-javascript-action>

# ## Case study: a simplified version of the Python Python cookiecutter package `ci.yml` workflow:
# 
# - Let's break down a simplified version of the [`ci.yml`](https://github.com/py-pkgs/py-pkgs-cookiecutter/blob/main/%7B%7Bcookiecutter.package_name%7D%7D/.github/workflows/ci.yml) workflow file to start to better understand a real use case of GitHub Actions.
# 

# ### Exercise: Orientating ourselves with the `ci.yml` workflow
# 
# Let's answer the following questions to start better understanding the `ci.yml` workflow.
# 
# 1. How many jobs are there?
# 
# 2. How many steps are there?
# 
# 3. What which steps are actions and which are commands
# 
# 4. What is the type of runner
# 
# 5. What events trigger this workflow?

# ### Exercise: Adding the `ci.yml` workflow to your `pycount*` repository
# 
# Let's add the `ci.yml` workflow to our `pycount*` repository from week 1!
# 
# 1. Go to the actions tab for your GitHub repository
# 
# 2. Click on "*set up a workflow yourself*"
# 
# 3. Delete the template action provided to you, and paste the `ci.yml` file above into the text editor. Rename the file `ci.yml`.
# 
# 4. Click "Start commit", enter a commit message and then click "Commit".

# ## Storing and use GitHub Actions credentials safely via GitHub Secrets
# 
# Some of the tasks we want to do in our workflows require authentication. However, the whole point of this is to automate this process - so how can we do that without sharing our authentication tokens, usernames or passwords in our workflow files?
# 
# GitHub Secrets is the solution to this! 
# 
# GitHub Secrets are encrypted environment variables that are used only with GitHub Actions, and specified on a repository-by-repository basis. They can be accessed in a workflow file via: `${{ secrets.SECRET_NAME }}`
# 
# See GitHub's help docs for how to do this: <https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets>

# ## Authenticating with the `GITHUB_TOKEN`
# 
# What if you need to do Git/GitHub things in your workflow? Like checkout your files to run the tests? Create a release? Open an issue? To help with this GitHub automatically (i.e., you do not need to create this secret) creates a secret named `GITHUB_TOKEN` that you can access and use in your workflow. You access this token in your workflow file via:
# 
# ```
# ${{ secrets.GITHUB_TOKEN }}
# ```
# 
# ## Creating and accessing environment variables in GitHub Actions
# 
# Sometimes our commands or actions need environment variables. In both of these scenarios, we create environment variables and access them within a step via: 
# 
# ```
# steps:
#   - name: Hello env vars
#     run: echo $VARIABLE_NAME1 $VARIABLE_NAME2
#     env:
#       VARIABLE_NAME1: <variable_value1>
#       VARIABLE_NAME2: <variable_value2>
# ```
# 
# 

# ## Matrix workflows
# 
# We don't want our software to just work on one operating system, or just one version of Python or R. Ideally it is compatible with the three major operating systems as well as a couple versions of the programming language it was written it.
# 
# How do we ensure this? Well, we could have several GitHub Action workflows, each of which runs the job on a different version of Python, on a different operating system. However, there would be a lot of redundancy in those workflows, with the only differences between them being the operating system of the runner and the version of Python.
# 
# A more efficient way to do this with GitHub Actions workflows is to use matrix workflows. In these workflows, we use a matrix variable, which we specify as: 
# 
# ```
# strategy:
#   matrix:
#     <variable_name>: [<value1>, <value2>]
# ```
# 
# which we can refer to in the workflow steps as:
# 
# ```
# ${{ matrix.<variable_name> }}
# ```
# 
# When we do this, GitHub Actions runs multiple jobs, one for each of the values in the matrix variable.

# ### Exercise: in English, what this version of `ci.yml` file do?
# 
# Now that we have some understanding of GitHub Actions workflows, let's use that knowledge to write in English what each of the steps do in this more complicated version of the workflow found in  `ci.yml`.
# 
# ```
# name: ci
# 
# on:
#   # Trigger the workflow on push or pull request to main
#   push:
#     branches:
#       - main
#   pull_request:
#     branches:
#       - main
# 
# jobs:
#   ci:
#     runs-on: ${{ matrix.os }}
#     strategy:
#       matrix:
#         os: [ubuntu-latest, macos-latest, windows-latest]
#         python-version: 3.9
#         
#     steps:
#     - name: Setup Python
#       uses: actions/setup-python@v2
#       with:
#         python-version: 3.9
#     
#     - name: Checkout repository
#       uses: actions/checkout@v2
#   
#     - name: Install Poetry
#       uses: snok/install-poetry@v1
#     
#     - name: Install package
#       run: poetry install
#    
#     - name: Test with pytest
#       run: poetry run pytest tests/ --cov=pycounts_tb --cov-report=xml
#       
#     - name: Upload coverage to Codecov  
#       uses: codecov/codecov-action@v2
#       with:
#         file: ./coverage.xml    # coverage report
#         fail_ci_if_error: true
# ```
# 
# #### Steps in English:
# 
# 1. Set up and install Python on the runner
# 
# 2. Checking out the files of the repository to the runner (last commit)
# 
# 3. Install Poetry
# 
# 4. Use Poetry to install dependencies and the package
# 
# 5. Run tests and check coverage, generate a coverage report
# 
# 6. Send the coverage report to codecov.io
# 
# #### *How many jobs are run? What does each do?*
# 

# ## Setting up GitHub Actions workflows with R
# 
# The dev version of `usethis` has functions that will let you set-up your CI using GitHub Actions with ease! Here's a quickstart guide below, and more details can be found in the [Github actions with R](https://ropenscilabs.github.io/actions_sandbox/) book.
# 
# 1. Add the `covr` package as a suggested dependendency to your package via: `usethis::use_package("covr", type = "Suggests")`
# 
# 2. Add a GitHub Actions workflows that runs a comprehensive build check across the major operating systems and runs the test suite and calculates coverage via: `usethis::use_github_action_check_standard()` and `usethis::use_github_action("test-coverage.yaml")`
# 
# 3. Link your R package GitHub repo with [codecov.io](https://codecov.io/)
# 
# 4. Copy the [codecov.io](https://codecov.io/) token for that repo from [codecov.io](https://codecov.io/) and add that as a GitHub Secret named `CODECOV_TOKEN`
# 
# 5. Add the [codecov.io](https://codecov.io/) badge markdown syntax to your `README.Rmd` and knit to render the `README.md` file.
# 
# 6. Push your local changes to GitHub and sit back and watch the magic happen ✨
# 
# ![](https://media.giphy.com/media/3osxYyxqXmZQt7DPtm/giphy.gif)

# ## Resources:
# 
# ### Curated list of awesome actions to use on GitHub 🎉
# 
# - <https://github.com/sdras/awesome-actions>
# 
# ### GitHub Actions for the R community
# - <https://github.com/r-lib/actions>

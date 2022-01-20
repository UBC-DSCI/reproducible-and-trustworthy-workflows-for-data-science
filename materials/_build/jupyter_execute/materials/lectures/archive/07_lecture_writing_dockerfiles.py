#!/usr/bin/env python
# coding: utf-8

# # Lecture 7 - Writing your own Dockerfile!

# ## Learning Objectives
# 
# By the end of the lecture, students should be able to:
# 
# - Use Docker to run RStudio and Jupyter
# - Write a Dockerfile
# - Build a Docker image from a Dockerfile on your laptop
# - List good Docker base images for R and Python projects

# ## Using Docker to run RStudio
# 
# To keep your Data Science team, or even just yourself, organized using the same dependencies to develop code, you can use Docker to run RStudio!

# #### Let's do it!
# 
# #### Step 1 - launch the Docker app (for OSX & Windows only)
# - Use launchpad/Finder/Start menu/etc to find and launch Docker
# 
# 
# #### Step 2 - get tidyverse image from Dockerhub
# - open command line (terminal/GitBash)
# - type: `docker pull rocker/tidyverse`
# - verify that it successfully pulled by typing: `docker images`, you should see something like:
# ```
# REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
# rocker/tidyverse          latest              a2cd50729659        17 hours ago        1.82GB
# ttimbers/makefile2graph   latest              823dcba8f792        13 months ago       469MB
# ```

# #### Step 3 - run the tidyverse image interactively and link it to your computer's disk
# Note: The absolute path on your laptop should be where you cloned data_analysis_pipeline_eg
# 
# - do this by typing (use the appropriate paths for your computer!):
# 
# ```
# docker run --rm -p 8787:8787 -e PASSWORD="test" -v <absolute path on laptop>:/home/rstudio/data_analysis_pipeline_eg rocker/tidyverse
# ```
# 
# Now, to get to the RStudio GUI/interface, you need to open a web browser and go to this URL: http://localhost:8787
# 
# If it worked, then you should be at an RStudio Sign In page. To sign in, use the following credentials:
# 
# **username:** rstudio
# 
# **password:** test
# 
# Now you should be able to use RStudio inside the browser! Try out some R code to test that it works!
# 
# Sample R code to try:
# 
# ```
# library(ggplot2)
# my_scatplot <- ggplot(mtcars,aes(x=wt,y=mpg)) + geom_point() + theme_bw()
# my_scatplot + xlab('Weight (x 1000lbs)') + ylab('Miles per Gallon') + geom_smooth()
# ```

# #### Step 4 - use the tidyverse image to make an `.Rmd`
# 
# Try making a `.Rmd` and saving it in the `data_analysis_pipeline_eg` `src` directory.
# 
# 
# #### Step 5 - exit from the tidyverse docker image
# 
# To exit from this tidyverse Docker image, type `Control-C` at the command line/terminal/GitBash where you launched/ran the image from. Alternatively you can close the command line/terminal/GitBash instead. Closing the browser tab/window does not kill/close the instance of the image.
# 
# *note - there are other ways to close/kill Docker images. We will learn these shortly.*
# 
# If you now look in the `src` directory of the data analysis project you should see the `.Rmd` you created there.

# ### How to re-attach to an exited container
# 
# There are several ways to do this and it really depends on what precisely you are trying to accomplish. In general, you will need the container ID and/or name:
# 
# ```
# docker ps -a
# ```
# 
# Then, run the following `attach` command to re-attach the container:
# 
# ```
# docker container attach <container id OR name>
# ```

# #### Debrief - what did we just do? 
# 
# Let's now dig deeper into the commands and tools we just used to become more familiar with Docker! Let's fill in this table to explain what each part of our Docker commands did:
# 
# | command/flag `docker` | What it does          | 
# |--------------|-----------------------|
# | `-p`         | Connects Container to a port on your machine so that you can run a program through a web browser |
# | `-e`         | Set simple environment variables in the container you’re running. E.g., PASSWORD="test" |
# | `-v path1:path2`  | maps path1 locally to path2 in the Docker container |

# ## Using Docker to run Jupyter
# 
# Steps:
# 
# 1. Download docker image with Dash + other dependencies: 
#     - `docker pull jupyter/datascience-notebook`
# 2. Create a new container:
#     - `docker run --rm -it -p 8888:8888 -v /$(pwd):/home/jupyter jupyter/datascience-notebook`
# 3. Copy the url printed out that looks like the one shown below to your browser: 
# 
# ```http://127.0.0.1:8888/?token=6e4af655f82dd55d80fd0328d3e61ab32320febfc0b4153c```
#   
# That's it!
# 
# When you are done, use Ctrl+C to stop the container from the terminal you launched it from.

# ## Dockerfiles
# 
# - A `Dockerfile` is a plain text file that contains commands primarily about what software to install in the Docker image. This is the more trusted and transparent way to build Docker images.

# - Once we have created a `Dockerfile` we can build it into a Docker image.

# - Docker images are built in layers, and as such, `Dockerfiles` always start by specifiying a base Docker image that the new image is to be built on top off

# - Docker containers are all Linux containers and thus use Linux commands to install software, however there are different flavours of Linux (e.g., Ubuntu, Debian, CentOs, RedHat, etc) and thus you need to use the right Linux install commands to match your flavour of container. For this course we will focus on Ubuntu- or Debian-based images and thus use `apt-get` as our installation program.

# ## Workflow for building a Dockerfile

# 1. Choose a base image to build off (from https://hub.docker.com/)

# 2. Create a `Dockerfile` named `Dockerfile` and save it in an appropritate project repo. Open that file and type `FROM <BASE_IMAGE> on the first line`.

# 3. In a terminal, type `docker run --rm -it <IMAGE_NAME>` and interactively try the install commands you think will work. Edit and try again until the install command works.

# 4. Write working install commands in the `Dockerfile`, preceeding them with `RUN` and save the Dockerfile.

# 5. After adding every 2-3 commands to your `Dockerfile`, try building the Docker image via `docker build --tag <TEMP_IMAGE_NAME> <PATH_TO_DOCKERFILE_DIRECTORY>`

# 6. Once the entire Dockerfile works from beginning to end on your laptop, then you can finally move to building remotely (e.g., creating a [trusted build on GitHub Actions]).

# ## Demo workflow for creating a Dockfile locally
# 
# We will demo this workflow together to build a Docker image locally on our machines that has R and the `cowsay` R package installed.
# 
# Let's start with the `debian:stable` image, so the first line of our `Dockerfile` should be as such:
# 
# ```
# FROM debian:stable
# ```
# 
# Now let's run the `debian:stable` image so we can work on our install commands to find some that work!
# 
# ```
# $ docker run --rm -it debian:stable
# ```
# 
# Now that we are in a container instance of the `debian:stable` Docker image, we can start playing around with installing things. To install things in the Debian flavour of Linux we use the command `apt-get`. We will do some demo's in class today, but a more comprehensive tutorial can be found [here](https://www.digitalocean.com/community/tutorials/how-to-manage-packages-in-ubuntu-and-debian-with-apt-get-apt-cache).

# To install R on Debian, we can figure out how to do this by following the CRAN documentation available [here](https://cran.r-project.org/bin/linux/debian/).
# 
# First they recommend updating the list of available software package we can install with `apt-get` to us via the `apt-get update` command:
# 
# ```
# root@5d0f4d21a1f9:/# apt-get update
# ```
# 
# Next, they suggest the following commands to install R:
# 
# ```
# root@5d0f4d21a1f9:/# apt-get install r-base r-base-dev
# ```
# 
# OK, great! That seemed to have worked! Let's test it by trying out R! 
# 
# ```
# root@5d0f4d21a1f9:/# R
# 
# R version 3.5.2 (2018-12-20) -- "Eggshell Igloo"
# Copyright (C) 2018 The R Foundation for Statistical Computing
# Platform: x86_64-pc-linux-gnu (64-bit)
# 
# R is free software and comes with ABSOLUTELY NO WARRANTY.
# You are welcome to redistribute it under certain conditions.
# Type 'license()' or 'licence()' for distribution details.
# 
# R is a collaborative project with many contributors.
# Type 'contributors()' for more information and
# 'citation()' on how to cite R or R packages in publications.
# 
# Type 'demo()' for some demos, 'help()' for on-line help, or
# 'help.start()' for an HTML browser interface to help.
# Type 'q()' to quit R.
# 
# > 
# 
# ```
# 
# Awesome! This seemed to have worked! Let's exit R (via `q()`) and the Docker container (via `exit`). Then we can add these commands to the Dockerfile, proceeding them with `RUN` and try to build our image to ensure this works.
# 
# Our `Dockerfile` so far:
# ```
# FROM debian:stable
# 
# RUN apt-get update
# 
# RUN apt-get install r-base r-base-dev -y 
# ```

# ```
# $ docker build --tag testr1 src
# ```
# 
# Wait! That didn't seem to work! Let's focus on the last two lines of the error message:
# 
# ```
# Do you want to continue? [Y/n] Abort.
# The command '/bin/sh -c apt-get install r-base r-base-dev' returned a non-zero code: 1
# ```
# 
# Ohhhh, right! As we were interactively installing this, we were prompted to press "Y" on our keyboard to continue the installation. We need to include this in our Dockerfile so that we don't get this error. To do this we append the `-y` flag to the end of the line contianing `RUN apt-get install r-base r-base-dev`. Let's try building again!
# 
# Great! Success! Now we can play with installing R packages! 
# 
# Let's start now with the test image we have built from our `Dockerfile`:
# 
# ```
# $ docker run -it --rm testr1
# ```
# 
# Now while we are in the container interactively, we can try to install the R package via:
# 
# ```
# root@51f56d653892:/# Rscript -e "install.packages('cowsay')"
# ```
# 
# And it looks like it worked! Let's confirm by trying to call a function from the `cowsay` package in R:
# 
# ```
# root@51f56d653892:/# R
# 
# > cowsay::say("Smart for using Docker are you", "yoda")
# ```
# 
# 
# 
# Great, let's exit the container, and add this command to our `Dockerfile` and try to build it again!
# 
# ```
# root@51f56d653892:/# exit
# ```
# 
# Our `Dockerfile` now:
# ```
# FROM debian:stable
# 
# RUN apt-get update
# 
# RUN apt-get install r-base r-base-dev -y 
# 
# RUN Rscript -e "install.packages('cowsay')"
# ```
# 
# Build the `Dockerfile` into an image:
# 
# ```
# $ docker build --tag testr1 src
# 
# $ docker run -it --rm testr1
# ```
# 
# Looks like a success, let's be sure we can use the `cowsay` package:
# 
# ```
# root@861487da5d00:/# R
# 
# > cowsay::say("why did the chicken cross the road", "chicken")
# 
# ```
# 
# Hurray! We did it! Now we can automate this build on Docker Hub and share this Docker image with the world!
# 
# <img src="https://media.giphy.com/media/ZcKASxMYMKA9SQnhIl/giphy-downsized.gif">
# Source: https://giphy.com/gifs/memecandy-ZcKASxMYMKA9SQnhIl

# ## Dockerfile command summary
# 
# #### Most common ones you will use
# 
# | Command | Description |
# |---------|-------------|
# | FROM    | States which base image the new Docker image should be built on top of |
# | RUN     | Specifies that a command should be run in a shell |
# 
# #### Others you may see and have to encounter
# 
# | Command | Description |
# |---------|-------------|
# | ENV | Sets environment variables |
# | EXPOSE | Specifies the port the container should listen to at runtime |
# | COPY or ADD | adds files (or URL's in the case of ADD) to a container's filesystem |
# | CMD | Specifies a command to run (this provides the default for executing a container) |
# 
# And more here in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

# ## Choosing a base image for your Dockerfile
# 
# <img src="https://themuslimtimesdotinfodotcom.files.wordpress.com/2018/10/newton-quotes-2.jpg?w=1334" width=700>
# 
# Source: https://themuslimtimes.info/2018/10/25/if-i-have-seen-further-it-is-by-standing-on-the-shoulders-of-giants/

# ## Good base images to work from for R or Python projects!
# 
# | Image | Software installed | 
# |-------|--------------------|
# | [rocker/tidyverse](https://hub.docker.com/r/rocker/tidyverse/) | R, R packages (including the tidyverse), RStudio, make |
# | [continuumio/anaconda3](https://hub.docker.com/r/continuumio/anaconda3/) | Python 3.7.4, Ananconda base package distribution, Jupyter notebook |
# | [jupyter/scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook) | Includes popular packages from the scientific Python ecosystem. |
# 
# For mixed language projects, I would recommend using the `rocker/tidyverse` image as the base and then installing Anaconda or miniconda as I have done here: https://github.com/UBC-DSCI/introduction-to-datascience/blob/b0f86fc4d6172cd043a0eb831b5d5a8743f29c81/Dockerfile#L19
# 
# This is also a nice tour de Docker images from the Jupyter core team: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#selecting-an-image

# ## Dockerfile FAQ:

# ### Where does the Dockerfile live?
# 
# The Dockerfile should live in the root directory of your project.

# ### How do I make a Docker image from a Dockerfile?
# 
# There are 2 ways to do this! I use the first when developing my Dockerfile (to test quickly that it works), and then the second I use when I think I am "done" and want to have it archived on [Docker Hub](https://hub.docker.com/). 
# 
# 1. Build a Docker image locally on your laptop
# 
# 2. Build a Docker image using trusted [Automated builds](https://docs.docker.com/docker-cloud/builds/automated-build/) on GitHub Actions

# ### How do I build a Docker image locally on my laptop  
#  
# From the directory that contains your Dockerfile (usually your project root):
# 
# ```
# docker build --tag IMAGE_NAME:VERSION .
# ```
#     
# *note: `--tag` let's you name and version the Docker image. You can call this anything you want. The version number/name comes after the colon*
#     
# After I build, I think try to `docker run ...` to test the image locally. If I don't like it, or it doesn't work, I delete the image with `docker rmi {IMAGE_NAME}`, edit my Dockerfile and try to build and run it again.

# ### How do I know what commands to use to install things on Linux?
# 
# 1. Look at the MDS Linux install instructions: [https://ubc-mds.github.io/resources_pages/install_ds_stack_ubuntu/](https://ubc-mds.github.io/resources_pages/install_ds_stack_ubuntu/)
# 
# 2. Look at other Dockerfiles

# ## What's next?
# 
# - best practices for package and container versioning
# - running scripts (including Makefiles) non-interactively via the command line
# - reproducibility & data analysis project wrap-up

#!/usr/bin/env python
# coding: utf-8

# # Lecture 8 - Reproducibility wrap-up

# ## Learning Objectives
# 
# By the end of the lecture, students should be able to:
# 
# - Build a Docker image from a Dockerfile using GitHub Actions
# - Run a Docker container non-interactively
# - Version Docker images and report software and package versions
# - Articulate why reproducibility is important for data analysis
# - Choose the appropriate level or reproducibility workflows/tooling based on project complexity and desired shareability

# ## Build a Docker image from a Dockerfile on GitHub Actions
# 
# Building a Docker image from a Dockerfile using an automated tool (e.g., DockerHub or GitHub Actions) lets others trust your image as they can clearly see which Dockerfile was used to build which image.  

# We will do this in this course by using GitHub Actions (a continuous integration tool) because is provides a great deal of nuanced control over when to trigger the automated builds of the Docker image, and how to tag them.

# An example GitHub repository that uses GitHub Actions to build a Docker image from a Dockerfile and publish it on DockerHub is available here: [https://github.com/ttimbers/gha_docker_build](https://github.com/ttimbers/gha_docker_build)
# 
# We will work through a demonstration of this now starting here: [https://github.com/ttimbers/dockerfile-practice](https://github.com/ttimbers/dockerfile-practice)

# ## Running a Docker container non-interactively
# 
# So far we have been running our containers interactively, but sometimes we want to automate further and run things non interactively. We do this be dropping the `-it` flag from our `docker run` command as well as calling a command or a script after the docker image is specified.
# 
# The general form for for running things non-interactively is this:
# 
# ```
# docker run --rm -v PATH_ON_YOUR_COMPUTER:VOLUME_ON_CONTAINER DOCKER_IMAGE PROGRAM_TO_RUN PROGRAM_ARGUMENTS
# ```
# 
# For example, let's use the container we built last class to non-interactively run a `cowsay::say` function call to print some asci art with a cute message! 
# 
# ```
# $ docker run --rm ttimbers/dockerfile-practice:v0.1.0 Rscript -e "library(cowsay); say('Snow again this week?', 'snowman')"
# ```
# 
# 

# For example, let's use the container we built last class to non-interactively run a `cowsay::say` function call to print some asci art with a cute message! 
# 
# ```
# $ docker run --rm ttimbers/dockerfile-practice:v1.0 Rscript -e "library(cowsay); say('Snow again this week?', 'snowman')"
# ```

# And if succesfful, we should get:
# 
# ```
# ----- 
# Snow again this week? 
#  ------ 
#     \   
#      \
#      _[_]_
#       (")
#   >--( : )--<
#     (__:__) [nosig]
# ```  
# 
# *note - I will use the version of the image that exists on Docker Hub, but you are free to use the one we built last class, they should be the same.*

# Now that was a silly example, but this can be made powerful so that we can run an analysis pipeline, such as a Makefile non-interactively using Docker! Here's a demo we can try: https://github.com/ttimbers/data_analysis_pipeline_eg/tree/v4.0
# 
# ### Exercise 1: 
# 
# Download https://github.com/ttimbers/data_analysis_pipeline_eg/archive/v4.0.zip, unzip it and navigate to the root of the project directory, try to run the analysis via `make all`.
# 
# ### Exercise 2: 
# 
# Now try to run the analysis using Docker via:
# 
# ```
# docker run --rm -v /$(pwd):/home/rstudio/data_analysis_eg ttimbers/data_analysis_pipeline_eg make -C /home/rstudio/data_analysis_eg all
# ```
# 
# *note - windows users must use Git Bash, set Docker to use Linux containers, and have shared their drives with Docker (see docs [here](https://token2shell.com/howto/docker/sharing-windows-folders-with-containers/)) for this to work*
# 
# 
# If that was too easy (i.e., both worked), try running this analysis with and without Docker: https://github.com/ttimbers/breast_cancer_predictor

# Now let's try a more complex project (the breast cancer predictor):
# 
# ### Exercise 3: 
# 
# Download https://github.com/ttimbers/breast_cancer_predictor/archive/v4.0.zip, unzip it and navigate to the root of the project directory, try to run the analysis via `make clean` (to reset the project state) and `make all` (to run the analysis).
# 
# ### Exercise 4: 
# 
# Now try to run reset the project state using Docker via:
# 
# ```
# docker run --rm -v /$(pwd):/home/rstudio/breast_cancer_predictor ttimbers/bc_predictor:v4.0 make -C /home/rstudio/breast_cancer_predictor clean
# ```
# 
# Now try to run the analysis using Docker via:
# 
# ```
# docker run --rm -v /$(pwd):/home/rstudio/breast_cancer_predictor ttimbers/bc_predictor:v4.0 make -C /home/rstudio/breast_cancer_predictor all
# ```
# 
# *note - windows users must use Git Bash, set Docker to use Linux containers, and have shared their drives with Docker (see docs [here](https://token2shell.com/howto/docker/sharing-windows-folders-with-containers/)) for this to work*

# What we just did was run our Makefile non-interactively. We had to change a few things in our Make command to make this work (no pun intended). 
# 
# First, we run our Makefile from a different directory. So to point at a Makefile using a path we use `make -C PATH_TO_MAKEFILE`. Following that we added our Makefile target, in this case `all`. 
# 
# If we wanted to reset our analysis to a clean state where no analysis had been done, we could just change the target from `all` to `clean` and everything else would stay the same:
# 
# ```
# docker run --rm -v /$(pwd):/home/rstudio/data_analysis_eg ttimbers/data_analysis_pipeline_eg make -C /home/rstudio/data_analysis_eg make
# ```
# 
# 

# ## Version Docker images and report software and package versions
# 
# It is easier to create a Docker image from a Dockerfile and tag it (or use it's digest) than to control the version of each thing that goes into your Docker image.
# 
# - tags are human readable, however they can be associated with different builds of the image (potentially using different Dockerfiles...)
# - digests are not human readable, but specify a specific build of an image
# 
# Example of how to pull using a tag: 
# ```
# docker pull ttimbers/dockerfile-practice:v1.0
# ```
# 
# Example of how to pull using a digest:
# ```
# docker pull ttimbers/dockerfile-practice@sha256:cc512c9599054f24f4020e2c7e3337b9e71fd6251dfde5bcd716dc9b1f8c3a73
# ```
# 
# Tags are specified when you build on Docker Hub on the Builds tab under the Configure automated builds options. Digests are assigned to a build. You can see the digests on the Tags tab, by clicking on the "Digest" link for a specific tag of the image.

# ### How to get the versions of your software in your container
# 
# Easiest is to enter the container interactively and poke around using the following commands:
# 
# - `python --version` and `R --version` to find out the versions of Python and R, respectively
# - `pip freeze` in the bash shell to find out Python package versions
# - Enter R and load the libraries used in your scripts, then use `sessionInfo()` to print the package versions

# ### But I want to control the versions!
# 
# ### How to in R:
# 
# #### The Rocker team's strategy
# 
# This is not an easy thing, but the Rocker team has made a concerted effort to do this. Below is their strategy:
# 
# > Using the R version tag will naturally lock the R version, and also lock the install date of any R packages on the image. For example, rocker/tidyverse:3.3.1 Docker image will always rebuild with R 3.3.1 and R packages installed from the 2016-10-31 MRAN snapshot, corresponding to the last day that version of R was the most recent release. Meanwhile rocker/tidyverse:latest will always have both the latest R version and latest versions of the R packages, built nightly.
# 
# See [VERSIONS.md](https://github.com/rocker-org/rocker-versioned/blob/master/VERSIONS.md) for details, but in short they use the line below to lock the R version (or view in r-ver Dockerfile [here](https://github.com/rocker-org/rocker-versioned/blob/c4a9f540d4c66a6277f281be6dcfe55d3cb40ec0/r-ver/3.6.1.Dockerfile#L76) for more context):
# ```  
#     && curl -O https://cran.r-project.org/src/base/R-3/R-${R_VERSION}.tar.gz \
# ```
# 
# And this line to specify the CRAN snapshot from which to grab the R packages (or view in r-ver Dockerfile [here](mhttps://github.com/rocker-org/rocker-versioned/blob/c4a9f540d4c66a6277f281be6dcfe55d3cb40ec0/r-ver/3.6.1.Dockerfile#L121) for more context):
# ```
#     && Rscript -e "install.packages(c('littler', 'docopt'), repo = '$MRAN')" \
# ```
# 
# 

# What is `MRAN`? Everyday Microsoft takes daily snapshots of the CRAN R package repository and archives them! We can choose a day in time and install all our packages from there, ensuring that everytime we build our Docker image we end up with the same version of the R package, no matter which day we build it on.
# 
# So, a simpler example from above, without using an variable (like the Rocker group does is):
# 
# ```
# RUN Rscript -e "install.packages('gapminder', repos = 'https://mran.revolutionanalytics.com/snapshot/2016-10-19')"
# ```
# 
# #### A new thing that might be useful in the future?
# 
# [renv](https://rstudio.github.io/renv/articles/renv.html) - this is new! 🎉

# ### How to in Python:
# 
# Python version:
# 
# - `conda`  to specify an install of specific Python version, either when downloading (see example [here](https://github.com/ContinuumIO/docker-images/blob/8e10242c6d7804a0e991a9d9d758e25b340f4fce/miniconda3/debian/Dockerfile#L10), or after downloading with `conda install python=3.6`).
# - Or you can install a specific version of Python yourself, as they do in the Python official images (see [here](https://github.com/docker-library/python/blob/master/3.7/stretch/slim/Dockerfile) for example), but this is more complicated.
# 
# For Python packages, there are a few tools:
# - conda (via `conda install scipy=0.15.0` for example)
# - pip (via `pip install scipy=0.15.0` for example)

# ### Take home messages:
# 
# - At a minimum, tag your Docker images or reference image digests
# - If you want to version installs inside the container, use base images that version R & Python, and add what you need on top in a versioned manner!

# ## Some tips and tricks:
# 
# 1. `docker run ... -p 8888:8888` hard codes the port! If you already are using the port (i.e., already running Jupyter on your laptop you will get an error... `jupyter notebook list` will list all running instances of Jupyter on your machine. To stop all jupyter notebook processes on your laptop, type: `jupyter notebook stop`.
# 
# 2. How to see all docker images installed on your computer: `docker images`. Want to delete and image? `docker rmi <IMAGE name>` or `docker rmi <IMAGE ID>`.
# 
# 3. How to see any running and stopped but still dangling containers: `docker ps -a`
# 
# 4. How to stop a running container: `docker stop <CONTAINER ID>`. If that doesn't work, you can be more forceful with `docker kill <CONTAINER ID>`. Finally, to remove the stopped container: `docker rm  <CONTAINER ID>` (again, you can be more forceful by adding the `--force` flag).

# ### Docker compose
# 
# Docker compose is a tool that uses a `YAML` file to configure/specify how you want to run one or more Docker containers. To use Docker compose, we create a `docker-compose.yml` file that specifies things such as:
# - the Docker images (and version)
# - the ports
# - volume mapping
# - any environment variables

# Then to run the Docker container using the specifications in the `docker-compose.yml` file, we run:
# 
# ```
# docker-compose run --rm service command
# ```
# 
# - `service` is a name you give to your application configurations in the `docker-compose.yml`
# - `command` is some command or script you would like to run (e.g., `make all`)

# Here is an example `docker-compose.yml`:

# ```
# services:
#   analysis-env:
#     image: ttimbers/bc_predictor:v4.0
#     ports:
#       - "8787:8787"
#     volumes:
#       - .:/home/rstudio/introduction-to-datascience
#     environment:
#       PASSWORD: password
# ```

# And to run the container and the analysis we would type:

# ```
# docker-compose run --rm analysis-env make -C /home/rstudio/breast_cancer_predictor all
# ```
# 
# This means we do not have to type out the:
# - ports
# - volume mapping
# - environment variables
# - and potentially more!

# ## How to make a trustworthy analysis:

# 1. It should be reproducible and transparent

# 2. It should be correct

# 3. It should be fair, equitable and honest

# ## Discussion
# 
# - Why is reproducibility is important for data analysis?
# 
# - How do I choose the level of investment of reproducibility for a given project?

# ## Course learning objectives:
# 
# 
# By the end of the course, students are expected to be able to:
# 
# - Map a data analysis question to appropriate analysis
# - Write R, Python and shell scripts for non-interactive data analysis.
# - Run literate coding documents (Jupyter notebooks and R Markdown - documents) non-interactively.
# - Use a Git/GitHub forking-pull request collaboration approach to collaboratively work on a data analysis project.
# - Automate data science workflows (using e.g., Make).
# - Manage project software and environment dependencies (using e.g., Docker)
# 

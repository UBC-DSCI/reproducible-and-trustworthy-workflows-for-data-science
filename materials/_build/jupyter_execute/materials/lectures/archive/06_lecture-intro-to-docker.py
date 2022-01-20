#!/usr/bin/env python
# coding: utf-8

# # Lecture 6 - Introduction to Docker

# ## Learning Objectives
# 
# By the end of the lecture, students should be able to:
# 
# - Explain the difference between running software/scripts in a virtual machine vs. a container
# - Use a Docker image to run some software

# ## Documenting and loading dependencies
# 
# You've made some beautiful data analysis pipeline/project using make, R, and/or Python. It runs on your machine, but how easily can you, or someone else, get it working on theirs? The answer usually is, it depends...
# 
# What does it depend on?
# 
# 
# 
# 

# - Does your README and your scripts make it blatantly obvious what programs and packages need to run your data analysis pipeline/project? 
#     

# - Do you also document the version numbers of the programs and packages you used? This can have big consequences when it comes to replicability... (Remember the [change to random number generation](https://blog.revolutionanalytics.com/2019/05/whats-new-in-r-360.html) in R?)

# ## What is Docker?
# 
# "*Docker containers wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries – anything that can be installed on a server. This guarantees that the software will always run the same, regardless of its environment.*"
# 
# *Source: https://www.docker.com/what-docker*

# ## Container versus Virtual Machines
# 
# ![alt tag](img/container_v_vm.png)
# *Source: https://www.docker.com/resources/what-container*
# 
# *Key take home - Docker shares the host's operating system, whereas virtual machines have a completely separate, additional operating system. This can make Docker lighter (smaller in terms of size) and more resource and time-efficient than using a virtual machine.*

# ## Motivating example - a dependency graph for a data analysis project
# 
# We can use the tool [makefile2graph](https://github.com/lindenb/makefile2graph) to make a dependency diagram for our data analysis projects from our `Makefile`'s. 
# 
# **Problem** - [makefile2graph](https://github.com/lindenb/makefile2graph) is a pain to install (especially on Windows...)
# 
# **Solution** - let's use the docker container I built previously to run this!
# 

# #### Let's do it!
# 
# #### Step 0 - Install Docker (do this once)
# - Follow the [instructions in the MDS installation guide](https://ubc-mds.github.io/resources_pages/installation_instructions/) to do this.

# #### Step 1 - launch the Docker app (for OSX & Windows only)
# - Use launchpad/Finder/Start menu/etc to find and launch Docker

# #### Step 2 - get makefile2graph image from Dockerhub
# - open command line (terminal/GitBash)
# - type: `docker pull ttimbers/makefile2graph`
# - verify that it successfully pulled by typing: `docker images`, you should see something like:
# ```
# REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
# ttimbers/makefile2graph   latest              823dcba8f792        13 months ago       469MB
# ```

# #### Wait! Where did this come from? [Docker Hub](https://hub.docker.com/)!
# 
# 
# - [Docker Hub](https://hub.docker.com/) is like GitHub but just for Docker images. 
# - So what you downloaded was a Docker image that lives in this repository: https://hub.docker.com/r/ttimbers/makefile2graph/

# #### Step 3 - launch a container from the image and poke around!
# 
# - type: `docker run -it ttimbers/makefile2graph`
# - If it worked, then your command line prompt should now look something like this:
# 
# ```
# root@ad0560c5b81a:/# 
# ```
# - use `ls`, `cd`, `pwd` and explore the container
# - type `exit` to leave when you are done (your prompt will look normal again)!

# #### Step 4 - clean up your container!
# 
# - After you close a container it still "hangs" around... 
# - View any existing containers using `docker ps -a`
# - Kill the container by typing `docker rm <container_id>`
# - Prove to yourself that the container is no longer "hanging around" via `docker ps -a`, but that you still have the image installed (via `docker images`)

# #### That's a lot of work...
# 
# - We can tell Docker to delete the container upon exit using the `--rm` flag in the run command.
# - Type the command below to run the container again, exit it and prove to yourself that the container was deleted (but not the image!):
# 
# ```
# docker run -it --rm ttimbers/makefile2graph
# ```

# #### Image vs container?
# 
# Analogy: The program Chrome is like a Docker image, whereas a Chrome window is like a Docker container.
# 
# <img src="img/instance_analogy.png" width="600" align="left"/>

# Here is another schematic from a [blog post](https://blog.octo.com/en/docker-registry-first-steps/) by Arnaud Mazin:
# 
# ![Containers_vs_images](img/docker-stages.png)
# *Source: [OctoTalks](https://blog.octo.com/en/docker-registry-first-steps/)*

# #### Step 5 - connect the container to your hard drive
# 
# To run the `makefile2graph` program on a file that exists on our laptop we will need to mount at least part of our filesystem as a volume on the Docker container. We do that with `-v <absolute path on laptop>:<relative path from container home directory>`.
# 
# To mount `data_analysis_pipeline_eg-3-3.0`:
# 
# 1. Download [this version](https://github.com/ttimbers/data_analysis_pipeline_eg/archive/v3.0.zip) of the `data_analysis_pipeline_eg` repository.
# 
# 2. Unzip it and navigate to the root of the project directory.
# 
# 3. Get your current working directory (e.g., using `pwd`).
# 
# 4. Type the following (filling in the absolute path for your laptop):
# 
# ```
# docker run -it --rm -v <local_version>:<container_folder> ttimbers/makefile2graph
# ```
# 
# 5. Use `ls`, `cd`, `pwd` and explore the container now, can you see the files on your laptop? Specifically the Makefile?
# 
# ### Windows notes for mounting volumes:
# - Windows machines need to explicitly share drives with Docker
# - On Windows, the laptop path depends what shell you are using, here are some details:
#     - If you are going to run it in Git Bash, then the command should be: `docker run --rm -it -v /$(pwd):<PATH_ON_CONTAINER> <IMAGE_NAME>` to share the current directory.
#     - If you are going to run it in Power Shell, then the command should be: `docker run --rm -it -v <ABSOLUTE_PATH_TO_CONTAINER>:<PATH_ON_CONTAINER> <IMAGE_NAME>` (`pwd` and variants do not seem to work). And the path must be formatted like: `C:\Users\tiffany.timbers\Documents\project\:/home/project`

# #### Step 6 - use the makefile2graph program to create the dependency graph (this will be required for milestone 4
# 
# - Inside the container, navigate into `data_analysis_pipeline_eg`
# - Type the following to create a `.png` that illustrates the dependencies of your `Makefile`:
# 
# ```
# makefile2graph > Makefile.dot
# dot -Tpng Makefile.dot -o Makefile.png
# ```
# 
# - Exit from the container (via `exit`)
# 
# - Use your laptop (not the container) to open `Makefile.png` to view the dependency diagram
# 
# *note - the above commands for step 6 are not Docker commands, they are commands for the `makefile2graph` program. Read the docs for that Software here: https://github.com/lindenb/makefile2graph*
# 

# #### Debrief - what did we just do? 
# 
# Let's now dig deeper into the commands and tools we just used to become more familiar with Docker! Let's fill in this table to explain what each part of our Docker commands did:
# 
# | command/flag | What it does          | 
# |--------------|-----------------------|
# | `pull`       | Downloads a Docker image from Docker Hub |
# | `images`     | Tells you what images are installed on your machine                     |
# | `run`        | Launches a Docker container from an image                      |
# | `-it`        | Tells Docker to run the container interactively                      |
# | `--rm`       | Makes a container ephemeral (deletes it upon exit)                      |
# | `-v`         | Mounts a volume of your laptop to the Docker container                     |
# | `exit`       | Exits a Docker container                      |

# ## Where to next?
# 
# - Installing things in linux (most containers used in Data Science are linux based)
# 
# - Creating your own Docker image!

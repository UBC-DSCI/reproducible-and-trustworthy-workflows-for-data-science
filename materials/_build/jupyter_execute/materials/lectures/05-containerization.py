#!/usr/bin/env python
# coding: utf-8

# # Managing dependencies using containerization

# ## Topic learning objectives
# 
# By the end of this topic, students should be able to:
# 
# 1. Explain what containers are, and why they can be useful for reproducible data
# analyses
# 2. Discuss the advantages and limitations of containerization (e.g., Docker) in the
# context of reproducible data analyses
# 3. Compare and contrast the difference between running software/scripts in a virtual
# environment, a virtual machine and a container
# 4. Evaluate, choose and justify an appropriate environment management solution based
# on the data analysis project’s complexity, expected usage and longevity.
# 5. Use a containerization software (e.g., Docker) to run the software needed for your
# analysis
# 6. Write a container file (e.g., Dockerfile) that can be used to reproducibly build a
# container image that would contain the needed software and environment
# dependencies of your Data Science project
# 7. Use manual and automated tools (e.g., Docker, GitHub Actions) to build and share
# container images
# 8. List good container base images for Data Science projects

# ## Introduction to containerization
# 
# ### Documenting and loading dependencies
# 
# You've made some beautiful data analysis pipeline/project using make, R, and/or Python. It runs on your machine, but how easily can you, or someone else, get it working on theirs? The answer usually is, it depends...
# 
# What does it depend on?
# 
# 
# 
# 

# 1. Does your `README` and your scripts make it blatantly obvious what programming languages and packages need to run your data analysis pipeline/project? 
#     

# 2. Do you also document the version numbers of the programming languages and packages you used? This can have big consequences when it comes to reproducibility... (*e.g.*,the [change to random number generation](https://blog.revolutionanalytics.com/2019/05/whats-new-in-r-360.html) in R in 2019?)
# 
# 3. Did you document what other software (beyond the the programming languages and packages used) and operating system dependencies are needed to run your data analysis pipeline/project?
# 
# *Virtual environments can be tremendously helpful with #1 & #2, however, they may or may not be helpful to manage #3...* __*Enter containerization as a possible solution!*__

# ### What is a container?
# 
# Containers are another way to generate (and share!) isolated computational environments. They differ from virtual environments (which we discussed previously) in that they are even more isolated from the computers operating system, as well as they can be used share many other types of software, applications and operating system dependencies. 
# 
# Before we can fully define containers, however, we need to define **virtualization**. Virtualization is a process that allows us to divide the the elements of a single computer into several virtual elements. These elements can include computer hardware platforms, storage devices, and computer network resources, and even operating system user spaces (e.g., graphical tools, utilities, and programming languages). 
# 
# Containers virtualize operating system user spaces so that they can isolate the processes they contain, as well as control the processes’ access to computer resources (e.g., CPUs, memory and desk space). What this means in practice, is that an operating system user space can be carved up into multiple containers running the same, or different processes, in isolation. Below we show the schematic of a container whose virtual user space contains the:
# - R programming language, the Bioconductor package manager, and two Bioconductor packages
# - Galaxy workflow software and two toolboxes that can be used with it
# - Python programming language, iPython interpreter and Jupyter notebook package
# 
# <img src="img/13742_2016_article_135_f7.jpeg" width=250>
# 
# **Schematic of a container for genomics research.** Source: <https://doi.org/10.1186/s13742-016-0135-4>
# 
# 
# #### Exercise - running a simple container
# 
# To further illustrate what a container looks like, and feels like, we can use Docker (containerization software) to run one and explore. First we will run an linux (debian-flavoured) container that has R installed. To run this type:
# 
# ```
# docker run --rm -it rocker/r-base:3.6.3
# ```
# 
# When you successfully launch the container, R should have started. Check the version of R - is it the same as your computer's version of R? Use `getwd()` and `list.files()` to explore the containers filesystem from R. Does this look like your computer's filesystem or something else?
# 
# #### Exercise - running a container with a web app
# 
# Next, try to use Docker to run a container that contains the RStudio server web-application installed:
# 
# ```
# docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.1.2
# ```
# 
# Then visit a web browser on your computer and type: <http://localhost:8787>
# 
# If it worked, then you should be at an RStudio Sign In page. To sign in, use the following credentials:
# 
# - **username:** rstudio
# - **password:** apassword
# 
# The RStudio server web app being run by the container should look something like this: 
# 
# <img src="img/rstudio-container-web-app.png" width=600>
# 

# ## Contrasting containers with virtual machines
# 
# Virtual machines are another technology that can be used to generate (and share) isolated computational environments. Virtual machines emulate the functionality an entire computer on a another physical computer. With virtual machine the virtualization occurs at the layer of software that sits between the computer's hardware and the operating system(s). This software is called a hypervisor. For example, on a Mac laptop, you could install a program called [Oracle Virtual Box](https://www.virtualbox.org/) to run a virtual machine whose operating system was Windows 10, as the screen shot below shows:
# 
# <img src="https://www.virtualbox.org/raw-attachment/wiki/Screenshots/Windows_8.1_on_OSX.png">
# 
# 
# **A screenshot of a Mac OS computer running a Windows virtual machine.** Source: <https://www.virtualbox.org/wiki/Screenshots>
# 
# Below, we share an illustration that compares where virtualization happens in containers compared to virtual machines. This difference, leads to containers being more light-weight and portable compared to virtual machines, and also less isolated.
# 
# <img src="img/container_v_vm.png" width=600>
# 
# *Source: https://www.docker.com/resources/what-container*
# 
# 
# **Key take home:** - Containerization software shares the host's operating system, whereas virtual machines have a completely separate, additional operating system. This can make containers lighter (smaller in terms of size) and more resource and time-efficient than using a virtual machine.*

# ## Contrasting common computational environment virtualization strategies
# 
# | Feature | Virtual environment | Container | Virtual machine |
# |---------|---------------------|-----------|-----------------|
# | Virtualization level | Application | Operating system user-space | Hardware |
# | Isolation | Programming languages, packages | Programming languages, packages, **other software, operating system dependencies, filesystems, networks** | Programming languages, packages, other software, operating system dependencies, filesystems, networks, **operating systems** |
# | Size | Extremely light-weight | light-weight | heavy-weight |
# 

# ## Virtualization strategy advantages and disadvantages for reproducibility
# 
# Let's collaboratively generate a list of advantages and disadvantages of each virtualization strategy in the context of reproducibility:
# 
# 
# ### Virtual environment
# 
# #### Advantages
# - Extremely small size
# - Porous (less isolated) - makes it easy to pair the virtualized computational environment with files on your computer
# - Specify these with a single text file
# 
# #### Disadvantages
# - Not always possible to capture and share operating system dependencies, and other software your analysis depends upon
# - Computational environment is not fully isolated, and so silent missed dependencies
# 

# ### Containers
# 
# #### Advantages
# - Somewhat light-weight in size (manageable for easy sharing - there are tools and software to facilitate this)
# - Possible to capture and share operating system dependencies, and other software your analysis depends upon
# - Computational environment is fully isolated, and errors will occur if dependencies are missing
# - Specify these with a single text file
# - Can share volumes and ports (advantage compared to virtual machines)
# 
# #### Disadvantages
# - Possible security issues - running software on your computer that you may allow to be less isolated (i.e., mount volumes, expose ports)
# - Takes some effort to share volumes and ports (disadvantage compared to virtual environments)
# 

# ### Virtual machine
# 
# #### Advantages
# - High security, because these are much more isolated (filesystem, ports, etc)
# - Can share an entirely different operating system (might not so useful in the context of reproducibility however...)
# 
# #### Disadvantages
# - Very big in size, which can make it prohibitive to share them
# - Takes great effort to share volumes and ports - which makes it hard to give access to data on your computer
# 

# ## Container useage workflow
# 
# A schematic of Container useage workflow from a [blog post](https://blog.octo.com/en/docker-registry-first-steps/) by Arnaud Mazin:
# 
# <img src="img/docker-stages.png" width=600>
# 
# *Source: [OctoTalks](https://blog.octo.com/en/docker-registry-first-steps/)*

# ## Image vs container?
# 
# Analogy: The program Chrome is like a Docker image, whereas a Chrome window is like a Docker container.
# 
# <img src="img/instance_analogy.png" width="600">

# You can list the container **images** on your computer that you pulled using Docker via: `docker images`. You should see a list like this when you do this:
# 
# ```
# REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE
# rocker/rstudio             4.1.2     ff47c56c9c0b   8 days ago      1.89GB
# continuumio/miniconda3     latest    4d529c886124   4 weeks ago     399MB
# jupyter/base-notebook      latest    8610b7acbd67   5 weeks ago     683MB
# jupyter/minimal-notebook   latest    4801dcfde35b   2 months ago    1.38GB
# rocker/r-base              latest    91af7f4c94cd   3 months ago    814MB
# ubuntu                     focal     ba6acccedd29   3 months ago    72.8MB
# rocker/r-base              3.6.3     ddcf1852524d   23 months ago   679MB
# ```
# 
# You can list the states of containers that have been started by Docker on your computer (and not yet removed) via: `docker ps -a`:
# 
# ```
# CONTAINER ID   IMAGE                  COMMAND   CREATED          STATUS          PORTS                                       NAMES
# 9160100c7d4b   rocker/r-base:3.6.3    "R"       5 seconds ago    Up 4 seconds                                                friendly_merkle
# 0d0871c90313   rocker/rstudio:4.1.2   "/init"   33 minutes ago   Up 33 minutes   0.0.0.0:8787->8787/tcp, :::8787->8787/tcp   exciting_kepler
# ```

# ## What is a container registry
# 
# A container registry Is a remote repository used to share container images. This is similar to remote version control repositories for sharing code. Instead of code however, it is container images that are pushed and pulled to/from there. There are many container registries that can be used, but for this course we will focus on the widely-used DockerHub container registry: <https://hub.docker.com/>
# 
# #### Demonstration
# 
# Let's visit the repositories for the two container images that we used in the exercise earlier in class:
# 
# - [rocker/r-base](https://hub.docker.com/r/rocker/r-base)
# - [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio)
# 
# Question: how did we get the images for the exercise earlier in class? We were just prompted to type `docker run...`
# 
# Answer: `docker run ...` will first look for images you have locally, and run those if they exist. If they do not exist, it then attempts to pull the image from DockerHub.

# ## How do we specify a container image?
# 
# Container images are specified from plain text files! In the case of the Docker containerization software, we call these `Dockerfiles`. We will explain these in more detail later, however for now it is useful to look at one to get a general idea of their structure:
# 
# Example `Dockerfile`:
# 
# ```
# FROM continuumio/miniconda3
# 
# # Install Jupyter, JupterLab, R & the IRkernel
# RUN conda install -y --quiet \
#     jupyter \
#     jupyterlab=3.* \
#     r-base=4.1.* \
#     r-irkernel
# 
# # Install JupyterLab Git Extension
# RUN pip install jupyterlab-git
# 
# # Create working directory for mounting volumes
# RUN mkdir -p /opt/notebooks
# 
# # Make port 8888 available for JupyterLab
# EXPOSE 8888
# 
# # Install Git, the nano-tiny text editor and less (needed for R help)
# RUN apt-get update && \
#     apt-get install --yes \
#     git \
#     nano-tiny \
#     less
# 
# # Copy JupyterLab start-up script into container
# COPY start-notebook.sh /usr/local/bin/
# 
# # Change permission of startup script and execute it
# RUN chmod +x /usr/local/bin/start-notebook.sh
# ENTRYPOINT ["/usr/local/bin/start-notebook.sh"]
# 
# # Switch to staring in directory where volumes will be mounted
# WORKDIR "/opt/notebooks"
# ```
# 
# The commands in all capitals are Docker commands. `Dockerfile`s typically start with a `FROM` command that specifies which base image the new image should be built off. Docker images are built in layers - this helps make them more light-weight. The `FROM` command is usually followed by `RUN` commands that usually install new software, or execute configuration commands. Other commands in this example copy in needed configuration files, expose ports, specify the working directory, and specify programs to execute at start-up.
# 
# #### Demonstration of container images being built from layers
# 
# Let's take a look at the `Dockerfile` for the `jupyter/docker-stacks` `r-notebook` container image:
# - [Dockerfile](https://github.com/jupyter/docker-stacks/blob/master/r-notebook/Dockerfile)
# 
# *Question: What images does it build off?*

# ## Running containers
# 
# Below we demonstrate how to run containers using the [`continuumio/miniconda3` image](https://hub.docker.com/r/continuumio/miniconda3) as an example:

# #### Step 1 - launch the Docker app (for OSX & Windows only)
# - Use launchpad/Finder/Start menu/etc to find and launch Docker
# 
# > Note: Docker might already be running, if so great, but if its not, the commands below will not work. So it is always good to check!

# #### Step 2 - get container image from Dockerhub
# - open the terminal
# - type: `docker pull continuumio/miniconda3`
# - verify that it successfully pulled by typing: `docker images`, you should see something like:
# ```
# REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE
# continuumio/miniconda3     latest    4d529c886124   4 weeks ago     399MB
# ```
# 
# > Note 1: You can skip this step and just got onto `docker run ...` as that command will pull the image if you do not have it locally.
# >
# > Note 2: If you ever need to delete a container image from your computer, you can run `docker rmi <IMAGE_ID>` to do so.

# #### Step 3 - launch a container from the image and poke around!
# 
# - type: `docker run -it continuumio/miniconda3`
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
# - Remove the container by typing `docker rm <container_id>`
# - Prove to yourself that the container is no longer "hanging around" via `docker ps -a`, but that you still have the image installed (via `docker images`)
# 
# > Note: to remove running containers, you will need to first stop them via `docker stop <container_id>`

# #### That's a lot of work...
# 
# - We can tell Docker to delete the container upon exit using the `--rm` flag in the run command.
# - Type the command below to run the container again, exit it and prove to yourself that the container was deleted (but not the image!):
# 
# ```
# docker run -it --rm continuumio/miniconda3
# ```

# ## Mounting volumes to containers
# 
# Often times we want to use the software made available to us in containers on files on our computers. 
# To do this, we need to explicitly tell Docker to mount a volume to the container. 
# We can do this via: `-v <path_to_computer_directory>:<absolute_path_to_container_directory>`
# 
# Often, we want to mount the volume from our current directory (where we are working) and we can do that with a short-form of `/$(pwd)` in place of the path to our computer's directory.
# 
# To mount our current directory to a container from the `continuumio/miniconda3` image we type the following on your laptop:
# 
# ```
# docker run -it --rm -v /$(pwd):/home/my_mounted_volume continuumio/miniconda3
# ```
# 
# Navigate to the directory where you mounted your files via: `cd /home/my_mounted_volume` and type `ls` to ensure you can see them.
# 
# > Note: if you are mounting volumes to a container from a Docker image that runs a web app, be sure to read the documentation to see where you should mount that volume. Usually the web apps are only exposed to certain directories and you will only be able to access the files in the mounted volume if you mount them to the correct place. For example, in the `rocker/rstudio` image that we loaded earlier, volumes need to be mounted within `/home/rstudio/` to be able to access them via the RStudio server web app.
# 
# ### Windows notes for mounting volumes:
# - Windows machines need to explicitly share drives with Docker - this should be part of your computer setup!
# - On Windows, the laptop path depends what shell you are using, here are some details:
#     - If you are going to run it in Windows terminal, then the command should be: `docker run --rm -it -v /$(pwd):<PATH_ON_CONTAINER> <IMAGE_NAME>` to share the current directory.
#     - If you are going to run it in Power Shell, then the command should be: `docker run --rm -it -v <ABSOLUTE_PATH_TO_CONTAINER>:<PATH_ON_CONTAINER> <IMAGE_NAME>` (`pwd` and variants do not seem to work). And the path must be formatted like: `C:\Users\tiffany.timbers\Documents\project\:/home/project`

# ## Mapping ports to containers with web apps
# 
# [Docker documentation on Container networking](https://docs.docker.com/config/containers/container-networking/)
# 
# If we want to use a graphical user interface (GUI) with our containers, for example to be able to use the computational environment in the container in an integrated development environment (IDE) such as RStudio or JupyterLab, then we need to map the correct port from the container to a port on our computer.
# 
# To do this, we use the `-p` flag with `docker run`, specifying the port in the container on the left-hand side, and the port on your computer (the container/Docker host) on the right-hand side of `:`. For example, to run the `rocker/rstudio` container image we would type `-p 8787:8787` to map the ports as shown in the `docker run` command below:
# 
# 
# ```
# docker run --rm -p 8787:8787 -e PASSWORD="apassword" rocker/rstudio:4.1.2
# ```
# 
# Then to access the web app, we need to navigate a browser url to `http://localhost:<COMPUTER_PORT>`. In this case we would navigate to <http://localhost:8787> to use the RStudio server web app from the container.
# 
# Note that we can only map one port on our computer (the container/Docker host) to a container at any given time. However,
# our computer (the container/Docker host) has many ports we can choose from to map. So if we wanted to run a second `rocker/rstudio` container, then we could map it to a different port as shown below:
# 
# ```
# docker run --rm -p 8788:8787 -e PASSWORD="apassword" rocker/rstudio:4.1.2
# ```
# 
# When we do this, to run the app in a browser on our computer, we need to go to <http://localhost:8788> (instead of <http://localhost:8787>) to access this container as we mapped it to the `8788` port on our computer (and not `8787`).
# 
# 
# Another important note is that the container port is specific to the container, and the web app installed therein. So we cannot change that without changing the container image, and/or application installed therein. Where do you learn what port is exposed in a container image? The image documentation should specify this. For example, in the [`rocker/rstudio` container image documentation](https://hub.docker.com/r/rocker/rstudio) it states:
# 
# <img src="img/rocker-rstudio-port-docs.png" width=600>
# 
# *Source: <https://hub.docker.com/r/rocker/rstudio>*

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
# For example, let's use the container run a `cowsay::say` function call to print some asci art with a cute message! 
# 
# ```
# $ docker run --rm ttimbers/dockerfile-practice:v0.1.0 Rscript -e "library(cowsay); say('Snow again this week?', 'snowman')"
# ```
# 
# 
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
# Now that was a silly example, but this can be made powerful so that we can run an analysis pipeline, such as a Makefile non-interactively using Docker! Here's a demo we can try: https://github.com/ttimbers/data_analysis_pipeline_eg/tree/v4.0
# 
# #### Exercise 1: 
# 
# Download https://github.com/ttimbers/data_analysis_pipeline_eg/archive/v4.0.zip, unzip it and navigate to the root of the project directory, try to run the analysis via `make all`.
# 
# #### Exercise 2: 
# 
# Now try to run the analysis using Docker via:
# 
# ```
# docker run --rm -v /$(pwd):/home/rstudio/data_analysis_eg ttimbers/data_analysis_pipeline_eg make -C /home/rstudio/data_analysis_eg all
# ```
# 
# *note - windows users must use Git Bash, set Docker to use Linux containers, and have shared their drives with Docker (see docs [here](https://token2shell.com/howto/docker/sharing-windows-folders-with-containers/)) for this to work*

# ## Docker commands
# 
# The table below summarizes the Docker commands we have learned so far and can serve as a useful reference when we are using Docker:
# 
# | command/flag | What it does          | 
# |--------------|-----------------------|
# | `pull`       | Downloads a Docker image from Docker Hub |
# | `images`     | Tells you what container images are installed on your machine |
# | `rmi`        | Deletes a specified container image from your machine |
# | `ps -a`      | Tells you what containers are running on your machine |
# | `stop`       | Stops a specified running container |
# | `rm`         | Removes a specified stopped container |
# | `run`        | Launches a container from an image |
# | `-it`        | Tells Docker to run the container interactively  |
# | `--rm`       | Makes a container ephemeral (deletes it upon exit)  |
# | `-v`         | Mounts a volume of your computer to the Docker container |
# | `-p`         | Specifies the ports to map a web app to |
# | `-e`         | Sets environment variables in the container (*e.g.*, PASSWORD="apassword") |
# | `exit`       | Exits a Docker container|

# ## Building container images from `Dockerfile`'s
# 
# - A `Dockerfile` is a plain text file that contains commands primarily about what software to install in the Docker image. This is the more trusted and transparent way to build Docker images.
# 
# - Once we have created a `Dockerfile` we can build it into a Docker image.
# 
# - Docker images are built in layers, and as such, `Dockerfiles` always start by specifiying a base Docker image that the new image is to be built on top off.
# 
# - Docker containers are all Linux containers and thus use Linux commands to install software, however there are different flavours of Linux (e.g., Ubuntu, Debian, CentOs, RedHat, etc) and thus you need to use the right Linux install commands to match your flavour of container. For this course we will focus on Ubuntu- or Debian-based images and thus use `apt-get` as our installation program.
# 
# 

# ### Workflow for building a Dockerfile
# 
# 1. Choose a base image to build off (from https://hub.docker.com/).
# 
# 2. Create a `Dockerfile` named `Dockerfile` and save it in an appropriate project repository. Open that file and type `FROM <BASE_IMAGE> on the first line`.
# 
# 3. In a terminal, type `docker run --rm -it <IMAGE_NAME>` and interactively try the install commands you think will work. Edit and try again until the install command works.
# 
# 4. Write working install commands in the `Dockerfile`, preceeding them with `RUN` and save the `Dockerfile`.
# 
# 5. After adding every 2-3 commands to your `Dockerfile`, try building the Docker image via `docker build --tag <TEMP_IMAGE_NAME> <PATH_TO_DOCKERFILE_DIRECTORY>`.
# 
# 6. Once the entire Dockerfile works from beginning to end on your laptop, then you can finally move to building remotely (e.g., creating a trusted build on GitHub Actions).

# ### Demo workflow for creating a `Dockfile` locally
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
# 
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
# 
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
# Hurray! We did it! Now we can automate this build on GitHub, push it to Docker Hub and share this Docker image with the world!
# 
# <img src="https://media.giphy.com/media/ZcKASxMYMKA9SQnhIl/giphy-downsized.gif">
# Source: https://giphy.com/gifs/memecandy-ZcKASxMYMKA9SQnhIl

# ## Tips for installing things programmatically on Debian-flavoured Linux
# 
# ### Installing things with `apt-get`
# 
# Before you install things with `apt-get` you will want to update the list of packages that `apt-get` can see. We do this via `apt-get update`. 
# 
# Next, to install something with `apt-get` you will use the `apt-get install` command along with the name of the software. For example, to install the Git version control software we would type `apt-get install git`. Note however that we will be building our containers non-interactively, and so we want to preempt any questions/prompts the installation software we will get by including the answers in our commands. So for example, to `apt-get install` we append `--yes` to tell `apt-get` that yes we are happy to install the software we asked it to install, using the amount of disk space required to install it. If we didn't append this, the installation would stall out at this point waiting for our answer to this question. Thus, the full command to Git via `apt-get` looks like:
# 
# ```
# apt-get install --yes git
# ```

# ### Breaking shell commands across lines
# 
# If we want to break a single command across lines in the shell, we use the `\` character. 
# For example, to reduce the long line below which uses `apt-get` to install the programs Git, Tiny Nano, Less, and wget:
# 
# ```
# apt-get install --yes git nano-tiny less wget
# ```
# 
# We can use `\` after each program, to break the long command across lines and make the command more readable (especially if there were even more programs to install). Similarly, we indent the lines after `\` to increase readability:
# 
# ```
# apt-get install --yes \
#     git \
#     nano-tidy \
#     less \
#     wget
# ```
# 
# ### Running commands only if the previous one worked
# 
# Sometimes we don't want to run a command if the command that was run immediately before it failed. We can specify this in the shell using `&&`. For example, if we want to not run `apt-get` installation commands if `apt-get update` failed, we can write:
# 
# ```
# apt-get update && \
#     apt-get install --yes git
# ```

# ## `Dockerfile` command summary
# 
# Most common `Dockerfile` commands I use:
# 
# | Command | Description |
# |---------|-------------|
# | FROM    | States which base image the new Docker image should be built on top of |
# | RUN     | Specifies that a command should be run in a shell |
# | ENV | Sets environment variables |
# | EXPOSE | Specifies the port the container should listen to at runtime |
# | COPY or ADD | adds files (or URL's in the case of ADD) to a container's filesystem |
# | ENTRYPOINT | Configure a container that will run as an executable |
# | WORKDIR | sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, COPY and ADD instructions that follow it in the `Dockerfile` |
# 
# And more here in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

# ## Choosing a base image for your Dockerfile
# 
# <img src="https://themuslimtimesdotinfodotcom.files.wordpress.com/2018/10/newton-quotes-2.jpg?w=1334" width=700>
# 
# Source: https://themuslimtimes.info/2018/10/25/if-i-have-seen-further-it-is-by-standing-on-the-shoulders-of-giants/
# 
# ### Good base images to work from for R or Python projects!
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
# 
# #### 1. Where does the `Dockerfile` live?
# 
# The Dockerfile should live in the root directory of your project.
# 
# #### 2. How do I make an image from a `Dockerfile`?
# 
# There are 2 ways to do this! I use the first when developing my `Dockerfile` (to test quickly that it works), and then the second I use when I think I am "done" and want to have it archived on [Docker Hub](https://hub.docker.com/). 
# 
# 1. Build a Docker image locally on your laptop
# 
# 2. Build a Docker image and push it to DockerHub using GitHub Actions, 
# 
# #### 3. How do I build an image locally on my laptop  
#  
# From the directory that contains your `Dockerfile` (usually your project root):
# 
# ```
# docker build --tag IMAGE_NAME:VERSION .
# ```
#     
# *note: `--tag` let's you name and version the Docker image. You can call this anything you want. The version number/name comes after the colon*
#     
# After I build, I think try to `docker run ...` to test the image locally. If I don't like it, or it doesn't work, I delete the image with `docker rmi {IMAGE_NAME}`, edit my Dockerfile and try to build and run it again.

# ## Build a Docker image from a Dockerfile on GitHub Actions
# 
# Building a Docker image from a Dockerfile using an automated tool (e.g., DockerHub or GitHub Actions) lets others trust your image as they can clearly see which Dockerfile was used to build which image.  
# 
# We will do this in this course by using GitHub Actions (a continuous integration tool) because is provides a great deal of nuanced control over when to trigger the automated builds of the Docker image, and how to tag them.
# 
# An example GitHub repository that uses GitHub Actions to build a Docker image from a Dockerfile and publish it on DockerHub is available here: [https://github.com/ttimbers/gha_docker_build](https://github.com/ttimbers/gha_docker_build)
# 
# We will work through a demonstration of this now starting here: [https://github.com/ttimbers/dockerfile-practice](https://github.com/ttimbers/dockerfile-practice)

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
# - `pip freeze` or `conda list` in the bash shell to find out Python package versions
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
# ### A newer thing that might be useful!
# 
# You can pair [renv](https://rstudio.github.io/renv/articles/docker.html?q=docker#running-docker-containers-with-renv) with Docker - this is new and will be covered in tutorial this week! 🎉
# 
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
# 
# ### Take home messages:
# 
# - At a minimum, tag your Docker images or reference image digests
# - If you want to version installs inside the container, use base images that version R & Python, and add what you need on top in a versioned manner!

# ## Docker compose
# 
# Docker compose is a tool that uses a `YAML` file to configure/specify how you want to run one or more Docker containers. To use Docker compose, we create a `docker-compose.yml` file that specifies things such as:
# - the Docker images (and version)
# - the ports
# - volume mapping
# - any environment variables
# 
# Then to run the Docker container using the specifications in the `docker-compose.yml` file, we run:
# 
# ```
# docker-compose run --rm service command
# ```
# 
# - `service` is a name you give to your application configurations in the `docker-compose.yml`
# - `command` is some command or script you would like to run (e.g., `make all`)
# 
# Here is an example `docker-compose.yml`:
# 
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
# 
# And to run the container and the analysis we would type:
# 
# ```
# docker-compose run --rm analysis-env make -C /home/rstudio/breast_cancer_predictor all
# ```
# 
# This means we do not have to type out the:
# - ports
# - volume mapping
# - environment variables
# - and potentially more!

# ## Where to next?
# 
# - Testing code written for data science

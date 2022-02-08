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
# RUN apt-get update --yes && \
#     apt-get install --yes --no-install-recommends \
#     git
#     #nano-tiny \
#     #less
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
# > Note: You can skip this step and just got onto `docker run ...` as that command will pull the image if you do not have it locally.

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

# ## Docker commands
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
# | `-p`         | Specifies the ports to map a web app to |
# | `exit`       | Exits a Docker container                      |

# ## Where to next?
# 
# - Installing things in linux (most containers used in Data Science are linux based)
# 
# - Creating your own Docker image!

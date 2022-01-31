#!/usr/bin/env python
# coding: utf-8

# # Virtual environments

# ## Attribution
# 
# The conda virtual environment section of this guide
# was originally published at http://geohackweek.github.io/ under a CC-BY license
# and has been updated to reflect recent changes in conda,
# as well as modified slightly to fit the MDS lecture format.
# 
# ## Topic learning goals
# 
# By the end of the lecture you will be able to:
# 
# 1. Manage virtual environments with `conda` and `renv`.
# 
# 

# ## Virtual environments
# 
# Virtual environments let's you have multiple versions of packages
# and programs on the same computer
# without them creating conflicts with each other.
# You will be using virtual Python and R environments
# throughout the program to setup your packages for different courses.

# ## Conda
# 
# [**conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system for any programming language**;
# though it is the most popular in the python community.
# [Anaconda](https://www.continuum.io/why-anaconda) is a data science platform for Python
# that comes with a lot of packages by default. Unlike Anaconda,
# Miniconda doesn't come with any installed packages by default,
# and we can pick and choose which ones we want.
# Both include Python and conda.
# 
# ### Managing Conda
# 
# Let's first start by checking if conda is installed.
# 
# ```
# conda --version
# ```
# 
# To see which conda commands are available,
# type `conda --help`.
# To see the full documentation for any command of these commands,
# type the command followed by `--help`.
# For example,
# to learn about the conda update command:
# 
# ```
# conda update --help
# ```
# 
# Let's update our conda to the latest version.
# Note that you might already have the latest version since we downloaded it recently.
# 
# ```
# conda update conda
# ```
# 
# You will see some information about what there is to update
# and be asked if you want to confirm.
# The default choice is indicated with `[]`,
# and you can press <kbd>Enter</kbd> to accept it.
# It would look similar to this:
# 
# ```
# Using Anaconda Cloud api site https://api.anaconda.org
# Fetching package metadata: ....
# .Solving package specifications: .........
# 
# Package plan for installation in environment //anaconda:
# 
# The following packages will be downloaded:
# 
#     package                    |            build
#     ---------------------------|-----------------
#     conda-env-2.6.0            |                0          601 B
#     ruamel_yaml-0.11.14        |           py27_0         184 KB
#     conda-4.2.12               |           py27_0         376 KB
#     ------------------------------------------------------------
#                                            Total:         560 KB
# 
# The following NEW packages will be INSTALLED:
# 
#     ruamel_yaml: 0.11.14-py27_0
# 
# The following packages will be UPDATED:
# 
#     conda:       4.0.7-py27_0 --> 4.2.12-py27_0
#     conda-env:   2.4.5-py27_0 --> 2.6.0-0
#     python:      2.7.11-0     --> 2.7.12-1
#     sqlite:      3.9.2-0      --> 3.13.0-0
# 
# Proceed ([y]/n)? y
# 
# Fetching packages ...
# conda-env-2.6. 100% |################################| Time: 0:00:00 360.78 kB/s
# ruamel_yaml-0. 100% |################################| Time: 0:00:00   5.53 MB/s
# conda-4.2.12-p 100% |################################| Time: 0:00:00   5.84 MB/s
# Extracting packages ...
# [      COMPLETE      ]|###################################################| 100%
# Unlinking packages ...
# [      COMPLETE      ]|###################################################| 100%
# Linking packages ...
# [      COMPLETE      ]|###################################################| 100%
# ```
# 
# In this case,
# conda itself needed to be updated,
# and along with this update some dependencies also needed to be updated.
# There is also a NEW package that was INSTALLED in order to update conda.
# You don't need to worry about remembering to update conda,
# it will let you know if it is out of date when you are installing new packages.

# ## Managing Environments
# 
# ### What is a conda environment and why is it so useful?
# 
# Using `conda`, you can create an isolated python *environment* for your project.
# An environment is a set of packages that can be used in one or multiple projects.
# There are several major  benefits of using environments:
# 
# 
# - You can guarantee that someone else can reproduce your project 
#   by specifying which package versions your used
#   and making it easy for others to install the same versions.
# - If two of your projects relies on different versions of the same package,
#   you can install these in different environments.
# - If you want to play around with a new package,
#   you don't have to change the packages you use for your data analysis
#   and risk messing something up.
# - When you develop your own packages,
#   it is essential to use environments,
#   since you want to to make sure you know exactly which packages yours depend on,
#   so that it runs on other systems than your own.
# 
# The default environment is the `base` environment,
# which contains only the essential packages from Miniconda.
# You can see that your shell's prompt string is prefaced with `(base)`
# when you are inside this environment.
# In the setup guide,
# we gave your instructions for how to activate this environment by default
# every time you open Bash.
# There are two ways of creating a conda environment.
# 
# 1. Manual specifications of packages.
# 2. An environment file in YAML format (`environment.yaml`).

# ### Creating environment by manually specifying packages
# 
# We can create `test_env` conda environment by typing `conda -n <name-of-env>`.
# However,
# it is often useful to specify more than just the name of the environment,
# e.g. the channel from which to install packages, the Python version,
# and a list of packages to install into the new env.
# In the example below,
# I am creating the `test_env` environment
# that uses python 3.7 and a list of libraries: `jupyterlab` and `pandas`.
# 
# ```
# conda create -n test_env -c conda-forge python=3.7 jupyterlab pandas=1.0.2
# ```
# 
# conda will solve any dependencies between the packages like before
# and create a new environment with those packages.
# Usually,
# we don't need to specify the channel,
# but in this case I want to get the very latest version of these packages,
# and they are made available in `conda-forge`
# before they reach the default conda channel.
# 
# To activate this new environment,
# you can type `conda activate test_env`
# (and `conda deactivate` for deactivating).
# Since you will do this often,
# we created an alias shortcut `ca`
# that you can use to activate environments.
# To know the current environment that you're in you can look at the prefix
# of the prompt string in your shell which now changed to (`test_env`).
# And to see all your environments,
# you can type `conda env list`.

# ### Sharing Environments with others
# 
# To share an environment, you can export your conda environment to an environment file,
# which will list each package and its version
# in the format `package=version=build`.
# 
# Exporting your environment to a file called `environment.yaml`
# (it could be called anything,
# but this is the conventional name
# and using it makes it easy for others
# to recognize that this is a conda env file,
# the extension can be either `.yaml` or `.yml`):
# 
# ```
# conda env export -f environment.yaml
# ```
# 
# Remember that `.yaml` files are plain text,
# so you can use a text editor such as VS Code to open them.
# If you do,
# you will realize that this environment file has A LOT more packages
# than `jupyterlab` and `pandas`.
# This is because the default behavior is to also list the dependencies
# that were installed together with these packages,
# e.g. `numpy`.
# This is good in the sense that it gives an exact copy of *everything*
# in your environment.
# 
# However,
# some dependencies might differ between operating systems,
# so this file *might* not work with someone from a different OS.
# To remedy this,
# you can append the `--from-history` flag,
# which look at the history of the packages you explicitly told conda to install
# and only list those in the export.
# The required dependencies will then be handled in an OS-specific manner during the installation,
# which guarantees that they will work across OSes.
# This `environment.yaml` file would be much shorter and look something like this:
# 
# ```yaml
# name: test_env
# channels:
#   - conda-forge
#   - defaults
# dependencies:
#   - conda
#   - python=3.7
#   - pandas==1.0.2
#   - jupyterlab
# ```
# 
# Importantly,
# this will not include the package version
# unless you included it when you installed 
# with the `package==version` syntax.
# For an environment to be reproducible,
# you **NEED** to add the version string manually.

# ### Creating environment from an environment file
# 
# Now, let's install `environment.yaml` environment file above so that we can create a conda environment called `test_env`.
# 
# ```
# $ conda env create --file environment.yaml
# ```

# ### Copying an environment
# 
# We can make an exact copy of an environment to an environment with a different name.
# This maybe useful for any testing versus live environments or different Python 2.7 versions for the same packages.
# In this example, `test_env` is cloned to create `live_env`.
# 
# ```
# conda create --name live_env --clone test_env
# ```

# ### Deleting an environment
# 
# Since we are only testing out our environment,
# we will delete `live_env` to remove some clutter.
# *Make sure that you are not currently using `live_env`.*
# 
# ```
# conda env remove -n live_env
# ```

# ### Making environments work well with JupyterLab
# 
# In brief,
# you need to install the `ipykernel` package
# in any new environment your create,
# and the `nb_conda_kernels` package needs to be installed
# in the environment where JupyterLab is installed.
# 
# By default,
# JupyterLab only sees the conda environment where it is installed.
# Since it is quite annoying to install JupyterLab and its extensions separately in each environment,
# there is a package called `nb_conda_kernels` that makes it possible
# to have a single installation of JupyterLab access kernels in other conda environments.
# This package needs to be installed in the conda environment
# where JupyterLab is installed.
# 
# Lastly,
# you also need to install a kernel in the new conda environment
# so that it can be detected by `nb_conda_kernels`.
# This kernel can be installed via the package `ipykernel` for Python
# and the `r-irkernel` package for R
# ([more info in the nb_conda_kernels README](https://github.com/Anaconda-Platform/nb_conda_kernels#installation)).

# ## Managing Packages
# 
# ### Seeing what packages are available
# 
# We will now check packages that are available to us.
# The command below will list all the packages in an environment, in this case `test_env`.
# The list will include versions of each package, the specific build,
# and the channel that the package was downloaded from.
# `conda list` is also useful to ensure that you have installed the packages that you desire.
# 
# ```
# conda list
# ```
# 
# ```
# # packages in environment at //miniconda/envs/test_env:
# #
# Using Anaconda Cloud api site https://api.anaconda.org
# blas                      1.1                    openblas    conda-forge
# ca-certificates           2016.9.26                     0    conda-forge
# certifi                   2016.9.26                py27_0    conda-forge
# cycler                    0.10.0                   py27_0    conda-forge
# freetype                  2.6.3                         1    conda-forge
# functools32               3.2.3.2                  py27_1    conda-forge
# libgfortran               3.0.0                         0    conda-forge
# ```

# ### Searching for a certain package
# 
# Some packages might not be available in conda, but are available in [pypi](https://pypi.python.org/pypi).
# For example, we will search for rasterio within the [anaconda cloud](https://anaconda.org/).
# *It is not necessary to create an account with anaconda cloud, unless you'd like to contribute in the future when you are pro with conda.*
# 
# In this example, we will use rasterio from conda-forge. The anaconda cloud page for rasterio will show how to install the package, compatible OS, individual files for that package, etc.
# 
# With conda you can do this search within the command line:
# 
# ```
# conda search rasterio
# ```
# 
# ```
# Using Anaconda Cloud api site https://api.anaconda.org
# Run 'anaconda show <USER/PACKAGE>' to get more details:
# Packages:
#      Name                      |  Version | Package Types   | Platforms      
#      ------------------------- |   ------ | --------------- | ---------------
#      IOOS/rasterio             |    1.0a2 | conda           | linux-64, win-32, win-64, osx-64
#      Terradue/rasterio         |   0.32.0 | conda           | linux-64       
#                                           : Fast and direct raster I/O for use with Numpy and SciPy
#      anaconda/rasterio         |   0.36.0 | conda           | linux-64, win-32, win-64, linux-32, osx-64
#      conda-forge/rasterio      |    1.0a2 | conda           | linux-64, win-32, win-64, osx-64
#                                           : Rasterio reads and writes geospatial raster datasets
#      dharhas/rasterio          |   0.23.0 | conda           | win-64         
#                                           : Rasterio reads and writes geospatial raster datasets.
#      erdc/rasterio             |   0.23.0 | conda           | win-64         
#                                           : Rasterio reads and writes geospatial raster datasets.
#      jesserobertson/rasterio   |   0.23.0 | conda           | linux-64, linux-32, osx-64
#      jhamman/rasterio_to_xarray | 2016.03.16-1558 | ipynb           |                
#                                           : IPython notebook
#      krisvanneste/rasterio     |   0.26.0 | conda           | win-64         
#      ocefpaf/rasterio          |   0.19.1 | conda           | linux-64, osx-64
#      omgarcia/rasterio         |   0.25.0 | conda           | linux-64       
#      pypi/rasterio             |   0.13.2 | pypi            |                
#                                           : Fast and direct raster I/O for Python programmers who use Numpy
#      robintw/rasterio          |   0.35.1 | conda           | osx-64         
#                                           : Rasterio reads and writes geospatial raster datasets
#      sgillies/rasterio         |     0.15 | conda           | osx-64         
#      ztessler/rasterio         |   0.31.0 | conda           | osx-64         
#                                           : Fast and direct raster I/O for use with Numpy and SciPy
# Found 15 packages
# ```

# ### Installing conda package
# 
# Under the name column of the result in the terminal or the package column in the Anaconda Cloud listing,
# shows the necessary information to install the package.
# e.g. conda-forge/rasterio.
# The first word list the channel that this package is from and the second part shows the name of the package.
# 
# To install the latest version available within the channel, do not specify in the install command. We will install version 0.35 of `rasterio` from conda-forge into `test_env` in this example. Conda will also automatically install the dependencies for this package.
# 
# ```
# conda install -c conda-forge rasterio=0.35
# ```
# 
# If you have a few trusted channels that you prefer to use, you can pre-configure these so that everytime you are creating an environment, you won't need to explicitly declare the channel. 
# 
# ```
# conda config --add channels conda-forge
# ```

# #### Removing a conda Package
# 
# We decided that rasterio is not needed in this tutorial, so we will remove it from `test_env`.
# Note that this will remove the main package rasterio and its dependencies (unless a dependency was installed explicitly at an earlier point in time or is required be another package).
# 
# ```
# conda remove -n test_env rasterio
# ```
# 
# ```
# Using Anaconda Cloud api site https://api.anaconda.org
# Fetching package metadata .........
# Solving package specifications: ..........
# 
# Package plan for package removal in environment //anaconda/envs/test_env:
# 
# The following packages will be REMOVED:
# 
#     rasterio: 0.35.1-np111py27_1 conda-forge
# 
# Proceed ([y]/n)? y
# 
# Unlinking packages ...
# [      COMPLETE      ]|#######################################################################################################| 100%
# ```

# Remeber that when you forget a specific command
# you can type in the help command we have created `mds-help`
# in you terminal to see a list of all commands we use in MDS.

# # R environments
# 
# In R,
# environments are managed by `renv`,
# which works with similar principles as `conda`,
# and other virtual environment managers,
# but the commands are different.
# To see which commands are used in `renv`,
# you can [visit the project website](https://rstudio.github.io/renv/articles/renv.html).
# Briefly,
# `renv::init()` is used to create a new env,
# `renv::snapshot` is used to save/export the environment to a file (`renv.lock`),
# and installing and removing packages are done as usual
# via the `install.packages()` and `remove.packages()` commands.

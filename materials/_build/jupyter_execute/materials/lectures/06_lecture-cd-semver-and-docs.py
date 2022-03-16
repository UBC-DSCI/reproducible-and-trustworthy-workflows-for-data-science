#!/usr/bin/env python
# coding: utf-8

# # Lecture 6: Introductions to Continuous Development (CD), package documentation & publishing
# 

# ## Learning objectives:
# By the end of this lecture, students should be able to:
# - Define continuous deployment
# - Explain why continuous deployment is superior to manually deploying software
# - Use GitHub Actions to set-up automated deployment of Python packages upon push to the master branch
# - Explain semantic versioning, and define what constitutes patch, minor, major and breaking changes
# - Write conventional commit messages that are useful for semantic release
# - Generate well formatted function and package-level documentation for Python packages using Sphinx & Read the Docs
# - Generate well formatted function and package-level documentation for R using Roxygen and `pkgdown`
# - Publish Python packages to test PyPI
# - Publish R packages to GitHub, document how to install them via `devtools::install_github`

# ## Continous Deployment (CD)
# 
# Defined as the practice of automating the deployment of software that has successfully run through your test-suite.
# 
# For example, upon merging a pull request to master, an automation process builds the Python package and publishes to PyPI without further human intervention. 

# ### Why use CD?
# 
# - little to no effort in deploying new version of the software allows new features to be rolled out quickly and frequently
# - also allows for quick implementation and release of bug fixes
# - deployment can be done by many contributors, not just one or two people with a high level of Software Engineering expertise

# ### Why use CD?
# 
# Perhaps this story is more convincing:
# 
# *The company, let’s call them ABC Corp, had 16 instances of the same software, each as a different white label hosted on separate Linux machines in their data center. What I ended up watching (for 3 hours) was how the client remotely connected to each machine individually and did a “capistrano deploy”. For those unfamiliar, Capistrano is essentially a scripting tool which allows for remote execution of various tasks. The deployment process involved running multiple commands on each machine and then doing manual testing to make sure it worked.*
# 
# *The best part was that this developer and one other were the only two in the whole company who knew how to run the deployment, meaning they were forbidden from going on vacation at the same time. And if one of them was sick, the other had the responsibility all for themselves. This deployment process was done once every two weeks.*
# 
# [*Source*](https://levelup.gitconnected.com/heres-why-continuous-integration-and-deployment-is-so-important-to-the-software-development-c0caeead5881)*: Tylor Borgeson*
# 

# Infrequent & manual deployment makes me feel like this when it comes time to do it:
# 
# ![](https://media.giphy.com/media/bEVKYB487Lqxy/giphy.gif)

# *and so it can become a viscious cycle of delaying deployment because its hard, and then making it harder to do deployment because a lot of changes have been made since the last deployment...*

# So to avoid this, we are going to do continuous deployment when we can! And where we can't, we will automate as much as we can up until the point where we need to manually step in.

# ## Using GitHub Actions to perform CD for your Python package
# 
# We will be building off what we learned last class about continuous integration with GitHub actions for Python. What we need to change to make a continuous deployment work for our package?
# 
# - change the event trigger
# 
# - change the runner to one machine - ubuntu
# 
# - bump the version
# 
# - create a release on GitHub that corresponds to that version
# 
# - build our package
# 
# - publish to (test) PyPI
# 
# 

# ### Exercise: read [`ci-cd.yml`](https://github.com/py-pkgs/py-pkgs-cookiecutter/blob/main/%7B%7Bcookiecutter.package_name%7D%7D/.github/workflows/ci-cd.yml)
# 
# To make sure we understand what is happening in our workflow that performs CD, 
# let's read [`ci-cd.yml`](https://github.com/py-pkgs/py-pkgs-cookiecutter/blob/main/%7B%7Bcookiecutter.package_name%7D%7D/.github/workflows/ci-cd.yml) and convert each **step** to a human-readable explanation:
# 
# #### ci job:
# 
# 1. Sets up Python on the runner 
# 
# 2. Checkout our repository files from GitHub and put them on the runner
# 
# 3. Installs poetry
# 
# 3. Installs our package and the package dependencies
# 
# 4. Run test suite and get coverage report
# 
# 5. Upload coverage report to codecov.io
# 
# 6. Build the documentation
# 
# #### cd job:
# 
# 1. 
# 
# 2. 
# 
# 3. 
# 
# 4. 
# 
# 5. 
#  
# 6. 
# 
# 
# > Note: I filled in the steps we went over last class, so you can just fill in the new stuff
# 
# **_Question: when does the `cd` job run?_**

# ### How can we automate version bumping?
# 
# Let's look at the step that accomplishes this:
# 
# ```
#  # Step 4. Use PSR to make release
#     - name: Python Semantic Release
#       run: |
#           pip install python-semantic-release
#           git config user.name github-actions
#           git config user.email github-actions@github.com
#           semantic-release publish
# ```
# 
# Our key command in this step is `semantic-release publish`. 
# 
# [Python semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) is a Python tool which parses commit messages looking for keywords to indicate how to bump the version. It bumps the version in the `pyproject.toml` file.
# 
# To understand how it works so that we can use it, we need to understand **semantic versioning** and how to write **conventional commit** messages.
# 
# Let's unpack eack of these on its own.

# ## Semantic versioning

# - When we make changes and publish new versions of our packages, we should tag these with a version number so that we and others can view and use older versions of the package if needed. 
# 

# - These version numbers should also communicate something about how the underlying code has changed from one version to the next. 

# - Semantic versioning is an agreed upon "code" by developers that gives meaning to version number changes, so developers and users can make meaningful predictions about how code changes between versions from looking solely at the version numbers.

# - Semantic versioning assumes version 1.0.0 defines the API, and the changes going forward use that as a starting reference.

# ## Semantic versioning
# 
# Given a version number `MAJOR.MINOR.PATCH` (e.g., `2.3.1`), increment the:

# - MAJOR version when you make incompatible API changes (often called breaking changes 💥) 

# - MINOR version when you add functionality in a backwards compatible manner ✨↩️

# - PATCH version when you make backwards compatible bug fixes 🐞
# 
# *Source: https://semver.org/*

# ### Semantic versioning case study

# **Case 1:** In June 2009, Python bumped versions from 3.0.1, some changes in the new release included:
# - Addition of an ordered dictionary type
# - A pure Python reference implementation of the import statement
# - New syntax for nested with statements

# **Case 2:** In Dec 2017, Python bumped versions from 3.6.3, some changes in the new release included:
# 
# - Fixed several issues in printing tracebacks (`PyTraceBack_Print()`).
# - Fix the interactive interpreter looping endlessly when no memory.
# - Fixed an assertion failure in Python parser in case of a bad `unicodedata.normalize()`

# **Case 3:** In Feb 2008, Python bumped versions from 2.7.17, some changes in the new release included:
# - `print` became a function
# - integer division resulted in creation of a float, instead of an integer
# - Some well-known APIs no longer returned lists (e.g., `dict.keys`, `dict.values`, `map`)

# ### Exercise: name that semantic version release
# 
# Reading the three cases posted above, think about whether each should be a major, minor or patch version bump. Answer the chat when prompted.

# ## Conventional commit messages
# 
# Python semantic-release by default uses a parser that works on the conventional (or Angular) commit message style, which is:
# 
# ```
# <type>(optional scope): succinct description of the change
# 
# (optional body: the motivation for the change and contrast this with previous behavior)
# 
# (optional footer: note BREAKING CHANGES here, as well as any issues to be closed)
# ```
# 

# How to affect semantic versioning with conventional commit messages:
# - a commit with the type `fix` leads to a patch version bump
# - a commit with the type `feat` leads to a minor version bump
# - a commit with a body or footer that starts with `BREAKING CHANGE:` - these can be of any type

# > Note - commit types other than `fix` and `feat` are allowed. Recommeneded ones include `docs`, `style`, `refactor`, `test`, `ci` and [others](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#type).

# ### An example of a conventional commit message
# 
# ```
# git commit -m "feat(function_x): added the ability to initialize a project even if a pyproject.toml file exists 
# ```

# What kind of version bump would this result in?

# ### Another example of a conventional commit message
# 
# ```
# git commit -m "feat: change to use of `%>%` to add new layers to ggplot objects
# 
# BREAKING CHANGE: `+` operator will no longer work for adding new layers to ggplot objects after this release
# ```

# What kind of version bump would this result in?

# ### Some practical notes for usage in your packages:
# 
# 0. You must add `python-semantic-release` as a dev dependency via poetry
# 
# 1. You must add the following to the tool section of your `pyproject.toml` file as shown below, for this to work (filling in `<package_name>` with the appropriate value). [Table 8.2](https://py-pkgs.org/08-ci-cd#psr-table) from the Python packages book explains each of these in more detail.
#     
#     ```
#     [tool.semantic_release]
#     version_variable = "pyproject.toml:version" # version location
#     branch = "main"                             # branch to make releases of
#     changelog_file = "CHANGELOG.md"             # changelog file
#     build_command = "pip install poetry && poetry build"  # build dists
#     dist_path = "dist/"                         # where to put dists
#     upload_to_pypi = false                      # don't auto-upload to PyPI
#     remove_dist = false                         # don't remove dists
#     patch_without_tag = "true"                  # always bump version on CD, even without angular commit (default is patch)
#     ```
#     
# 2. If `feat` or `BREAKING CHANGES:` are not included in the commits when a pull request is merged to master, by default Python's `semantic-release` bumps the patch version.

# ### A practical notes for usage in your packages:
# 
# If you have been working with main branch protection, you will need to change something to use `ci-cd.yml` work for continuous deployment. The reason for this, is that this workflow (which bumps versions and deploy the package) is triggered to run **after** the pull request is merged to main. Therefore, when we bump the versions in the `pyproject.toml` file awe need to push these changes to the main branch - however this is problematic given that we have set-up main branch protection!
# 
# What are we to do?
# 
# #### Solution 1: 
# 
# Remove main branch protection. This is not the most idealistic solution, however it is a simple and practical one.
# 
# #### Possible solution 2: 
# 
# (I say possible because this is still experimental for me and not well tested)
# 
# Another option may be use a bot to briefly turn off main branch protection just before we push the files where we bumped the version, and then use the bot to turn it back on again after pushing. To do this, we will use the [`benjefferies/branch-protection-bot` action](https://github.com/benjefferies/branch-protection-bot).
#     
# Looking at [`ci-cd.yml`](https://github.com/py-pkgs/py-pkgs-cookiecutter/blob/main/%7B%7Bcookiecutter.package_name%7D%7D/.github/workflows/ci-cd.yml), we could add the `branch-protection-bot` action to **turn off** main branch protection after the step named "checkout" but before the step named "Python Semantic Release". We could also add the `branch-protection-bot` action to **turn on** main branch protection after the step named "Python Semantic Release" but before the step named "Publish to TestPyPI".
#     
# Below is the section of our [`ci-cd.yml`](https://github.com/py-pkgs/py-pkgs-cookiecutter/blob/main/%7B%7Bcookiecutter.package_name%7D%7D/.github/workflows/ci-cd.yml) **before** we add the `branch-protection-bot`:
#     
# ```    
#     # Check-out repository so we can access its contents
#     - uses: actions/checkout@v2
#       with:
#         fetch-depth: 0
#         
#     # Use PSR to make release
#     - name: Python Semantic Release
#       run: |
#           pip install python-semantic-release
#           git config user.name github-actions
#           git config user.email github-actions@github.com
#           semantic-release publish
#           
#     # Publish to TestPyPI
#     - uses: pypa/gh-action-pypi-publish@release/v1
#       with:
#         user: __token__
#         password: {% raw %}${{ secrets.TEST_PYPI_API_TOKEN }}{% endraw %}
#         repository_url: https://test.pypi.org/legacy/
#         skip_existing: true
# ```
#     
# Below is the section of our [`ci-cd.yml`](https://github.com/py-pkgs/py-pkgs-cookiecutter/blob/main/%7B%7Bcookiecutter.package_name%7D%7D/.github/workflows/ci-cd.yml) **after** we add the `branch-protection-bot`:
# 
# ```
#     # Check-out repository so we can access its contents
#     - uses: actions/checkout@v2
#       with:
#         fetch-depth: 0
#         
#     - name: Disable admin branch protection
#       uses: benjefferies/branch-protection-bot@master
#       if: always()
#       with:
#           access_token: ${{ secrets.ACCESS_TOKEN }}
#           branch: main
#           enforce_admins: false
#           
#     # Use PSR to make release
#     - name: Python Semantic Release
#       run: |
#           pip install python-semantic-release
#           git config user.name github-actions
#           git config user.email github-actions@github.com
#           semantic-release publish
#           
#     - name: Enable admin branch protection
#       uses: benjefferies/branch-protection-bot@master
#       if: always()  # Force to always run this step to ensure "include administrators" is always turned back on
#       with:
#         access_token: ${{ secrets.ACCESS_TOKEN }}
#         branch: main
#         enforce_admins: true
#         
#     # Publish to TestPyPI
#     - uses: pypa/gh-action-pypi-publish@release/v1
#       with:
#         user: __token__
#         password: {% raw %}${{ secrets.TEST_PYPI_API_TOKEN }}{% endraw %}
#         repository_url: https://test.pypi.org/legacy/
#         skip_existing: true
# ```
#     
# Finally, to make this work you would need to add one of your team members personal GitHub access tokens as a GitHub secret named `ACCESS_TOKEN` (see [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) for how to get your personal GitHub access token).
# 
# - Demo of this in action from a project from last year: <https://github.com/UBC-MDS/NiceNumber>

# ### Demo of Continous Deployment!
# 
# - <https://github.com/ttimbers/pycounts_tat>

# ### What about CD with R packages
# 
# - This is not a common practice (yet!). One reason for this could be that CRAN has a policy where they only want to see updates every 1-2 months.
# 
# - Semantic versioning is used in Tidyverse R packages, but creating versions is done manually

# ## Package-level documentation for Python
# 
# There are several levels of documentation possible for Python packages:
# - code-level documentation (formatted docstrings)
# - package-level documentation via [`sphinx`](https://www.sphinx-doc.org/en/master/index.html)
# - package websites (via [Read the Docs](https://readthedocs.org/))

# ### Code & package-level documentation
# 
# - We learned the basics of how to write formatted docstrings for our functions in DSCI 511
# 

# - These docstrings can not only be accessed via `?function_name`, but can also be used to automatically generate package-level documentation via [`sphinx`](https://www.sphinx-doc.org/en/master/index.html)
# 

# - We already did this with our toy `foocat` package by:
#     - adding sphinx as a dev dependency via `poetry add --dev sphinx`
#     - create the `.rst` files for your package functions by running: `poetry run sphinx-apidoc -f -o docs/source <package_name>` from the project root
#     - and then ran `poetry run make html` from the docs directory

# ### Code & package-level documentation
# 
# - To have `sphinx` correctly render the docstring as package-level documentation, we need to either write our docstrings in the correct format for restructured text (RST) or we can use the `sphinx` extension `napolean` that can render Numpy- or Google-style docstrings (which are much easier for you to write and read).

# ### Example of RST formatted docstrings:
# 
# ```
# :type path: str
# :param field_storage: The :class:`FileStorage` instance to wrap
# :type field_storage: FileStorage
# :param temporary: Whether or not to delete the file when the File
#    instance is destructed
# :type temporary: bool
# :returns: A buffered writable file descriptor
# :rtype: BufferedFileStorage
# ```

# ### Example of Numpy-style docstrings:
# 
# ```
# Summary line.
# 
#     Extended description of function.
# 
#     Parameters
#     ----------
#     arg1 : int
#         Description of arg1
#     arg2 : str
#         Description of arg2
# 
#     Returns
#     -------
#     bool
#         Description of return value
# ```

# ### Code & package-level documentation
# 
# When using Numpy-style docstrings, we need to do the following:
# 
# - add `sphinxcontrib-napoleon` as a dev dependency via `poetry add --dev`
# 
# - add `extensions = ['sphinx.ext.napoleon']` to the docs configuration file (`docs/conf.py`) - we have already done this for you in the Cookiecutter template.

# ### Editing & Rendering package-level documentation
# 
# - As we did in the toy `pycounts*` package, we render the docs via running `poetry run make html` from the docs directory
# 
# - *Note: it is not essential that you locally render the docs, as we will see next that Read the Docs does this for your on their remote machines, however it is a best practice to do so because it is a lot faster than Read the Docs and therefore editing and proof-reading is more efficient when done locally.*

# ### Editing & Rendering package-level documentation
# 
# - The Python community has been heavily invested in ReStructuredText (rst) as a mark-up language for a long time, and thus `sphinx` works best when used with that as opposed to markdown (although it is possible, see [here](https://www.sphinx-doc.org/en/master/usage/markdown.html) for details).
# 
# - [ReStructuredText cheat sheet](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html)
# 
# 
# ### Vignettes
# 
# It is common for packages to have vignettes (think demos with narratives) showing how to use the package in a more real-world scenario than the documentation examples show. In your Python package, this ideally might go in something like the Usage section of the docs. However, that document is in rst for the template we gave you to use. So for your project, you could also put it in the README of your repo (or link to it from there). 
# 
# There is a new sphinx extension called [`nbsphinx`](https://nbsphinx.readthedocs.io/en/0.8.2/) that let's you use `.ipynb` files for package documentation. We have not used it yet in MDS, but it looks promising and we might adopt it in the future.

# ### Package websites (via [Read the Docs](https://readthedocs.org/))
# 
# The standard practice for hosting and sharing docs in the Python community is to use [Read the Docs](https://readthedocs.org/)
# 
# - Similar to codecov.io, to use Read the Docs with our package, we need to link it to our GitHub repository
# 
# - Read the Docs then checks out the files from the GitHub repo and uses their remote machines to render and serve your documentation
# 
# - To do this, Read the Docs needs access to the packages `pyproject.toml` file. This is done via the creation of a `.readthedocs.yml` file in the root of your project that looks like this:
# 
# ```
# build:
#   image: latest
# python:
#   version: 3.9
#   pip_install: true
#   extra_requirements:
#     - docs
# ```
# 
# *note - the version of Python specified here has to be a version that your package can be installed with!*

# ## Package documentation for R
# 
# There are several levels of documentation possible for R packages:
# - code-level documentation (Roxygen-style comments)
# - vignettes
# - package websites (via `pkgdown`)

# ### Code-level documentation (Roxygen-style comments)
# 
# - We learned the basics of how to write Roxygen-style comments in DSCI 511
# - In the package context, there are Namespace tags you should know about:
#     - `@export` - this should be added to all package functions you want your user to know about
#     - `@NoRd` - this should be added to helper/internal helper functions that you don't want your user to know about

# ### Vignettes
# - Think of your vignette as a demonstration of how someone would use your function to solve a problem. 
# 
# - It should demonstrate how the individual functions in your package work, as well as how they can be integrated together.
# 
# - To create a template for your vignette, run:
#     ```
#     usethis::use_vignette("package_name-vignette")
#     ```
#     
# - Add content to that file and knit it when done.
# 
# As an example, here's the `dplyr` vignette: <https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html>

# ### Package websites (via [`pkgdown`](https://pkgdown.r-lib.org/))
# 
# - Vignettes are very helpful, however they are not that discoverable by others, websites are a much easier way to share your package with others
# 
# - The `pkgdown` R package let's you build a beautiful website for your R package in 4 steps!
# 
#     1. Install `pkgdown`: `install.packages("pkgdown")
# 
#     2. Run `pkgdown::build_site()` from the root of your project, and commit and push the changes made by this.
# 
#     3. Turn on GitHub pages in your package repository, setting `main branch / docs folder` as the source.
#     
#     4. Oh wait, there's no step 4! 🎉

# In addition to the beautiful website, `pkgdown` automatically links to your vignette under the articles section of the website!!! 🎉🎉🎉
# 
# > #### Building your `pkgdown` site with GitHub Actions
# >
# > You can also configure a GitHub Actions workflow to automate the rebuilding of the `pkgdown` site 
# > anytime changes are pushed to your package's GitHub repository. 
# > You can do this by adding this GitHub Actions workflow file to `github/workflows`: 
# > <https://github.com/r-lib/actions/blob/v2-branch/examples/pkgdown.yaml>.
# > You can do this by locally running `usethis::use_github_action("pkgdown")` in the R console 
# > and pushing your changes to GitHub.com

# ## Publishing your Python package for this milestone:
# 
# For this course, we will publish your package on test PyPI and PyPI. You will use continuous deployment via the `ci-cd.yml` workflow file to do this.
# 
# To get your packages README and important links to show-up on the test PyPI and PyPI pages for your package, add the  following information to the [tool.poetry] table in pyproject.toml
# 
# ```
# readme = "README.md"
# homepage = "https://github.com/<github_username>/<github_repo>"
# repository = "https://github.com/<github_username>/<github_repo>"
# documentation = 'https://<package_name>.readthedocs.io'
# ```

# ## Publishing your R package for this milestone:
# 
# For this course, we will only publish your package on GitHub, not CRAN. For this to work, you need to push your package code to GitHub and provide users these instructions to download, build and install your package:
# 
# ```
# # install.packages("devtools")
# devtools::install_github("ttimbers/convertempr")
# ```
# 
# Next week we will talk about publishing on CRAN.

# ## Summary
# 
#  What did we learn today? Biggest take homes?
#  
#  - semantic versioning and automated versioning
#  
#  - how to use GitHub Actions
#  
#  - Difference between CI & CD
#  

# ## Where to next:
# 
# - Tha package indices, PyPI and CRAN
# - Peer review of data science software packages
# - Licenses

# ### Semantic versioning case study - answers
# 
# In 2008, Python bumped versions from 2.7.17 to 3.0.0. Some changes in the 3.0.0 release included:
# - `print` became a function
# - integer division resulted in creation of a float, instead of an integer
# - Some well-known APIs no longer returned lists (e.g., `dict.keys`, `dict.values`, `map`)
# - and many more (see [here](https://docs.python.org/3.0/whatsnew/3.0.html) if interested)
# 
# [*Source*](https://docs.python.org/3.0/whatsnew/3.0.html)

# In 2009, Python bumped versions from 3.0.1 to 3.1.0. Some changes in the 3.1.0 release included:
# - Addition of an ordered dictionary type
# - A pure Python reference implementation of the import statement
# - New syntax for nested with statements
# 
# [*Source*](https://www.python.org/download/releases/3.1/)

# In 2017, Python bumped versions from 3.6.3 to 3.6.4. Some changes in the 3.6.4 release included:
# 
# - Fixed several issues in printing tracebacks (`PyTraceBack_Print()`).
# - Fix the interactive interpreter looping endlessly when no memory.
# - Fixed an assertion failure in Python parser in case of a bad `unicodedata.normalize()`
# 
# [*Source*](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-4-final)

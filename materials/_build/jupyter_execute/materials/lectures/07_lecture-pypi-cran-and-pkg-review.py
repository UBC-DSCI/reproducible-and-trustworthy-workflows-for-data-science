#!/usr/bin/env python
# coding: utf-8

# # Lecture 7: Peer review of packages, and the package repositories/indices CRAN and PyPI
# 

# ## Learning objectives:
# By the end of this lecture, students should be able to:
# - Explain the advantage of using of packages that have undergone peer review
# - List the rOpenSci and PyOpenSci organizations aims and goals
# - Describe the peer review process used by the rOpenSci and PyOpenSci organizations
# - Describe the requirements for publishing packages on CRAN and PyPI
# - Explain the philosophical difference between how CRAN and PyPI gatekeep pacakges, and how this impacts the packages that are found on each repository/index

# ## [rOpenSci](https://ropensci.org/) 
# 
# ### aims and goals:
# 
# rOpenSci fosters a culture that values open and reproducible research using shared data and reusable software.

# We do this by:
# - Creating technical infrastructure in the form of carefully vetted, staff- and community-contributed R software tools that lower barriers to working with scientific data sources on the web

# - Creating social infrastructure through a welcoming and diverse community

# - Making the right data, tools and best practices more discoverable

# - Building capacity of software users and developers and fostering a sense of pride in their work

# - Promoting advocacy for a culture of data sharing and reusable software.
# 
# *Source: <https://ropensci.org/about/>*

# ### rOpenSci's open peer review process

# - Authors submit complete R packages to rOpenSci.

# - Editors check that packages fit into rOpenSci's scope, run a series of automated tests to ensure a baseline of code quality and completeness, and then assign two independent reviewers.

# - Reviewers comment on usability, quality, and style of software code as well as documentation. 

# - Authors make changes in response.

# - Once reviewers are satisfied with the updates, the package receives a badge of approval and joins rOpenSci's suite of approved pacakges.

# - Happens openly, and publicly on GitHub in issues.

# - Process is quite iterative and fast. After reviewers post a first round of extensive reviews, authors and reviewers chat in an informal back-and-forth, only lightly moderated by an editor. 
# 
# *Source: <https://numfocus.org/blog/how-ropensci-uses-code-review-to-promote-reproducible-science>*

# ###  rOpenSci's Guidance and Standards
# 
# What aspects of a package are reviewed? 

# - high-level best practices:
#     - is the code reusable (e.g. follow the DRY principle)?
#     - are sufficient edge cases tested?
#     - etc

# - low-level standards:
#     - are naming conventions for functions followed?
#     - did they make the best choices of dependencies for the package's intended tasks?
#     - etc
#     
# *Source: <https://numfocus.org/blog/how-ropensci-uses-code-review-to-promote-reproducible-science>*

# ###  rOpenSci's Review Guidebook
# 
# - <https://devguide.ropensci.org/>

# ### rOpenSci-reviewed packages:
# 
# - <https://ropensci.org/packages/>

# ### Let's look at an rOpenSci review!
# 
# All packages currently under review: <https://github.com/ropensci/software-review/issues>
# 
# - [Review of tidypmc](https://github.com/ropensci/software-review/issues/290)

# ### What do you get for having your package reviewed by rOpenSci?
# 
# - valuable feedback from the knowledgeable editors and reviewers
# - help with package maintenance and submission of your package to CRAN
# - promotion of your package on their website, blog and social media
# - packages that have a short accompanying paper can be automatically submitted to [JOSS](https://joss.theoj.org/) and fast-tracked for publication.

# ## [pyOpenSci](https://www.pyopensci.org/)
# 
# - A new organization, modelled after rOpenSci
# - scope is Python packages
# - First package submitted to pyOpenSci was in May 2019

# ### pyOpenSci's Review Guidebook
# 
# - <https://www.pyopensci.org/contributing-guide/intro.html>

# ## Practice peer review:
# 
# - MDS Open peer review: 
#     - Two years ago's cohort: <https://github.com/UBC-MDS/software-review>
#     - Last year's cohort: <https://github.com/UBC-MDS/software-review-2021>
#     - Your cohort: <https://github.com/UBC-MDS/software-review-2022>

# ### If you really enjoyed this course and the peer review...
# 
# You may want to consider getting involved with one of these organizations! Ways to get involved:
# 
# - Join the community forum [rOpensci](https://discuss.ropensci.org/) [pyOpensci](https://pyopensci.discourse.group/)
# - Virtually attend community calls! [rOpensci](https://ropensci.org/commcalls/) [pyOpensci](https://www.pyopensci.org/#community-meetings)
# - Volunteer to review packages! [rOpensci](https://ropensci.org/onboarding/) [pyOpenSci](https://forms.gle/wvwLaLQre58YLHpD6) 
# - Submit your package for review! [rOpensci](https://github.com/ropensci/software-review/#why-and-how-submit-your-package-to-ropensci) [pyOpensci](https://www.pyopensci.org/dev_guide/peer_review/aims_scope.html)

# ## CRAN
# 
# - CRAN (founded in 1997) stands for the "Comprehensive R Archive Network"
# 
# - it is a collection of sites which host identical copies of:
#     - R distribution(s)
#     - the contributed extensions (*i.e.,* packages)
#     - documentation for R
#     - binaries (i.e., packages)
# - as of 2012, there were 85 official ‘daily’ mirrors
# 
#  *Source: Hornik, K (2012). The Comprehensive R Archive Network. Wiley interdisciplinary reviews. Computational statistics. 4(4): 394-398. [doi:10.1002/wics.1212](https://onlinelibrary-wiley-com.ezproxy.library.ubc.ca/doi/full/10.1002/wics.1212)*

# > ### Binary vs source distributions, what's the difference?
# > 
# > Binary distributions are pre-compiled (computer readable), whereas source distributions have to be compiled before they are installed.
# > 
# > Precompiled binaries are often different for each operating system (e.g., Windows vs Mac)

# ### Number of packages hosted by CRAN over history
# 
# <img src="https://www.researchgate.net/publication/333159083/figure/fig1/AS:759374838517760@1558060478678/Number-of-R-packages-contributed-to-the-Comprehensive-R-Archive-Network-CRAN-as-a.png" width=800>
# 
# *Source: ["Reproducibility and Replicability in a Fast-Paced Methodological World"](https://journals.sagepub.com/doi/10.1177/2515245919847421) by Sacha Epskamp*

# ### What does it mean to be a CRAN package:
# 
# **A stamp of authenticity:**
# - passed quality control of the `check` utility
# 
# 

# **Ease of installation:**
# - can be installed by users via `install.packages` (it's actually the default!)
# - binaries available for Windows & Mac OS's
# 
# 

# **Discoverability:**
# - listed as a package on CRAN 

# **HOWEVER** - CRAN makes no assertions about the package's usability, or the efficiency and correctness of the computations it performs

# ### How to submit a package to CRAN
# 
# 1. Pick a version number.
# 2. Run and document `R CMD check`.
# 3. Check that you’re aligned with CRAN policies.
# 4. Update README.md and NEWS.md.
# 5. Submit the package to CRAN.
# 6. Prepare for the next version by updating version numbers.
# 7. Publicise the new version.
# 
# *Source: [Chapter 18 Releasing a package](https://r-pkgs.org/release.html) - R packages book by Hadley Wickham & Jenny Bryan*

# ### Notes on submitting to CRAN
# 
# - CRAN is staffed by volunteers, all of whom have other full-time jobs
# - A typical week has over 100 submissions and only three volunteers to process them all. 
# - The less work you make for them the more likely you are to have a pleasant submission experience... 

# ### Notes on submitting to CRAN (cont'd)
# 
# Technical things:
# 
# - Your package must pass `R CMD check` with the current development version of R (R-devel)
# - it must work on at least two platforms (CRAN uses the following 4 platforms: Windows, Mac OS X, Linux and Solaris) - use GitHub Actions to ensure this before submitting to CRAN!
# 
# *If you decide to submit a package to CRAN follow the detailed instructions in [Chapter 18 Releasing a package](https://r-pkgs.org/release.html) fromt the R packages book by Hadley Wickham & Jenny Bryan to do so. If you submit your package to rOpenSci, they will help you get everything in order for submission to CRAN as well!*

# ### Notes on submitting to CRAN (cont'd)
# 
# CRAN policies: <https://cran.r-project.org/web/packages/policies.html>
# 
# Most common problems (from the R packages book):
# 
# - The maintainer’s e-mail address must be stable, if they can’t get in touch with you they will remove your package from CRAN. 
# 
# - You must have clearly identified the copyright holders in DESCRIPTION: if you have included external source code, you must ensure that the license is compatible.
# 
# - Do not make external changes without explicit user permission. Don’t write to the file system, change options, install packages, quit R, send information over the internet, open external software, etc.
# 
# - Do not submit updates too frequently. The policy suggests a new version once every 1-2 months at most.

# ### If your submission fails:
# 
# Read section 18.6.1 "On failure" from  [Chapter 18 Releasing a package](https://r-pkgs.org/release.html) - R packages book by Hadley Wickham & Jenny Bryan*
# 
# TL;DR - Breathe, don't argue, fix what is needed and re-submit.

# ## PyPI
# 
# - should be pronounced like "pie pea eye"
# - also known as the Cheese Shop (a reference to the Monty Python's Flying Circus sketch "Cheese Shop")

# In[12]:


from IPython.display import YouTubeVideo
YouTubeVideo('zB8pbUW5n1g')


# Don't get the joke? I didn't either without historical context. When PyPI was first launched it didn't have many Python packages on it - similar to a cheese shop with no cheese 😆

# ### the Cheese Shop (er, PyPI)
# 
# - PyPI (founded in 2002) stands for the "Python Package Index"
# 
# -  hosts Python packages of two different forms:
#     - sdists (source distributions)
#     - precompiled "wheels (binaries)
# - heavily cached and distributed
# - currently contains > 9000 projects

# ### Number of packages hosted by PyPI over history
# 
# <img src="https://www.researchgate.net/profile/Marat_Valiev2/publication/328595587/figure/fig1/AS:687258193633280@1540866530197/Number-of-new-PyPI-packages-per-month.png" width=800>
# 
# *Source: ["Ecosystem-level determinants of sustained activity in open-source projects: a case study of the PyPI ecosystem"](https://dl.acm.org/doi/10.1145/3236024.3236062) by  Marat Valiev, Bogdan Vasilescu & James Herbsleb*

# ### What does it mean to be a PyPI package:
# 
# **Ease of installation:**
# - can be installed by users via `pip install` (it's actually the default!)
# - universal binaries available for packages that are written solely in Python

# **Discoverability:**
# - listed as a package on PyPI

# HOWEVER, there is no required check for your package is required to pass... As long as you can bundle it as something that PyPI recognizes as an sdist or wheels then it can go on PyPI... This allows the process to be fully automated, but QC is lower than it is for CRAN.

# ### How to submit a package to PyPI
# 
# - use `poetry build` to build your package to both a sdist & universal wheels format 
# 
# - use `poetry publish -u <USERNAME> -p <PASSWORD>` to publish your package to PyPI
# 
# > Note 1: to publish to PyPI there is no need to specift the repository because it is the default.
# >
# > Note 2: you can now use a token to authenticate when you publish to PyPI and test PyPI, see [these docs](https://pypi.org/help/#apitoken) for more details on how. This is now the recommeded method over using a username and password (more secure).

# ### Points for discussion 
# 
# - Is one model better or worse? 
# 
# - Importance & complimentarity of organizations like rOpenSci & pyOpenSci with CRAN and PyPI, respecitively

# ### Where to next?
# - licenses

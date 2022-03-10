#!/usr/bin/env python
# coding: utf-8

# # Reproducible reports

# ## Topic learning objectives
# 
# By the end of this topic, students should be able to:
# 
# 1. Discuss the advantages and disadvantages of using literate code documents (e.g.,
# Jupyter, R Markdown) for writing analytic reports compared to What You See Is
# What You Get (WYSIWYG) editors (e.g., Word, Pages)
# 2. Compare and contrast the different implementations for literate code documents (e.g.,
# Jupyter and R Markdown) and discuss where some implementations shine with
# regards to reproducibility of data analysis and where there is still room for
# improvement
# 3. Execute and render literate code documents
# 4. Generate tables of contents, label and number figures and tables, and format
# bibliographies in a reproducible and automatted manner

# ## Reproducible reports vs What You See Is What You Get (WYSIWYG) editors
# 
# Reproducible reports are reports where automation is used to update a report when changes to data or data analysis methods lead to changes in data analysis artifacts (e.g., figures, tables, inline text values). This automation is usually specified and controlled by code. In the field of data science, the most common implementations of this are: 
# 
# - R Markdown
# - Jupyter
# - LaTeX 
# 
# > Note: R Markdown and Jupyter are not completely separable from LaTeX, as they both wrap LaTeX when the desired output is PDF.
# 
# Most implementations of reproducible reports involve a process called rendering, where a document containing code and/or markup language used to specify the text formatting, document layout, figure and table placement and numbering, bibliography formatting, *etc*, is converted to an output more suitable for consumption (e.g., beautifully formatted PDF or html document) by some software.
# 
# <img src="img/render-report/render-report.png" width=700>
# 
# This contrasts from What You See Is What You Get (WYSIWYG) software or editors (e.g., Microsoft Word, Google Docs, etc), where the document that is being edited looks exactly like the final document - there is no rendering process. WYSIWYG reports are typically easier to get started with and use. However, they are usually quite limited in their ability to automatically update a report when changes to data or data analysis methods lead to changes in data analysis artifacts. This makes them less reproducible, and can lead to errors when repeated manual updating of data analysis artifacts is needed when analysis is iterated on during development. 
# 
# <img src="img/word.png" width=300>

# ## R Markdown
# 
# R Markdown is one implementation of a reproducible reporting tool.
# It is very user friendly and has become very powerful -
# allowing a great deal of control over formatting 
# with the ability to render to many different outputs. 
# Including:
# - PDF
# - html
# - Word
# - Powerpoint presentation
# - many more!
# 
# It is a mix of markdown primarily used for narrative text,
# and code chunks where code can be executed in an engine.
# It was originally created for the R programming language,
# but can be used with several others, including Python.
# 
# #### Exercise - get to know R Markdown
# 
# Let's get to know R Markdown! Open RStudio and create a new R Markdown document, choosing HTML as the output format. 
# Look at the source document that is created, where is the narrative text written? Where is the code written? How does this differ from Jupyter?
# 
# #### Exercise - render your first document
# 
# There are two ways to render a document from the Rmd source to the desired output. One is using a button in RStudio - the knit button that looks like this:
# 
# <img src="img/knit.png" width=90>
# 
# Try clicking that button and see what happens!
# 
# Another way you can do this is through code! Try running this in the R console (replacing `"FILEPATH/FILE.Rmd"` with the file path to where you saved this R Markdown document:
# 
# ```
# rmarkdown::render("FILEPATH/FILE.Rmd", output_format = "html_document")
# ```
# 
# #### Exercise - checkout the new visual markdown editor
# 
# RStudio has implemented a new feature for working with R Markdown to make it more similar to working with Jupyter - it is called the visual markdown editor. Checkout this feature by clicking the visual markdown editor button when you have an R Markdown file open in the editor. The button looks like this:
# 
# <img src="img/viz-md-button.png" width=50>

# ### A helpful hint for successfully working with R Markdown documents
# 
# Given that you need to render the entire document to see your Markdown and LaTeX rendered,
# it is important to "knit" often as you make changes.
# If you make an error in a LaTeX equation for example,
# it will stop the knitting/rendering process
# and you will not get to see the rendered document.
# So by knitting/rendering often
# you will know where the last changes you made are
# and then will be able to easily identify and fix your errors.

# ### Running, editing and creating code chunks
# 
# Just like Jupyter notebooks,
# R Markdown has code cells,
# although they're more commonly referred to as code "chunks" or "blocks".
# These are based off fenced Markdown code blocks
# and always start and end with 3 backticks (\`\`\`),
# just like in Markdown.
# Unique to R Markdown
# is that the leading three backticks are followed by curly braces
# containing the language engine you want to run,
# which for r looks like this `{r}`.
# Additional metadata can be included,
# for example a name to reference the code chunk:
# 
# ````
# ```{r my first code chunk}
# x <- 5
# x
# ```
# ````
# 
# There are other language engines that can be used in RMarkdown,
# you can learn more about that [here](https://bookdown.org/yihui/rmarkdown/language-engines.html).
# 
# All code cells are run when you knit/render the entire document
# (like pressing "Run all" in JupyterLab).
# By default,
# the code in the chunk and the code output will be included in your rendered document.
# You can also run the code by clicking the green play button on the right-hand side of the code chunk.

# ### Naming code chunks and R Markdown document sections
# 
# When you include Markdown headers
# (using the `#` symbol)
# R Studio automatically creates a pop-up-like menu
# for you to use to navigate the document,
# which you can access
# by clicking the bar below this editor panel.
# It looks like:
# 
# <img src="img/menu0.png" width=500>
# 
# <img src="img/menu1.png" width=500>
# 
# By clicking on any of the headings in the pop-up-like menu,
# RStudio will navigate you to that section of the R Markdown document.
# Try clicking on one to see how it works.
# 
# In addition to Markdown headings,
# RStudio also keeps track of code chunks in that menu.
# By default RStudio names the chunks by their position
# (e.g. Chunk 1, Chunk 2, etc).
# But in reality those names are not that useful
# and it is more helpful to give code chunks meaningful names.
# For example,
# in the code chunk below where we use a for loop to sum the numbers from 1 to 10,
# we name the chunk "for-loop-sum".
# 
# ````R
# ```{r for-loop-sum}
# # initialize sum to 0
# loop_sum <- 0
# 
# # loop of a sequence from 1 to 10 and calculate the sum
# for (i in seq(1:10)){
#   loop_sum <- loop_sum + i
# }
# 
# print(loop_sum)
# ```
# ````
# 
# **Do not duplicate code chunk names,
# this will break the rendering of your document!**

# ### Code chunk options
# 
# There are many code chunk options that you can set.
# These options let you customize chunk behavior,
# including whether a chunk is evaluated,
# whether to include the output in the rendered document,
# etc.
# A short list of code chunk options is shown below,
# but you can find an extensive list starting on the second page of
# [this](https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf) document.
# 
# <img src="img/chunk_options.jpeg" width=500>
# 
# You can set the chunk options at either a global level
# (once set they will be applied to all code chunks in the `.Rmd` file)
# or locally for a specific chunk
# (these will override the global chunk options if they are contradictory).
# 
# Global options are usually set in one chunk at the top of the document
# and looks like this (this is a screenshot):
# 
# ````r
# ```{r setup, include=FALSE}
# knitr::opts_chunk$set(echo = FALSE)
# ```
# ````
# 
# Global chunk options are set by adding them as arguments to `knitr::opts_chunk$set(...)`
# (put them in place of `...` and separate multiple options with a comma).
# The only global chunk options set in this document is `echo = FALSE`,
# which hides the code chunks and only shows the output,
# something that can be useful for non-technical reports.
# 
# Local chunk options are set by adding the options in the curly braces of a code chunk
# after the language engine and code chunk name.
# For example,
# to not display warnings in a single code chunk
# we would use the `warning = FALSE` code chunk as follows:
# 
# ````r
# ```{r correlation no warning, warning = FALSE}
# # some R code that throws a warning
# cor( c( 1 , 1 ), c( 2 , 3 ) )
# ```
# ````

# > ### A few tips and tricks
# > 
# > - R Markdown support inline evaluated code via the following syntax
# >     ```
# >     Adding 3 to 4 gives `r 4 + 3`.
# >     The value of `x` is currently `r x`.
# >     ```
# > - Latex equations can be written the same way as in Jupyter notebooks
# >   and standard markdown documents.
# >       - `$\alpha = 5$` for inline latex and `$$\alpha = 5$$` for a math block.
# >       - When hovering over equations,
# >         R will display the rendered equation in a pop up.
# > - R Markdown is built upon the Pandoc Markdown engine.
# >   This is useful to know since the [Pandoc manual](https://pandoc.org/MANUAL.html)
# >   is a great exhaustive resource for looking up anything Markdown related.
# > - One of the features made available thanks to Pandoc
# >   is support for citations and bibliographies.
# >     - Let's cite the R-package by typing `citation()` into the console,
# >       and copying the BibTex citation into a new document
# >       that we call `rstudio-demo.bib 
# >       and adding an identifier string (a key) before the first comma,
# >       e.g. `r-lang`.
# >     - Include the following field in the YAML metadata
# >       in the beginning of the document: `bibliography: rstudio-demo.bib`,
# >       then cite it somewhere in the text by adding `[@r-lang]`.
# >       The bibliography will be appended to the document,
# >       so it is advisable to add a heading saying `# References`
# >       at the very end.
# > - When working with R Markdown
# >   (and code in general)
# >   be careful that you don't copy stylized quotation marks
# >   because these will not work.
# >   For example, this will throw an error:
# >   ```
# >   a = “This string”
# >   ```
# >   
# >   It should look like this instead:
# >   
# >   ```
# >   a = "This string"
# >   ```

# ### Creating a table of contents
# 
# A table of contents can be automatically generated by specifying `toc: true` in the YAML front matter. It must be indented as so:
# 
# ```
# output: 
#   github_document:
#     toc: true
# ```
# 
# This works for all output file types I have explored so far!

# ### Create tables and table descriptions
# 
# Data frames and other rectangular objects in R can be made into nice tables using `knitr::kable`. At the most basic level the syntax is:
# 
# ```knitr::kable(data_frame)```
# 
# To have a table description stay associated with the table, use the `caption` argument. For example:
# 
# ```knitr::kable(data_frame, caption = "Table 1. This is a summary of the data set")```
# 
# A couple notes:
# - If you render to `github_document` or `html_document` you do need to manually write the "Table 1." in your figure caption. If you render to `pdf_document` you do not.
# - Want fancier tables? Use the `kableExtra` package! See docs here: https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html
# 

# ### Resize figures and keep figure descriptions associated with their figures
# 
# There are two ways to do this, and you they depend on whether you are creating the figure from an R object vs a file.
# 
# #### 1. Resizing figures and writing figure captions generated from an R plot object
# 
# Here you need to:
# - `fig.width=<WIDTH>, fig.height=<HEIGHT>` in the R code chunk options.
# - `fig.cap = "CAPTION"` in the R code chunk options. 
# 
# #### 2. Resizing figures and writing figure captions generated from a saved file (e.g., .png) 
# 
# Here you need to:
# - use `knitr::include_graphics(<FILE_PATH>)` inside a code chunk to point the figure file
# - `fig.cap` in the R code chunk options to write the figure caption
# - use `out.width = '40%'` and `out.height = '40%'` in the R code chunk options to set the figure size. 

# ### Referencing values from code inline in the narrative text
# 
# You can refer to values stored in code inside your markdown text using the `r object` surrounded by backticks.
# 
# This is extremely useful for iterating over an analysis near the final stages when you already have the report written, or when doing parameterized reports (more on these in a bit). 
# 
# However, the value you represent must be a vector.

# ### Create a references section for citing external sources
# 
# DO NOT format references by hand, you will drive yourself nuts, especially the more references you collect! Instead use R Markdowns bibliography/citiation functionality. Below is a brief introduction, full docs [here](https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html).
# 
# #### Steps to citing in R Markdown
# 1. Add `bibliography: PATH/FILENAME.bib` to the YAML front matter
# 
# 2. At the very end of the `.Rmd` file add `# References`
# 
# 3. Create `PATH/FILENAME.bib` (this is a plain text file) and place citations in there using bibtex citation format (see examples [here](https://www.economics.utoronto.ca/osborne/latex/BIBTEX.HTM)).
# 
# 4. In the `.Rmd` mardown text, use `@label` (corresponds to the first string inside the `{}` in the `.bib` file for the reference of interest) to do a in-text citation.
# 
# #### Getting bibtex citations
# 
# Bibtex citations for code (R & Python programming languages and their respective packages) can be obtained from the sources:
# - `citatation()` function in R (no argument will give you the citation for R, adding a package name as a string to the function call will give you the citation for that package)
# - For Python, I have found I have had to do this somewhat manually from package GitHub repos or docs pages (some packages exist to do this, but none seem to work flawlessly out of box). See my demo `.bib` file here for an example: https://github.com/ttimbers/breast_cancer_predictor/blob/master/doc/breast_cancer_refs.bib
# 
# Bibtex citations for papers can usually be found via Google scholar:
# 
# #### 1. Search for the paper on Google Scholar
# - visit https://scholar.google.com/
# 
# #### 2. Use Goolge Scholar to get the citation
# - Click on the quotation icon under the paper:
# 
# ```{figure} img/google_scholar_step_1.png
# ---
# width: 600px
# name: google_scholar_step_1
# align: left
# ---
# ```
# 
# - Click on the Bibtex link on the pop-up box:
# 
# ```{figure} img/google_scholar_step_2.png
# ---
# width: 600px
# name: google_scholar_step_2
# align: left
# ---
# ```
# 
# - Copy the BibTeX citation to your .bib file
# ```
# @article{ahmad2007k,
#   title={A k-mean clustering algorithm for mixed numeric and categorical data},
#   author={Ahmad, Amir and Dey, Lipika},
#   journal={Data \& Knowledge Engineering},
#   volume={63},
#   number={2},
#   pages={503--527},
#   year={2007},
#   publisher={Elsevier}
# }
# ```

# Note: The Zotero reference manager now works nicely with R Markdown too! You might want to try this for your project, see here: <
# <https://www.rstudio.com/blog/rstudio-1-4-preview-citations/#citations-from-zotero>

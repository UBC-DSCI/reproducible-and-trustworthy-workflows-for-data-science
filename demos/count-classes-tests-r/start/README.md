# Counting the observations in each class

This is the starting point for writing a tested function for a data analysis.

The analysis in `notebooks/eda.qmd` counts the observations in each class
of the Wisconsin Breast Cancer data set.
We count classes like this in almost every classification problem,
so we will move that code into a function, `count_classes()`, in `R/count_classes.R`,
and write tests for it in `tests/testthat/`.

## Set up

Restore the R packages this project uses with renv:

```bash
Rscript -e 'renv::restore(prompt = FALSE)'
```

Then render the analysis
(it needs the Quarto CLI, and internet access to download the data):

```bash
quarto render notebooks/eda.qmd
```

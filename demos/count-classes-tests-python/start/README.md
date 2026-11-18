# Counting the observations in each class

This is the starting point for writing a tested function for a data analysis.

The analysis in `notebooks/eda.qmd` counts the observations in each class
of the Wisconsin Breast Cancer data set.
We count classes like this in almost every classification problem,
so we will move that code into a function, `count_classes`, in `src/count_classes.py`,
and write tests for it in `tests/`.

## Set up

Create the project's environment with uv:

```bash
uv sync
```

Then render the analysis
(it needs the Quarto CLI, and internet access to download the data):

```bash
uv run quarto render notebooks/eda.qmd
```

To run it chunk by chunk instead,
open `notebooks/eda.qmd` in VS Code or Positron with the project's `.venv` as the Python interpreter.

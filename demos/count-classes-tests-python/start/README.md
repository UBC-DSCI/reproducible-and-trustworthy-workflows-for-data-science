# Counting the observations in each class

This is the starting point for writing a tested function for a data analysis.

The analysis in `notebooks/eda.ipynb` counts the observations in each class
of the Wisconsin Breast Cancer data set.
We count classes like this in almost every classification problem,
so we will move that code into a function, `count_classes`, in `src/count_classes.py`,
and write tests for it in `tests/`.

## Set up

Create the project's environment with uv:

```bash
uv sync
```

Then open `notebooks/eda.ipynb` in VS Code or Positron with the project's `.venv` as the kernel,
or start JupyterLab with `uv run --with jupyterlab jupyter lab`.

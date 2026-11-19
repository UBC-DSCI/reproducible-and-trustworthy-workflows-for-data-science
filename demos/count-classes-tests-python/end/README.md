# Demo of tests for functions used in data analysis

This repository shows how to set up unit tests
for functions that are used in a data analysis.
This is one step away from making a Python package.

The demo data analysis is in `notebooks/eda.qmd`.
It calls a function, `count_classes`,
which lives in `src/count_classes.py`
and calculates the number of observations in each class of a data set.

The tests for `count_classes`, and the code that makes their test data,
live in `tests/test_count_classes.py`.
`pytest` only looks for tests in files whose names start with `test_`
or end with `_test.py`.

## Run the tests

Create the project's environment with uv, then run the tests:

```bash
uv sync --locked
uv run pytest
```

To render the analysis
(it needs the Quarto CLI, and internet access to download the data):

```bash
uv run quarto render notebooks/eda.qmd
```

This writes `notebooks/eda.html`.
To run it chunk by chunk instead,
open `notebooks/eda.qmd` in VS Code or Positron with the project's `.venv` as the Python interpreter.

## Dependencies

Python 3.14 and the packages in `pyproject.toml`
(pandas, and for development ipykernel, Jupyter and PyYAML for Quarto, NumPy and pytest),
locked in `uv.lock`.

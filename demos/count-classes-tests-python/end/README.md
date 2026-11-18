# Demo of tests for functions used in data analysis

This repository shows how to set up unit tests
for functions that are used in a data analysis.
This is one step away from making a Python package.

The demo data analysis is in `notebooks/eda.ipynb`.
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

To run the notebook (it needs internet access to download the data),
open `notebooks/eda.ipynb` in VS Code or Positron with the project's `.venv` as the kernel,
or start JupyterLab with `uv run --with jupyterlab jupyter lab`.

## Dependencies

Python 3.14 and the packages in `pyproject.toml`
(pandas, and for development ipykernel, NumPy and pytest),
locked in `uv.lock`.

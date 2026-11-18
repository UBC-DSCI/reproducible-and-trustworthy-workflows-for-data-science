# count-classes-tests-python

First pass, to be reviewed when taught.

This demo walks through the test-driven workflow for a function
that a data analysis uses,
without making a Python package.
The function, `count_classes()`, counts the observations in each class of a pandas DataFrame.
It lives in `src/`,
its tests and their test data live in `tests/test_count_classes.py`,
`pytest` runs the tests,
and the analysis notebook imports the function.

It is used by
[Testing: Python (pytest)](../../book/lectures/1030-testing-python-pytest.qmd),
in the section "Where do the function and test files go?".
The R version is [count-classes-tests-r](../count-classes-tests-r/).

Adapted from Tiffany Timbers' <https://github.com/ttimbers/demo-tests-ds-analysis-python>.
The function, test data and tests here follow the chapter,
which has moved on from that repository.

## What is in it

- `start/` is a uv project with the analysis notebook `notebooks/eda.ipynb`,
  which counts the classes inline with pandas.
  It has no `src/` or `tests/` folder and no pytest yet.
- `end/` adds the function in `src/count_classes.py`
  and the test data and tests in `tests/test_count_classes.py`.
  The notebook imports the function instead of counting inline.

## Live coding from `start/` to `end/`

Copy `start/` out of this repository and run `git init` in it.
The numbered steps match the chapter's five steps.

0. Run `uv sync`.
1. Create `src/count_classes.py`
   and write the function's specification and docstring
   with an empty body (`pass`).
2. Run `uv add --dev pytest numpy`
   (the test data uses NumPy's random numbers).
   Create `tests/test_count_classes.py`.
   At the top, import the function from `src/` with the `sys.path` lines,
   then write three empty test functions
   (expected use, edge cases, errors).
   The file name must start with `test_`,
   or `pytest` will not find it.
3. Write the code that makes the test data at the top of the test file.
4. Fill in the `assert` statements and `pytest.raises()`,
   and run `uv run pytest`.
   All three tests fail.
5. Write the function body and run `uv run pytest` again.
   All three pass.
6. In `notebooks/eda.ipynb`, import the function
   (`sys.path.append('..')`, then `from src.count_classes import count_classes`)
   and replace the inline counting with `count_classes(cancer, 'Class')`.

## Run `end/`

From this folder:

```bash
cd end
uv sync --locked
uv run pytest
```

The last line of the output is `3 passed`.

To run the notebook (it needs internet access to download the data),
open `notebooks/eda.ipynb` in VS Code or Positron with the project's `.venv` as the kernel,
or start JupyterLab with `uv run --with jupyterlab jupyter lab`.

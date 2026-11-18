# `pycounts` demo: building, testing and releasing a Python package with uv

First pass, to be reviewed when taught.

`pycounts` is a small Python package that counts the words in a text file and plots them.
The class builds it with uv from an empty `uv init --package` skeleton,
tests it with pytest, measures its coverage,
and sets up GitHub Actions to test and release it.
Along the way it gains `count_char()` and `count_letters()`,
the functions the testing chapter writes with test-driven development.

It is used in these chapters:

- [Introduction to R & Python packages](../../book/lectures/1110-packaging.qmd),
  in the "Tour de Python packages" list;
- [Packaging: Python](../../book/lectures/1120-packaging-python.qmd),
  for the essential package files;
- [Package testing: Python (pytest)](../../book/lectures/1210-package-testing-python-pytest.qmd),
  for `count_char()`, `count_letters()` and their tests;
- [Package coverage: Python](../../book/lectures/1220-package-coverage-python.qmd);
- [Case study: Python CI workflow](../../book/lectures/1350-github-actions-case-study-python.qmd)
  and [Deploying and publishing packages](../../book/lectures/1510-continuous-deployment.qmd),
  for the `ci-cd.yml` workflow.

The Poetry chapters,
[Packaging: Python (Poetry)](../../book/lectures/1140-packaging-python-poetry.qmd)
and [Continuous deployment: Python (Poetry)](../../book/lectures/1520-continuous-deployment-python-poetry.qmd),
also use `pycounts`,
but they are moving to the book's Archive and this demo does not follow them.

## Where it came from

Adapted from Tiffany Timbers' <https://github.com/ttimbers/pycounts_tt25>
and <https://github.com/ttimbers/pycounts_tt_2024>,
which were made with the [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter)
and Poetry.
Both are licensed MIT by Tiffany Timbers.
The package itself is the example in [Python Packages](https://py-pkgs.org/)
by Tomas Beuzen and Tiffany Timbers.
`count_char()`, `count_letters()` and their tests come from the 1210 chapter,
where they make up a separate package called `countchar`.

## What is here

- `start/` is exactly what `uv init --package --python 3.14 --author-from none pycounts` creates:
  `pyproject.toml` (with uv's `uv_build` build backend),
  `src/pycounts/__init__.py` (a `main()` that prints "Hello from pycounts!"),
  an empty `README.md`, `.python-version` (3.14) and `.gitignore`.
  It has no `uv.lock` yet; the first `uv run` or `uv sync` creates it.
- `end/` is the finished package:
  - `src/pycounts/pycounts.py` (`load_text()`, `clean_text()`, `count_words()`),
    `src/pycounts/plotting.py` (`plot_words()`),
    `src/pycounts/count_char.py` and `src/pycounts/count_letters.py`;
  - `src/pycounts/__init__.py`, which sets `__version__`
    and puts `count_words()` and `plot_words()` in the package namespace;
  - `tests/` with a test file per module, a shared fixture in `conftest.py`,
    and the data files `einstein.txt` and `text.txt`;
  - `pyproject.toml` declaring `matplotlib`, a `dev` group with `pytest` and `pytest-cov`,
    and a `[tool.semantic_release]` table, locked in `uv.lock`;
  - `.github/workflows/ci-cd.yml`, which runs only once `end/` is its own GitHub repository
    (see [Continuous integration and deployment](#continuous-integration-and-deployment)).

## Making your own copy

Each student copies `start/` into a repository of their own.
From the root of this repository, in a terminal (Git Bash on Windows):

```bash
cp -R demos/pycounts/start ~/pycounts
cd ~/pycounts
git init -b main
git add .
git commit -m "Initial commit"
```

Or let uv make the folder.
`uv init --package --python 3.14 pycounts` creates a `pycounts/` folder with the same files
and runs `git init` in it,
except that uv fills in `authors` from your Git name and email.

## Live coding, from `start/` to `end/`

The steps follow the chapters in order,
and each stage can be taught on its own.
Copy any file you do not want to type from `end/`.

### Packaging ([1110](../../book/lectures/1110-packaging.qmd) and [1120](../../book/lectures/1120-packaging-python.qmd))

1. Tour `start/` against the chapter's list of essential files
   (`pyproject.toml`, `src/pycounts/__init__.py`),
   and run `uv run pycounts` to see "Hello from pycounts!".
2. Delete the `main()` stub from `src/pycounts/__init__.py`
   and the `[project.scripts]` table from `pyproject.toml`,
   and give the project a real `description`.
3. Write `src/pycounts/pycounts.py` with `load_text()`, `clean_text()` and `count_words()`,
   and try it on the Zen of Python, as the Python Packages book does:

   ```bash
   uv run python -c "import this" > zen.txt
   uv run python -c "from pycounts.pycounts import count_words; print(count_words('zen.txt'))"
   ```
4. `uv add matplotlib`, then write `src/pycounts/plotting.py` with `plot_words()`.
5. Put `__version__`, `count_words()` and `plot_words()` in `src/pycounts/__init__.py`,
   so that `import pycounts` then `pycounts.count_words` works.
6. `uv add --dev pytest`,
   add `tests/einstein.txt`, `tests/test_pycounts.py` and `tests/test_plotting.py`,
   and run `uv run pytest`.

### Testing ([1210](../../book/lectures/1210-package-testing-python-pytest.qmd))

1. Create `src/pycounts/count_char.py` with the docstring and `pass` as its body,
   and `tests/test_count_char.py` with `test_count_char()`.
   `uv run pytest` fails with `assert None == 5`.
2. Make the function `return len(input_string)`, and the test passes.
   Swap in the `for` loop version to show the test still passes.
3. Add the `isinstance()` check that raises `TypeError`,
   and `test_count_char_wrong_input()` with `pytest.raises()`.
4. Add `tests/text.txt` and one test per line,
   then replace the repeated file reading with the `text_data` fixture,
   then the three tests with one `@pytest.mark.parametrize` test.
5. Add `src/pycounts/count_letters.py` and `tests/test_count_letters.py`,
   and move the `text_data` fixture into `tests/conftest.py` so both test files share it.

### Coverage ([1220](../../book/lectures/1220-package-coverage-python.qmd))

1. `uv add --dev pytest-cov`.
2. `uv run pytest --cov=pycounts` for line coverage,
   `uv run pytest --cov=pycounts --cov-branch` for branch coverage,
   and `uv run pytest --cov=pycounts --cov-report html` for a report in `htmlcov/`.
   With every test in `end/`, coverage is 100%.
   Comment out `test_count_char_wrong_input()` to show the `raise` line as missed
   and its branch as partly covered.

### Continuous integration and deployment ([1350](../../book/lectures/1350-github-actions-case-study-python.qmd) and [1510](../../book/lectures/1510-continuous-deployment.qmd))

1. Add `.github/workflows/ci-cd.yml` and the `[tool.semantic_release]` table in `pyproject.toml`
   from `end/`.
2. Push to GitHub and watch the `ci` job run.
3. Set up the secrets, rename the package, and make a conventional commit
   (see the next section) to watch the `cd` job release it.

## Running `end/`

From a terminal, in `demos/pycounts/end/`:

```bash
uv sync --locked
uv run pytest
uv run pytest --cov=pycounts --cov-branch
uv build
```

`uv run pytest` reports `10 passed`,
the coverage run reports 100% line and branch coverage,
and `uv build` writes `pycounts-0.1.0.tar.gz` and `pycounts-0.1.0-py3-none-any.whl` to `dist/`.

## Continuous integration and deployment

`end/.github/workflows/ci-cd.yml` only runs once `end/` is copied out into its own GitHub repository.
It has the same two jobs as the `py-pkgs-cookiecutter` workflow the chapters read,
with uv in place of Poetry:

- `ci` runs on every push and pull request.
  It installs the package with `uv sync --locked`,
  runs the tests with coverage, and sends the report to Codecov.
- `cd` runs only after `ci` passes on a push to `main`.
  Python Semantic Release reads the conventional commit messages since the last release,
  bumps the version in `pyproject.toml`,
  and runs the `build_command` from `pyproject.toml`,
  which updates `uv.lock` to the new version (otherwise the next `uv sync --locked` fails)
  and builds the package.
  It then commits, tags, and creates a GitHub release.
  The job publishes to TestPyPI, installs the new version back from TestPyPI,
  publishes to PyPI, and attaches the built files to the GitHub release.

Before the `cd` job can publish:

1. Add the repository secrets `TEST_PYPI_API_TOKEN` and `PYPI_API_TOKEN`
   (and `CODECOV_TOKEN` for Codecov), as in the 1520 chapter.
2. Rename the package, because `pycounts` is already taken on PyPI.
   The quickest way, which keeps `import pycounts` working,
   is to change `name` in `pyproject.toml` (for example to `pycounts-<your initials>`),
   add the table below to `pyproject.toml`,
   change `version(__name__)` in `src/pycounts/__init__.py` to `version("pycounts-<your initials>")`,
   change `pycounts==$VERSION` in the workflow's "Test install from TestPyPI" step to the new name,
   and run `uv lock`.

   ```toml
   [tool.uv.build-backend]
   module-name = "pycounts"
   ```
3. If `main` is protected, the release commit cannot be pushed with the default `GITHUB_TOKEN`.
   Use a personal access token in a `RELEASE_TOKEN` secret instead,
   as the 1520 chapter describes,
   in the `token:` of the `cd` job's checkout step and in its `GH_TOKEN` variables.

The workflow has not been run on GitHub yet.
The Python Semantic Release configuration was tested locally in a scratch Git repository.
There, a `feat:` commit releases `0.1.0` and the next `feat:` commit bumps it to `0.2.0`,
and after a bump `uv.lock` records the new version and `uv sync --locked` passes.

## Changes from the source repositories

- uv replaces Poetry.
  `pyproject.toml` uses the standard `[project]` table instead of `[tool.poetry]`,
  `[dependency-groups]` instead of `[tool.poetry.group.dev.dependencies]`,
  and the `uv_build` backend instead of `poetry-core`.
  `uv.lock` replaces `poetry.lock`,
  and `.python-version` pins Python 3.14 (`requires-python = ">=3.14"`, as `uv init` writes it;
  the sources allowed Python 3.11 or 3.9 and up).
- `start/` is the output of `uv init --package` instead of the `py-pkgs-cookiecutter`,
  so there is no `docs/`, `CHANGELOG.md`, `CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE` or `.readthedocs.yml`.
  The Sphinx documentation and its Read the Docs configuration (which installs Poetry) are left out of `end/` as well.
- The package is called `pycounts`, not `pycounts_tt25` or `pycounts_tt_2024`.
- `plot_words()` returns the bar container, as in `pycounts_tt_2024` and the Python Packages book,
  matching its docstring; `pycounts_tt25` returned `plt.gcf()`.
  `tests/test_plotting.py` checks the type and number of bars, as the Python Packages book does,
  instead of `pycounts_tt25`'s `pytest-mpl` image comparison with a baseline PNG.
- Development dependencies are only `pytest` and `pytest-cov`.
  The sources also declared `jupyter`, `myst-nb`, Sphinx themes and extensions,
  `pytest-mpl` and `python-semantic-release`,
  and `pycounts_tt25` declared `wordcloud`, which it never imported.
- `count_char()`, `count_letters()`, `tests/conftest.py`, `tests/text.txt` and their tests are new,
  from the 1210 chapter, as modules of `pycounts` instead of a `countchar` package.
  `tests/test_count_char.py` keeps all three of the chapter's tests
  (the examples, the `TypeError` check and the parametrized lines);
  the chapter's final listing shows only the parametrized one.
- `tests/einstein.txt` is the one from `pycounts_tt_2024`
  (`pycounts_tt25`'s has stray spaces in the middle).
  `zen.txt` is left out.
- The workflow uses `astral-sh/setup-uv`, `uv sync --locked`, `uv run` and `uv publish`
  instead of Poetry and `pypa/gh-action-pypi-publish`,
  runs Python Semantic Release 10.7.0 through `uvx`
  instead of its v8.3.0 GitHub Action (whose container has no uv to run the `build_command`),
  sets a Git user for the release commit,
  drops the documentation build step,
  and moves `actions/checkout` and `codecov/codecov-action` to v7.
  It uses `GITHUB_TOKEN`, like the `py-pkgs-cookiecutter`,
  instead of the sources' `RELEASE_TOKEN`.
- `[tool.semantic_release]` points at `project.version`,
  sets `allow_zero_version = true` so releases stay at 0.x as in the sources
  (Python Semantic Release 10 otherwise makes the first release 1.0.0),
  and re-locks before building.
  The sources' `branch` and `changelog_file` settings are dropped,
  because version 10's defaults (`main`, `CHANGELOG.md`) are the same.

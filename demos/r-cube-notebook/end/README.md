# r-cube-notebook

Practice repository for resolving merge conflicts in Jupyter notebooks.

## Instructions

1. On GitHub, click the Actions tab,
   and then click on the workflow .github/workflows/main.yml.
   You should see a "Run workflow" button with a drop-down menu.
   From that menu, select "Run workflow"
   (this triggers GitHub Actions to create a commit in your remote repository).

2. Locally on your computer, fix the second line in the code cell in `cube.ipynb`
   so that it calculates the cube, not the square
   (e.g., change `x^2` to `x^3`).
   Commit your changes to version control via Git and push your changes to GitHub.

3. Resolve the merge conflict so that you can see your changes on GitHub.

## Running `cube.ipynb`

This copy also carries an environment for running the notebook,
which is not part of the exercise:
JupyterLab from `pyproject.toml` and `uv.lock` (uv),
and the R kernel, IRkernel, from `DESCRIPTION` and `renv.lock` (renv).
From a terminal, in this folder:

```bash
uv sync --locked
Rscript -e 'renv::restore(prompt = FALSE)'
uv run Rscript -e 'IRkernel::installspec(user = FALSE, sys_prefix = TRUE)'
uv run jupyter lab
```

The third line registers the R kernel inside `.venv/` only.
Then open `cube.ipynb` and run all cells; the last one prints `8`.

## Credits

Adapted from Tiffany Timbers' <https://github.com/ttimbers/r-cube-notebook>.

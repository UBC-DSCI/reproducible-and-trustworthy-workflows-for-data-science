# `r-cube-notebook` demo: resolving a merge conflict in a Jupyter notebook

First pass, to be reviewed when taught.

The same exercise as the [`r-cube`](../r-cube/) demo, with a Jupyter notebook in place of an R script.
`cube.ipynb` (R kernel) defines a `cube()` function that squares instead of cubing,
and its last cell shows `cube(2)` as `4`.
A GitHub Actions workflow, run by hand, plays a collaborator
who pushes one fix (`x * x * x`, with the output changed to `8`) to GitHub,
while the student commits a different fix (`x^3`) to the same line locally.
Pulling then stops with a merge conflict inside the notebook's JSON,
which Jupyter cannot open until the student resolves it in a text editor.

It is used in the chapter
[Merge conflicts](../../book/lectures/0230-git-merge-conflicts.qmd),
in the exercise's second part, "Resolving merge conflicts in a more complex text file".

## Where it came from

Adapted from Tiffany Timbers' <https://github.com/ttimbers/r-cube-notebook>
(MIT licence, kept as `LICENSE` in `start/` and `end/`).
Its workflow downloaded the collaborator's version of `cube.ipynb`
from <https://github.com/ttimbers/r-cube-commit-source>.
That change is now made inside the workflow itself (see "Changes" below).

## What is here

- `start/` is the repository students begin with:
  - `cube.ipynb`, with `x^2` on the second line of its first code cell;
  - `.github/workflows/main.yml`, the workflow that commits `x * x * x` (and the output `8`) and pushes it;
  - `README.md`, the student instructions;
  - `LICENSE`, `r-cube-notebook-start.Rproj` and `.gitignore`.
  It has no environment files:
  students open the notebook with the Jupyter and IRkernel from their course setup.
- `end/` is the same repository after the conflict is resolved in favour of the student's fix
  and the notebook is re-run:
  `cube.ipynb` has `x^3`, its last cell shows `8`,
  and its metadata records R 4.6.2 (it said 4.1.2).
  Keeping `x * x * x` instead is just as correct.
  So that the notebook can be run, `end/` also has an environment that is not part of the exercise:
  JupyterLab from `pyproject.toml`, `uv.lock` and `.python-version` (uv),
  and IRkernel from `DESCRIPTION`, `renv.lock`, `.Rprofile` and `renv/` (renv).

## Making your own copy on GitHub

The chapter says to click "Use this template".
A folder cannot be used as a template,
so each student copies `start/` into a new repository of their own instead.
From the root of this repository, in a terminal (Git Bash on Windows):

```bash
cp -R demos/r-cube-notebook/start ~/r-cube-notebook
cd ~/r-cube-notebook
git init -b main
git add .
git commit -m "Initial commit"
```

Then create an empty repository called `r-cube-notebook` on GitHub
(no README, licence or `.gitignore`) and push to it:

```bash
git remote add origin https://github.com/<your-username>/r-cube-notebook.git
git push -u origin main
```

If that push is refused with a message about the `workflow` scope,
see the same note in the [`r-cube` README](../r-cube/README.md#making-your-own-copy-on-github).

## Live coding, from `start/` to `end/`

1. On GitHub, open the Actions tab, click the workflow `.github/workflows/main.yml`,
   and click "Run workflow".
   When it finishes, `cube.ipynb` on GitHub has `x * x * x`, in a commit "Here's a fix to the file!".
   Do not pull it.
2. Locally, open `cube.ipynb` in JupyterLab, change `x^2` to `x^3`,
   run the notebook (the last cell shows `8`), save, and commit:
   `git commit -am "Calculate the cube, not the square"`.
3. `git push origin main` is rejected with `! [rejected] main -> main (fetch first)`.
4. `git pull --no-rebase origin main` stops with `CONFLICT (content): Merge conflict in cube.ipynb`.
   (A plain `git pull` stops earlier with "You have divergent branches";
   see the [`r-cube` README](../r-cube/README.md#live-coding-from-start-to-end).)
5. Try to open `cube.ipynb` in JupyterLab.
   It will not load, because the conflict markers make the file invalid JSON.
6. Open it in a text editor instead.
   The conflict is in the cell's `source`:

   ```
       "cube <- function(x) {\n",
   <<<<<<< HEAD
       " x^3\n",
   =======
       " x * x * x\n",
   >>>>>>> <commit id>
       "}"
   ```

   Keep one of the two lines and delete the three marker lines.
   This is the only conflict:
   both sides changed the output to `8`, so Git merged the outputs on its own.
   (If you do not re-run the notebook in step 2, the result is the same,
   because only GitHub's side changed the output lines.)
7. Open the notebook in JupyterLab again to check that it loads and runs,
   then finish the merge and push:

   ```bash
   git add cube.ipynb
   git commit --no-edit
   git push origin main
   ```

8. Talk about why notebooks conflict more than scripts:
   outputs, execution counts and metadata all change when you run a notebook,
   so two people who ran it can conflict on lines neither of them edited.

## Running `end/`

From a terminal, in `demos/r-cube-notebook/end/`:

```bash
uv sync --locked
Rscript -e 'renv::restore(prompt = FALSE)'
uv run Rscript -e 'IRkernel::installspec(user = FALSE, sys_prefix = TRUE)'
uv run jupyter nbconvert --to notebook --execute --stdout cube.ipynb | grep -F '"[1] 8"'
```

The last command prints `"[1] 8"`, from the executed notebook's last cell.
The third command registers the R kernel in `.venv/` only, not in your own Jupyter.
To work in the notebook instead, run `uv run jupyter lab`.

The kernel starts R in `end/`, where `.Rprofile` activates renv,
so IRkernel comes from the renv library.
For the same reason, opening `end/cube.ipynb` from another Jupyter
fails to start the R kernel until `renv::restore()` has been run in `end/`.

## Changes from the source repository

- The workflow no longer depends on another repository.
  It used `curl` to download `cube.ipynb` from `ttimbers/r-cube-commit-source`;
  it now edits the notebook with
  `sed -i -e 's/x\^2/x * x * x/' -e 's/"4"$/"8"/' -e 's/"\[1\] 4"$/"[1] 8"/' cube.ipynb`,
  which gives a file byte-identical to the downloaded one (checked locally with the same expressions).
  If the notebook no longer contains `x^2` when the workflow runs,
  it now fails with "nothing to commit" instead of overwriting the student's fix.
- The workflow also uses `actions/checkout@v7` instead of `@v2`,
  pushes with `git push` instead of `ad-m/github-push-action@master`,
  asks for `contents: write` instead of `write-all`,
  and drops `fetch-depth: 0` and `git pull origin main`.
  It still has no `name:`, so the Actions tab lists it as `.github/workflows/main.yml`.
  `actionlint` reports no problems with it, but it has not yet been run on GitHub.
- The student README drops the "Use this template" and "Clone" steps and the repeated heading.
- Added `.gitignore` (`.Rproj.user/`, `.Rhistory`, `.RData`, `.ipynb_checkpoints/`, and `.venv/` in `end/`)
  and the `.Rproj` files.
- `end/` adds the uv and renv environment described above; the source had none.

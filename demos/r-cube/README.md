# `r-cube` demo: resolving a merge conflict in an R script

First pass, to be reviewed when taught.

A practice repository that makes a merge conflict on purpose.
`cube.r` defines a `cube()` function that squares instead of cubing.
A GitHub Actions workflow, run by hand, plays a collaborator
who pushes one fix (`x * x * x`) to GitHub,
while the student commits a different fix (`x^3`) to the same line locally.
Pulling then stops with a merge conflict in `cube.r` for the student to resolve.

It is used in the chapter
[Merge conflicts](../../book/lectures/0230-git-merge-conflicts.qmd),
in the exercise's first part, "Resolving merge conflicts in a simple text file".
The second part uses the [`r-cube-notebook`](../r-cube-notebook/) demo.

## Where it came from

Adapted from Tiffany Timbers' <https://github.com/ttimbers/r-cube>
(MIT licence, kept as `LICENSE` in `start/` and `end/`).
Its workflow downloaded the collaborator's version of `cube.r`
from <https://github.com/ttimbers/r-cube-commit-source>.
That change is now made inside the workflow itself (see "Changes" below).

## What is here

- `start/` is the repository students begin with:
  - `cube.r`, with `x^2` on its second line;
  - `.github/workflows/main.yml`, the workflow that commits `x * x * x` to that line and pushes it;
  - `README.md`, the student instructions;
  - `LICENSE`, `r-cube-start.Rproj` and `.gitignore`.
- `end/` is the same repository after the conflict is resolved in favour of the student's fix,
  so `cube.r` has `x^3` on its second line.
  Keeping `x * x * x` instead is just as correct.
  `end/` has no `renv` or `DESCRIPTION`, because `cube.r` uses only base R.

## Making your own copy on GitHub

The chapter says to click "Use this template".
A folder cannot be used as a template,
so each student copies `start/` into a new repository of their own instead.
From the root of this repository, in a terminal (Git Bash on Windows):

```bash
cp -R demos/r-cube/start ~/r-cube
cd ~/r-cube
git init -b main
git add .
git commit -m "Initial commit"
```

`cp -R` copies the hidden `.github/` folder too, which the exercise needs.
Then create an empty repository called `r-cube` on GitHub
(no README, licence or `.gitignore`) and push to it:

```bash
git remote add origin https://github.com/<your-username>/r-cube.git
git push -u origin main
```

With the GitHub CLI, `gh repo create r-cube --public --source=. --push` does both steps.

If the push is refused with a message about the `workflow` scope,
the token Git is using may not push files under `.github/workflows/`
(clicking "Use this template" never needed that permission).
Pushing over SSH avoids it.
If the GitHub CLI is Git's credential helper, run `gh auth refresh -s workflow` once,
since `gh auth login` asks only for the `repo`, `read:org` and `gist` scopes.
A personal access token needs the `workflow` scope ticked.

## Live coding, from `start/` to `end/`

1. On GitHub, open the Actions tab, click the workflow `.github/workflows/main.yml`,
   and click "Run workflow".
   When it finishes, `cube.r` on GitHub has `x * x * x`, in a commit "Here's a fix to the file!".
   Do not pull it.
2. Locally, change `x^2` to `x^3` in `cube.r` and commit:
   `git commit -am "Calculate the cube, not the square"`.
3. `git push origin main` is rejected with `! [rejected] main -> main (fetch first)`,
   because GitHub has a commit you do not have.
4. Pull it, asking Git to merge:

   ```bash
   git pull --no-rebase origin main
   ```

   Git stops with `CONFLICT (content): Merge conflict in cube.r`.
   A plain `git pull` stops earlier with "You have divergent branches and need to specify how to reconcile them",
   unless `git config --global pull.rebase false` has been run once.
5. Open `cube.r` and walk through the markers:

   ```
   cube <- function(x) {
   <<<<<<< HEAD
    x^3
   =======
    x * x * x
   >>>>>>> <commit id>
   }
   ```

   Keep one of the two lines and delete the three marker lines.
6. Check the function still works, `Rscript -e 'source("cube.r"); cube(2)'` (prints `[1] 8`),
   then finish the merge and push:

   ```bash
   git add cube.r
   git commit --no-edit
   git push origin main
   ```

7. On GitHub, `cube.r` now has your line,
   and the commit history shows both fixes joined by a merge commit.

## Running `end/`

From a terminal, in `demos/r-cube/end/`:

```bash
Rscript -e 'source("cube.r"); cube(2)'
```

This prints `[1] 8`.

## Changes from the source repository

- The workflow no longer depends on another repository.
  It used `curl` to download `cube.r` from `ttimbers/r-cube-commit-source`;
  it now runs `sed -i 's/x\^2/x * x * x/' cube.r`,
  which gives a file byte-identical to the downloaded one (checked locally with the same `sed` expression).
  One difference: if `cube.r` no longer contains `x^2`
  (because the student pushed their fix before running the workflow),
  the workflow now fails with "nothing to commit" instead of overwriting the student's fix.
- The workflow also uses `actions/checkout@v7` instead of `@v2`,
  pushes with `git push` instead of the third-party `ad-m/github-push-action@master`,
  asks for `contents: write` instead of `write-all`,
  and drops `fetch-depth: 0` and `git pull origin main`, which it did not need.
  It still has no `name:`, so the Actions tab lists it as `.github/workflows/main.yml`, as the chapter says.
  `actionlint` reports no problems with it, but it has not yet been run on GitHub.
- The student README drops the "Use this template" and "Clone" steps (now in this README)
  and the repeated "## Instructions" heading.
- Added `.gitignore` (`.Rproj.user/`, `.Rhistory`, `.RData`) and the `.Rproj` files.

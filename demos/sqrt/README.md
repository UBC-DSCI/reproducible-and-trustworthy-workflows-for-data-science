# `sqrt` demo: branches, merging and main branch protection

First pass, to be reviewed when taught.

A tiny repository to practise Git branches and pull requests on.
`sqrt.py` prints the square root of the number passed as `--n`.
On a branch, students make it raise a helpful error for negative numbers,
push the branch, and later merge it into a protected `main` through a pull request.

It is used in two chapters:

- [Git branches](../../book/lectures/0260-git-branches.qmd),
  in the exercise at the end of "Creating a branch using the command line"
  (branch `better_error_msg`, fix `sqrt.py`, push the branch);
- [Main branch protection](../../book/lectures/0350-github-branch-protection.qmd),
  in the exercise "Setting up main branch protection".

## Where it came from

Adapted from Tiffany Timbers' <https://github.com/ttimbers/sqrt>,
a GitHub template repository
(its README credits an example by [Meghan Allen](https://www.cs.ubc.ca/~meghana/)).
That repository has no licence file,
so the code is credited to Tiffany Timbers and Meghan Allen.

## What is here

- `start/` is the repository students begin with:
  the template's `sqrt.py`, unchanged,
  and a uv project to run it
  (`pyproject.toml` declaring `click`, `uv.lock`, `.python-version` (3.14) and `.gitignore`),
  plus a `README.md`.
- `end/` is the same repository after the `better_error_msg` branch is merged into `main`.
  The only difference is two lines in `sqrt.py`:

  ```python
  def main(n):
      if n < 0:
          raise Exception("n should not be a negative number")
      print(math.sqrt(n))
  ```

## Making your own copy on GitHub

The chapters say to click "Use this template" (0260) or to import the repository (0350).
A folder cannot be used as a template,
so each student copies `start/` into a new repository of their own instead.
From the root of this repository, in a terminal (Git Bash on Windows):

```bash
cp -R demos/sqrt/start ~/sqrt
cd ~/sqrt
git init -b main
git add .
git commit -m "Initial commit"
```

Then create an empty repository called `sqrt` on GitHub
(no README, licence or `.gitignore`, so that the first push is not rejected),
and push to it:

```bash
git remote add origin https://github.com/<your-username>/sqrt.git
git push -u origin main
```

With the GitHub CLI, `gh repo create sqrt --public --source=. --push` does both steps.

## Live coding, from `start/` to `end/`

### Branches ([Git branches](../../book/lectures/0260-git-branches.qmd))

1. Run the script, once with a positive number and once with a negative one:

   ```bash
   uv sync
   uv run python sqrt.py --n=25
   uv run python sqrt.py --n=-4
   ```

   The first prints `5.0`.
   The second ends in a traceback with
   `ValueError: expected a nonnegative input, got -4.0`
   (Python 3.14's wording; older Pythons say `math domain error`).
2. Create the branch and switch to it with `git switch -c better_error_msg`.
3. Add the check from the chapter to `main()` in `sqrt.py`, before the `print()`
   (see `end/sqrt.py`), and run `uv run python sqrt.py --n=-4` again.
   It now ends with `Exception: n should not be a negative number`.
4. Commit it with `git add sqrt.py` and `git commit -m "Raise a helpful error for negative numbers"`.
5. `git switch main` and look at `sqrt.py`: the check is not there.
6. `git switch better_error_msg`: the check is back.
7. `git push origin better_error_msg`,
   then show the branch on GitHub (the branch drop-down, and the "Compare & pull request" banner).

### Main branch protection ([Main branch protection](../../book/lectures/0350-github-branch-protection.qmd))

1. On GitHub, go to Settings > Branches and add a branch protection rule for `main`,
   with "Require a pull request before merging" and "Require approvals" ticked.
   Branch protection is only enforced on public repositories
   unless the account has GitHub Pro or Team (GitHub Education includes Pro),
   so make the repository public if the rule does not take effect.
2. On `main`, make a small commit and `git push origin main`.
   GitHub rejects the push because `main` is protected.
   Undo it locally with `git reset --hard origin/main`.
3. Open a pull request from `better_error_msg` into `main` and merge it.
   You cannot approve your own pull request,
   so on a repository of your own either add a classmate as a collaborator to review it,
   or, as the repository's admin, tick GitHub's option to merge without waiting for the requirements.
4. `git switch main` and `git pull origin main`.
   The local repository now matches `end/`.

## Running `end/`

From a terminal, in `demos/sqrt/end/`:

```bash
uv sync --locked
uv run python sqrt.py --n=25
uv run python sqrt.py --n=-4
```

The first command prints `5.0`.
The second exits with a traceback ending in
`Exception: n should not be a negative number`.

## Changes from the source repository

- `start/` and `end/` are uv projects (`pyproject.toml`, `uv.lock`, `.python-version`, `.gitignore`).
  The source had no environment file;
  its README listed `click` and `math` (which is part of Python) as the packages needed.
- The README now shows `uv run python sqrt.py --n=25` instead of `python sqrt.py --n=25`,
  and links to the source repository.
- `sqrt.py` in `start/` is unchanged.
  `end/sqrt.py` adds the check the 0260 chapter gives, indented to fit the function.

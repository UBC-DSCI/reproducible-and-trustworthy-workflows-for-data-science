## Reproducible and Trustworthy Workflows for Data Science

Tiffany A. Timbers, Joel Ostblom, Florencia D'Andrea, Rodolfo Lourenzutti, Daniel Chen

Course notes for teaching concepts and practices 
related to reproducible and trustworthy workflows for data science.
Specifically we cover workflows for writing reproducible, 
robust and valid computer scripts, analytic reports 
and data analysis pipelines, computational environments,
as well as testing and deployment of software written for data analysis. 
Emphasis is placed on how to collaborate on the above tasks effectively 
with others using version control tools, 
such as Git and GitHub. 
Concepts are learned and applied using real data and case studies.

## Project setup

The book is written with Quarto and runs both R and Python code,
so rendering it needs:

- [Quarto](https://quarto.org/docs/get-started/)
- R 4.6.2, the version recorded in `renv.lock`
  ([rig](https://github.com/r-lib/rig) installs it with `rig add 4.6.2`)
- [uv](https://docs.astral.sh/uv/getting-started/installation/),
  which installs the Python version in `.python-version` for you

Then, from the project root:

```bash
make setup    # install the Python and R packages
make render   # render the book into book/_book/
make preview  # preview the book, re-rendering on save
```

`make help` lists every target.

### Python packages (uv)

Python packages are declared in `pyproject.toml` and locked in `uv.lock`.
`uv sync` (run by `make setup`) creates `.venv/` with exactly those versions,
and `make render` and `make preview` run Quarto through `uv run`,
so the book's Python code runs in that environment.
To add a package, run `uv add <package>`
and commit both `pyproject.toml` and `uv.lock`.

### R packages (renv)

R packages are locked in `renv.lock`.
`renv::restore()` (run by `make setup`) installs them into the project library,
and Quarto uses that library automatically through the project's `.Rprofile`.
renv only reads the packages listed in `DESCRIPTION`,
not the `library()` calls in the chapters,
so to add a package:
add it to `DESCRIPTION`,
install it with `renv::install("<package>")`,
then run `renv::snapshot()`,
and commit both `DESCRIPTION` and `renv.lock`.

### Continuous integration

The workflows in `.github/workflows/` build the book with the same versions:
`setup-uv` installs the Python in `.python-version` and runs `uv sync --locked`,
and `r-version` pins R.
When you move the book to a new version of R,
update `r-version` in both `publish.yml` and `pr.yml`
to match the version in `renv.lock`.

### Publishing and pull request previews

Every push to `main` renders the book and deploys it to the `gh-pages` branch
(`.github/workflows/publish.yml`),
which GitHub Pages serves at
<https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/>.

Every pull request from a branch in this repository also renders the book
and publishes a preview at
`https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/pr-preview/pr-<N>/`,
where `<N>` is the pull request number
(`.github/workflows/pr.yml`, using [pr-preview-action](https://github.com/rossjrw/pr-preview-action)).
A bot comment on the pull request links to the preview,
and the preview is removed when the pull request closes.
Pull requests from forks cannot publish a preview,
because their workflow runs cannot write to this repository.

## Chapter filenames and URLs

Chapter files in `book/lectures/` are named `PPCC-<url>.qmd`
so they sort in the order the course runs:
`PP` is the part (`02` is Version Control with Git, `90` the appendix, `99` the archive)
and `CC` the chapter within it, in steps of 10.
`0240-git-ignore.qmd` is the fourth chapter of part 2.

The number never reaches the published URL:
each chapter sets its URL with `output-file` in its front matter,
and that URL describes the topic, not the chapter's position.

```yaml
---
title: "Ignoring files with `.gitignore`"
output-file: git-ignore.html
aliases:
  - 040-version-control-1.html#git-ignore
---
```

- **Adding a chapter:** give it an `output-file`:
  lowercase, hyphens only, and `<topic>-<language>-<tool>` for a variant of a topic
  (`data-validation-python-pandera`).
  Name the file after it, numbered into the gap where it belongs
  (`0235-…` goes between `0230-git-merge-conflicts.qmd` and `0240-git-ignore.qmd`),
  and add it to `book/_quarto.yml`.
  Its learning objectives go in `book/learning_objectives/` under the same filename.
- **Moving or renumbering a chapter:** rename the file freely and leave `output-file` alone.
  A part that runs out of gaps can be renumbered in one batch.
- **Splitting a chapter:** the piece that keeps the opening keeps the old URL in `aliases`.
  Every other piece lists the old URL with the anchor of each section it took
  (`040-version-control-1.html#git-ignore`),
  so links to those sections land on the right chapter.
- **Retiring a chapter:** when the course replaces a chapter's tool or approach,
  move the chapter to the Archive part at the end of the book:
  rename it to `99CC-<url>.qmd` and list it under `parts/archive.qmd` in `book/_quarto.yml`.
  Its URL stays the same.
- **Changing a published URL:** avoid it. If you must, add the old URL to `aliases`
  so existing links redirect.

## License: 
Software licensed under the [MIT License](https://spdx.org/licenses/MIT.html), non-software content licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the [license file](LICENSE.md) for more information.

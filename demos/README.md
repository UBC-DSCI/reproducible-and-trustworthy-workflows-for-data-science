# Demos

Small example projects that the book's chapters build in class.
Each one used to live in its own GitHub repository;
they now live here, one folder per demo.

First pass, to be reviewed as each demo is taught.

## How a demo is laid out

Each demo has a `README.md` and up to two projects:

- `start/` is where the class starts:
  the boilerplate we live-code from.
  It may leave out some dependencies on purpose,
  when adding them is part of the lesson.
- `end/` is the finished solution.
  It is self-contained and runnable:
  it declares and locks everything it needs
  (`DESCRIPTION` and `renv.lock` for R, `pyproject.toml` and `uv.lock` for Python).

## Open each project on its own

Open `start/` or `end/` as its own project,
so that the working directory is that folder,
not this repository:

- **RStudio:** open the `.Rproj` file inside `start/` or `end/`.
- **Positron or VS Code:** *File > Open Folder…* and pick `start/` or `end/`.
- **A terminal:** `cd` into `start/` or `end/` before running anything.

Paths in the code, such as `data/` or `tests/testthat`,
are relative to that folder.

## Start from `start/`

`start/` is meant to become a new git repository of your own.
Copy it out of this repository first,
so that its history is not mixed up with the book's:

```bash
cp -R demos/<demo>/start ~/<demo>
cd ~/<demo>
git init
```

To use it with GitHub (for example, to run GitHub Actions),
create an empty repository on GitHub and push your copy to it.

## Run `end/`

From inside `end/`:

- **R:** `Rscript -e 'renv::restore()'`, then the commands in the demo's `README.md`.
- **Python:** `uv sync --locked`, then `uv run ...` as the demo's `README.md` shows.

## The demos

| Demo | Chapters | Language |
|---|---|---|
| [`sqrt`](sqrt/) | Git branches, branch protection | Python |
| [`r-cube`](r-cube/), [`r-cube-notebook`](r-cube-notebook/) | Merge conflicts | R |
| [`scripts`](scripts/) | Scripts | R and Python |
| [`pipeline-shell`](pipeline-shell/) | Pipelines with scripts | Python |
| [`pipeline-make`](pipeline-make/) | Pipelines with Make | Python |
| [`count-classes-tests-r`](count-classes-tests-r/) | Testing: R (testthat) | R |
| [`count-classes-tests-python`](count-classes-tests-python/) | Testing: Python (pytest) | Python |
| [`vdiffr-pretty-scatter`](vdiffr-pretty-scatter/) | Testing images | R |
| [`foofactors`](foofactors/) | Packaging, R packages | R |
| [`pycounts`](pycounts/) | Packaging, package testing, continuous deployment | Python |
| [`docker-uv`](docker-uv/) | Python packages with uv in an image | Python |

Most demos are adapted from Tiffany Timbers' course repositories;
each demo's `README.md` says where it came from.

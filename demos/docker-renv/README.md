# docker-renv

First pass, to be reviewed when taught.

## What it teaches

Putting an renv project's R packages into a Docker image:
`RENV_PATHS_LIBRARY=/opt/renv/library` in R's `Renviron.site`,
copying `renv.lock`, `.Rprofile` and `renv/activate.R` before `renv::restore()`,
and running the project with the project folder mounted at `/workspace`.

It is used by the chapter "R packages with renv in an image"
(`book/lectures/0645-containers-renv.qmd`, on the `containers-rewrite` branch until it is merged).
Its renv lines are the same as in [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv),
which the chapter "Python and R in one image" builds.
The Python version is [docker-uv](../docker-uv/).

## Folders

- `start/`: the renv project (`DESCRIPTION`, `renv.lock`, `.Rprofile`, `renv/`, `hello.R`), with no `Dockerfile`.
- `end/`: the same project with its `Dockerfile`.

## Live-coding steps

From a copy of `start/`:

1. `Rscript -e 'renv::restore(prompt = FALSE)'`, then `Rscript hello.R`, on your computer.
2. Write the `Dockerfile` in `end/`, one instruction at a time:
   `FROM rocker/r-ver:4.6.2`, the `apt-get` line for `curl`, `WORKDIR /workspace`,
   the `RENV_PATHS_LIBRARY` line, the two `COPY` lines, `RUN Rscript -e "renv::restore()"`.
3. `docker build --tag docker-renv .`
4. `docker run --rm -v "$(pwd):/workspace" docker-renv Rscript hello.R`
5. `docker run --rm -v "$(pwd):/workspace" docker-renv Rscript -e ".libPaths()"`
   starts with `/opt/renv/library`, not the `renv/library` folder on your computer.

## Run `end/`

```bash
cd end
docker build --tag docker-renv .
docker run --rm -v "$(pwd):/workspace" docker-renv Rscript hello.R
```

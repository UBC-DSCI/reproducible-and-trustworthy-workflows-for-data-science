# R packages with renv in a Docker image

A small R project, `hello.R`, whose packages renv installs into a Docker image.
The image starts from `rocker/r-ver:4.6.2`, Ubuntu Linux with R 4.6.2.

## Build and run

```bash
docker build --tag docker-renv .
docker run --rm -v "$(pwd):/workspace" docker-renv Rscript hello.R
```

On Windows, in Git Bash, write `-v "/$(pwd):/workspace"`;
in PowerShell, write `-v "${PWD}:/workspace"`.

## Dependencies

R 4.6.2 and the packages in `DESCRIPTION` (cowsay), locked in `renv.lock`
from Posit Package Manager (`https://p3m.dev/cran/latest`).
renv uses explicit snapshots (`renv/settings.json`),
so `renv::snapshot()` records only what `DESCRIPTION` lists, and what those packages need.

# R packages with renv in a Docker image

A small R project, `hello.R`, ready to put into a Docker image.
It runs on your computer with renv:

```bash
Rscript -e 'renv::restore(prompt = FALSE)'
Rscript hello.R
```

Next, write a `Dockerfile` that installs its packages with renv.

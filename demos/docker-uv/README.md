# docker-uv

First pass, to be reviewed when taught.

## What it teaches

Putting a uv project's Python packages into a Docker image:
copying uv into the image with `COPY --from`,
`UV_PROJECT_ENVIRONMENT=/opt/venv`,
copying `pyproject.toml`, `uv.lock` and `.python-version` before `uv sync --locked`,
and running the project with the project folder mounted at `/workspace`.

It is used by the chapter "Python packages with uv in an image"
(`book/lectures/0640-containers-uv.qmd`, on the `containers-rewrite` branch until it is merged).
Its uv lines are the same as in [docker-uv-renv](https://github.com/chendaniely/docker-uv-renv),
which the chapter "Python and R in one image" builds.

## Folders

- `start/`: the uv project (`pyproject.toml`, `uv.lock`, `.python-version`, `hello.py`), with no `Dockerfile`.
- `end/`: the same project with its `Dockerfile`.

## Live-coding steps

From a copy of `start/`:

1. `uv run hello.py` runs the project on your computer (and creates `.venv/`).
2. Write the `Dockerfile` in `end/`, one instruction at a time:
   `FROM ubuntu:24.04`, `COPY --from=ghcr.io/astral-sh/uv:0.13.7 ...`, `WORKDIR /workspace`,
   `ENV UV_PROJECT_ENVIRONMENT=/opt/venv`, the `COPY` of the three files, `RUN uv sync --locked`.
3. `docker build --tag docker-uv .`
4. `docker run --rm -v "$(pwd):/workspace" docker-uv uv run hello.py`
5. `docker run --rm -v "$(pwd):/workspace" docker-uv uv run python -c "import sys; print(sys.prefix)"`
   prints `/opt/venv`, even though your computer's `.venv/` is mounted at `/workspace/.venv`.

## Run `end/`

```bash
cd end
docker build --tag docker-uv .
docker run --rm -v "$(pwd):/workspace" docker-uv uv run hello.py
```

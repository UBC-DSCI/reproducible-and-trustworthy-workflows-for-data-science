# Python packages with uv in a Docker image

A small Python project, `hello.py`, whose packages uv installs into a Docker image.
The image starts from Ubuntu, which has no Python:
uv installs the Python version in `.python-version` while the image is built.

## Build and run

```bash
docker build --tag docker-uv .
docker run --rm -v "$(pwd):/workspace" docker-uv uv run hello.py
```

On Windows, in Git Bash, write `-v "/$(pwd):/workspace"`;
in PowerShell, write `-v "${PWD}:/workspace"`.

## Dependencies

Python 3.14 and the packages in `pyproject.toml` (cowsay), locked in `uv.lock`.
The image copies uv 0.13.7 from `ghcr.io/astral-sh/uv:0.13.7`.

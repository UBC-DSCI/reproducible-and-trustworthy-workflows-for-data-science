# Ubuntu Linux, with no Python: uv installs Python itself
FROM ubuntu:24.04

# install python uv
# https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

# The project is mounted over /workspace, so the packages go in /opt
WORKDIR /workspace

# python packages in /opt/venv
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
COPY pyproject.toml uv.lock .python-version ./
# --locked: stop if uv.lock doesn't match pyproject.toml
RUN uv sync --locked

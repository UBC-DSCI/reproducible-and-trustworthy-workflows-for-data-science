# sqrt

A repository for practicing branching, merging, and main branch protection.
Developed for the UBC Master of Data Science program.

## Usage

Install the dependencies once with `uv sync`.
Then, for example, to calculate the square root of 25:

```bash
uv run python sqrt.py --n=25
```

```
5.0
```

## Dependencies

- Python 3.14 or later, managed by [uv](https://docs.astral.sh/uv/)
- The Python package `click` (declared in `pyproject.toml`, locked in `uv.lock`)

## Credits

Adapted from Tiffany Timbers' <https://github.com/ttimbers/sqrt>.
This example was derived from an example originally developed by
[Meghan Allen](https://www.cs.ubc.ca/~meghana/).

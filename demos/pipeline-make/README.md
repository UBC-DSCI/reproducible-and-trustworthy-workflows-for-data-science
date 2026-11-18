# Pipeline demo: a data analysis pipeline driven by GNU Make

First pass, to be reviewed when taught.

This demo replaces the shell script of the
[shell pipeline demo](../pipeline-shell/) with a `Makefile`.
Make reruns only the steps whose inputs have changed,
and `clean` targets reset the analysis to its starting point.
The analysis is the same:
two Python scripts count the words in four novels
and plot the 10 most frequent words,
and a Quarto report shows the four plots.

It is used in the chapter
[Data analysis pipelines with GNU Make](../../book/lectures/0920-pipelines-make.qmd).

## Where it came from

Adapted from Tiffany Timbers'
<https://github.com/ttimbers/data-analysis-pipeline-make-practice>
(last commit December 2024),
which is adapted from Software Carpentry's
[Automation and Make](https://swcarpentry.github.io/make-novice/) lesson
(CC BY 4.0, see `LICENSE.md`).
The novels are from Project Gutenberg
(see `data/LICENSE_TEXTS.md`).

## What is here

- `start/` is what the class starts from,
  the finished shell pipeline demo:
  the data, the two scripts, the report, the driver script `run_all.sh`,
  empty `results/` folders (kept by a `README.md` in each),
  and the Python environment (`pyproject.toml` and `uv.lock`).
- `end/` is the same with a `Makefile` added,
  exactly as the chapter's final version (in "Improving the Makefile").

The four novels in `data/` take about 2 MB
(`last.txt` is the largest at about 1 MB).
They are kept because the lesson needs them as they are.
`pipeline-shell/` has the same files,
and git stores identical files only once.

## Live coding, from `start/` to `end/`

Copy `start/` somewhere outside this repository and run `git init` in it.
Run `uv sync`, then `source .venv/bin/activate`
(`source .venv/Scripts/activate` in Git Bash on Windows),
so that `make` and the `python` in the `Makefile` use the project's environment.
Then, from its root:

1. Write a `Makefile` with one rule for `results/isles.dat`,
   and run `make results/isles.dat`.
   Indent an action with spaces to see `missing separator`.
2. Run it again to see `is up to date`,
   then `touch data/isles.txt` and run it again to see it rebuild.
3. Add a `clean` rule.
4. Add the rule for `results/figure/isles.png`,
   then the rules for `abyss`,
   and an `all` target at the top.
5. Finish the `Makefile` for all four books and the report
   (the chapter's "Finish off the Makefile!" version).
6. Add `.PHONY`, then the `dats`, `figs`, `clean-dats`, `clean-figs`
   and `clean-all` targets (the chapter's final version, in `end/`).

## Run `end/`

You need uv, Quarto and GNU Make (3.81, the version macOS ships, is enough).

```bash
cd end
uv sync --locked
uv run make all
uv run make clean-all
```

`make all` writes `results/*.dat`, `results/figure/*.png`
and `report/count_report.html` (with `report/count_report_files/`),
and `make clean-all` deletes them all.

# Pipeline demo: a data analysis pipeline driven by a shell script

First pass, to be reviewed when taught.

This demo shows how a shell script, `run_all.sh`,
can run every step of a small analysis in order
and so record how the analysis was done.
Two Python scripts count the words in four novels
(`scripts/wordcount.py`) and plot the 10 most frequent words
(`scripts/plotcount.py`),
and a Quarto report shows the four plots.

It is used in the chapter
[Data analysis pipelines with scripts](../../book/lectures/0910-pipelines-scripts.qmd).
Its `end/` is the starting point of the [Make pipeline demo](../pipeline-make/),
used in the next chapter.

## Where it came from

Adapted from Tiffany Timbers'
<https://github.com/ttimbers/data-analysis-pipeline-bash-practice>
(last commit December 2024),
which is adapted from Software Carpentry's
[Automation and Make](https://swcarpentry.github.io/make-novice/) lesson
(CC BY 4.0, see `LICENSE.md`).
The novels are from Project Gutenberg
(see `data/LICENSE_TEXTS.md`).

## What is here

- `start/` is what the class starts from:
  the data, the two scripts, the report, empty `results/` folders
  (kept by a `README.md` in each),
  and the Python environment (`pyproject.toml` and `uv.lock`).
- `end/` is the same with the driver script `run_all.sh` added,
  exactly as the chapter's final version.

The four novels in `data/` take about 2 MB
(`last.txt` is the largest at about 1 MB).
They are kept because the lesson needs them as they are.
`pipeline-make/` has the same files,
and git stores identical files only once.

## Live coding, from `start/` to `end/`

Copy `start/` somewhere outside this repository and run `git init` in it.
Then, from its root:

1. Run `uv sync`, then count the words in one book
   with `uv run python scripts/wordcount.py --input_file=data/isles.txt --output_file=results/isles.dat`,
   and look at the result with `head -5 results/isles.dat`.
2. Plot it with
   `uv run python scripts/plotcount.py --input_file=results/isles.dat --output_file=results/figure/isles.png`.
3. Put those two commands in `run_all.sh`, with a comment header,
   and run it with `uv run bash run_all.sh`.
4. Extend `run_all.sh` to all four books
   and add `quarto render report/count_report.qmd` at the end.
5. Discuss what is not ideal:
   it reruns every step every time,
   and cleaning up means deleting every output by hand.

## Run `end/`

You need uv and Quarto.

```bash
cd end
uv sync --locked
uv run bash run_all.sh
```

This writes `results/*.dat`, `results/figure/*.png`
and `report/count_report.html` (with `report/count_report_files/`).
Delete them afterwards with:

```bash
rm -f results/*.dat results/figure/*.png report/count_report.html
rm -rf report/count_report_files
```

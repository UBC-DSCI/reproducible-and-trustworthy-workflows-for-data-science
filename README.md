## Reproducible and Trustworthy Workflows for Data Science

Tiffany A. Timbers, Joel Ostblom, Florencia D'Andrea, Rodolfo Lourenzutti, Daniel Chen

Course notes for teaching concepts and practices 
related to reproducible and trustworthy workflows for data science.
Specifically we cover workflows for writing reproducible, 
robust and valid computer scripts, analytic reports 
and data analysis pipelines, computational environments,
as well as testing and deployment of software written for data analysis. 
Emphasis is placed on how to collaborate on the above tasks effectively 
with others using version control tools, 
such as Git and GitHub. 
Concepts are learned and applied using real data and case studies.

## Chapter filenames and URLs

Chapter files in `book/lectures/` are named `PPCC-<url>.qmd`
so they sort in the order the course runs:
`PP` is the part (`02` is Version Control with Git, `90` the appendix, `99` the archive)
and `CC` the chapter within it, in steps of 10.
`0240-git-ignore.qmd` is the fourth chapter of part 2.

The number never reaches the published URL:
each chapter sets its URL with `output-file` in its front matter,
and that URL describes the topic, not the chapter's position.

```yaml
---
title: "Ignoring files with `.gitignore`"
output-file: git-ignore.html
aliases:
  - 040-version-control-1.html#git-ignore
---
```

- **Adding a chapter:** give it an `output-file`:
  lowercase, hyphens only, and `<topic>-<language>-<tool>` for a variant of a topic
  (`data-validation-python-pandera`).
  Name the file after it, numbered into the gap where it belongs
  (`0235-…` goes between `0230-git-merge-conflicts.qmd` and `0240-git-ignore.qmd`),
  and add it to `book/_quarto.yml`.
  Its learning objectives go in `book/learning_objectives/` under the same filename.
- **Moving or renumbering a chapter:** rename the file freely and leave `output-file` alone.
  A part that runs out of gaps can be renumbered in one batch.
- **Splitting a chapter:** the piece that keeps the opening keeps the old URL in `aliases`.
  Every other piece lists the old URL with the anchor of each section it took
  (`040-version-control-1.html#git-ignore`),
  so links to those sections land on the right chapter.
- **Retiring a chapter:** when the course replaces a chapter's tool or approach,
  move the chapter to the Archive part at the end of the book:
  rename it to `99CC-<url>.qmd` and list it under `parts/archive.qmd` in `book/_quarto.yml`.
  Its URL stays the same.
- **Changing a published URL:** avoid it. If you must, add the old URL to `aliases`
  so existing links redirect.

## License: 
Software licensed under the [MIT License](https://spdx.org/licenses/MIT.html), non-software content licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the [license file](LICENSE.md) for more information.

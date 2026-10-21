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

Chapter files in `book/lectures/` are numbered (`040-version-control-1.qmd`)
so they sort in the order the course runs.
The number never reaches the published URL:
each chapter sets its URL with `output-file` in its front matter,
and that URL describes the topic, not the chapter's position.

```yaml
---
title: "Version control: Git history and merge conflicts"
output-file: git-history-merge-conflicts.html
aliases:
  - 040-version-control-1.html
---
```

- **Adding a chapter:** give the file a number that places it in the order,
  add it to `book/_quarto.yml`, and give it an `output-file`:
  lowercase, hyphens only, and `<topic>-<language>-<tool>` for a variant of a topic
  (`data-validation-python-pandera`).
- **Moving or renumbering a chapter:** rename the file freely and leave `output-file` alone.
- **Changing a published URL:** avoid it. If you must, add the old URL to `aliases`
  so existing links redirect.

## License: 
Software licensed under the [MIT License](https://spdx.org/licenses/MIT.html), non-software content licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the [license file](LICENSE.md) for more information.

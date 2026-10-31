.PHONY: help setup preview render clean publish

help: ## List the targets
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-8s %s\n", $$1, $$2}'

setup: ## Install the Python (uv) and R (renv) environments
	uv sync
	Rscript -e 'renv::restore(prompt = FALSE)'

preview: ## Preview the book, re-rendering on save
	uv run quarto preview book/index.qmd --port 54321

render: clean ## Render the book into book/_book/
	uv run quarto render book/

clean: ## Remove the rendered book and render leftovers
	rm -rf book/_book
	rm -rf book/lectures/*.quarto_ipynb
	rm -rf book/lectures/*.log
	rm -rf book/.quarto

publish: ## No need: GitHub Actions publishes the book and PR previews
	@echo "No need to publish manually: GitHub Actions does this for you."
	@echo "  - every push to main deploys the book to GitHub Pages (.github/workflows/publish.yml)"
	@echo "  - every pull request from a branch gets a preview at pr-preview/pr-<N>/ (.github/workflows/pr.yml)"

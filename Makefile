.PHONY: help setup preview render clean publish

help: ## List the targets
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-8s %s\n", $$1, $$2}'

setup: ## Install the Python (uv) and R (renv) environments
	uv sync
	Rscript -e 'renv::restore(prompt = FALSE)'

preview: ## Preview the book, re-rendering on save
	uv run quarto preview book/index.qmd --port 54321

render: clean ## Render the book into docs/
	uv run quarto render book/

clean: ## Remove the rendered book and render leftovers
	rm -rf docs
	rm -rf book/lectures/*.quarto_ipynb
	rm -rf book/lectures/*.log
	rm -rf book/.quarto

publish: ## Render the book and publish it to the gh-pages branch
	uv run quarto publish gh-pages book --no-prompt --no-browser

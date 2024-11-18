@PHONY: preview render clean publish

preview:
	quarto preview book/index.qmd --port 54321

render:
	make clean
	quarto render book/

clean:
	rm -rf docs

publish:
	quarto publish gh-pages book --no-prompt --no-browser

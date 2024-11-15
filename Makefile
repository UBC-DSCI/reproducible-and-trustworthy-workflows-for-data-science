@PHONY: preview render

preview:
	quarto preview book/index.qmd --port 54321

render:
	make clean
	quarto render book/

clean:
	rm -rf docs

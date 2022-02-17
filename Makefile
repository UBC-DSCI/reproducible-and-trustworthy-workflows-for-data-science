book:
	cp README.md materials/README.md
	jupyter-book build materials
	if [ ! -d "docs" ]; then mkdir docs; fi
	if [ ! -f ".nojekyll" ]; then touch docs/.nojekyll; fi
	cp -r materials/_build/html/* docs

clean-book:
	rm -rf docs/*
	rm -rf materials/_build/*
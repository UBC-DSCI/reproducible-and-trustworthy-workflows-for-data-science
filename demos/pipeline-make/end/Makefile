# Makefile
# Tiffany Timbers, Nov 2018

# This driver script completes the textual analysis of
# 3 novels and creates figures on the 10 most frequently
# occuring words from each of the 3 novels. This script
# takes no arguments.

# example usage:
# make all

.PHONY: all dats figs clean-dats clean-figs clean-all

# run entire analysis
all: report/count_report.html

# count words
dats: results/isles.dat \
results/abyss.dat \
results/last.dat \
results/sierra.dat

results/isles.dat : scripts/wordcount.py data/isles.txt
	python scripts/wordcount.py \
		--input_file=data/isles.txt \
		--output_file=results/isles.dat
results/abyss.dat : scripts/wordcount.py data/abyss.txt
	python scripts/wordcount.py \
		--input_file=data/abyss.txt \
		--output_file=results/abyss.dat
results/last.dat : scripts/wordcount.py data/last.txt
	python scripts/wordcount.py \
		--input_file=data/last.txt \
		--output_file=results/last.dat
results/sierra.dat : scripts/wordcount.py data/sierra.txt
	python scripts/wordcount.py \
		--input_file=data/sierra.txt \
		--output_file=results/sierra.dat

# plot
figs : results/figure/isles.png \
	results/figure/abyss.png \
	results/figure/last.png \
	results/figure/sierra.png

results/figure/isles.png : scripts/plotcount.py results/isles.dat
	python scripts/plotcount.py \
		--input_file=results/isles.dat \
		--output_file=results/figure/isles.png
results/figure/abyss.png : scripts/plotcount.py results/abyss.dat
	python scripts/plotcount.py \
		--input_file=results/abyss.dat \
		--output_file=results/figure/abyss.png
results/figure/last.png : scripts/plotcount.py results/last.dat
	python scripts/plotcount.py \
		--input_file=results/last.dat \
		--output_file=results/figure/last.png
results/figure/sierra.png : scripts/plotcount.py results/sierra.dat
	python scripts/plotcount.py \
		--input_file=results/sierra.dat \
		--output_file=results/figure/sierra.png

# write the report
report/count_report.html : report/count_report.qmd figs
	quarto render report/count_report.qmd

clean-dats :
	rm -f results/isles.dat \
		results/abyss.dat \
		results/last.dat \
		results/sierra.dat

clean-figs :
	rm -f results/figure/isles.png \
	results/figure/abyss.png \
	results/figure/last.png \
	results/figure/sierra.png

clean-all : clean-dats \
	clean-figs
	rm -f report/count_report.html
	rm -rf report/count_report_files

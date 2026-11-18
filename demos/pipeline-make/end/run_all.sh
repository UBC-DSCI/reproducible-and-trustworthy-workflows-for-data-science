# run_all.sh
# Tiffany Timbers, Nov 2018

# This driver script completes the textual analysis of
# 3 novels and creates figures on the 10 most frequently
# occurring words from each of the 3 novels. This script
# takes no arguments.

# example usage:
# bash run_all.sh

# count the words
python scripts/wordcount.py \
    --input_file=data/isles.txt \
    --output_file=results/isles.dat
python scripts/wordcount.py \
    --input_file=data/abyss.txt \
    --output_file=results/abyss.dat
python scripts/wordcount.py \
    --input_file=data/last.txt \
    --output_file=results/last.dat
python scripts/wordcount.py \
    --input_file=data/sierra.txt \
    --output_file=results/sierra.dat

# create the plots
python scripts/plotcount.py \
    --input_file=results/isles.dat \
    --output_file=results/figure/isles.png
python scripts/plotcount.py \
    --input_file=results/abyss.dat \
    --output_file=results/figure/abyss.png
python scripts/plotcount.py \
    --input_file=results/last.dat \
    --output_file=results/figure/last.png
python scripts/plotcount.py \
    --input_file=results/sierra.dat \
    --output_file=results/figure/sierra.png

# write the report
quarto render report/count_report.qmd

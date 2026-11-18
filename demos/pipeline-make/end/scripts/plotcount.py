import click
import pandas as pd
import matplotlib.pyplot as plt

@click.command()
@click.option('--input_file', type=str, help = 'Path (including filename) to data file')
@click.option('--output_file', type=str, help = 'Path (including filename) of where to locally write the file')

def main(input_file, output_file):
    '''Generates a barchart of wordcounts for the 10 most frequent words'''
    data = pd.read_csv(input_file, sep = ' ', header = None, encoding='latin-1')
    data = data.rename(columns = {0:'word', 1:'count', 2:'frequency'})
    data.sort_values(by = 'count')
    word_count_plot = data.iloc[:10,:2].plot.bar(x = 'word', y = 'count',
                                             color = 'blue',
                                             figsize = (5, 2),
                                            rot = 0)
    plt.savefig(output_file)

if __name__ == "__main__":
    main()

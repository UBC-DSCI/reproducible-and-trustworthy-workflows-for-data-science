import click
import yaml
import pandas as pd

@click.command()
@click.option('--config', type=click.Path(exists=True))
def main(config):
    """
    Main function that loads config and runs analysis.
    """
    # Load the config file
    with open(config, "r") as f:
        config_dict = yaml.safe_load(f)

    # Access values from the dictionary
    input_path = config_dict['input_data']
    cols_to_keep = config_dict['keep_cols']

    # Read data
    raw_data = pd.read_csv(input_path)
    
    # Example usage of config variables
    clean_data = raw_data[cols_to_keep]
    
    print(f"Data loaded from {input_path}")
    print(f"Model type: {config_dict['model_settings']['type']}")

    # Save the cleaned data to the path specified in the config file
    clean_data.to_csv(config_dict['output_data'], index=False)

if __name__ == "__main__":
    main()

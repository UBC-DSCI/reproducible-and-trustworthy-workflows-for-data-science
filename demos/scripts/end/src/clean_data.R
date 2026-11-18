"This script cleans data based on parameters in a config file.

Usage: clean_data.R --config=<config>

Options:
--config=<config>  Path to the YAML configuration file
" -> doc

library(tidyverse)
library(docopt)
library(yaml)

opt <- docopt(doc)

main <- function(config_path) {
  
  # read in the config file
  config <- read_yaml(config_path)
  
  # Access values from the config list
  raw_data <- read_csv(config$input_data)
  
  # Example: selecting columns defined in the YAML file
  clean_data <- raw_data |>
    select(all_of(config$keep_cols))
    
  print(paste("Data cleaned. Keeping columns:", paste(config$keep_cols, collapse = ", ")))
  
  # Save the cleaned data to the path specified in the config file
  write_csv(clean_data, config$output_data)
}

main(opt$config)

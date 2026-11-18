import os
import sys

import numpy as np
import pandas as pd
import pytest

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.count_classes import count_classes

# Set seed for reproducibility
np.random.seed(2024)

# Test input data
two_classes_2_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class2", "class1", "class2"],
        "values": np.round(np.random.uniform(size=4), 1),
    }
)

two_classes_2_and_1_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class1", "class2"],
        "values": np.round(np.random.uniform(size=3), 1),
    }
)

one_class_2_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class1"],
        "values": np.round(np.random.uniform(size=2), 1),
    }
)

empty_df = pd.DataFrame({"class_labels": [], "values": []})

two_classes_2_obs_as_dict = {
    "class_labels": ["class1", "class2", "class1", "class2"],
    "values": np.round(np.random.uniform(size=4), 1),
}

# Expected test outputs
two_classes_2_obs_output = pd.DataFrame(
    {"class": ["class1", "class2"], "count": [2, 2]}
)

two_classes_2_and_1_obs_output = pd.DataFrame(
    {"class": ["class1", "class2"], "count": [2, 1]}
)

one_class_2_obs_output = pd.DataFrame({"class": ["class1"], "count": [2]})


# `count_classes` should return a pandas DataFrame,
# with the number of rows corresponding to the number of unique classes
# in the `class_col` from the original DataFrame. The new DataFrame
# will have a `class` column whose values are the unique classes,
# and a `count` column, whose values will be the number of observations
# for each class
def test_count_classes_success():
    assert isinstance(count_classes(two_classes_2_obs, "class_labels"), pd.DataFrame)
    assert count_classes(two_classes_2_obs, "class_labels").equals(two_classes_2_obs_output)
    assert count_classes(two_classes_2_and_1_obs, "class_labels").equals(two_classes_2_and_1_obs_output)


# `count_classes` should return a DataFrame with one row if there is only one class,
# and an empty DataFrame, with `class` and `count` columns,
# if the input DataFrame is empty
def test_count_classes_edge():
    assert count_classes(one_class_2_obs, "class_labels").equals(one_class_2_obs_output)
    empty_result = count_classes(empty_df, "class_labels")
    assert empty_result.empty
    assert list(empty_result.columns) == ["class", "count"]


# `count_classes` should throw an error when incorrect types
# are passed to the `data_frame` argument
def test_count_classes_errors():
    with pytest.raises(TypeError):
        count_classes(two_classes_2_obs_as_dict, "class_labels")

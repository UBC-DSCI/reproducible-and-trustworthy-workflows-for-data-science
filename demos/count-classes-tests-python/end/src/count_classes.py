# translated my R Code to Python using ChatGPT, then edited.
# R Code source: demos/count-classes-tests-r/end/R/count_classes.R in
# https://github.com/UBC-DSCI/reproducible-and-trustworthy-workflows-for-data-science

import pandas as pd


def count_classes(data_frame, class_col):
    """
    Count class observations in a pandas DataFrame.

    Creates a new DataFrame with two columns, listing the classes present
    in the input DataFrame and the number of observations for each class.

    Parameters
    ----------
    data_frame : pandas.DataFrame
        The input DataFrame containing the data to analyze.
    class_col : str
        The name of the column in the DataFrame containing class labels.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with two columns:
        - 'class': Lists the unique classes found in the input DataFrame.
        - 'count': Lists the number of observations for each class in the input DataFrame.
        It will have one row for each class present in the input DataFrame.

    Raises
    ------
    TypeError
        If `data_frame` is not a pandas DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.read_csv('mtcars.csv')  # Replace 'mtcars.csv' with your dataset file
    >>> result = count_classes(data, 'am')
    >>> print(result)
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("`data_frame` should be a pandas DataFrame")
    # Group by the class column and count the observations for each class
    result = data_frame.groupby(class_col).size().reset_index(name="count")
    # Rename the class column to match the R function
    result = result.rename(columns={class_col: "class"})
    return result

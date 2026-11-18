def count_char(input_string):
    """Count the number of characters in a string.

    Parameters
    ----------
    input_string : str
        The input string whose characters will be counted.

    Returns
    -------
    int
        The number of characters in the input string.

    Examples
    --------
    >>> count_char("hello")
    5
    >>> count_char("")
    0
    >>> count_char("Python is cool")
    14
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input to be str, got {type(input_string)}")
    return len(input_string)

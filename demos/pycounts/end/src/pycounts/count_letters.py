# code adapted from a ChatGPT answer
import unicodedata


def count_letters(input_string):
    """
    Counts the number of letters in a string, excluding spaces, numbers, and symbols.

    Parameters
    ----------
    input_string : str
        The input string to count.

    Returns
    -------
    int
        The number of "letters" in the input string.

    Examples
    --------
    # counts the string 'Hello, world! 123'
    >>> count_letters("Hello, 世界! 123")
    7
    """

    # categories starting with 'L' are letters.
    # e.g., 'Lu' for uppercase letter, 'Ll' for lowercase letter
    is_letter = [
        True for char in input_string if unicodedata.category(char).startswith("L")
    ]
    return sum(is_letter)

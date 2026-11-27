import pytest

from pycounts.count_char import count_char


def test_count_char():

    string = "hello"
    expected = 5
    actual = count_char(string)
    assert actual == expected

    string = ""
    expected = 0
    actual = count_char(string)
    assert actual == expected

    string = "Python is cool"
    expected = 14
    actual = count_char(string)
    assert actual == expected


def test_count_char_wrong_input():
    with pytest.raises(TypeError):
        count_char(123)


@pytest.mark.parametrize(
    "test_data_line_number, expected_count", [(0, 34), (1, 10), (2, 7)]
)
def test_line_n(text_data, test_data_line_number, expected_count):
    string = text_data[test_data_line_number].strip()
    assert count_char(string) == expected_count

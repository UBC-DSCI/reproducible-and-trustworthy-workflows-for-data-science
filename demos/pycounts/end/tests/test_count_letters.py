import pytest

from pycounts.count_letters import count_letters


@pytest.mark.parametrize(
    "test_data_line_number, expected_count", [(0, 27), (1, 9), (2, 5)]
)
def test_line_n(text_data, test_data_line_number, expected_count):
    string = text_data[test_data_line_number].strip()
    assert count_letters(string) == expected_count

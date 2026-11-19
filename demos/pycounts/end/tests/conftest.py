import pytest


@pytest.fixture
def text_data():
    file_path = "tests/text.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

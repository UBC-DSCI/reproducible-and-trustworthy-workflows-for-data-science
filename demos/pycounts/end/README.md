# pycounts

Calculate word counts in a text file!

## Installation

```bash
uv add pycounts
```

## Usage

`pycounts` can count the words in a text file and plot the results:

```python
import pycounts
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = pycounts.count_words(file_path)
fig = pycounts.plot_words(counts, n=10)
plt.show()
```

It can also count the characters and the letters in a string:

```python
from pycounts.count_char import count_char
from pycounts.count_letters import count_letters

count_char("Python is cool")    # 14
count_letters("Hello, 世界! 123")  # 7
```

## Development

```bash
uv sync                                    # install the package and its dev dependencies
uv run pytest                              # run the tests
uv run pytest --cov=pycounts --cov-branch  # with line and branch coverage
uv build                                   # build the sdist and wheel into dist/
```

## Credits

`pycounts` is the example package from the
[Python Packages](https://py-pkgs.org/) book by Tomas Beuzen and Tiffany Timbers.

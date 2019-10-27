---
authors:
    - Eric J. Ma
date: 2019-10-27
---

# Testing your code

Writing tests for code is a basic software skill.
Writing tests helps build confidence in the _stability_ of our code.

## When do we write tests?

There are two "time scales" at which I think this question can be answered.

The first time scale is "short-term".
As soon as we finish up a function, that first test should be written.
Doing so lets us immediately sanity-check our intuition
about the newly-written fuction.

## How do we get set up with testing?

In a Python project, first ensure that you have `pytest` installed.
If you follow recommended practice
and have one `conda` environment per project,
then you should be able to install `pytest` using `conda`:

```bash
# if you use conda:
conda install pytest
# if you use pip:
pip install pytest
```

## The anatomy of a test

When using `pytest`, your tests take on the function name:

```python
from custom_library import my_function

def test_my_function():
    """Test for my_function."""
    # set up test here.
    assert some_condition
```

We can then execute the test from the command line:

```bash
pytest .
```

_Voila!_ The tests will be executed, and you will see them run one by one.

##

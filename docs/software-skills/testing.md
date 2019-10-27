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

## The kinds of tests you could write

Let's go through the kinds of tests you might want to write.

### Execution tests

I started with this kind of test because
these are the simplest to understand:
we simply execute a function to make sure that it runs without breaking.

```python
from custom_lib import my_function

def test_my_function():
    """Execution test for my_function."""
    my_function()
```

This kind of test is useful when your function is not parameterized,
and simply calls on other functions inside your library.
It is also incredibly useful as a starter test
when you cannot think of a better test to write.

One place where I have used this test pattern
is when we built a project dashboard using Panel.
The dashboard is made from many complex layers of function calls,
involving database queries, data preprocessing, cached results, and more.
Sporadically, something would break,
and it was something difficult to debug.
By wrapping the dashboard execution inside a Python function
and executing it by simply calling `dashboard()`,
we could discover bugs as soon as they showed up,
rather than so-called "in production".

### Example-based test

An example-based test looks basically like this:

```python
from custom_lib import another_function

def test_another_function():
    arg1 = ...
    arg2 = ...
    result = another_function(arg1, arg2)

    expected_result = ...

    assert result == expected_result
```

Basically, we set up the test with an example,
and check that when given a set of pre-specified inputs,
a particular expected result is returned.

When writing code in the notebook,
I find myself writing example-based tests informally all the time.
They are those "sanity-checks" function calls
where I manually check that the result looks correct.
I am sure you do too.

So rather than rely on manually checking,
it makes perfect sense to simply
copy and paste the code into a test function
and execute them.

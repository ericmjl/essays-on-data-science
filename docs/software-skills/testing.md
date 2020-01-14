# Testing your code

Writing tests for code is a basic software skill.
Writing tests helps build confidence in the _stability_ of our code.

## When to write tests

There are two "time scales" at which I think this question can be answered.

The first time scale is "short-term".
As soon as we finish up a function, that first test should be written.
Doing so lets us immediately sanity-check our intuition
about the newly-written fuction.

The second time scale is "longer-term".
As soon as we discover bugs, new tests should be added to the test suite.
Those new tests should either cover that exact bug,
or cover the class of bugs together.

## How to get setup

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

### Advanced Testing

The above I consider to be basic, bare minimum testing
that a data scientist can do.
Of course, there are more complex forms of testing
that a QA engineer would engage in,
and I find it useful to know at least what they are
and what tools we have to do these forms of testing
in the Python ecosystem:

- Parameterized tests: [`pytest` has these capabilities](https://docs.pytest.org/en/latest/parametrize.html).
- Property-based tests: [`hypothesis` gives us these capabilities](https://hypothesis.readthedocs.io/en/latest/details.html).

## Tests for Data

Data are notoriously difficult to test,
because it is a snapshot of the stochastic state of the world.
Nonetheless, if we impose prior knowledge on our testing,
we can ensure that certain errors in our data never show up.

### Nullity Tests

For example, if we subject a SQL query to a series of transforms
that are supposed to guarantee a densely populated DataFrame,
then we can write a **nullity test**.

```python
def test_dataframe_function():
    """Ensures that there are no null values in the dataframe function."""
    df = dataframe_function(*args, **kwargs)
    assert pd.isnull(df).sum().sum() == 0
```

### `dtype` Tests

We can also check that the dtypes of the dataframe are correct.

```python
def test_dataframe_dtypes():
    """Checks that the dtypes of the dataframe are correct."""
    dtypes = {
        "col1": float32,
        "col2": int,
        "col3": object,
    }
    df = dataframe_function(*args, **kwargs)
    for col, dtype in dtypes.items():
        assert df[col].dtype == dtype
```

### Bounds Tests

We can also check to make sure that our dataframe-returning function
yields data in the correct bounds for each column.

```python
def test_dataframe_bounds():
    """Checks that the bounds of datsa are correct."""
    df = dataframe_function(*args, **kwargs)
    # For a column that can be greater than or equal to zero.
    assert df["column1"].min() >= 0

    # For a column that can only be non-zero positive.
    assert df["column2"].min() > 0

    # For a column that can only be non-zero negative.
    assert df["column3"].max() < 0
```

DataFrame tests are a special one for data scientists,
because the dataframe is the idiomatic data structure
that we engage with on an almost daily basis.

### Column Name Tests

Having stable and consistent column names in the dataframes that we use
is extremely important;
the column names are like our API to the data.
Hence, checking that a suite of expected column names exist in the dataframe
can be very useful.

```python
def test_dataframe_names():
    """Checks that dataframe column names are correct."""
    expected_column_names = ["col1", "col2", "col3"]
    df = dataframe_function(*args, **kwargs)

    # Check that each of those column names are present
    for c in expected_column_names:
        assert c in df.columns

    # (Optional) check that _only_ those columns are present.
    assert set(df.columns) == set(expected_column_names)
```

### Other statistical property tests

Testing the mean, median, and mode are difficult,
but under some circumstances,
such as when we know that the data are drawn from some distribution,
we might be able to write a test for the central tendencies of the data.

Placing an automated test
that checks
whether the data matches a particular parameterized distribution
with some probability value
is generally not a good idea,
[because it can give a false sense of security](https://allendowney.blogspot.com/2013/08/are-my-data-normal.html).
However, if this is a key modelling assumption
and you need to keep an automated, rolling check on your data,
then having it as a test
can help you catch failures in downstream modelling early.
In practice, I rarely use this because the speed at which data come in
are slow relative to the time I need to check assumptions.
Additionally, the stochastic nature of data
means that this test would be a flaky one,
which is an undesirable property for tests.

## Parting words

I hope this essay gives you some ideas
for implementing testing in your data science workflow.
As with other software skills,
these are skills that become muscle memory over time,
hence taking the time from our daily hustle
to practice them makes us more efficient in the long-run.
In particular, the consistent practice of testing
builds confidence in our codebase,
not just for my future self, but also for other colleagues
who might end up using the codebase too.

-----

## A Glossary of Testing in Data Science

**Manual testing**:
Basically where we use a Jupyter notebook
and manually inspect that the function works to how we’re expecting.

**Automated testing**:
Where we provide a test suite and use a test runner (e.g. `pytest`)
to automatically execute all of the tests in the suite.

**Example-based testing**:
Where we provide one or more hard-coded examples in our test suite,
and test that our function works on those examples.

**Parameterized testing**:
Where we provide examples as parameters to our test functions,
helping us reduce code duplication in our test functions.
Not necessarily something distinct from example-based testing.

**Auto-manual testing**:
A not-so-tongue-in-cheek way of describing
automated testing using hard-coded examples.

**Property-based testing**:
Where we use an automatic generator of examples
that fulfill certain “properties”.
For example, numbers with range constraints,
or strings generated from an alphabet of a certain length or less.
Property-based testing builds on top of parameterized testing.

**Data testing**:
Where we test the “correctness” of our data.
Property-based testing can be used here,
or we can hard-code checks on our data
that we know should be invariant over time.

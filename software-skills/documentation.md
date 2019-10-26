# Documenting your code

Writing lightweight documentation is a practice that I found
sorely lacking in data science practice.
In this essay, I will show you how to introduce lightweight documentation
into your code.

## Why document your code?

There are a few good reasons to document your code.

Firstly, your future self will thank you
for having a plain English translation of what you _intended_ to do
with that block of code.
Oftentimes, the _intent_ behind the code
is lost in the translation from our heads to actual code.

Secondly, other readers of your code
will also thank you.

Thirdly, by clarifying what exactly you intended to accomplish with a block of code,
as well as the major steps taken towards accomplishing those goals,
you often will end up with a much cleaner implementation in the end.

## When should you document your code?

A pragmatic choice would be once you find yourself accomplishing
a logical chunk of work.

I usually do it as soon as I define a Python function.

## Where should your code documentation go?

As a general rule of thumb, having code documentation as close to the actual source code
is probably the best way to approach this.

For Python programmers, this would imply taking advantage of __docstrings__!

**Docstrings** occur in the following places:

1. Right after a function or class method definition.
1. Right inside a class definition.
1. Right at the top of a `.py` module.

An anti-pattern here would be writing your documentation in an external system, such as a Wiki.
(Woe betide the code developer who writes code docs in Confluence...)
This is because the documentation is not proximal to the source code.
I have found myself forgetting to update the docstrings after updating the source code.
If it's easy to forget to update the docs when the docs are right next to the source,
imagine how much easier it is to forget to update external docs!

Where, then, would documentation on how the code is organized live then?
I would argue it should be pushed as close to the source code as possible.
For example, we can use the `.py` module docstrings
to describe the intent behind why certain entire modules exist.

## Can you show an example?

Of course! First off, here is a skeleton to follow:

```python
"""
This module houses all functions that cannot be neatly categorized
in other places.
"""

def my_function(arg1, arg2):
    """
    Calculates something based on arg1 and arg2.

    This calculated thing is intended to be used
    by `this_other_function`,
    so the return type should not be changed.

    :param arg1: Describe arg1
    :param arg2: Describe arg2
    :returns: ``the_thing_being_returned``, a pandas DataFrame (for example).
    """
    the_thing_being_returned = ...  # implement the function
    return the_thing_being_returned
```

Now, let's see this in action with a function
that returns a snake-cased version of a string
with all punctuation also removed.
(This is a simplified implementation of what is implemented in `pyjanitor`'s
`clean_names` function.)

```python
import string

def clean_string(s):
    """
    Remove all punctuation from string, and convert to lower_snake_case.

    An example of the input and output:

        "My string!" -> "my_string"

    :param s: String to clean.
    """
    s = s.replace(string.punctuation, "_").replace(" ", "_").strip("_").lower()
    return s
```

You may notice that the docstring is longer than the implementation.
Frequently (though not always),
I have found that when docstring length exceeds implementation length,
it is a sign that the author(s) of the code
have been thoughtful about its implementation.
This bodes well for working in a team,
especially when a data scientist hands over a prototype
to the engineering team.

## But we don't have time to do this?

The main objections to injecting "basic software engineering"
into a data scientist's workflow
usually center around not having enough time.

As always, I am sympathetic to this objection,
because I also operate under time constraints.

One thing I will offer is that docs are an investment of time
for the team, rather than for the individual.
We save multiples of time downstream
when we write good docs.
One way to conceptualize this is the number of person-hours saved
down the road by oneself and one's teammates when good docs exist.
We minimize the amount of time spent reading code
to grok what it is about.

At the same time,
the practice of clarifying what we intend to accomplish with the function
can help bring clarity to the implementation.
This I have mentioned above.
Having a clean implementation makes things easier to maintain later on.
Hence, time invested now on good docs
also helps us later on.

As with other software engineering skills,
this is a skill that can be picked up, refined, and honed.
We get more efficient at writing docs the more we do it.

## Parting words

I hope this essay has helped you get a feel
for how you can write well-documented code.
At the same time, I hope that by showing you a simple anchoring example
that you will be able to replicate the pattern in your own work.

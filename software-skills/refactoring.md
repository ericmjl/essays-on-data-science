# Refactoring your code

How many times have you found yourself copy/pasting code from one notebook to another?
If it the answer is "many", then this essay probably has something for you.
We're going to look at the practice of "refactoring" code,
and how it applies in a data science context.

## Why refactor

When writing code, we _intend_ to have a block of code do one thing.
As such, its multiple application should have a single source of truth.
However, the practice of copying and pasting code
gives us multiple sources of truth.
Refactoring code, thus,
gives us a way of establishing a single source of truth for our functions,
which can be called on in multiple situations.

## When to refactor

The short answer is "basically whenever you find yourself hitting copy+paste"
on your keyboard.

## How do we refactor

The steps involved are as follows.

1. Wrap the semi-complex block of code in a function.
1. Identify what you would consider to be an "input" and "output" for the function.
1. Take specific variable names and give them more general names.

## An example

Let's take the example of a chunk of code that takes a protein sequence,
compares it to a reference sequence,
and returns all of the mutations that it has.
(We will only implemenet a naive version for the sake of pedagogy.)

```python
sequence1 = ...
sequence2 = ...

mutations = []
for i, (letter1, letter2) in enumerate(zip(sequence1, sequence2)):
    mutations.append(f"{letter1}{i+1}{letter2}")
mutations = "; ".join(m for m in mutations)
```

This more or less should accomplish what we want.
Let's now apply the ideas behind refactoring to this code block.

```python
def mutation_string(reference, sequence, sep="; "):
    mutations = []
    for i, (letter1, letter2) in enumerate(zip(reference, sequence)):
        mutations.append(f"{letter1}{i+1}{letter2}")
    return f"{sep}".join(m for m in mutations)
```

You'll notice the three steps coming into play.

**Firstly**, we simply shifted the main logic of the code into a function definition.

**Secondly**, we then generalized the function a bit,
by renaming `sequence1` and `sequence2` to what we usually intend for it to be,
a `sequence` of interest and a `reference` sequence.

**Finally**, we defined those two as inputs,
alongside a keyword argument called `sep`,
which defines the separator between each mutation.

## Bonus

On the basis of this function definition,
we can do some additional neat things!

For example, in protein sequence analysis,
our `reference` sequence is usually kept constant.
Hence, we can actually create a custom `mutation_string`
for our reference sequence using `functools.partial`
by fixing `reference` to a particular value,
thus eliminating the need to repetitively pass in the same reference string.

```python
from functools import partial

protein1 = ...  # define the string here.

prot1_mut_string = partial(mutation_string, reference=protein1)

protein2 = ...  # define the string here.

mutstring = prot1_mut_string(sequence=protein2)
```

## Where should this function be refactored to

You can choose to keep it in the notebook, and that would be fine
if the function was used only in a single notebook.

If you find yourself needing to call on that same function from another notebook,
do the right thing and create a `utils.py` (or analogous) Python module
that lives in the same directory as the notebook.
Then, import the refactored function from `utils.py`.

If you feel sophisticated, you can also create a custom Python library
for your project. I will address this in a separate essay.

An anti-pattern, though, would be to attempt to treat the notebook as source code
and import the function from one notebook into another.
Notebooks are great for one thing:
weaving functions together into an integrarted analysis.
I'm of the opinion that we should use a tool the way it was intended,
and bring in other tools to do what we need.
In this respect, I think that DataBricks notebooks does the wrong thing
by bowing to bad human first instincts rather than encouraging productive behaviours.

## Where do we find time to do this

I hear this concern, as I went through the same concerns myself.

Isn't it faster to just copy/paste the code?
What if I don't end up reusing the code elsewhere?
Isn't the time then wasted?

In thinking back to my own habits, I realized early on
that doing this was not a matter of technical ability
but rather a matter of mindset.

Investing the time into doing simple refactoring alongside my analyses
does take immediate time away from the analysis.
However, the deliberate practice of refactoring early on
earns back multiples of the time spent as the project progresses.

Moreover, if and when the project gets handed over "in production",
or at least shared with others to use,
our colleagues can spend less time is spent navigating a spaghetti-like codebase,
and more time can be spent building a proper mental model of the codebase
to build on top of.

On the possiblity of not reusing the code elsewhere,
I would strongly disagree.
Refactoring is not a common skill, while copy/pasting code is.
Every chance we get to refactor code is practicing the skill,
which only gets sharper and more refined as we do it more.
Hence, even for the sake of getting more practice
makes it worthwhile to do refactoring at every chance.

## Concluding words

I hope this mini-essay demystifies the practice of code refactoring,
and gives you some ideas on how to make it part of your workflow.

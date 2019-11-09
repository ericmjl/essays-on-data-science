# Recursion

Recursion is an incredibly useful concept to know.
To be clear, it is distinct from looping, but is related.
I think it's helpful for data scientists
to have recursion as a programming trick in their back pocket.
In this essay, let's take an introductory look at recursion,
and where it can come in handy.

## What recursion looks like

Recursion happens when we have a function
that calls itself by default
or else returns a result when some stopping criteria is reached.

A classic example of recursion
is in finding the root of a tree from a given node.
Here, we essentially want to follow every node's predecessor
until we reach a node that has no predecessor.

In code form, this looks something like this:

```python linenums="1"
def find_root(G, n):
    predecessor = G.predecessor(n)
    if G.predecessor(n):
        return find_root(G, predecessor)
    else:
        return n
```

Generally, we first compute something on the basis of the inputs (line 2).
This is usually some form of finding a new substitute input
on which we can check a condition (lines 4 and 6).
Under one condition, we return the function call with a new input,
and under another condition, we return the desired output.

## Why you would use recursion

Recursion is essentially a neat way to write a loop concisely,
and can be useful, say,
under circumstances where we do not know
the exact number of loop iterations needed
before we encounter the stopping condition.

## Where recursion shows up in a real-life situation

I can speak to one situation at work
where I was benchmarking some deep neural network models,
and also testing hyperparameters on a grid.
There, I used YAML files to keep track of parameters and experiments,
and in order to keep things concise,
I implemented a very lightweight YAML inheritance scheme,
where I would have a master "template" experiment,
but use child YAML files that inherited from the "master" template
in which certain parts of the experiment parameters were changed.
(An example might be one where the master template
specified the use of the Adam optimizer with a particular learning rate,
while the child templates simply modified the learning rate.)

As the experiments got deeper and varied more parameters,
things became more tree-like,
and so I had to navigate the parameter tree from the child templates
up till the root template, which by definition had no parents.
After finding the root template,
I could then travel back down from the root template,
iteratively updating the parameters
until I reached the child template of interest.

The more general scenario to look out for is in graph traversal problems.
If your problem can be cast in terms of a graph data structure
that you need to program your computer to take a walk over,
then that is a prime candidate for trying your hand at recursion.

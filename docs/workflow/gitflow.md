# Principled Git-based Workflow in Collaborative Data Science Projects

[GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)
is an incredible branching model for working with code.
In this essay, I would like to introduce it to you, the data scientist,
and show how it might be useful in your context,
especially for working with multiple colleagues on the same project.

## What GitFlow is

GitFlow is a way of working with multiple collaborators on a git repository.
It originated in the software development world,
and gives software developers a way of keeping new development work
isolated from reviewed, documented, and stable code.

At its core, we have a "source of truth" branch called `master`,
from which we make branches on which development work happens.
Development work basically means new code, added documentation, more tests, etc.
When the new code, documentation, tests, and more are reviewed,
a pull request is made to merge the new code back into the `master` branch.

Usually, the act of making a branch is paired with raising an issue on an issue tracker,
in which the problem and proposed solution are written down.
Merging into master is paired with a code review session,
in which another colleague (or the tech lead) reviews the code to be merged,
and approves (or denies) code merger
based on whether the issue raised in the issue tracker has been resolved.

From my time experimenting with GitFlow at work,
I think that when paired with other principled workflows
that doen't directly interact with Git,
can I think be of great utility to data scientists.
It does, however, involve a bit of change in the common mode of working
that data scientists use.

## GitFlow in a data science project

Here is how I think GitFlow can be successfully deployed in a data science project.

Everything starts with the unit of analysis that we are trying to perform.

We start by defining the question that we are trying to answer.
We then proceed forward by sketching out an analysis plan
(let's call this an analysis sketch),
which outlines the data sources that we need,
the strategy for analyzing the data
(roughly including models we think might be relevant to the scale of the problem,
the plots we think might be relevant to make,
and where we think, on the basis of probable results,
the analysis might be able to go).

None of this is binding, which makes the analysis sketch

Outline:

- What is GitFlow?
  - A brief history: software world
  - Why it works in software development
- How we can use GitFlow in DS context
  - Define a problem to investigate.
  - Define a deliverable of some kind.
    - Software: code
    - Analysis: plots or notebook with a concluding statement
    - Scope out what action will be taken on the basis of the analysis.
    - If no action can be taken, analysis priority should go down.
  - Create issue describing a plan for what needs to be done.
  - Create off from `master` branch in which that work is done.
  - Finish the work, merge branch into master, and close issue.
  - Raise new issues as they show up.
- Changes to DS mindset to adopt GitFlow
  - Cannot carry out endless analyses. End point + action required.
  - Forces us to be more thoughtful about how we spend our time.
    - Does not restrict the problem space though!
    - We are still free to investigate problems.
    - We just have to justify and document them better.

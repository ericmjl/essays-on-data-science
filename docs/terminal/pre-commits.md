---
authors:
    - Eric J. Ma
date: 2019-10-28
---

# Using `pre-commit` git hooks to automate code checks

Git hooks are an awesome way
to automate checks on your codebase locally
before committing them to your code repository.

That said, setting them up
involves digging into the `.git` folder of your repository,
and can feel intimidating to set up and replicate
across multiple local clones of repositories.

Thankfully, there is an easier way about.

The developers of the `pre-commit` framework have given us a wonderful tool
to standardize and automate the replication of pre-commit git hooks.

## What git hooks are

Git hooks are basically commands that are run just before or after
git commands are executed.
In this essay's context, I basically consider it
a great way to run automated checks on our code before we commit them.

## Getting started with `pre-commit`

First off, you should follow the `pre-commit` instructions for getting setup.
These instructions are availble
on the [`pre-commit`](https://pre-commit.com/) website.
For those of you who know what you are doing
and just want something to copy/paste:

```bash
conda install -c conda-forge pre-commit
pre-commit sample-config > .pre-commit-config.yaml
pre-commit install
pre-commit run --all-files
```

## Configuring your `pre-commit`

While the default set is nice, you might want to install other hooks.

For example, a Python project
might want to default to using `black` as the code formatter.
To enable automatic `black` formatting _and_ checking before committing code,
we need to add `black` to the configuration file that was produced
(`.pre-commit-config.yaml`).

```yaml
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
```

A classic mistake that I made was to add black directly underneath the default:

```yaml
# THIS IS WRONG!!!
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
    -   id: black  # THIS IS WRONG!!!
```

You will get an error if you do this. Be forewarned!

## Updating your pre-commit after updating `.pre-commit-config.yaml`

If you forgot to add a hook but have just edited the YAML file to do so,
you will need to run the command to install the hooks.

```bash
pre-commit install-hooks
#  Optional
pre-commit run --all-files
```

Now, the new hooks will be installed.

## What happens when you use pre-commit

As soon as you write your commit your source files,
just before the commit happens,
your installed pre-commit hooks execute.
If the hooks modify any files,
then the commit is halted,
and the files that were modified will show up as being "modified"
or "untracked"
in your git status.

At this point, add the files that were modified by your pre-commit hooks,
commit those files,
and re-enter your commit message.
In this way, you will prevent yourself from committing code
that does not pass your code checks.

## Good pre-commit hooks for Python projects

My opinionated list of nice hooks to have can be found below.

- black
- pydocstyle
- isort

## Benefits of setting up pre-commit (and hooks)

By setting up a standard configuration that gets checked into source control,
we are setting our team up for success working together.
Opinionated checks are now delegated to automated machinery
rather than requiring human intervention,
hence freeing us up to discuss higher order issues
rather than nitpicking on code style.

Moreover, by using the `pre-commit` framework, we take a lot of tedium out
in setting up the pre-commit git hooks correctly.
I've tried to do that before, and found writing the bash script to be
a fragile task to execute.
It's fragile because I'm not very proficient in Bash,
and I have no other way of testing the git pre-commit hooks
apart from actually making a commit.
Yet, it seems like we should be able to modularize our hooks,
such that they are distributed, installed, and executed in a standard fashion.
This is what the pre-commit framework gives us.

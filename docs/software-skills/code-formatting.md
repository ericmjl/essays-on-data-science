# Formatting your code

One key insight from the Python programming language
is that code is read more often than it is written.
Hence, writing code in a fashion that makes it easy to read
is something that can only be beneficial.

But formatting code is a nit-picky and tedious matter, isn't it?
Moreover, code style is one of those things that are not substantive enough
to engage in flame wars.
It really is one of those things we should just get over with, right?

Yes, and it is possible to be "just over and done with it"
if we use automation tools to help us take care of code formatting
so that we don't have to think about it.

## Introducing `black`

`black` is an opinionated code formatter for the Python programming language.
It comes with sane defaults,
and produces consistently formatted code with a single command at the terminal.

### Installing `black`

To install it, we can either use `pip` or `conda`:

```bash
# for pip users
pip install black
# for conda users
conda install black
```

### Using `black`

We can use black directly at the command line in our project directory,
with configurations called at the command line for convenience.

```bash
# Format all .py files within and underneath current working directory.
black -l 79 .
```

## Introducing `isort`

`isort` is a package for sorting your imports in a source `.py` file.
Once again, this is the sort of thing
you definitely don't want to do by hand.

### Installing `isort`

`isort` is also conda- and pip-installable.

```bash
# pip users
pip install isort
# conda users
conda install isort
```

### Using `isort`

Just like with black, we can use `isort` to automagically sort our imports.
As an example we will call it at the command line with certain options enabled.

```bash
# -r: recurses down below the current working directory.
# -y: automatically overwrite original source file with sorted imports.
isort -r -y .
```

## Building automation for code formatting

Automatically executing automagic commands is pretty awesome.
Let's see how we can enable this.

### Makefiles

I also place `black` as part of a series of commands used in code style checking
in a Makefile, to run all of those commands together.

```makefile
format:
    isort -r -y .
    black -l 79 .
```

With that Makefile command,
we can now execute all code formatting commands with a single call.

_Side note:_ I usually do `isort` first
because `black` will make detect `isort`-ed code as not properly formatted,
hence I defer to `black` to make the final changes.

### Pre-commit hooks

We can also use pre-commit hooks to catch non-properly-formatted code,
and run the code formatters over the code,
preventing them from being merged if any formatting has to take place.
This ensures thatwe never commit code that is incorrectly formatted.

Getting set up with pre-commit hooks is another topic,
but there are already great resources that can be searched for online
on how to get setup.

## Concluding words

I hope this short essay gives you an overview
of the tools that you can use to format your code automatically.
Code formatting is important for readability,
but isn't worth the tedium.
Letting automation save your time is the wise thing to do.

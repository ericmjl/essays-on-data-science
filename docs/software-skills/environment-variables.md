# A Data Scientist's Guide to Environment Variables

You might have encountered a piece of software asking you for permission to modify your `PATH` variable,
or another program's installation instructions cryptically telling you
that you have to "set your `LD_LIBRARY_PATH` variable correctly".

As a data scientist, you might encounter other environment variable issues
when interacting with your compute stack
(particularly if you don't have full control over it, like I do).
This post is meant to demystify what an environment variable is,
and how it gets used in a data science context.

## What Is An Environment Variable?

First off, let me explain what an environment variable is,
by going in-depth into the `PATH` environment variable.
I'd encourage you to execute the commands here inside your bash terminal
(with appropriate modifications -- read the text to figure out what I'm doing!).

When you log into your computer system, say,
your local computer’s terminal or your remote server via SSH,
your bash interpreter needs to know where to look for particular programs,
such as `nano` (the text editor), or `git` (your version control software),
or your Python executable. This is controlled by your PATH variable.
It specifies the paths to folders where your executable programs are found.

By historical convention, command line programs,
such as `nano`, `which`, and `top`,
are found in the directory `/usr/bin`.
By historical convention, the `/bin` folder is for software binaries,
which is why they are named `/bin`.
These are the ones that are bundled with your operating system,
and as such, need special permissions to upgrade.

Try it out in your terminal:

```
$ which which
/usr/bin/which
$ which top
/usr/bin/top
```

Other programs are installed (for whatever reason) into `/bin` instead. `ls` is one example:

```
$ which ls
/bin/ls
```

Yet other programs might be installed in other special directories:

```
$ which nano
/usr/local/bin/nano
```

How does your Bash terminal figure out where to go to look for stuff?
It uses the `PATH` environment variable.
It looks something like this:

```
$ echo $PATH
/usr/bin:/bin:/usr/local/bin
```

The most important thing to remember about the `PATH` variable is that it is "colon-delimited".
That is, each directory path is separated by the next using a "colon" (`:`) character.
The order in which your bash terminal is looking for programs goes from left to right:

- `/usr/bin`
- `/bin`
- `/usr/local/bin`

On my particular computer, when I type in `ls`,
my bash interpreter will look inside the `/usr/bin` directory first.
It'll find that `ls` doesn't exist in `/usr/bin`,
and so it'll move to the next directory, `/bin`.
Since my `ls` exists under `/bin`,
it'll execute the `ls` program from there.

You can see, then, that this is simultaneously super flexible for customizing your compute environment,
yet also potentially super frustrating if a program modified your `PATH` variable without you knowing.

Wait, you can actually modify your `PATH` variable? Yep, and there's a few ways to do this.

## How To Modify the `PATH` variable

### Using a Bash Session

The first way is transient, or temporary, and only occurs for your particular bash session.
You can make a folder have higher priority than the existing paths by "pre-pending" it to the `PATH` variable:

```
$ export PATH=/path/to/my/folder:$PATH
$ echo $PATH
/path/to/my/folder:/usr/bin:/bin:/usr/local/bin
```

Or I can make it have a lower priority than existing paths by "appending" it to the `PATH` variable:

```
$ export PATH=$PATH:/path/to/my/folder
$ echo $PATH
/usr/bin:/bin:/usr/local/bin:/path/to/my/folder
```

The reason this is temporary is because I only export it during my current bash session.

### `bashrc` or `.bash_profile` File

If I wanted to make my changes somewhat more permanent,
then I would include inside my `.bashrc` or `.bash_profile` file.
(I recommend using the `.bashrc` file.)
The `.bashrc`/`.bash_profile` file lives inside your home directory
(your `$HOME` environment variable specifies this),
and is a file that your bash interpreter will execute first load.
It will execute all of the commands inside there.
This means, you can change your PATH variable by simply putting inside your `.bashrc`:

```
...other stuff above...
# Make /path/to/folder have higher priority
export PATH=/path/to/folder:$PATH

# Make /path/to/other/folder have lower priority
export PATH=$PATH:/path/to/folder
...other stuff below...
```

## Data Science and the `PATH` environment variable

Now, **how is this relevant to data scientists?**
Well, if you're a data scientist, chances are that you use Python,
and that your Python interpreter comes from the Anaconda Python distribution
(a seriously awesome thing, go get it!).
What the Anaconda Python installer does is prioritize
the `/path/to/anaconda/bin` folder in the `PATH` environment variable.
You might have other Python interpreters installed on your system
(that is, Apple ships its own).
However, this `PATH` modification ensures that
each time you type `python` into your Bash terminal,
ou execute the Python interpreter shipped with the Anaconda Python distribution.
In my case, after installing the Anaconda Python distribution, my `PATH` looks like:

```
$ echo $PATH
/Users/ericmjl/anaconda/bin:/usr/bin:/bin:/usr/local/bin
```

Even better, what conda environments do is
prepend the path to the conda environment binaries folder
while the environment is activated.
For example, with my blog, I keep it in an environment named `lektor`.
Thus...

```
$ echo $PATH
/Users/ericmjl/anaconda/bin:/usr/bin:/bin:/usr/local/bin
$ which python
/Users/ericmjl/anaconda/bin/python
$ source activate lektor
$ echo $PATH
/Users/ericmjl/anaconda/envs/lektor/bin:/Users/ericmjl/anaconda/bin:/usr/bin:/bin:/usr/local/bin
$ which python
/Users/ericmjl/anaconda/envs/lektor/bin/python
```

Notice how the bash terminal now preferentially picks the Python inside the higher-priority `lektor` environment.

If you've gotten to this point, then you'll hopefully realize there's a few important concepts listed here. Let's recap them:

- `PATH` is an environment variable stored as a plain text string used by the bash interpreter to figure out where to find executable programs.
- `PATH` is colon-delimited; higher priority directories are to the left of the string, while lower priority directories are to the right of the string.
- `PATH` can be modified by prepending or appending directories to the environment variable. It can be done transiently inside a bash session by running the `export` command at the command prompt, or it can be done permanently across bash sessions by adding an `export` line inside your `.bashrc` or `.bash_profile`.

## Other Environment Variables of Interest

Now, what other environment variables might a data scientist encounter? These are a sampling of them that you might see, and might have to fix, especially in contexts where your system administrators are off on vacation (or taking too long to respond).

### General Use

For general use**, you'll definitely want to know where your `HOME` folder is -- on Linux systems, it's often `/home/username`, while on macOS systems, it's often `/Users/username`.  You can figure out what `HOME` is by doing:

```
$ echo $HOME
/Users/ericmjl
```

### Python

**If you're a Python user**,
then the `PYTHONPATH` is one variable that might be useful.
It is used by the Python interpreter,
and specifies where to find Python modules/packages.

### C++ libraries

**If you have to deal with C++ libraries**,
then knowing your `LD_LIBRARY_PATH` environment variable is going to be very important.
I'm not well-versed enough in this to espouse on it intelligently,
so I would defer to [this website](http://xahlee.info/UnixResource_dir/_/ldpath.html)
for more information on best practices for using the `LD_LIBRARY_PATH` variable.

### Spark

**If you're working with Spark**,
then the `PYSPARK_PYTHON` environment variable would be of interest.
This essentially tells Spark which Python to use for both its driver and its workers;
you can also set the `PYSPARK_DRIVER_PYTHON`
to be separate from the `PYSPARK_PYTHON` environment variable, if needed.

### Data science apps

**If you're developing data science apps**,
then according to the [12 factor app development principles](https://12factor.net),
your credentials to databases and other sensitive information
are securely stored and dynamically loaded into the environment at runtime.
How then do you mimic this in a "local" environment (i.e. your computer)
without hard-coding sensitive information in your source `.py` files?

One way to handle this situation is as follows:
Firstly, create a `.env` file in your home directory.
In there, store your credentials:

```bash
SOME_PASSWORD="put_your_pw_here"
SOME_USERNAME="put_your_username_here"
```

Next, add it to your `.gitignore`, so you never add it to your version control system.

```bash
# other things
.env
```

Finally, in your source `.py` files, use `python-dotenv` to load the environment variables at runtime.

```python
from dotenv import load_dotenv
load_dotenv()

import os

username = os.getenv("SOME_USERNAME")
password = os.getenv("SOME_PASSWORD")
```

## Hack Your Environment Variables

This is where the most fun happens!
Follow along for some stuff you might be able to do
by hacking your environment variables.

### Hack #1: Enable access to PyPy.

I occasionally keep up with the development of PyPy,
but because PyPy is not yet the default Python interpreter,
and is not yet `conda install`-able,
I have to put it in its own `$HOME/pypy/bin` directory.
To enable access to the PyPy interpreter,
I have to make sure that my `/path/to/pypy` is present
in the `PATH` environment variable,
but at a lower priority than my regular CPython interpreter.

### Hack #2: Enable access to other language interpreters/compilers.

This is analogous to PyPy.
I once was trying out Lua's JIT interpreter to use Torch for deep learning,
and needed to add a path to there in my `.bashrc`.

### Hack #3: Install Python packages to your home directory.

On shared Linux compute systems that use the `modules` system
rather than `conda` environments,
a `modulefile` that you load might be configured
with a virtual environment that *you don't have permissions to modify*.
If you need to install a Python package,
you might want to `pip install --user my_pkg_name`.
This will install it to `$HOME/.local/lib/python-[version]/site-packages/`.
Ensuring that your `PYTHONPATH`
includes `$HOME/.local/lib/python-[version]/site-packages`
at a high enough priority is going to be important in this case.

### Hack 4: Debugging when things go wrong.

In case something throws an error,
or you have unexpected behaviour --
something I encountered before was my Python interpreter
not being found correctly after loading all of my Linux modules --
then a way to debug is to temporarily set your PATH environment variable
to some sensible "defaults" and sourcing that,
effectively "resetting" your PATH variable,
so that you can manually prepend/append while debugging.

To do this, place the following line inside a file named `.path_default`,
inside your home directory:

```
export PATH=""  # resets PATH to an empty string.
export PATH=/usr/bin:/bin:/usr/local/bin:$PATH  # this is a sensible default; customize as needed.
```

After something goes wrong,
you can reset your PATH environment variable by using the "source" command:

```
$ echo $PATH
/some/complicated/path:/more/complicated/paths:/really/complicated/paths
$ source ~/.path_default
$ echo $PATH
/usr/bin:/bin:/usr/local/bin
```

Note - you can also execute the exact same commands inside your bash session;
the interactivity may also be helpful.

## Conclusion

I hope you enjoyed this article, and that it'll give you a, ahem,
path forward whenever you encounter these environment variables!

## Thank you for reading!

If you enjoyed this essay and would like to receive early-bird access to more,
[please support me on Patreon][patreon]!
A coffee a month sent my way gets you _early_ access to my essays
on a private URL exclusively for my supporters
as well as shoutouts on every single essay that I put out.

[patreon]: https://patreon.com/ericmjl

Also, I have a free monthly newsletter that I use as an outlet
to share programming-oriented data science tips and tools.
If you'd like to receive it, sign up on [TinyLetter][tinyletter]!

[tinyletter]: https://tinyletter.com/ericmjl

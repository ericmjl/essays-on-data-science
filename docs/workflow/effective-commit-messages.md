# Effective Git Commits in Data Science

Continuing on the theme of the use of Git in data science,
I thought I would write about how to use git commits effectively
in our day-to-day data science work.

## How `git` commits are intended to be used

Git commits are intended to be used as a running log
of what gets checked into a code repository.
In software engineering,
each commit is intended to be a “logical unit of work”.

One intent behind defining a commit as a “logical unit of work”
is that in case that logical unit of work turned out to be faulty,
we can revert that unit of work and _only_ that unit of work
without touching other units of work.

Git commits can also help us track who made contributions to a repository,
as each commit also contains information about the committer
(e.g. name and email address).

We can view the commit history at the terminal
by typing the following incantation:

```bash
git log --decorate --graph
```

That will give us an interface to the commit log.
It will show a running log of the commits to the project,
as well as every commit message that was put in.
Writing commit messages
as if we're going to read them at a later date in reverse sequential order
can help us write better commit messages.

## `git` commits in analysis-heavy projects

In the software world, `git` commits are a logical way to work.
By comparison, in data analysis-heavy work,
it is seemingly more difficult to define
a “logical unit of work” thank we might in software engineering.

After all,
what exactly constitutes a “logical unit” of work in data analytics?
Is it the answering of a question?
That might yield commits/changes that are very large.
Is it a software change?
That might yield commits/changes that are too small.
Admittedly, there is a bit of an art to getting this right.

Here, I think treating `git` commits more as a "log of work done"
and less of "report of work done"
might be helpful in adapting `git` as a lab notebook-style log book.

### Effective `git` commits

But before we describe how, a few preliminaries are in order.
L et’s take a look at
what effective and informative commit messages accomplish:

**Firstly**, if we are committing something that is work-in-progress
(and yes, this should be permitted, because end-of-day always rolls by),
a commit message can mark the fact that there is still work to be done,
and describe enough prose to resume context the next day.

**Secondly**, when used in tandem with a timeline,
an informative commit message lets us quickly isolate when work was done,
thus allowing us to retrace the progression of the project.

**Finally**,
good commit messages allow others we collaborate with
to get a handle on the work that was already done.
Well-written `git` commit messages can help colleagues that review our work
get quickly up-to-speed on what was done, and what to review.

In other words,
effective commit messages act like documentation
for our future selves and for others.
Once again, the “social coding” paradigm comes back.

??? question "Social coding?"

    Social coding:
    where we aren’t programming something alone,
    but rather writing code in collaboration with others’ input.
    OSS development is a wonderful example of this.

## `git` commit messages: examples in data science contexts

Let’s see a few examples in action.

### The Trivial Change Message

If we applied trivial changes,
such as code formatting,
rather than writing a message that read:

???+ failure "Don't do this"

    ```text
    black
    ```

Perhaps a a more informative message might be:

???+ success "Do this"

    ```text
    Applied code formatting (make format).
    ```

We don’t need an extended message (unlike those we might see later), because it is a trivial change.

Now, I have been guilty of just writing `black` as the commit message,
but usually that is in the context where I am working on my own project alone.
Keeping in mind that commit messages are intended to be read by others,
the more informative version is clearer to read
and only takes practice to become second nature.

### The Work-In-Progress (WIP) Message

Sometimes, the end of the day rolls by just like that,
or we realize we have a mid-afternoon meeting to attend
(these are, _the wurst_ sausages!).
In those scenarios, putting in a WIP commit may be helpful.

So instead of writing a commit message that reads:

???+ failure "Don't do this"

    ```text
    WIP loaded data
    ```


We instead can write a commit message that reads:

???+ success "Do this"

    ```text
    WIP finished code that loads data into memory

    We still need to do the following:

    - Check statistical covariation between columns
            and remove correlated features.
    - Identify the best predictors.
    ```

Now, when we look at the `git log`,
we will see something that looks like this
right at the top of our development branch:

```
* commit abe3d2e8ed55711a57835d96e67207aa2f07f383 (HEAD -> feature-branch)
| Author: Me <abc@xyz.com>
| Date:   Fri Nov 15 14:01:13 2019 -0500
|
|     WIP finished code that loads data into memory
|
|     We still need to do the following:
|
|     - Check statistical covariation between columns and remove correlated features.
|     - Identify the best predictors.
|
* commit ...
```

In this way, the `git` commit log gives us a way
to use it as a “lab notebook”-style running log of what’s we have done.

### The Report on Progress

Pedantically,
this is distinguished from the WIP message described above
by being a “final” (but not necessarily binding) message in the work log.

An uninformative commit message for this would look like:

???+ failure "Don't do this"

    ```text
    Finally done with model building
    ```

By contrast, an informative one might look something like this:

???+ success "Do this"

    ```text
    Model building (Issue #34) ready for review

    Finished:

    - Pipeline taking data from input (strings) to activity prediction.
    - Custom code for data pipeline has been stored in custom package.
        Tests and docs written.
    - Notebooks documenting work are also written.
        Static HTML version for archival also generated.

    Not done:

    - Hyperparameter selection.
        This is the logical next step,
        and as agreed at last meeting, of highest priority.
    ```text

Admittedly, it can be tough to know when to write this one,
and I think it’s because it _feels_ like
we might want to be sure that this is _absolutely_ the place
that we _actually_ want to write such a message.

To this, I would suggest
simply commit (pun intended) to writing it when appropriate,
and worry about minor things in later commits.

## Squashed commits

If we squash commits in our `git` workflow (e.g. when merging branches),
then writing such detailed commit messages might seem unnecessary.
To which my response is, yes indeed!
In the case of using squashed commits
really only the final commit message
ends up being stored in the running log of what gets done.
Hence, it makes perfect sense to focus writing good commit messages
only at the merge stage,
rather than at every single commit.

## Intentional adoption of better commit messages

As I have observed with my own and colleagues’ workflows,
we do not regularly write informative commit messages
because we don’t read the git log.
Then again, we don’t read the git log
because it doesn’t contain a lot of information.

Hold on, that sounds kind of circular, doesn’t it?

I think the chicken-and-egg cycle at some point has to be broken.
By starting at _some_ point,
we break a vicious cycle of uninformative logging,
and allow us to break into a virtuous cycle of good record-keeping.
And that really is what this essay is trying to encourage:
**better record-keeping!**

## Further Reading

1. [How to Write a Git Commit Message][git-chrisbeams]
by [Chris Beams][chrisbeams].

[git-chrisbeams]: https://chris.beams.io/posts/git-commit/
[chrisbeams]: https://chris.beams.io/

??? note "A note to Chris"

    Thank you for writing a wonderful article.
    I'll be praying for a speedy recovery, Chris.

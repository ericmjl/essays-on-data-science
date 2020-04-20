# A Review of the Python Data Science Dashboarding Landscape in 2019

## Introduction

As Pythonista data scientists,
we are spoiled for choice when it comes to developing front-ends
for our data apps.
We used to have to fiddle with HTML in Flask (or Plotly's Dash),
but now, there are tools in which
"someone wrote the HTML/JS so I didn't have to".

Let me give a quick tour of the landscape of tools
as I've experienced it in 2019.

### Beginnings: Voila

Previously, I had test-driven
[Voila](https://voila.readthedocs.io/en/latest/).
The key advantage I saw back then was that in my workflow,
once I had the makings of a UI present in the Jupyter notebook,
and just needed a way to serve it up
independent of having my end-users run a Jupyter server,
then Voila helped solve that use case.
By taking advantage of existing the `ipywidgets` ecosystem
and adding on a way to run and serve the HTML output of a notebook,
Voila solved that part of the dashboarding story quite nicely.
In many respects,
I regard Voila as the first proper dashboarding tool for Pythonistas.

That said, development in a Jupyter notebook
didn't necessarily foster best practices
(such as refactoring and testing code).
When my first project at work ended,
and I didn't have a need for further dashboarding,
I didn't touch Voila for a long time.

### Another player: Panel

Later, [Panel](http://panel.pyviz.org/) showed up.
Panel's development model allowed a more modular app setup,
including importing of plotting functions defined inside `.py` files
that returned individual plots.
Panel also allowed me to prototype in a notebook and see the output live
before moving the dashboard code into a source `.py` file.

At work, we based a one-stop shop dashboard for a project on Panel,
and in my personal life,
I also built a
[minimal panel app](https://github.com/ericmjl/minimal-panel-app)
that I also
[deployed to Heroku](https://minimal-panel-app.herokuapp.com/).
Panel was definitely developed
targeting notebook and source file use cases in mind,
and this shows through in its source development model.

That said, panel apps could be slow to load,
and without having a "spinner" solution in place
(i.e. something to show the user
that the app is "doing something" in the background),
it sometimes made apps _feel_ slow
even though the slowness was not Panel's fault really.
(My colleagues and I pulled out all the tricks in our bag to speed things up.)

Additionally, any errors that show up don't get surfaced to the app's UI,
where developer eyeballs are on -
instead, they get buried in the browser's JavaScript console
or in the Python terminal where the app is being served.
When deployed, this makes it difficult to see where errors show up
and debug errors.

### Enter Streamlit

Now, Streamlit comes along, and some of its initial demos are pretty rad.
In order to test-drive it,
I put together this [little tutorial](https://minimal-streamlit.herokuapp.com/)
on the Beta probability distribution for my colleagues.

Streamlit definitely solves some of the pain points
that I've observed with Panel and Voila.

The most important one that I see is that errors are captured by Streamlit
and bubbled up to the UI,
where our eyeballs are going to be when developing the app.
For me, this is a very sensible decision to make, for two reasons:

Firstly, it makes debugging interactions that much easier.
Instead of needing to have two interfaces open,
the error message shows up right where the interaction fails,
in the same browser window as the UI elements.

Secondly, it makes it possible for us
to use the error messages as a UI "hack" to inform users
where their inputs (e.g. free text) might be invalid,
thereby giving them _informative error messages_.
(Try it out in the Beta distribution app:
it'll give you an error message right below
if you try to type something that cant be converted into a float!)

The other key thing that Streamlit provides as a UI nice-ity
is the ability to signal to end-users that a computation is happening.
Streamlit does this in three ways, two of which always come for free.
**Firstly**, if something is "running",
then in the top-right hand corner of the page,
the "Running" spinner will animate.
**Secondly**, anything that is re-rendering will automatically be greyed out.
**Finally**, we can use a special context manager
to provide a custom message on the front-end:

```python
import streamlit as st
with st.spinner("Message goes here..."):
    # stuff happens
```

So all-in-all, Streamlit seems to have a solution of some kind
for the friction points that I have observed with Panel and Voila.

Besides that, Streamlit, I think, uses a procedural paradigm,
rather than a callback paradigm, for app construction.
We just have to think of the app as a linear sequence of actions
that happen from top to bottom.
State is never really an issue, because every code change
and interaction re-runs the source file from top to bottom, from scratch.
When building quick apps,
this paradigm really simplifies things compared to a callback-based paradigm.

Finally, Streamlit also provides a convenient way to add text to the UI
by automatically parsing as Markdown any raw strings unassigned to a variable
in a `.py` file and rendering them as HTML.
This opens the door to treating a `.py` file as a
[literate programming document](https://en.wikipedia.org/wiki/Literate_programming),
hosted by a Python-based server in the backend.
It'd be useful especially in teaching scenarios.
(With `pyiodide` bringing the PyData stack to the browser,
I can't wait to see standalone `.py` files rendered to the DOM!)

Now, this isn't to say that Streamlit is problem-free.
There are still rough edges,
the most glaring (as of today) in the current release
is the inability to upload a file and operate on it.
This has been fixed in [a recent pull request](https://github.com/streamlit/streamlit/pull/488),
so I'm expecting this should show up in a new release any time soon.

The other not-so-big-problem that I see with Streamlit at the moment
is the procedural paradigm -
by always re-running code from top-to-bottom afresh on every single change,
apps that rely on long compute may need a bit more thought to construct,
including the use of Streamlit's caching mechanism.
Being procedural does make things easier for development though,
and on balance, I would not discount Streamlit's simplicity here.

## Where does Streamlit fit?

As I see it, Streamlit's devs are laser-focused on enabling devs
to _very quickly_ get to a somewhat good-looking app prototype.
In my experience, the development time for the Beta distribution app
took about 3 hours, 2.5 of which were spent on composing prose.
So effectively, I only used half an hour doing code writing,
with a live and auto-reloading preview
greatly simplifying the development process.
(I conservatively estimate that this is about 1.5 times
as fast as I would be using Panel.)

Given Streamlit, I would use it to develop two classes of apps:
(1) very tightly-focused utility apps that do one lightweight thing well, and
(2) bespoke, single-document literate programming education material.

I would be quite hesitant to build more complex things;
then again, for me, that statement would be true more generally anyways
with whatever tool.
In any case, I think bringing UNIX-like thinking to the web
is probably a good idea:
we make little utilities/functional tools
that can pipe standard data formats from to another.

## Common pain points across all three dashboarding tools

A design pattern I have desired is to be able to serve up a fleet of small,
individual utilities served up from the same codebase,
served up by individual server processes,
but all packaged within the same container.
The only way I can think of at the moment
is to build a custom Flask-based gateway
to redirect properly to each utility's process.
That said, I think this is probably out of scope
for the individual dashboarding projects.

## How do we go forward?

The ecosystem is ever-evolving, and,
rather than being left confused by the multitude of options available to us,
I find myself actually being very encouraged
at the development that has been happening.
There's competing ideas with friendly competition between the developers,
but they are also simultaneously listening to each other and their users
and converging on similar things in the end.

That said, I think it would be premature to go "all-in" on a single solution
at this moment.
For the individual data scientist,
I would advise to be able to build something
using each of the dashboarding frameworks.
My personal recommendations are to know how to use:

- Voila + `ipywidgets` in a Jupyter notebook
- Panel in Jupyter notebooks and standalone `.py` files
- Streamlit in `.py` files.

These recommendations stem mainly from
the ability to style and layout content without needing much knowledge of HTML.
In terms of roughly when to use what,
my prior experience has been that
Voila and Streamlit are pretty good for quicker prototypes,
while Panel has been good for more complex ones,
though in all cases, we have to worry about speed impacting user experience.

From my experience at work,
being able to quickly hash out key visual elements in a front-end prototype
gives us the ability to better communicate with UI/UX designers and developers
on what we're trying to accomplish.
Knowing how to build front-ends ourselves
lowers the communication and engineering barrier
when taking a project to production.
It's a worthwhile skill to have;
be sure to have it in your toolbox!

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

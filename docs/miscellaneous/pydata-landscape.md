# An Opinionated and Unofficial Guide to the PyData Ecosystem

Last Updated: 30 May 2020

This essay is the culmination of many years
of learning to navigate the PyData ecosystem.
Other data science ecosystems appear to have a major supportive entity,
for example the R world has RStudio putting brain power and personnel
into software and community development.
Julia also has one, Julia Computing.
The Python world, by contrast, seems a bit more fragmented,
with a myriad of large and small groups;
highly famed individuals and other individuals toiling quietly in the background;
commercial and not-for-profit entities developing tools together, and more.
What is considered “standard”
and perhaps the “one and preferably only one way of doing something”
sometimes isn’t entirely clear.

In addition, given the age of the language and its growth
during the _Homo interconnectus_ era,
ways of “doing things” have evolved over time,
and yet vestiges of the past lurk all over the place on the internet.
For example, the `matplotlib` `pylab` API has been long deprecated,
but a newcomer who stumbles upon an old StackOverflow Q&A
may not know better if they see the now-deprecated line,
`from pylab import *`.

The combination of longevity and diversity
means navigating the Python data science ecosystem
can sometimes be intimidating for someone
who is used to a more unified ecosystem.
A colleague of mine who moved from Matlab to R
found RStudio’s open source approach refreshing
(and yes, I really dig what they’re doing as a Public Benefit Corporation too!),
but when he dipped his toes into the Python world,
he found the Python world a bit like the “Wild Wild West” -
confusing, to say the least.

## The keys to navigating the PyData world

Personally, I think that one of the keys to navigating the PyData ecosystem
is to discard the “one vendor and tool to rule them all” mentality,
and to embrace the fact that you can glue (almost) anything you want together.
In other words, to _embrace the latent hacker inside of you_.
Every person is a hacker at heart;
we MacGyver/improvise all the time,
and it’s no different when we do modern development of software.

Another key to navigating the PyData world
is to recognize that it is comprised of a collection
of wonderfully talented individuals who are using the language
to solve a myriad of problems,
and that open source tools are often a byproduct of this creative energy.
The corollary is that every tool is geared
with a bias towards the particular problems
that the author was originally solving.
If you find your use cases are similar, that’s great!
And if you find that you use cases are not similar,
the right way to approach the community is to either
(1) work with package authors to improve their tool,
(2) develop patches/workarounds around that tool,
(3) or develop and release your own.
Disparaging another tool
just because it doesn't work the way you think it does
should never be on your list of appropriate actions.
I would call you an “insecure bro” if you do that.

## How to use this essay?

Alright, with those preface words in place,
you probably came to this essay
because you want a “map” of where to go when you want to do stuff.
That will be the structure of this essay;
I will intentionally keep descriptions of tools and packages high-level.
My goal here is to illuminate the variety of packages
and their associated practical contexts in which they get used.

I will structure the essay in terms of "what should I use to do X",
or "where should I go to do Y".

Use the right navigation bar
to find the question that you're interested in having answered.
If you can't find the exact thing, use the search bar above.
And if you still can't find the thing you're interested in learning about,
send me a question on the Issue Tracker for this repository!

## What do I do when I want to...

### What should I use to handle tabular/structured data?

If your data are small enough to fit in RAM,
`pandas`](https://pandas.pydata.org/) should be your “go-to” package.
Its API has become a community idiom,
and lots of derivative packages target
the `pandas` API for drop-in compatibility.
Also, it’s just hit version 1.0! (Happy birthday, Pandas!)

Amongst the derivative packages include:

- [`dask`](https://docs.dask.org/en/latest/dataframe.html)
- [`vaex`](https://vaex.readthedocs.io/en/latest/) both provide a scalable DataFrame API.
- [`modin`](https://github.com/modin-project/modin) also scales the `pandas` API.

Building on top of the `pandas` API,
I ported over the `janitor` R package functions
to [`pyjanitor`](https://pyjanitor.readthedocs.io/),
to provide convenient data cleaning functions that one can “chain”.
It’s now grown to the point
where multiple individuals have made
their first open source contributions through the project!

### Which plotting packages should I use?

[`matplotlib`](https://matplotlib.org/) is the workhorse package
that has been steadily evolving for a very long time!
It was also the first one that I picked up for general purpose plotting.
Because it provides a lot of low-level plotting components,
it is extremely powerful and flexible.
I also made my first open source contribution through the package,
in which I helped rework the examples to use the `pyplot` API
rather than the deprecated `pylab` API.
Even today, I still use it for highly bespoke and customized plotting;
its SVG output also makes for `git` diff-able figures too!

For a convenient statistical visualization API,
[`seaborn`](https://seaborn.pydata.org/) is where you would want to go.
It provides the ability to do faceting, pair plots, and more,
using a declarative API that interoperates nicely with `pandas`.

To go to web plotting,
[Bokeh](https://docs.bokeh.org/en/latest/index.html),
[HoloViews](http://holoviews.org/),
[Altair](https://altair-viz.github.io/)
and [Plotly](https://plotly.com/python/statistical-charts/)
are where you probably would want to head to.
[hvPlot](https://hvplot.holoviz.org/) is the sibling package to HoloViews,
providing a high-level plotting API.

Everything is moving quickly in the “Python web plotting” space,
so the best way to invest in yourself is to know how to read code
from each of the libraries.
HoloViews and hvPlot are part of
the [`pyviz`](https://pyviz.org/) ecosystem of packages
supported and developed by Anaconda developers.
(I ❤️ what Anaconda has been doing all this while!)

### What tools should I use for dashboarding?

The original thing I would have done to build a dashboard
is to program a Flask app,
write HTML templates and style it with custom CSS,
and inject plot figures as base64-encoded strings
or Bokeh plots.
Thankfully, those days are over now!

The key thing you’ll want to look for in a dashboarding package
is a set of _widgets_ that you can program interactions on,
as well as tools to display visualizations on the interface.
Here’s an overview of the tools that I’ve worked with.

Firstly,
[Voila](https://github.com/voila-dashboards/voila)
builds upon the Jupyter `ipywidgets` ecosystem,
and allows a data scientist to compose prose and widgets together
while staying within the Jupyter notebook environment.
Voila, in my opinion, is “_l’original_” of dashboard tooling.

[Panel](http://panel.pyviz.org/),
which comes from the PyViz ecosystem of packages,
uses the Bokeh ecosystem of widgets.
This piece of history makes sense
only in light of the packages being developed originally at Anaconda.
The Panel devs, however, are now also building in `ipywidgets` interoperability.
Panel allows you to move outside of the Jupyter notebook to build apps.

[Streamlit](https://docs.streamlit.io/) is another dashboard creation package
that embraces the “scripting” mindset.
Streamlit apps are essentially one long Python script
that is continually executed from top to bottom
(not unlike what we would expect from a Jupyter notebook).
Streamlit apps give you an extremely fast path
to realize your idea as a prototype;
because of its idioms, it is my current “go-to” tool.

From personal experience, Streamlit has helped me go fast from idea to prototype.
However, its programming idioms encourage
a “dump everything into the script” programming style,
which may make apps harder to maintain and modify long-term.
Panel and Voila encourage the more modular style of programming,
but that slows me down to getting a prototype stood up.
It seems the tradeoff lies not in the package _per se_,
but in the programming model for building UIs.

The other package that I have not yet used
is Plotly’s [Dash](https://plotly.com/dash/).
From my colleagues’ description, it plays very nicely with HTML standards,
so for production systems that require branding
because they are external, client-facing, this might be a great way to go.
(I, on the other hand,
happen to not work on data products that require a branding.)

### How do I deploy my dashboard app?

Deploying a dashboard app usually means you need a place to host it separate from the machine on which you do your exploratory project work.

The key idea here is to use a platform as a service, or to use a Docker container.

If your company provides a PaaS,
such as a Heroku-like service (they are the originals!),
then you should be using it!
With a PaaS, you _declare_ the resources that you need for your app
using configuration files,
and let the PaaS system reproducibly build exactly what you've declared
_on every push to your `master` branch_!
Doing things this way seriously simplifies the deployment of your dashboard app.

If your company doesn't provide a PaaS,
then I would recommend figuring out how to use Docker.
Docker itself won't allow you to deploy the app on a separate computer
(you need other tooling
and possibly will have to work with your DevOps team
to get containers deployed to the web),
but it _will_ at least get you a build of your project
that is isolated from your _development_ environment.

### What packages should I use for machine learning?

Thankfully, the community has really coalesced around `scikit-learn`,
with many packages going as far as adopting its API idioms.
(Adopting and conforming to API idioms is a _good_ thing!
Don't let Oracle's lawsuit against Google fool you otherwise.)
For the vast majority of ML problems
(which don’t really need deep learning methods),
`scikit-learn` should be your go-to package.

The ecosystem of packages that all adopt `scikit-learn`'s APIs include:

- [XGBoost](https://xgboost.readthedocs.io/en/latest/)
- [CatBoost](https://catboost.ai)
- [TPOT](http://epistasislab.github.io/tpot/): AutoML on top of scikit-learn
- [PyCaret](https://pycaret.org): low-code machine learning on top of `scikit-learn`-compatible packages.

At this point, I usually default to PyCaret to get baseline models quickly set up.
It is basically painless and automates many routine tasks
that I would otherwise end up writing many lines of code for.

### Tensor and Deep Learning Libraries

Those who know me well enough will know that I'm a fan of community standard APIs.
So when it comes to Tensor computing,
I naturally will first recommend the packages that _play nicely with one another_.
Here, there are obvious ones:

- [NumPy](https://numpy.org): the workhorse! Also basically evolving into a community-standard API.
- [CuPy](https://cupy.chainer.org): NumPy API on GPUs
- [Dask Arrays](https://docs.dask.org/en/latest/array.html): Distributed CPU and GPU arrays
- [JAX](https://jax.readthedocs.io): NumPy on CPU, GPU and TPU, plus automatic differentiation as a first-class citizen!

In particular, I want to highlight JAX.
It's non-trivial to build
a robust and general purpose automatic differentiation system
that also works within the boundaries of known community idioms,
but that is _exactly_ what the JAX (and original `autograd`) devs did.
In fact, the guys who taught me deep learning are the JAX developers,
for which I remain eternally thankful:
anthropomorphisms of neural networks no longer capture my attention.

Regardless, though, there's still a smaller (but sizeable)
group of people who use the deep learning frameworks quite productively,
even though they do not have perfect interoperability with the NumPy API:

- PyTorch
- TensorFlow
- Gluon

PyTorch and Chainer share a lineage,
and if I understand history correctly, Chainer was the original.
That said, PyTorch was backed by a behemoth tech firm in SV (Facebook),
while Chainer was supported by a Japanese consulting firm (Preferred Networks),
and we know that the monopolistic tendencies of Silicon Valley won out.
The Chainer team at Preferred Networks have discontinued further development,
instead providing CuPy and Optuna.

### Statistical Modelling

It’s taken me many years of studying to finally reach this conclusion:
it _seriously_ pays to know the core concepts
of “effect size” and probability distributions.
Those, more than significance tests, matter.
Additionally, being able to describe data generating processes
through the lens of probability distributions is extremely fundamental.

All of this is a long-winded way to say,
_don't rely on canned statistics!_
Go learn it well.
And if you are lucky enough to do so, learn it Bayesian first,
or rather, from the lens of simulating data generating processes.
Everything in statistics makes sense
only in light of data generating distributions.

Now, with that said, how do we do statistical inference,
especially _Bayesian_ statistical inference?

[PyMC3](https://docs.pymc.io/)
is one of the two major probabilistic programming languages for Pythonistas,
the other being Stan (through the PyStan interface).
I personally have developed and contributed to PyMC3,
and am extremely fond of being able to do Bayesian statistics
without needing to learn another domain-specific language,
so I have a biased interest in the package.
It pairs with [ArviZ](https://arviz-devs.github.io/arviz/index.html),
a package that provides visual diagnostics
for Bayesian statistical analysis workflows.

Theano, the tensor library that PyMC3 is built on top of,
seems to have a few years more of life in its belt,
though the compatibilities with modern operating systems
are starting to show through the cracks.

[PyMC4](https://github.com/pymc-devs/pymc4) is the next generation of PyMC,
and is built on top of Tensorflow Probability,
and already has an alpha release made.

Other probabilistic programming languages are also under constant development,
not least one of which I'm paying close attention to
being [`mcx`](https://rlouf.github.io/mcx/build/html/index.html),
which is built on top of JAX!

If you are well-versed in statistics,
and you know the assumptions of the models you’re using,
and you’re able to correctly interpret them,
then [`statsmodels`](https://www.statsmodels.org/stable/index.html)
provides a unified interface to “standard” statistical inference algorithms,
including linear models, time series models, and more.
As with all models, **know the tools that you’re wielding** well enough
to know when they can fail!

### Scalable Computing

In the PyData ecosystem, there are two major players: Dask and Spark.

In my personal experience,
[Dask](https://dask.org/) has been the more productive tool to use.
It’s easy to install,
provides a near-perfect drop-in replacement for the NumPy and Pandas APIs,
and is easy to get going
without additional software on existing cluster systems (e.g. GridEngine).
[Coiled Computing](https://coiled.io/), led by Dask creator Matthew Rocklin,
is also apparently working on tooling
to enable individual data scientists to scale to the cloud
_easily_ from a single laptop.
I can’t wait to see what happens there.

That said, if you’re stuck with [Spark](https://spark.apache.org/)
because of legacy systems,
there’s thankfully a not-so-bad ecosystem of packages in the Spark world.
(Its API policy, though,
plays less nicely with the rest of the FOSS PyData world.)

NVIDIA has also been investing heavily in the PyData stack
with a suite of GPU-accelerated tools, [RAPIDS](https://rapids.ai/).
In there are a suite of packages
that are actively developed for GPU-accelerated DataFrames (cuDF),
graph analytics (cuGraph),
SQL query engines (BlazingSQL), machine learning (cuML),
and more.
Definitely worth keeping an eye out on.

### How should I obtain a Python?

I’ve deliberately worded it as “a Python”.

If you’re doing data science work, in my opinion,
the best way to install Python
is to [grab `miniconda`](https://docs.conda.io/en/latest/miniconda.html),
and ensure that each of your environments have their own `conda` environment.

### What are environments, and how should I structure/maintain them?

There are basically two idiomatic ways.
For data science users, `conda` probably should be your default,
especially if you need access to non-Python libraries.
For non-data science users, use of `venv` is probably a good way to go,
though it only handles Python packages.

Each project you work on really should have its own conda environment.
The way to do this is to make sure each project
lives in its own isolated directory on your filesystem,
and contains an `environment.yml` file
that fully specifies every single package you need to work on the project.

If you want to take this one step further,
use Docker containers!
VSCode has the ability [to open any repository inside a "development container"][devcontainer].
I've test-driven this on some projects that I work on,
including `pyjanitor`, notes on causal inference, Network Analysis Made Simple, and more.


### Which Integrated Development Environment (IDE) and/or text editor should I use?

Which IDE/text editor you use is personal, but the general idea here is to “learn one really well, and be dangerous enough with 2-3 more.” Here’s a partial list you can think about:

IDEs:

- [Visual Studio Code](https://code.visualstudio.com/) for software development. Their notebook support is also not bad. The remote extension lets you work really well. Also LiveShare works wonders. Finally, opening repositories on GitHub inside pre-defined "development containers" seriously simplifies the whole process of getting setup in a new computer.
- [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/) for notebook + software development. Notebooks are first-class citizens here.
- [PyCharm](https://www.jetbrains.com/pycharm/). They have free licenses for open source developers.
- [Sublime Text](https://www.sublimetext.com/). I go to this one for times I need a fast text editor up and running.

Personally, I stick with Jupyter and VSCode,
though I’ve picked up enough [`nano`](https://www.nano-editor.org/) hacks
to work with it in the terminal.

More than anything, though, don’t disparage anybody’s use of their favorite text editor.
At the same time, be ready to use the ones that allow collaborative text editing.

### Should I worry about `git`? What tools around it should I use?

The short answer is a resounding yes!

The longer answer is as follows:
Knowing how to use a version control system will make you more versatile as a data scientist.
The biggest advantage of knowing a modern version control system
is the ability to introduce a workflow that lets you experiment on branches
isolated from a gold standard source of verified, tested, and “known-to-work” collection code and notebook.
Everything around that builds on this tooling.

This includes the most important downstream feature of using `git` on the web:
being able to automatically trigger builds of _anything_,
including static sites, Docker development containers, documentation, and more.
Once you embrace this workflow plus all of the automation surrounding it,
you level up your skill level!

Through whatever accidents of history,
`git` has emerged as the _de facto_ version control system
for modern software and data science workflows.
Knowing it will let you, a data scientist,
work more effectively with your engineering counterparts.

In using `git`, there is only one other tool I would recommend knowing, that is `pre-commit`.
It gives you the ability to apply automatic code and notebook checks before you commit anything into the repository,
thus preventing “bad practices” from seeping in,
such as having large figures in your notebooks checked into your version control repository.
Pre-commit will stop the committing from happening if code and/or notebook checks fail.
Some tools like black and nbstripout will also automagically modify the offending files for you,
so that when you do the commit once more after that, the checks will pass.

### How do I build documentation for my projects?

Documentation is usually the last thing on everybody’s minds with a project,
but it is also _the only thing that will scale you_ and expand the reach of your project.
Investing in documentation, thus, increases your impact. Don’t neglect it.

With documentation,
static site generators that produce standalone HTML documents are what you probably want to go for.
This allows you to host the documentation on the internet (or your organization’s intranet).
(Where to host the HTML pages is a different question, this section only discusses how to generate them.)

So what tools are available for documentation?

The workhorse of the Python documentation world is Sphinx.
It comes with a lot of features and extensions, and many developers swear by it.
Many others, however, also swear a ton because of it, because it is complicated to learn,
and the syntax is not easy to remember — especially if one doesn’t write documentation _every day_ like code!
If you’re willing to invest the time to learn,
you’ll be amazed at the power that Sphinx provides for building static HTML documentation.
Think of Sphinx as the matplotlib of documentation: old, low-level, and extremely powerful.

If you prefer Markdown documentation,
then consider using MkDocs, which is an up-and-coming documentation system.
Markdown is quite idiomatic to write,
has a nice one-to-one correspondence to HTML,
lets you interleave HTML,
and as such makes writing documentation much simpler.
An ecosystem of packages that you can mix-and-match are available
to help with automatic parsing of docstrings (for API docs),
and the `mkdocs-material` package provides very fancy ways
to write device screen-responsive documentation with built-in static site search (no server required).
Personally, I’ve switched to writing all new docs using MkDocs and `mkdocs material`.
(This site itself is built using mkdocs material!)
There are some compatibility rough spots that I have seen,
but that should not discourage you from trying it out.

### What do I do to solve my code copy/pasting problem?

You’ve found yourself copying and pasting code across notebooks,
and now it’s unsustainable to keep modifying them in 13 places.
Writing a software library will help you consolidate your code in a single source of truth,
which will let you update once to be applied everywhere the code is called.

Python comes with all of the tools you need to make your own software library
and import it into your notebooks and apps.
There is an official [Python Packaging Tutorial](https://packaging.python.org/tutorials/packaging-projects/)
that you should refer to when building your own Python packages.

### How do I test my code?

Running and writing tests may sound like something only Quality Assurance engineers should be doing,
but because data scientists are writing code, having good software skills helps.
You don’t need to go far, you only need to have the basics on hand.

[`unittest`](https://docs.python.org/3/library/unittest.html) is built into the Python standard library,
and you can get started pretty easily.

On the other hand, [`pytest`](https://docs.pytest.org/en/latest/) has become a very common testing package.
The developers put a lot of thought into how the API is developed.
As such, it is easy to get started with, extremely capable for complex situations,
and runs everything in between very productively.

To take your testing to the next level,
add in [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) to your list of packages to experiment with.
Hypothesis has helped me find edge cases in my code that I never would have thought to find.
The docs are also amazing, and it's easy to get started with
on select parts of your code base (especially if you're not ready to commit all-in)!

### How do I guarantee the reproducibility of my notebooks?

You’ll want to know how to do this if you are writing notebooks that contain crucial analyses that you need to reproduce.

Thankfully, there is one idiomatic way to handle this, and that is by using `nbconvert`.
The `nbconvert` docs provide documentation
on how to [programmatically execute your notebooks](https://nbconvert.readthedocs.io/en/latest/execute_api.html)
from Python and the command line.

Then, you'll want to subject your notebooks to "continuous execution".
The general idea is to master a “continuous pipeline runner”.
A few for open source projects include:

- Azure Pipelines
- Travis CI
- CircleCI
- Jenkins (your company may host it internally).

If you develop the ability to work with `git` properly,
then the entire world of automatic pipeline runners is at your fingertips!
Almost every pipeline runner can be triggered on new commits to any pre-specified branches,
and also come with the ability to execute checks automatically
on any pull request branches,
thereby guaranteeing that you have fully reproducible builds!

## Was there something missing that you still have questions about?

If so, head over to the [issue tracker](https://github.com/ericmjl/essays-on-data-science/issues)
and post it there;
don't forget to reference the essay!

## With thanks

Special shout-out to my Patreon supporters,
Eddie Janowicz, and Carol Willing, and Hector Munoz!
Thank you for keeping me caffeinated
and supporting my work that gets shared with the rest of the PyData community!

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

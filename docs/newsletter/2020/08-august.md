# Data Science Programming August 2020 Newsletter

Hello fellow datanistas!

Welcome to the August edition
of the programming-oriented data science newsletter!

This edition of the newsletter has a large dose of SciPy 2020 inside it.
I participated in the conference as a tutorial instructor
(and as one of the Financial Aid chairs),
though I did also miss Austin TX food!
(Seriously, Texan BBQ is one of the best!)
If you're interested in seeing the whole playlist,
[check it out on YouTube](https://www.youtube.com/enthought)!
If not, come check out some of those that I've watched and liked,
my subset curated for you!

## [Frictionless Data for Reproducible Biology by Lilly Winfree](https://youtu.be/vZAi4OnfH-Q)

The reason I like this talk is primarily
because of the idea of "Data Packages",
where raw data and its metadata are packaged in a machine-readable format.
In my mind, I'm contrasting this idea against
the large-scale data collection efforts;
in biosciences, many datasets are small and designed for one question,
but may be useful for other problems by providing,
for example, useful priors on parameters.
Here, a data package helps users ship and
distribute a self-contained unit of data
that others can build on top of.
I'm imagining many cool use cases,
both in public-facing research and in internal-facing workflows!

## [Continuous Integration for Scientific Python Projects by Stanley Seibert](https://youtu.be/OAlr9vY5XLU)

In this talk, Stan Seibert (one of the Numba core developers)
speaks about the advantages of standing up
a continuous integration pipeline for your code,
as well as challenges that you'll encounter along the way.
I find this to be a useful video for data scientists,
because in it Stan gives a good overview of what to look out for.

## [Awkward Array: Manipulating JSON like Data with NumPy like Idioms by Jim Pivarski](https://youtu.be/WlnUF3LRBj4)

This one has to be one of my favourite talks,
because the package featured in there has an awesome name,
brings over NumPy idioms and semantics into world of nested
and "awkwardly"-structured data.

## [JAX: Accelerated Machine Learning Research by Jake Vanderplas](https://youtu.be/z-WSrQDXkuM)

I'm a fan of the NumPy API
because it's the array-computing _lingua franca_ of the Python world,
and I strongly believe that targeting a common API
(and evolving it in a community-oriented fashion)
is the right way to build the PyData ecosystem.
JAX does this by making array-oriented automatic differentiation,
GPU/TPU acceleration,
just-in-time compilation,
and vectorized mapping all first-class citizens
alongside the idiomatic NumPy API.
I love it and totally dig it!
And I use it for research and production at work.
I'd encourage you to try it out too!

## [`matplotlib` Data Model by Hannah Aizenman](https://youtu.be/XC0M76CmzHg)

If you use `matplotlib`, then this Maintainer's track talk by Hannah Aizenman
is going to make your eyes light up!
In here, she talks about CZI-funded work
to refactor the data model underneath `matplotlib`,
which will enable a _ton_ of really cool things downstream.
I'm not going to spoil it for you; check it out!
(And also check out the other _cool talks_ by the other maintainers!)

## [Interactive Supercomputing with Jupyter at NERSC by Rollin Thomas](https://youtu.be/nU-FDFrtOvM)

I think this is a great case study talk that shows how JupyterHub is used
at a research institution to help facilitate computational research.
If your organization is thinking about setting something up,
I think this talk will give you valuable insights and lessons!

## [Tutorials](https://www.youtube.com/playlist?list=PLYx7XA2nY5Gde-6QO98KUJ9iL_WW4rgYf)

If I _really_ wanted to, I would have listed all 10 tutorials down here amongst my recommendations,
but I know you came for a curation.
Here's the two that I think are most generally useful for data scientists:

- [Introduction to Conda for (Data) Scientists](https://youtu.be/qn5zfdJtcYc): This being such a foundational tool for distributing data science packages, I think it's work getting our mental models straightened out!
- [Jupyter Interactive Widget Ecosystem](https://youtu.be/8IYbdshUd9c): With Jupyter notebooks being so idiomatic, and with widgets being so useful for dashboarding, pedagogy and more, this one is an easy recommendation!

But seriously, check out all 10 of them!

## From my collection

Here's a few snippets of my participation this year at SciPy!

- [Call prediction, prediction, not inference!](https://youtu.be/VzRj55pas3I?t=435) (My ~~rant~~ lightning talk at SciPy.)
- [Bayesian Data Science by Simulation](https://youtu.be/8eh5A72hIWM) (tutorial I led, based on material I co-developed with Hugo Bowne-Anderson!)

In some other news, the [Network Analysis Made Simple eBook has launched](https://leanpub.com/nams)!
In line with my personal philosophy
of democratizing access to learning material,
everything is [freely available online](https://ericmjl.github.io/Network-Analysis-Made-Simple/index.html),
but if you'd like to support us (mostly by keeping us caffeinated)
or would like an offline copy to keep that will be kept up-to-date for life,
please consider purchasing a copy!

## Thank you for reading!

Alrighty, I shan't toot my own horn anymore.
I hope you enjoyed this special SciPy curation edition of the programming-oriented data science newsletter!
As always, let me know on [Twitter](twitter.com/ericmjl)
if you've enjoyed the newsletter,
and I'm always open to hearing about the new things you've learned from it.
Next month, we resume regular scheduled, ahem, programming!

Meanwhile, if you'd like to get early access to new written tutorials,
essays, 1-on-1 consulting and complimentary access to the Skillshare workshops that I make,
I'd appreciate your support on [Patreon](patreon.com/ericmjl)!

Stay safe, stay indoors, and keep hacking!

Cheers,
Eric

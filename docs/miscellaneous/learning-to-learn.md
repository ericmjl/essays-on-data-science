# How I Learned to Learn

In this essay, I'd like to reflect back on
how I learned to learn new things.
For a data scientist, it's impossible to know _everything_,
but I do think that having a broad knowledge base can be very handy.
Especially when confronted with a new problem class,
having a broad toolkit of methods to solve it
can give us a leg-up in terms of efficiency.

## Learning by doing/building/making

> "Carve out time to reinvent the wheel, to learn about the wheel."

One way that I think is very effective in learning new topics
is to learn by making things from scratch.
This trick, I believe, is particularly effective
when learning about the foundational topics that underlie
the API abstractions that we interact with
as data scientists.

For example, I learned quite a ton about architecting a deep learning library
by trying to make one myself.
The end result is [fundl], a deep learning framework that I wrote
that supports my own learning
about the so-called fancy math that belies deep learning models.
`fundl` fits in the **"model", "loss", "optimizer"** thought framework
that I rely on for reasoning about deep learning models,
and helps me focus on the "model" portion.

[fundl]: https://github.com/ericmjl/fundl

In there, I have used it at work to re-implement models that I have seen
implemented in other frameworks (e.g. PyTorch and TensorFlow),
and translate them into the NumPy API.
In doing so, I not only build familiarity with the models,
but also gain familiarity with the other tensor library APIs,
helping me to keep pace with framework development
while also leveraging existing knowledge that I have (in the NumPy API).

Through the process of implementing deep learning models,
I have also found my mental model
of linear algebra and data transformations has also grown.
For example, I no longer am satisfied to think of a deep learning model
in terms of an amorphous black box.
Rather, thanks to reimplemtation, I am much more inclined
to think about the model as doing some form of rotation and projection
in n-dimensional space,
which is exactly what dot products are all about.
Thinking this way, I think, prevents a predisposition towards
_anthropomorphization_ of machine learning models,
which is just a fancy term for ascribing human properties to models.

## Learning by teaching

> "Having made the wheel, share how it was made."

Teaching something is also an incredibly effective method
to learn a new topic.
I was able to learn graph theory during graduate school
not only because I used it as a tool in my research,
but also because I made teaching material in Python
and brought it to conferences to share the knowledge.

I think one of the key reasons
why teaching is so unreasonably effective in learning
is that it forces us to demonstrate our mastery over our knowledge
in two ways.

Firstly, in preparing the teaching material,
we anticipate the questions that may arise from others.
To address those questions, in turn, we must be prepared
with knowledge deeper than what we have chosen to present.

Secondly, any presentation of the material
involves a linearization of a messy knowledge graph.
In my conception, when I present material,
I am tracing a path through the knowledge graph,
while sprinkling in edges that branch off a main knowledge trunk.

I've been incredibly fortunate to have a few platforms to do teaching,
the primary one being the Python and data science conferences that I attend.

## Leveraging existing knowledge

"Projects that are adjacenct to what I know how to do."

## Seeking learning partners and teachers

Acknowledge David Duvenaud and Colin Carroll.

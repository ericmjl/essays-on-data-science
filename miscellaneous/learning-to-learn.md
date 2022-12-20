# How I Learned to Learn

In this essay, I'd like to reflect back on
how I learned to learn new things.
For a data scientist, it's impossible to know _everything_,
but I do think that having a broad knowledge base can be very handy.
Especially when confronted with a new problem class,
having a broad toolkit of methods to solve it
can give us a leg-up in terms of efficiency.
This set of reflections hopefully lights up some lighbulbs
for your own learning journey.

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

```mermaid
graph LR;
    A((A)) ==> B((B));
    A((A)) --> C((C));
    B((B)) ==> D((D));
    C((C)) ==> E((E));
    D((D)) ==> C((C));
    B((B)) --> E((E));
    D((D)) --> E((E));
```

The third point pertains to learning by teaching in quantitative topics.
By forcing myself to "teach" the ultimate dumb student
- a Python interpreter - to do math-y things,
I not only make concrete an abstract topic,
I also have to verify that the abstract topic is implemented correctly,
because a Python interpreter will definitely get it wrong
if I implemented it wrong.

I've been incredibly fortunate to have a few platforms to do teaching,
the primary one being the Python and data science conferences that I attend.
That said, there are many avenues for teaching
that you could take advantage of,
including at work (1-on-1 pair coding or workshops),
regional or international conferences,
e-learning platforms,
and more,
and I would encourage you to leverage the platform
that suits your situation best.

## Leveraging existing knowledge

> "Pick projects that are adjacenct to what I know how to do."

Continuing the "knowledge graph" analogy referenced above,
I have made an effort in my learning journey
to leverage as much existing knowledge that I can.
It seems to me that knowledge is best picked up and made to stick
when I can use one topic to anchor another, and vice versa.

A few lightweight examples that have showed up in my learning journey:

- [Connecting graph message passing with linear algebra](/machine-learning/message-passing)
- [Implementing Bayesian models from scratch but leveraging Python](/machine-learning/computational-bayesian-stats/)
- [Digging into deep learning starting from linear regression](https://github.com/ericmjl/dl-workshop)

In the process of leveraging my existing knowledge to learn new things,
I find that tying the learning process
to the creation of "minimally complex examples"
greatly accelerates my own learning process.


??? note "Minimally Complex Examples"

    These are examples that are simple to grok,
    but not trivial.
    For example, it's trivial to illustrate
    sampling from a (multivariate) Gaussian distribution,
    which is how [sampyl](https://github.com/mcleonard/sampyl)
    illustrates MCMC sampling on its docs page.
    However, it is non-trivial, and in fact quite illuminating,
    to illustrate sampling from a joint distribution
    of data, likelihood, and priors
    involving a Gaussian and its parameters.

## Seeking learning partners and teachers

> Learn and teach with others.

I also have to state that I have benefited much
from learning from others.
For example, my primary deep learning teacher was David Duvenaud,
back when he was a post-doc at Harvard.
(He is now a professor at the University of Toronto.)
It was from him through which I gained the framework of
deep learning as "model + loss + optimizer",
and if I remember correctly,
he was the one that taught me how to think about linear regression
in that exact framework.

Additionally, a friend from amongst the PyMC developers, Colin Carroll,
has been particularly helpful and inspiring.
I read [his blog](https://colindcarroll.com)
in which he writes about his own learnings and insights.
In particular, I very much appreciate how he uses "minimal complex examples"
to illustrate how things work.
He was also the one who kept reminding me
that gradient descent doesn't happen in MCMC,
which thus inspired the essay
[on MCMC](/machine-learning/computational-bayesian-stats/).

More generally,
I find that identifying learning partners and teachers
against whom I can check understanding
is a great "social" strategy for picking up ideas.
I generally try to find win-win scenarios,
where I can offer something in exchange,
as this helps balance out the learning partnership
and makes it win-win for my fellow learner too.

## Asking the "dumb" questions

One thing I do know I'm infamous for is asking dumb questions.
By "dumb" questions, I mostly mean questions that clarify basic ideas
that I might have missed, or still have a gap on.

In my mind, there are very, very few dumb questions.
(I would probably classify
repetitively asking the same basic questions over and over
as not being particularly smart -
use a notebook for heaven's sake!)
In a more intimate learning situation, say, a 1-on-1 session,
clarifying basic questions as soon as they come up
is a wonderful way of ensuring that
our foundational knowledge is strengthened.
In larger settings,
I am almost always certain
that someone else will share the same basic questions that I do.

## Concluding Words

This was neither a comprehensive reflection on how exactly I learn
nor a comprehensive overview of how everybody learns.
Nonetheless, it is my hope that you find it useful to reflect on,
and that it gives you ideas for learning new technical topics.

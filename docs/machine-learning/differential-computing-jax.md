# Differential Computing with JAX

The proliferation of differential computing tooling has been one of the biggest contributions
from the deep learning world in the 2010-2020 decade.
In this essay, I want to write about JAX, which in my personal opinion
has made the biggest strides forward
for interoperable differential computing in the Python data science world.

## On differential computing

Before we go on, we must first ask: what is differential computing all about?

I think at its core, we can think of differential computing as
"computing where derivatives (from calculus) are a first-class citizen".
This is analogous to probabilistic computing,
in which probabilistic constructs (such as probability distributions and MCMC samplers)
are given "first class" status in a language.
By "first class" status,
I mean that the relevant computing constructs
are a well-developed category of constructs in the language,
with clearly defined interfaces.

In differential computing,
being able to evaluate _gradients_ of a math function are at the heart of the language.
(How the gradients are used is a matter of application.)
The objective of a differential computing system is to write a program that gets a computer
to automatically evaluate gradients of a math function that we have written in that language.
This is where _automatic differentiation_ (AD) systems come into play.
They take a program, perhaps written as a Python function,
and automatically transform the program into, perhaps, another Python function,
which can be used to evaluate the derivative of the original function.

All of this falls under the paradigm of AD systems, as I mentioned earlier.
Symbolic differentiation can be considered one subclass of AD systems;
this is a point PyMC3 developer [Brandon Willard](https://brandonwillard.github.io) would make.
Packages such as `autograd` and now [JAX](https://github.com/google/jax) (also by the `autograd` authors)
are another subclass of AD systems,
which leverage the chain rule and a recorder tape of math operations called in the program
to automatically construct the gradient function.

## Where differential computing gets used

In case you've found yourself living like a digital hermit for the past decade
(no judgment, sometimes I do fantasize about going offline for a year),
_deep learning_ has been the place where automatic differentiation has been most utilized.
With deep learning, the core technical problem that needs to be solved is
optimizing parameters of a model to minimize some loss function.
It's here where the full set of partial derivatives of the loss function w.r.t. each parameter in the model
can be automatically calculated using an AD system,
and these partial derivatives can be used
to update their respective model parameters in the direction that minimizes loss.

Because deep learning models and their applications proliferated in the 2010-2020 decade,
AD systems were most commonly associated with neural networks and deep learning.
However, that is not the only place where AD systems show up.

For example, AD is used in the Bayesian statistical modelling world.
Hamiltonian Monte Carlo samplers use AD to help the sampler program
identify the direction in which its next MCMC step should be taken.
AD systems can also be used to optimize parameters 
of non-neural network models of the world against data,
such as Gaussian Mixture Models and Hidden Markov Models.
We can even use AD in a class of problems called "input design" problems,
where we try to optimize not the _parameters_ of the model w.r.t. some output,
but the _inputs_ (assuming we know how to cast the inputs into some continuous numerical space.)

## The landscape of AD systems

So where do AD systems live?
Firstly, they definitely live inside deep learning frameworks such as PyTorch and TensorFlow,
and other deep learning frameworks.
Without an AD system, these two deep learning frameworks would not work.

Secondly, they also live in independent packages.
In Julia, there are two AD packages: one called `Zygote.jl`, and the other called `AutoGrad.jl`;
both of them are actively developed.
`autograd`, which was the reference Python package that `AutoGrad.jl` was written against,
is also the precursor to JAX, which I think of as automatic differentiation on steroids.

## What makes JAX special?

With all of that said, the focus of this essay is JAX.
I wanted to bring a bit of focus to JAX
as I think its developers have been doing all the right things thus far in its development,
and I wanted to highlight these as reasons why you might want to use JAX in your next project.

### API-compatible differentiable computing

The Python scientific computing stack,
also known as the PyData or SciPy stack in the Python world,
provides a large library of numerical programs that can be composed together into higher order programs.
What JAX provides is a fully API-compatible reimplementation of the stack's differentiable functions,
with what I think is a near-complete coverage of functions.

As such, users familiar with NumPy and SciPy can,
with minimal changes to lines of code,
write _automatically differentiable_ versions of their existing programs,
and develop new programs that are also automatically differentiable.

How does this work?
I have written [a longer-form collection of teaching materials on this](https://github.com/ericmjl/dl-workshop),
but here is a quick example.
If I have a silly program like the following one:

```python
from jax.scipy.special import cholesky
import jax.numpy as np

def some_function(params, data):
    # do stuff with params, for example, a cholesky decomposition:
    U = cholesky(params)
    # followed by a sum of sine transform, for whatever reason it might be needed
    return np.sum(np.sin(U))
```

I can get the gradient function easily, using JAX's provided `grad` function:

```python
from jax import grad

dsome_function = grad(some_function)
```

`dsome_function` has the same function signature as `some_function`,
but instead of returning a scalar value,
it returns the derivative of `some_function` w.r.t. `params` (the first argument),
in the same (and possibly nested) data structure as `params`.
That is to say, if `params` were a tuple, or a dictionary, or a list,
or any other native Python construct,
`dsome_function` would return the same structure.

`grad` can do many more fancy things,
such as differentiating through loops and flow control,
and second through nth-order derivatives,
and I'd encourage you to check out the docs to learn more.
(That is out of scope for this essay, as I'm focusing on high level points.)

Providing `grad` as a first-class citizen
in an API-compatible fashion with the scientific Python computing stack
makes it very easy to adopt differential computing tooling in one's programs.

### API-compatibility with the rest of the PyData stack

A design choice made early on by the JAX developers
was full NumPy and SciPy API compatibility,
with minimal differences (mostly in the realm of random number generation)
that are very well-documented.
Incidentally, this practice is also adopted by Dask and CuPy,
which give us distributed and GPU-backed arrays respectively.
This practice reflects a healthy dose of respect
for what already exists and for end-users as well.

I think a contrasting example best illustrates this point.
Consider a PyTorch or TensorFlow array vs. a JAX NumPy array.

To plot a PyTorch array's values in `matplotlib`, one must first convert it to a NumPy array:

```python
a = torch.tensor([1, 2, 3])
plt.plot(a.numpy())
```

On the other hand, with JAX:

```python
import jax.numpy as np
a = np.array([1, 2, 3])
plt.plot(a)
```

The syntax with JAX is identical to what one might write with vanilla NumPy.
This is, I think, in part because JAX's developers have also strived
to adhere to [NEP18](https://numpy.org/neps/nep-0018-array-function-protocol.html).
Small API differences introduce micro-friction in programming,
which compound frustration over time;
JAX effectively eliminates that friction by adhering to an existing API
and not playing smartypants with it.

### Composable program transforms

JAX's `grad` function is merely the "gateway drug" to
this bigger idea of "composable program transforms".
`grad` is one example of a composable program transform:
that is transforming one program into another in a _composable_ fashion.
Other transforms include `vmap`, `lax.scan`, `jit`, and more.
These all accept Python functions and return Python functions.
`jit`, in particular, can accelerate a program anywhere from 2-100 fold on a CPU,
depending on what your reasonable baseline comparison is.

In particular, the latter three of the aformentioned transforms
allow for highly performant loop code, written without loops,
that can also be composed together.
In this [differential learning workshop](https://github.com/ericmjl/dl-workshop/) that I have been developing,
I provide further details in there, which you can take a look at.

There are other automatic program transformations that are in active development,
and one exciting realm I see is in the probabilistic programming world.
In PyMC3, for example, an automated transform happens when we take our PyMC3 syntax,
which is written in a domain specific language (DSL) implemented in Python,
and transform/compile it into a compute graph that gives us a _likelihood_ function.
It's as if PyMC3 gives us a `likelihood(func)` analogy to JAX's `grad` func.
If you've tried writing probabilistic model likelihoods by hand,
you'll know how much of a convenience this is!

## What JAX enables and doesn't enable

JAX as a package doesn't pretend to be a replacement for established deep learning frameworks.
That is because JAX doesn't provide the _deep learning_ abstractions as a first-class citizen;
its focus is on the much more generally useful idea of _composable program transformations_.
To compare it against a deep learning framework is a bit of a red herring - a distraction away from what JAX enables.

What JAX actually enables is for us to write numerical programs using the NumPy API
that are performant and automatically differentiable.
`vmap` and `lax.scan` help us eliminate Python loop overhead in our code;
`jit` just-in-time compiles code to accelerate it;
`grad` gives us differentiability,
thus opening the door for us to write 
performant optimization routines that solve real world problems.

At work, I have used JAX productively in both neural network and non-neural network settings,
with the unifying theme being gradient-based optimization of model parameters.
With JAX, I can seamlessly move between problem classes
while using the PyData community's idiomatic NumPy API.
We have used JAX to implement
Hierarchical Dirichlet Process autoregressive multivariate Gaussian hidden Markov models (what a mouthful!),
LSTM recurrent neural networks,
graph neural networks,
simple feed-forward neural networks,
linear models, and more...
and train them using the same gradient descent tooling available to us in JAX.

The upside here is that we could hand-craft each model
and tailor it to each problem encountered.
The code was written in a very explicit fashion
that exposed the many layers of abstractions that were sometimes needed.
Noe that this may also be viewed as the downside of writing JAX code --
we had to write a lot of code,
partially because the abstractions we needed weren't already implemented in some cases,
and partially because they aren't easily available in JAX in other cases.

One thing I wanted to highlight though:
leveraging simple tricks learned from the neural network and probabilistic programming worlds
(such as optimizing in unbounded rather than bounded space),
we were able to train covariance matrices in our multivariate Gaussian HMMs
using gradient descent rather than expectation-maximization,
and it _just worked_.
I found it amazing to see in action.

Now, the lack of deep learning abstractions in JAX
doesn't mean that JAX as a backend to other computing frameworks isn't available!
A flurry of development after JAX's initial release
led to a suite of deep learning libraries and probabilistic programming languages
targeting JAX as an array backend,
because of its provision of a library of Python-compatible composable program transformations.

For deep learning libraries,
an experimental [`stax`](https://jax.readthedocs.io/en/latest/jax.experimental.stax.html) module exists inside JAX;
my intern Arkadij Kummer and myself used it productively
in a JAX-based reimplementation of an LSTM model used for protein engineering.
[`flax`](https://flax.readthedocs.io), also developed by Googlers, exists,
and provides a PyTorch-like API that builds on top of the functional programming paradigm encouraged by JAX.
The [Neural Tangents](https://github.com/google/neural-tangents) package
for infinitely wide, Bayesian neural networks follows `stax`'s  idioms,
with well-documented differences (though without reasons given).

For probabilistic programming languages,
even TensorFlow Probability has a JAX backend as an alternative to the TensorFlow backend.
PyMC3, which is built on top of Theano, is getting a JAX-ified Theano backend too,
while [`mcx`](https://github.com/rlouf/mcx), written by a French software developer Remí Louf,
is a pedagogical PPL written entirely using JAX as a backend too.
Not to forget NumPyro, which is another JAX-based implementation
of the Pyro probabilistic programming language.

## Recent developments

JAX has been actively developed for over two years now,
and as a project, it continues to attract talent to the project.
The originators were Dougal Maclaurin, Matt Johnson, Alex Wiltschko and David Duvenaud
while they were at all at Harvard,
and has since grown to include many prominent Pythonistas
including Jake Vanderplas and Stephan Hoyer on the team.
(There are many more, whose names I don't know very well,
so my apologies in advance if I have left your name out.
For a full list of code contributors,
the [repository contributors page](https://github.com/google/jax/graphs/contributors) is the most definitive.)

## Learning more

I invested one of my vacation weeks crystallizing my learnings from working with JAX over the past year and a half,
and it's been extremely educational.
If you're interested in reading it,
you can find it at [my `dl-workshop` repository on GitHub](https://github.com/ericmjl/dl-workshop).
In there, in addition to the original content, which was a workshop on deep learning,
I also try to provide "simple complex examples" of how to use JAX idioms in solving modelling problems.

Besides that, JAX's documentation is quite well-written,
and you can find it at [jax.readthedocs.io](https://jax.readthedocs.io/en/latest/).
In particular, they have a very well-documented suite of "The Sharp Bits" to look out for
when using JAX, geared towards both power users of vanilla NumPy and beginners. 
If you're using JAX and run into unexpected behaviour,
I'd strongly encourage you to check out the post - 
it'll clear up many misconceptions you might have!

In terms of introductory material, a blog post by Colin Raffel,
titled ["You don't know JAX"](https://colinraffel.com/blog/you-don-t-know-jax.html),
is a very well-written introduction on how to use JAX.
Eric Jang also has a blog post on [implementing meta-learning in JAX](https://blog.evjang.com/2019/02/maml-jax.html),
which I found very educational for both JAX syntax and meta-learning.

While the most flashy advances of the deep learning world came from 2010-2020,
personally think that the most exciting foundational advance of that era
was the development of a general purpose automatic differentiation package like `autograd` and JAX.
At least for the Python world, it's enabled the writing of arbitrary models
in a highly compatible fashion with the rest of the PyData stack,
with differentiation and native compilation as first class program transformations.
The use of gradients is varied, with much room for creativity;
I'd definitely encourage you to try it out!

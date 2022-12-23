Hello, datanistas!

This month is a special edition dedicated to JAX!
It's a Python package built by some friends I made
while they were at Harvard's Intelligent and Probabilistic Systems lab,
and I was still in grad school.

I've been a fan of JAX ever since I started seriously developing
array programs that required the use of automatic differentiation.
What's up with JAX, you might ask?
It's a library that brings automatic differentiation
and many other composable program transformations to the NumPy API.

Why is automatic differentiation significant?
The reason is that the ability to calculate the _derivative_ of a function,
w.r.t. one or more of its arguments,
is essential to many computation realms.
For example, we can use gradient-based optimization
to train small and large models
to do maximum likelihood or maximum _a posteriori_ estimation
of model parameters.
Gradients are necessary for modern MCMC samplers,
which leverage gradients to guide where to draw a new posterior sample next.
Input design problems can also use gradient-based optimization,
in which we either optimize or sample new _inputs_ to achieve some output.

What JAX does is it takes a function that returns a scalar value
and returns the derivative of that function's output w.r.t. the inputs.
JAX accomplishes this by using the `grad` function,
which takes the function passed into it,
and _transforms_ it into another function that evaluates the gradient.
Gradient transformations are one example of
a broader class of _program transformations_,
which take a program (e.g. a function implemented in NumPy code)
and transforms it into another program (its derivative function).
JAX houses other program transformations,
including just-in-time compilation for speed-ups,
loop-replacement functions,
and more.

Here, I'm going to highlight a sampling of the JAX projects
that have come up on my radar
to showcase the diversity of numerical computation projects
that you can build with it.
Hopefully, it'll give you some encouragement to give JAX a try
if you haven't already done so!

## Neural network projects

Because differential programming is a broader thing than just neural networks,
you can write neural networks and more using JAX.
If you're not used to writing neural network models from scratch, not an issue:
there are a few neural network API frontends
that build _on top of_ JAX's NumPy API,
which implements PyTorch-like APIs.

- [`flax`](https://github.com/google/flax): A neural network library focused on flexibility.
- [`haiku`](https://github.com/deepmind/dm-haiku): One developed by the fine folks at DeepMind, alongside their other JAX projects.
- [`stax`](https://jax.readthedocs.io/en/latest/jax.experimental.stax.html?highlight=stax): JAX's internal experimental module for writing neural network models, which pairs well with its [`optimizers`](https://jax.readthedocs.io/en/latest/jax.example_libraries.optimizers.html) module!
- [`neural-tangents`](https://github.com/google/neural-tangents): Research that I have been following, one that provides "infinitely wide" versions of classical neural networks. It extends the `stax` API.

The best part of these projects?
You never have to leave the idiomatic NumPy API :).

## Probabilistic programming projects

As someone who has dabbled in Bayesian statistical modelling,
probabilistic programming is high on my watch list.

The first one I want to highlight is PyMC3.
More specifically, Theano.
One of our PyMC devs, Brandon Willard,
had the foresight to see that we could rewrite Theano to compile to JAX,
providing a modernized array computation backend
to Theano's symbolic graph manipulation capabilities.
It's in the works right now!
Read more about it on a [blog post written by the PyMC devs](https://pymc-devs.medium.com/the-future-of-pymc3-or-theano-is-dead-long-live-theano-d8005f8a0e9b).

The second one I want to highlight
is [NumPyro](https://github.com/pyro-ppl/numpyro),
a JAX-backed version of the Pyro probabilistic programming language.
A collection of Pyro enthusiasts built NumPyro;
one of its most significant selling points
is implementing the No-U-Turn Sampler (NUTS) in a performant fashion.

The third one I want to highlight
is [`mcx`](https://github.com/rlouf/mcx),
a learning project built by Remi Louf, a software engineer in Paris.
He has single-handedly implemented a probabilistic programming language
leveraging JAX's idioms.
I had the privilege of chatting with him about it
and test-driving early versions of it.

## Tutorials on JAX

Here are two tutorials on JAX that I have encountered,
which helped me along the way.

Colin Raffel has [a blog post on JAX](https://colinraffel.com/blog/you-don-t-know-jax.html)
that very much helped me understand how to use it. I highly recommend it!

Eric Jang has [a blog post on meta-learning](https://blog.evjang.com/2019/02/maml-jax.html),
with accompanying notebooks linked in the post,
that show how to do meta-learning using JAX.

Beyond that, the JAX docs have
[a great tutorial to help get you up to speed](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html).

## From my collection

As I've experimented with JAX and used it in projects at work,
here are things I've had a ton of fun building on top of JAX.

The first is [`jax-unirep`](https://elarkk.github.io/jax-unirep),
done together with one of my interns Arkadij Kummer,
in which we took a recurrent neural network
developed by the Church Lab at Harvard Medical School
and accelerated it over 100X using JAX,
while also extending its API for ease of use.
You can check out the [pre-print we wrote as well](https://www.biorxiv.org/content/10.1101/2020.05.11.088344v1.full).

The second is
a [tutorial on differential programming](https://ericmjl.github.io/dl-workshop/).
This one is one I'm continually building out
as I learn more about differential programming.
There are a few rough edges in there post-rewrite,
but I'm sharing this early in the spirit of working with an open garage door.
In particular, I had a ton of fun walking through
the math behind [Dirichlet process Gaussian mixture model clustering](https://ericmjl.github.io/dl-workshop/04-gaussian-clustering/03-dirichlet-process-clustering/).

## Thank you for reading

I hope you enjoyed this JAX edition of the Data Science Programming Newsletter!
Next month, we resume regular scheduled, ahem, programming :).
If you've enjoyed this newsletter,
please do share the [link to the newsletter subscribe page](http://tinyletter.com/ericmjl)
with those whom you think might benefit from it.

As always, let me know on [Twitter](https://twitter.com/ericmjl)
if you've enjoyed the newsletter,
and I'm always open to hearing about the new things you've learned from it.
Meanwhile, if you'd like to get early access to new content I make,
I'd appreciate your support on [Patreon](https://patreon.com/ericmjl)!

Stay safe, stay indoors, and keep hacking!

Cheers,
Eric

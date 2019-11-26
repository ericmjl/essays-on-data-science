# An Introduction to Computational Bayesian Statistics

In Bayesian statistics,
we often say that we are using "sampling" from a posterior distribution
to estimate what parameters could be,
given a model structure and data.
What exactly is happening here?

Examples that I have seen on "how sampling happens"
tends to focus on an overly-simple example
of sampling from a single distribution with known parameters.
I was wondering if I could challenge myself
to come up with a "simplest complex example"
that would illuminate ideas that were obscure to me before.
In this essay, I would like to share that knowledge with you,
and hopefully build up your intuition behind
what is happening in computational Bayesian inference.

## Probability Distributions

We do need to have a working understanding
of what a probability distribution is before we can go on.
Without going down deep technical and philosophical rabbit holes
(I hear they are deep),
I'll start by proposing
that "a probability distribution is an object
that has a math function
that allocates credibility points onto the number line".

Because we'll be using the Normal distribution extensively in this essay,
we'll start off by examining that definition
in the context of the standard Normal distribution.

### Base Object Implementation

Since the Normal distribution is an object,
I'm implying here that it can hold state.
What might that state be?
Well, we know from math that probability distributions have parameters,
and that the Normal distribution
has the "mean" and "variance" parameters defined.
In Python code, we might write it as:

```python
class Normal(object):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
```

### Probability Density Function

Now, I also stated that the Normal distribution has a math function
that we can use to allocate credibility points to the number line.
This function also has a name,
called a "probability distribution function", or the "PDF".
Using this, we may then extend extend this object
with a method called `.pdf(x)`,
that returns a number
giving the number of credibility points
assigned to the value of `x` passed in.

```python
import numpy as np

class Normal(object):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        return (
            1 / np.sqrt(2 * self.sigma ** 2 * np.pi)
            * np.exp(
                - (x - self.mu) ** 2
                / 2 * self.sigma ** 2
            )
```

If we pass in a number `x` from the number line,
we will get back another number that tells us
the number of credibility points given to that value `x`,
under the state of the Normal distribution instantiated.
We'll call this $P(x)$.

To simplify the implementation used here,
we are going to borrow some machinery already available to us
in the Python scientific computing ecosystem,
particularly from the SciPy stats module,
which gives us reference implementations of probability distributions.

```python
import numpy as np

class Normal(object):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

        # We instantiate the distribution object here.
        self.dist = norm(loc=mu, scale=sigma)

    def pdf(self, x):
        # Now, our PDF class method is simplified to be just a wrapper.
        return self.dist.pdf(x)
```

### Log Probability

A common task in Bayesian inference is computing the likelihood of data.
Let's assume that the data ${X_1, X_2, ... X_i}$ generated
are independent and identically distributed,
(the famous _i.i.d._ term comes from this).
This means, then, that the joint probability of the data that was generated
is equivalent to the product of the individual probabilities of each datum:

$$P(X_1, X_2, ... X_i) = P(X_1) P(X_2) ... P(X_i)$$

(We have to know the rules of probability to know this result;
it is a topic for a different essay.)

If you remember the notation above,
each $P(X_i)$ is an evaluation of $X_i$
on the distribution's probability density function.
It being a probability value means it is bound between 0 and 1.
However, multiplying many probabilities together
usually will result in issues with underflow computationally,
so in evaluating likelihoods,
we usually stick with log-likelihoods instead.
By the usual rules of math, then:

$$\log P(X_1, X_2, ..., X_i) = \sum_{j=1}^{i}\log P(X_i)$$

To our Normal distribution class,
we can now add in another class method
that computes the sum of log likelihoods
evaluated at a bunch of i.i.d. data points.

```python
import numpy as np

class Normal(object):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

        # We instantiate the distribution object here.
        self.dist = norm(loc=mu, scale=sigma)

    def pdf(self, x):
        # Now, our PDF class method is simplified to be just a wrapper.
        return self.dist.pdf(x)

    def sumlogpdf(self, x):
        return np.sum(self.pdf(x))
```

## Random Variables

### Definition

Informally, a "random variable" is nothing more than
a variable whose quantity is non-deterministic (hence random)
but whose probability of taking on a certain value
can be described by a probability distribution.

According to the Wikipedia definition of a random variable:

> A random variable has a probability distribution, which specifies the probability of its values.

As such, it may be tempting to conceive of a random variable
as an object that has a probability distribution attribute attached to it.

### Realizations of a Random Variable

On the other hand, it can also be convenient to invert that relationship,
and claim that a probability distribution
can generate realizations of a random variable.
The latter is exactly how SciPy distributions are implemented:

```python
from scipy.stats import norm

# Normal distribution can generate realizations of an RV
# The following returns a NumPy array of 10 draws
# from a standard normal distribution.
norm(loc=0, scale=1).rvs(10)
```

??? note "Realizations of a Random Variable"

    A "realization" of a random variable is nothing more than
    generating a random number
    whose probability of being generated
    is proportional to the random variable's probability distribution.

Because the generation of realizations of a random variable
is equivalent to sampling from a probability distribution,
we can extend our probability distribution definition
to include a `.sample(n)` method:

```python
import numpy as np

class Normal(object):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

        # We instantiate the distribution object here.
        self.dist = norm(loc=mu, scale=sigma)

    # ...

    def sample(self, n):
        return self.dist.rvs(n)
```

Now, if we draw 10 realizations of a Normally distributed random variable,
and the drawing of each realization has no dependence of any kind
on the previous draw,
then we can claim that each draw is **independent**
and **identically distributed**.
This is where the fabled "_iid_" term in undergraduate statistics classes
comes from.

## Data Generative Process

Now that we have covered what probability distributions are,
we can now move on to other concepts
that are important in Bayesian statistical modelling.

Realizations of a random variable,
or draws from its probability distribution,
are how a Bayesian assumes data are generated.
Describing how data are generated using probability distributions,
or in other words, writing down the "data generating process",
is a core activity in Bayesian statistical modelling.

Viewed this way, data values generated by a random process
depend on the underlying random variable's probability distribution.
In other words, the random variable realizations are known,
given the probability distribution used to model it.
Keep this idea in mind:
it is going to be important shortly.


## Bayes' Rule

Now that we've covered probability distributions,
we can move on to Bayes' rule.
You probably have seen the following equation:

$$P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

Bayes' rule states nothing more than the fact that
the conditional probability of B given A is equal to
the conditional probability of A given B
times the probability of B
divided by the probability of A.

When doing Bayesian statistical inference,
we commonly take a related but distinct interpretation:

$$P(H|D) = \frac{P(D|H)P(H)}{P(D)}$$

It may look weird,
but didn't we say before that data are realizations from a random variable?
Why are we now treating data as a random variable?
we are doing an unintuitive but technically correct step
of treating the data as being part of this probabilistic space $D$
alongside our model parameters $H$.
There's a lot of measure theory that goes into this interpretation,
which at this point I have not yet mastered,
and so will wave my hands in great arcs
and propose that this interpretation be accepted for now and move on.

??? note "Data are random variables?"

    Notes from a chat with my friend Colin Carroll,
    who is also a PyMC developer,
    gave me a lot to chew on, as usual:

    > The answer is in how you define "event" as
    > "an element of a sigma algebra".
    > intuitively, an "event" is just an abstraction,
    > so one event might be "the coin is heads",
    > or in another context the event might be
    > "the parameters are [0.2, 0.1, 0.2]".
    > And so analogously, "the data were configured as [0, 5, 2, 3]".
    > Notice also that the events are different
    > if the data being ordered vs unordered are different!

With the data + hypothesis interpretation of Bayes' rule in hand,
we can finally get going on

TBD:

- draw samples from distribution: gives us a bunch of random variates (RVs).
- if X is the random variable, then X_1, X_2, ..., X_i is a list of i.i.d. random variates from X's distribution, with each X_i being a realization of the random variable.

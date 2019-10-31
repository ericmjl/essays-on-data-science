# Reimplementing and Testing Deep Learning Models

At work, most deep learners I have encountered
have a tendency to take deep learning models
and treat them as black boxes that we should be able to wrangle.
While I see this as a pragmatic first step
to testing and proving out the value of a newly-developed deep learning model,
I think that stopping there
and not investing the time into understanding the nitty-gritty of the model
leaves us in a poor position
to know that model's
(1) applicability domain (i.e. where the model should be used),
(2) computational and statistical performance limitations, and
(3) possible engineering barriers to getting the model performant
in a "production" setting.

As such, with deep learning models,
I'm actually a fan of investing the time to re-implement the model
in a tensor framework that we all know and love,
NumPy (and by extension, JAX).

## Benefits of re-implementing deep learning models

Doing a model re-implementation from a deep learning framework
into NumPy code actually has some benefits for the time being invested.

### Developing familiarity with deep learning frameworks

Firstly, doing so forces us to know the translation/mapping
from deep learning tensor libraries into NumPy.
One of the issues I have had with deep learning libraries
(PyTorch and Tensorflow being the main culprits here)
is that their API copies something like 90% of NumPy API
without making easily accessible
the design considerations discussed when deciding to deviate.
(By contrast, CuPy has an explicit API policy
that is well-documented and front-and-center on the docs,
while JAX strives to replicate the NumPy API.)

My gripes with tensor library APIs aside, though,
translating a model by hand from one API to another
forces growth in familiarity with both APIs,
much as translating between two languages
forces growth in familiarity with both languages.

### Developing a mechanistic understanding of the model

It is one thing to describe a deep neural network
as being "like the brain cell connections".
It is another thing to know that the math operations underneath the hood
are nothing more than dot products (or tensor operations, more generally).
Re-implementing a deep learning model
requires combing over every line of code,
which forces us to identify each math operation used.
No longer can we hide behind an unhelpfully vague abstraction.

### Developing an ability to test and sanity-check the model

If we follow the workflow (that I will describe below)
for reimplementing the model,
(or as the reader should now see, translating the model between APIs)
we will develop confidence in the correctness of the model.
This is because the workflow I am going to propose
involves proper basic software engineering workflow:
writing documentation for the model,
testing it,
and modularizing it into its logical components.
Doing each of these requires a mechanistic understanding
of how the model works,
and hence forms a useful way of building intuition behind the model
as well as correctness of the model.

### Reimplementing models is _not_ a waste of time

By contrast, it is a highly beneficial practice
for gaining a deeper understanding into the inner workings
of a deep neural network.
The only price we pay is in person-hours,
yet under the assumption that the model is of strong commercial interest,
that price can only be considered an investment, and not a waste.

## A proposed workflow for reimplementing deep learning models

I will now propose a workflow for re-implementing deep learning models.

### Identify a coding partner

Pair programming is a productive way of teaching and learning.
Hence, I would start by identifying a coding partner
who has the requisite skillset and shared incentive
to go deep on the model.

Doing so helps a few ways.

Firstly, we have real-time peer review on our code,
making it easier for us to catch mistakes that show up.

Secondly, working together at the same time means that
both myself and my colleague will learn something about the neural network
that we are re-implementing.

### Pick out the "forward" step of the model

The "forward" pass of the model is where the structure of the model is defined:
basically the mathematical operations
that transform the input data into the output observations.

A few keywords to look out for
are the `forward()` and  `__calll__()` class methods.

```python
class MyModel(nn.Model):
    # ...
    def forward(self, X):
        # Implementation of model happens here.
        something = ...
        return something
```

For models that involve an autoencoder,
somewhat more seasoned programmers
might create a class method called `encoder()` and `decoder()`,
which themselves reference another model
that would have a `forward()` or `__call__()` defined.

```python
class AutoEncoder(nn.Model):
    # ...
    def forward(self, X):
        something = self.encoder(X)
        output = self.decoder(something)
        return output
```

Re-implementing the `forward()` part of the model
is usually a good way of building a map
of the equations that are being used
to transform the input data into the output data.

### Inspect the shapes of the weights

While the equations give the model _structure_,
the weights and biases, or the _parameters_,
are the part of the model that are optimized.
(In Bayesian statistics, we would usually presume a model structure,
i.e. the set of equations used alongside the priors,
and fit the model parameters.)

Because much of deep learning hinges on linear algebra,
and because most of the transformations that happen
involve transforming the _input space_ into the _output space_,
getting the shapes of the parameters is very important.

In a re-implementation exercise with my intern,
where we re-implemented
a specially designed recurrent neural network layer in JAX,
we did a manual sanity check through our implementation
to identify what the shapes would need to be
for the inputs and outputs.

### Write tests for the neural network components

Once we have the neural network model and its components implemented,
writing tests for those components is a wonderful way of making sure
that
(1) the implementation is correct, to the best of our knowledge, and that
(2) we can catch when the implementation might have been broken inadvertently.

The shape test (as described above) is one way of doing this.

```python
def test_layer_shapes():
    weights = np.random.normal(size=(input_dims, output_dims))
    data = np.random.normal(size=(batch_size, input_dims))
    output = nn_layer(weights, data)
    assert output.shape[1] == output_dims
```

If there are special elementwise transforms performed on the data,
such as a ReLU or exponential transform,
we can test that the numerical properties of the output are correct:

```python
def test_layer_shapes():
    weights = np.random.normal(size=(input_dims, output_dims))
    data = np.random.normal(size=(batch_size, input_dims))

    output = nn_layer(weights, data, nonlinearity="relu")
    assert np.all(output >= 0)
```

### Write tests for the entire training loop

Once the model has been re-implemented in its entirety,
prepare a small set of training data,
and pass it through the model,
and attempt to train it for a few epochs.

If the model, as implemented, is doing what we think it should be,
then after a dozen epochs or so,
the training loss should go down.
We can then test that the training loss at the end
is less than the training loss at the beginning.
If the loss does go down, it's necessary but not sufficient for knowing
that the model is implemented correctly.
However, if the loss _does not_ go down, then we will definitely know
that a problem exists somewhere in the code, and can begin to debug.

An example with pseudocode below might look like the following:

```python
from data import dummy_graph_data
from model import gnn_model
from params import make_gnn_params
from losses import mse_loss
from jax import grad
from jax.experimental.optimizers import adam

def test_gnn_training():
    # Prepare training data
    x, y = dummy_graph_data(*args, **kwargs)
    params = make_gnn_params(*args, **kwargs)

    dloss = grad(mse_loss)
    init, update, get_params = adam(step_size=0.005)
    start_loss  = mse_loss(params, model, x, y)

    state = init(params)
    for i in range(10):
        g = dloss(params, model, x, y)

        state = update(i, g, state)
        params = get_params(state)

    end_loss = mse_loss(params, model, x, y)

    assert end_loss < start_loss
```

A side benefit of this is that
if you commit to only judiciously changing the tests,
you will end up with a stable
and copy/paste-able
training loop that you know you can trust
on new learning tasks,
and hence only need to worry about swapping out the data.

### Build little tools for yourself that automate repetitive (boring) things

You may notice in the above integration test,
we wrote a lot of other functions
that make testing much easier,
such as dummy data generators,
and parameter initializers.

These are tools that make composing parts of the entire training process
modular and easy to compose.
I strongly recommend writing these things,
and also backing them with more tests
(since we will end up relying on them anyways).

### Now run your deep learning experiments

Once we have the model re-implemented and tested,
the groundwork is present for us to conduct extensive experiments
with the confidence that we know
how to catch bugs in the model
in a fairly automated fashion.

## Concluding words

Re-implementing deep learning models can be a very fun and rewarding exercise,
because it serves as an excellent tool
to check our understanding of the models that we work with.

Without the right safeguards in place, though,
it can also very quickly metamorphose into a nightmare rabbithole of debugging.
Placing basic safeguards in place when re-implementing models
helps us avoid as many of these rabbitholes as possible.

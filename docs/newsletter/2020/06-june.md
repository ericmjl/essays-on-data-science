# June 2020 Newsletter

Hello datanistas!

We're back with another edition of the programmer-oriented data science newsletter.
This month, I have so much I've learned and to share,
so I'm _thoroughly_ excited to be writing this newsletter edition!

## Python 3.9 Beta

First things first, Python 3.9's latest beta has been released!
There are new language features in there, including:

1. New dictionary operators
2. A topological sorter class in functools
3. A "least common multiple" (`lcm`) function in the math library,
4. And the best of them all: `string.removeprefix('prefix_goes_here')` and `string.removesuffix('suffix_goes_here')`!
This is a serious convenience piece for those of us who work with files!

Check out [Martin Heinz' blog post on Medium][py39] to learn more!

[py39]: https://medium.com/@martin.heinz/new-features-in-python-3-9-you-should-know-about-14f3c647c2b4

## The Data Science Design Manual

During this extraordinary COVID-19 time,
Springer did an extraordinary thing that I never expected:
They released a whole bucketload of books for free online!
One of them caught my eye: ["The Data Science Design Manual"][dsmanual].
Having browsed through the book PDF, I'm impressed by its coverage of the foundational topics
that I think _every_ data scientist should be equipped with:
statistical inference, data wrangling, linear algebra, and machine learning.
The author, Steven Skiena, also covers more in there.

Go [grab the PDF][dsmanual] while it's still free!

[dsmanual]: https://link.springer.com/book/10.1007%2F978-3-319-55444-0


## Easy `matplotlib` animations

Recently, [`celluloid`][celluloid]caught my eye: it's a package that lets you create `matplotlib` animations easily!

If you need a dead-simple example to convince you to check it out, here's one lifted straight from the repository:

```python
from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
for i in range(10):
    plt.plot([i] * 10)
    camera.snap()
animation = camera.animate()
```

But seriously though, if you use the workhorse Python drawing package `matplotlib` for anything,
this package can be considered to be one of those "great tricks to have" in your bag!


[celluloid]: https://github.com/jwkvam/celluloid

## Points of View

Continuing the theme of visualization,
I wanted to share with you a resource from Nature Methods that has influenced
the entirety of how I approach data visualization and figure design.
This is the [Points of View series][pov],
written by Bang Wong and Martin Krzywinski and many other co-authors.
The entire series [is available online][pov], and is a valuable resource to read.

Two fun tidbits: I devoured the entire series while doing my doctoral training,
eagerly awaiting each new release _like a Netflix addict_.
And I was thoroughly thrilled when Bang decided to join the department I work in at NIBR!
Imagine getting to work with your grad school hero :).

[pov]: http://blogs.nature.com/methagora/2013/07/data-visualization-points-of-view.html

## Document your tests!

For those of you who know me, I am a strong proponent of data scientists
being equipped with good, basic software skills.
When we write code in a "basically good" way (refactored, documented and tested),
we accelerate our productivity many-fold.
One of my interns reminded me of this when we realized
that something that would have otherwise taken days to get right in SQL
ended up being 10 minutes of work
because we documented and tested our pandas DataFrame caches.
(If you wish to read more about testing, I write about it [on my Essays on data science][test_code].)

[test_code]: https://ericmjl.github.io/essays-on-data-science/software-skills/testing/

Documenting code is important.
Turns out, your _test suite_ is also code!
So [in his blog post][doctest], Hyne Schlawack makes the argument that we ought to document our tests,
something that has become painfully obvious in some of the projects I have worked on.
His blog post, then, gets an absolute strong recommendation from me!

[doctest]: https://hynek.me/articles/document-your-tests/

## Development Containers

For those of you who, like myself, moonlight as a software engineer because you develop tools,
this next piece might come as music to your ears:
Visual Studio Code has [superb support for developing a project _inside_ a Docker container][devcontainer].
If you try it out, I guarantee you
the convenience of never having to get someone else set up with development instructions
will be liberating.

Since finding out about it on Thursday (28 May),
I've enabled dev containers on [my personal website][ericmjl],
[my Essays collection][essays],
and the [pyjanitor project][pyjanitor].
In each case, Dockerhub automatically builds containers on every commit to the default branch,
and those containers are referenced in the dev container configuration file,
which means _your local machine never has to build the container_,
you only have to pull it down!
I also got everything working remotely,
so my puny little 12" MacBook now uses a remote GPU-enabled development server.
Speaking of which, if you're interested in making an open source contribution,
or wish to just test-drive dev containers on an actual project,
check out [the docs I wrote for the pyjanitor project][devdocs]!

[devcontainer]: https://code.visualstudio.com/docs/remote/containers
[ericmjl]: https://github.com/ericmjl/website
[essays]: https://github.com/ericmjl/essays-on-data-science
[pyjanitor]: https://github.com/ericmjl/pyjanitor
[devdocs]: https://pyjanitor.readthedocs.io/contributing.html#get-started

## Continuous [STUFF]

I first saw what "Continuous X" meant
when I made my first pull requests to the `matplotlib` project,
and was hooked ever since.
Having a continuous pipeline runner
like Travis or Jenkins or Azure Pipelines
automatically run code and style checks on _every commit_
takes a ton of drudgery out of guaranteeing that our software works properly.
It's like having a Roomba go through your kitchen every time it knows you've finished a meal.
How does "continuous X" apply for data science projects though?

Turns out, individuals way more experienced than myself and much smarter than me
have been thinking about this problem too.
In particular, I want to highlight two articles,
one by [Danilo Sato, Arif Wider and Christoph Windheuser][cd_fowler]
and one [on Booklet.ai][cd_booklet].
In both cases, they raise possible ways to integrate pipeline-based automation into data projects,
making them robust and reproducible.
Be sure to check the articles out!

[cd_fowler]: https://martinfowler.com/articles/cd4ml.html
[cd_booklet]: https://booklet.ai/blog/continuous-delivery-machine-learning-cd4ml/

## From My Collection

I have two articles from my own collection to share.

The first one is about [**how to set up a personal platform as a service (PaaS) called Dokku**][blog_dokku].
It's written for those who are especially cheap (like yours truly)
and don't want to pay $7/month to Heroku for each project that gets hosted there.
For those of you who do want to learn the basics of Heroku-based deployment,
I have [a class on Skillshare][skillshare] that you can use too,
which is being used by the Insight Data Science Fellows in Boston!

[blog_dokku]: https://ericmjl.github.io/essays-on-data-science/miscellaneous/static-sites-on-dokku/
[skillshare]: https://skl.sh/3dbXxNa

The second one is about [**a hack to speed up data loading**][blog_cachier],
using a package called [`cachier`][cachier].
It's a neat hack - especially if you wrap specific data queries from a database into a Python function!

[cachier]: https://github.com/shaypal5/cachier
[blog_cachier]: https://ericmjl.github.io/blog/2019/10/18/caching-long-running-function-results/

## Humour

Let's close with some humorous stuff, if not at least to lighten the mood in these tumultuous times.

Firstly, _Hossein Siamaknejad actually did it_:
automate a game using Python.
And the hack was _absolutely brilliant_:
"RGB detection and programmatically controlled mouse and keyboard".
Props to you, [Hossein][hossein]!

[hossein]: https://www.linkedin.com/posts/siamaknejad_python-ai-automation-ugcPost-6665159908478066688-JB8I/

Secondly, the prolifically-hilarious Kareem Carr writes about ["practicing safe.... modelling"][kareem].

[kareem]: https://twitter.com/kareem_carr/status/1245731021707976704

## Happy, ahem, modelling :)

Hope you enjoyed this edition of the programmer-oriented data science newsletter!
If you'd like to get early access to new written tutorials, essays,
1-on-1 consulting (I just did one session with one of my supporters!)
and free access to the Skillshare workshops that I make,
I'd appreciate your support on Patreon!

Stay safe, stay indoors, and keep hacking!

Cheers,
Eric

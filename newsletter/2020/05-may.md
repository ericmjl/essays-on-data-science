# Data Science Programming May 2020 Newsletter

Hello fellow datanistas!

Here’s the May 2020 edition of my newsletter.
I’m trying out a slightly different formatting;
as always, though, I hope you find it useful.
If you have feedback, [do send it my way][shortmail]!

[shortmail]: http://shortmail.ericmjl.com/

## Multi-Task Learning in the Wild

I recently watched Andrej Karpathy’s [talk on multi-task learning][karpathy], and I learned a ton.
When you’re faced with hardware constraints,
how do you tweak your ML model to get better at more tasks?
Check out his talk to learn more.

[karpathy]: https://slideslive.com/38917690/multitask-learning-in-the-wilderness

## Gaussian processes explained quite simply

I’ve been a fan of Gaussian Processes for non-linear predictive modeling tasks,
especially when writing a neural network feels too much
for the small-ish data that I have.
Learning about them wasn’t easy though.
That said, there’s a wonderful blog post from Yuge Shi, a PhD student at Oxford, explaining GPs in a pretty intuitive fashion.
She put in enough pictures to accompany the math that you should find it [an enjoyable read][gp]!

[gp]: https://yugeten.github.io/posts/2019/09/GP/

## Preview of an exciting development using Dask

If you’re a Dask user, this next video preview is going to be music to your ears.
Matthew Rocklin,
lead developer of Dask and founder of Coiled Computing
(which is providing support for Dask and more)
just showed us spinning Dask clusters in the cloud from a laptop,
getting us to interactive-scale compute.
This is the dream:
burstable, interactive-time, portable, large-scale computing
from my laptop to the cloud with minimal config!
Check out [the screencast][dask] he made for a preview!

[dask]: https://www.youtube.com/watch?v=qaJcAvhgLy4

## SciPy 2020

Virtual SciPy 2020’s schedule has been released!
The conference has been a wonderful place
to learn about the latest in data science and scientific computing tooling.
Come check out the schedule [here][scipy].
I will be there presenting a tutorial on Bayesian statistics;
hope to see you there!

[here]: https://www.scipy2020.scipy.org/schedule

## Faster pandas applies with swifter

While seeking out faster ways to do `pandas` applies,
I learned about a new tool, called [`swifter`][swifter]!
It automatically finds the fastest way to apply a pandas function.
Fits very nicely into the paradigm
of “do one thing and only one thing well”.
Check out [the GitHub repository][swifter]
and let me know what you think of it!
I will be experimenting with it on `pyjanitor`
to see whether it does a better job
with speeding up some of the functions in there.

[swifter]: http://github.com/jmcarpenter2/swifter

## From my collection

### Sane path management in your project directory

I recently wrote [a little post][blog]
about how we can use Python’s pathlib to make file paths
a little more sane in our projects.
[`pyprojroot`][pyprojroot], the tool I feature in the post,
was developed by one of my Python conference dopplegangers, [Daniel Chen][danchen],
who has this wonderfully ironic habit of doing book giveaways and signings
of his Pandas book at R conferences :).

[blog]: https://ericmjl.github.io/blog/2020/4/21/use-pyprojroot-and-pythons-pathlib-to-manage-your-data-paths/

[pyprojroot]: https://github.com/chendaniely/pyprojroot/

[danchen]: https://chendaniely.github.io/

### Updates to our network analysis tutorial!

Finally, with my collaborator [Mridul Seth][mridul]
(who runs the GSoC program with NumFOCUS),
we’ve been updating our Network Analysis Made Simple repository!
My Patreon supporters will get early access to
the tutorial repository before its public launch later in the year,
so if you like it,
[please consider sending a cup of coffee each month][patreon]!
Your support would go a long way to supporting
the creation and maintenance of this teaching material!
(Up next will be Bayesian content - on probabilistic programming -
just in time for SciPy 2020!)

[mridul]: https://mriduls.github.io/
[patreon]: https://patreon.com/ericmjl

Stay safe and enjoy the sunshine!
Eric

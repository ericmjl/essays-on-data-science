# Data Science Programming July 2020 Newsletter

Hello datanistas!

Welcome to the July edition of the programming-oriented data science newsletter.

I usually try to send the newsletter on the first Monday of the month,
but this edition is a little bit later than usual,
and that’s because I was attending SciPy 2020’s virtual conference this month!
Be sure to [catch the videos on Enthought’s YouTube channel](https://www.youtube.com/c/enthought) next week,
when they are edited and uploaded!
(The talks are already up, check them out!)

Back to regular scheduled programming (\*cough cough the SciPy puns cough\*),
this month’s newsletter focuses on production ML systems and everything around it!

## [On getting ML models into production](http://veekaybee.github.io/2020/06/09/ml-in-prod/)

Vicki Boykis has this very well-written article titled
"[Getting machine learning to production](http://veekaybee.github.io/2020/06/09/ml-in-prod/)". In there, she details a lot of the struggle in getting an ML model into a production system. I found it very instructive to read. As it turns out, your ML model is kind of the least of your worries. I won’t spoil it for you - take a good 10 minutes out of your day to read it!

## [MLOps](https://mlops-github.com/)

Related to ML in production is the term
that is quickly becoming "a thing": MLOps.
In the same vein as DevOps, DevSecOps etc.,
it’s all about continuously running things
to check for reproducibility of your analyses,
and at least ensuring that the code continuously runs.
(Checking that everything is semantically correct
is still a human job that can’t be eliminated.)

GitHub has put together [a resource](https://mlops-github.com/)
to help you learn about some of the tooling to help you facilitate
the automation, collaboration, and reproducibility in your ML workflows.

If anything, I have found at work that continuously executed pipelines
are the basic unit of engineering reliability into both my software and my models,
and I’d encourage you to do the same!

## [Approach Your Data with a Product Mindset](https://hbr.org/2020/05/approach-your-data-with-a-product-mindset)

This one comes from the Harvard Business Review.
Usually the HBR is a tad too suit-oriented for my tastes,
but having been involved in some data products at work, this article resonated with me.
Production systems usually imply something that directly impact decision-making,
and "data products" are what help facilitate/accelerate that process.
Especially if there’s a focus on "unmet needs",
that’s when a data + model project can turn into something impactful.
Let me not spoil the read for you,
and instead [come check out the article here](https://hbr.org/2020/05/approach-your-data-with-a-product-mindset).
I hope it gives you inspiration for your work!

## [On Technical Debt...](https://matthewmcateer.me/blog/machine-learning-technical-debt/)

If you’ve read the paper titled
"[Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)",
then come read an article by Matthew McAteer,
in which he dissects the paper and teases out which points have been made obsolete as time progressed.
[It’s an eye-opening read](https://matthewmcateer.me/blog/machine-learning-technical-debt/)!

## Assortments of Goodies

Some other things I have found to be important and informative include:

* [The proposal of a DataFrame protocol for the PyData ecosystem](https://discuss.ossdata.org/t/a-dataframe-protocol-for-the-pydata-ecosystem/267)
* [A succinct introduction to metamorphic testing](https://www.hillelwayne.com/post/metamorphic-testing/)
* [`pbcopy` and `pbpaste`](https://langui.sh/2010/11/14/pbpaste-pbcopy-in-mac-os-x-or-terminal-clipboard-fun/), a macOS utility for copying things to the clipboard from the terminal
* and what I would consider to be [Coiled Computing’s manifesto](https://medium.com/coiled-hq/distributed-computing-for-data-scientists-bfabc72d39da)! (To be clear, they did not pay me to put this link in here, I’m genuinely excited about what they’re building!)

## From my collection

Now for some things from my own collection that I’m excited to share!

### [Network Analysis Made Simple](http://ericmjl.github.io/Network-Analysis-Made-Simple/)

Each year, I submit Network Analysis Made Simple to PyCon, SciPy and PyData conferences,
where they get recorded and are shared with the world for free.
This year, I’m super happy to announce that my co-instructor and I
have [revamped the website](http://ericmjl.github.io/Network-Analysis-Made-Simple/)!
We spent some time restructuring the material,
adding a theme that provides search,
and adding a pipeline that reproducibly builds the notebook collection.
For those of you who like eBook artifacts to keep, we also compiled a book!
[If you’re interested in it, come tell us what you think the book is worth](https://leanpub.com/nams).
We’ll be officially launching next week, after the final chapter is added to the collection!

([Bayesian Data Science by Simulation and Probabilistic Programming](https://github.com/ericmjl/bayesian-stats-modelling-tutorial)
is also undergoing a similar rebuild, stay tuned!)

A few colleagues have also given me feedback
that the Python data science ecosystem
is kind of like "the Wild Wild West".
Reflecting on my prior experience thus far,
I can appreciate the sentiment,
and so I sat down and wrote
[a long essay that tries to linearize/untangle the ecosystem for newcomers](https://ericmjl.github.io/essays-on-data-science/miscellaneous/pydata-landscape/).
I hope it’s useful for you too :).
My [Patreon supporters](https://ericmjl.github.io/essays-on-data-science/supporters/)
have had early access to the article for a while,
so if you appreciate the work, I’d love to hear from you on Patreon!

## Moar Twitter

Have you tried to unsubscribe from a email list and got the response that it can "take a few days"?
Well... follow [this thread](https://twitter.com/Joe8Bit/status/1156312965265707013) to learn why!
(I’d love it if you’d stay with this newsletter though!)

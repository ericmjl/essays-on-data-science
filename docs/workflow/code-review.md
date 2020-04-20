# Practicing Code Review

The practice of code review is extremely beneficial to the practice of software engineering.
I believe it has its place in data science as well.

## What code review is

Code review is the process by which a contributor's newly committed code
is reviewed by one or more teammate(s).
During the review process, the teammate(s) are tasked with ensuring that they

- understand the code and are able to follow the logic,
- find potential flaws in the newly contributed code,
- identify poorly documented code and confusing use of variable names,
- raise constructive questions and provide constructive feedback

on the codebase.

If you've done the practice of scientific research before,
it is essentially identical to peer review,
except with code being the thing being reviewed instead.

## What code review _isn't_

Code review is not the time
for a senior person to slam the contributions of a junior person,
nor vice versa.

## Why data scientists should do code review

### Reason 1: Sharing Knowledge

The first reason is to ensure that project knowledge
is shared amongst teammates.
By doing this, we ensure that
in case the original code creator needs to be offline for whatever reason,
others on the team cover for that person and pick up the analysis.
When N people review the code, N+1 people know what went on.
(It does not necessarily have to be N == number of people on the team.)

In the context of notebooks, this is even more important.
An analysis is complex,
and involves multiple modelling decisions and assumptions.
Raising these questions,
and pointing out where those assumptions should be documented
(particularly in the notebook)
is a good way of ensuring
that N+1 people know those implicit assumptions that go into the model.

### Reason 2: Catching Mistakes

The second reason is that
even so-called "senior" data scientists are humans,
and will make mistakes.
With my interns and less-experienced colleagues,
I will invite them to constructively raise queries about my code
where it looks confusing to them.
Sometimes, their lack of experience gives me an opportunity to explain
and share design considerations during the code review process,
but at other times, they are correct, and I have made a mistake in my code
that should be rectified.

### Reason 3: Social Networking

If your team is remote,
then code review can be an incredibly powerful way
of interacting with one another
in a professional and constructive fashion.

Because of code review,
even in the absence of in-person chats,
we still know someone else is looking at the product of our work.
The constructive feedback
and the mark of approval at the end of the code review session
are little plus points that add up to a great working relationship
in the long-run,
and reduce the sense of loneliness in working remotely.

## What code review can be

Code review can become a very productive time of learning for all parties.
What it takes is the willingness to listen to the critique provided,
and the willingness to raise issues on the codebase in a constructive fashion.

## How code review happens

Code review happens usually in the context of a pull request
to merge contributed code into the master branch.
The major version control system hosting platforms (GitHub, BitBucket, GitLab)
all provide an interface to show the "diff"
(i.e. newly contributed or deleted code)
and comment directly on the code, in context.

As such, code review can happen entirely asynchronously, across time zones,
and without needing much in-person interaction.

Of course, being able to sync up either via a video call,
or by meeting up in person,
has numerous advantages by allowing non-verbal communication to take place.
This helps with building trust between teammates,
and hence doing even "virtual" in-person reviews
can be a way of being inclusive towards remote colleagues.

## Parting words

If your firm is set up to use a version control system,
then you probably have the facilities to do code review available.
I hope this essay encourages you to give it a try.

## Thank you for reading!

If you enjoyed this essay and would like to receive early-bird access to more,
[please support me on Patreon][patreon]!
A coffee a month sent my way gets you _early_ access to my essays
on a private URL exclusively for my supporters
as well as shoutouts on every single essay that I put out.

[patreon]: https://patreon.com/ericmjl

Also, I have a free monthly newsletter that I use as an outlet
to share programming-oriented data science tips and tools.
If you'd like to receive it, sign up on [TinyLetter][tinyletter]!

[tinyletter]: https://tinyletter.com/ericmjl

# Hiring and Interviewing Data Scientists

Last year in 2021, I hired two new teammates into my home team.
While I had been involved in hiring data scientists in the past,
this was the first time I was primariliy responsible for the role.
When I first joined,
I thought I would have a bit of time to ease into
the team lead part of the role.
But by day 2, which was July 21,
my manager Andrew sent me a Teams message saying,
"Hey, two positions for you have been approved. Merry Christmas!"

## Criteria for Hiring

During this time, I had to develop the criteria for hiring.
Thankfully, our Talent Acquisition (TA) team had a process in place,
so I didn't have to design that half.
One thing that our department head, Dave Johnson, emphasized
was to keep the technical bar high
because we want to hire people who can hit the ground running straight away.
I also knew, from previous experience,
that I would enjoy working with bright individuals who were
quick to learn,
thorough in thinking through problems,
capable of going deep into technical details,
had sufficient humility to accept feedback,
and were also courageous enough to challenge my views.
The two whom we hired on the team fit these criteria perfectly,
and have helped me expand my ways of thinking too.

At the same time, our Talent Acquisition team suggested to us that
we shouldn't necessarily hire someone who hits
all of the required skills for that level,
but rather someone who has a majority of the skills necessary
and has shown the potential to learn the rest.
Why?
It's related to our psychology.
Most of us are motivated when we see a positive delta in our abilities,
receive affirmation that we are improving,
and can see the fruits of our labor in a finished product.
Hence, this advice ensures that our new hires
are both able to hit the ground running while also staying motivated longer.

## Interviewing for Code Skill

One thing I learned from the hiring process is that
without well-designed interview questions,
it's very easy to be fooled by general answers that a candidate provides.
They may not be faking it,
but they may also not be providing sufficient detail
to prove their technical knowledge.
Therefore, I had to learn how to ask questions
that were hard to fake answers to.
Though I disagree with much of Elon Musk's ways,
there is one that I read about that I think is very useful:
asking for specific details throughout the interview process.

Combining that with two other principles,
which are to:

1. ensure that the interview process tests skills directly related to the job, and
2. ensure that the process does not put an undue burden on the candidate.

### Interview Prompt

If an interviewer is structuring their interview process well,
they usually will have a prompt that a candidate is asked to respond to.
In this case, the prompt is as follows:

> Please walk me through a chunk of code that you've written.
> This will mimic a real life code review session.
> You can choose anything that you've written,
> as long as it's written in a language that I am familiar with.
> In order of familiarity, I can read Python, Java, and R.
> We will use this code for a code review session.

Any code was fine, as long as it was code that they wrote.
I would ask them to explain the code,
walk through design decisions and choices made,
and then ask them to explain how they would improve the code.
From what I know, this is likely an unconventional way of interviewing.

### Interviewing Goals

I designed this interview process with a few goals in mind.

Firstly, it **mimics a real-life code review session**.
It allows me to see how the candidate thinks about the code,
and to see if they have "senior" ways of thinking.
It also allows me to see how the candidate responds to feedback,
of the kind that we would often do in real code reviews,
about their code,
thereby revealing whether they have a defensive personality or not.
(To reveal: we have high standards, but we are also very gentle with feedback.)

Secondly, because this code is code that the candidate has written,
**the candidate has a "home court" advantage.**
They are not trying to write (leet)code
that hits some imagined standard in their head.
For them, this is real-life code that should be solving
a real life problem that they should be familiar with.
For us, it will be a realistic reflection of their current coding ability.

Thirdly, through this process,
I can also see how the candidate
translates their knowledge of a problem into code.
What abstractions are chosen, if any?
Do they match the hierarchy of scientific knowledge,
intended usage patterns,
or business problem involved?
Are they able to explain their design decisions and tradeoffs made?
When they design their code, are they thinking for the future?

The process of reviewing the code that the candidate wrote
is a great way of simulating how the candidate would work on the team.
Their code gives them a "home team" advantage,
but our gentle (but detailed) questioning
can reveal whether they have a defensive personality or not.
We don't want defensive personalities!
We want people who are willing to learn and improve,
and being able to engage a code reviewer on the details of their code
is a great way of revealing this.

## Interviewing for Modeling Skill

While I was able to interview for code skill,
I still had to figure out how to interview for modeling skill.
Here, riffing off the previous process,
I think I have a process that satisfies the same goals as before
while also being able to test for modeling skill.
In some ways, I believe this will supersede the previous process,
since I am going to be asking for something much more specific.

### Interview Prompt for Modeling Skills

Here is the prompt that I will be using in the future.

> Please teach me a probabilistic model of your choice.
> When explaining the model, please consider what the model is useful for,
> key ways it differs from related models,
> how it is trained,
> and how it is used.
> You will have 10 minutes for this part.
> Once we are done with that,
> please walk me through your implementation of that model in NumPy.
> You only need to implement the forward pass of the model,
> and not the training loop.
> Consider the design of the implementation,
> such as how parameters are stored,
> how the model is initialized,
> and the model's application programming interface (API).
> We will use this code as part of a mock code review session.
> This part will be 10 minutes long.

Once again, this prompt gives the home court advantage to the candidate,
is specific enough for me to be able to test for modeling skill,
and is also a realistic simulation of how a candidate will perform
in a critical part of our role, which is code review.

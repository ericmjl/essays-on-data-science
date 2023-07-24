# A Developer-First Guide to LLM APIs (March 2023)

Large Language Models (LLMs) are having a moment now!
We can interact with them programmatically in three ways:
OpenAI's official API,
LangChain's abstractions,
and LlamaIndex.
How do we choose among the three?
I'd like to use a minimally complex example to showcase how we might make this decision.

## The Problem

I blog.

(Ok, well, that's quite the understatement, given that you're reading it right now.)

As you probably can tell from my blog's design,
I need to summarize the blog post for the blog landing page.
Because I usually share the post on LinkedIn,
I also need to generate a LinkedIn post advertising the blog post.
I've heard that emojis are great when sharing posts on LinkedIn,
but I can only sometimes remember the names of appropriate emojis.
Some automation help would be great here.
Finally, if I can make a better title than I initially thought of,
that would also constitute an improvement.

I've decided that I wanted a tool that can summarize my blog posts,
generate appropriately emojified LinkedIn posts for me to advertise those posts,
and provide a catchy and engaging title without being clickbait.
These are tedious to write!
Wouldn't it be great to have a tool that can generate both?
That's the use case for LLMs!

## Desiderata

Here's the list of requirements I have to build the tool I want.

Firstly, I should be able to provide the _text_ of a blog post as input and get back:

1. A proposed title according to my desired specifications,
2. A summary to put onto my website's blog listing page, and
3. A LinkedIn post that I can use to share with others.

Secondly, the tool should minimize token usage.
Tokens equal money spent on this task,
so saving on token usage would increase my leverage trading time for money.

Finally, because I'm still writing some code to implement this tool,
I'd like to use a package that would provide the most easily maintained code.
Of course, that means a subjective judgment of how simple the abstractions are.

To that end, I will show how to implement this writing tool using three APIs currently available:
the official OpenAI Python API, the LangChain API, and the LlamaIndex API.
This exercise lets us see which ones are most suitable for this particular use case.
We will be using GPT-4 everywhere, as its quality is known to be superior to GPT-3.5.
Finally, I will focus on blog post summary generation and LinkedIn post generation
when comparing the APIs before choosing one framework to implement the complete program.

## The test blog post

The blog post I'll use for implementing this is my most recent one on the Arc browser.
I will be passing in the Lektor raw source without the title.
The raw source is available on [my website repository](https://raw.githubusercontent.com/ericmjl/website/main/content/blog/arc-browser-first-impressions/contents.lr).

According to [`tiktoken`](https://github.com/openai/tiktoken),
this text uses 1436 tokens to encode:

```python
blog_text = ... # taken from my raw source.

encoder = tiktoken.get_encoding("cl100k_base")
tokens = encoder.encode(blog_text)
len(tokens)
```

```text
1436
```

This is a constant throughout the post.

## Prompts

The prompts that I will use to generate the desired text are as follows.
If the three prompts are too long to remember,
you can focus on the one for summarization as an anchoring example.

### Summary

```python
summarization_prompt = f"""You are a blog post summarization bot.
Your take a blog post and write a summary of it.
The summary is intended to hook a reader into the blog post and entice them to read it.
You should add in emojis where appropriate.

My previous summaries sounded like this:

1. I finally figured out how to programmatically create Google Docs using Python. Along the way, I figured out service accounts, special HTML tags, and how to set multi-line environment variables. Does that tickle your brain?
2. Here is my personal experience creating an app for translating Ark Channel devotionals using OpenAI's GPT-3. In here, I write about the challenges I faced and the lessons I learned! I hope it is informative for you!
3. I discuss two Twitter threads that outline potential business ideas that could be built on top of ChatGPT3, a chatbot-based language model. What's the tl;dr? As mankind has done over and over, we build machines to solve mundane and repetitive tasks, and ChatGPT3 and other generative models are no exception!

The summary you generate should match the tone and style of the previously-generated ones.
"""
```

### LinkedIn Post Prompt

```python
linkedin_prompt = """You are a LinkedIn post generator bot.
You take a blog post and write a LinkedIn post.
The post is intended to hook a reader into reading the blog post.
The LinkedIn post should be written with one line per sentence.
Each sentence should begin with an emoji appropriate to that sentence.
The post should be written in professional English and in first-person tone.
"""
```

### Title Prompt

```python
title_prompt = """You are a blog post title generator.
You take a blog post and write a title for it.
The title should be short, ideally less than 100 characters.
It should be catchy but not click-baity,
free from emojis, and should intrigue readers,
making them want to read the summary and the post itself.
Ensure that the title accurately captures
the contents of the post.
"""
```

## Setup API key

Using OpenAI’s API requires we set the OpenAI API key before doing anything;
this is also true for using LangChain and LlamaIndex.
As always, to adhere to reasonable security practices when developing locally,
we should store the API key as an environment variable in a `.env` file
listed in the `.gitignore`of a repository
and then load the API key in our Jupyter notebooks.
Here is how we implement it. Firstly, the `.env` file:

```bash
 # .env
export OPENAI_API_KEY="..."
```

And then, at the top of our Jupyter notebook or Python script:

```python
from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
```

## Implementation using OpenAI's API

### Summarization

Let’s start off using the OpenAI Python API. To use GPT-4, we need to provide a chat history of messages that looks something like this:

```python
messages = [
    {"role": "system", "content": summarization_prompt},
    {"role": "user", "content": f"Here is my blog post source: {blog_post}"
]
```

Then, we pass the message history into the OpenAI chat completion class

```python
result = openai.ChatCompletion.create(messages=messages, model="gpt-4", temperature=0.0)
```

Once the API call has returned, we can see what gets returned:

```python
summary = result["choices"][0]["message"]["content"]
print(summary)
```

```text
I recently got my hands on the new [Arc browser](https://arc.net/) and I'm loving it! 🤩 Arc reimagines the browser as a workspace, helping us manage our chaotic tabs and multiple projects. Some cool features include tabs that expire ⏳, spaces for grouping tabs 🗂️, rapid switching between tabbed and full-screen mode 🖥️, side-by-side view for multitasking 📑, and automatic developer mode for locally hosted sites 🔧. Arc's focus on UI design is a game-changer for productivity and focus! Check out my first impressions and see if Arc could be your new favorite browser! 🚀
```

The total number of tokens used here is:

```python
len(encoder.encode(summarization_prompt)) \
+ len(encoder.encode(human_message["content"])) \
+ len(encoder.encode(summary))
```

```text
1870
```

### LinkedIn Post

Now, let's make the LinkedIn post.

```python
linkedin_prompt = {"role": "system", "content": linkedin_prompt}
messages = [linkedin_prompt, human_message]

result = openai.ChatCompletion.create(messages=messages, model="gpt-4", temperature=0.0)

linkedin_post = result["choices"][0]["message"]["content"]
print(linkedin_post)
```

```text
🚀 Just tried the new [Arc browser](https://arc.net/) for 24 hours!

🧠 It's designed to fit the modern multitasker's brain.

⏳ Love the tabs that expire feature - goodbye clutter!

🌐 Spaces for grouping tabs - perfect for juggling multiple projects.

🔍 Rapid switching between tabbed and full-screen mode for better focus.

📏 Side-by-side view for efficient multitasking.

👨‍💻 Automatic developer mode for locally hosted sites - a developer's dream!

🌟 Overall, Arc is a game-changer for productivity and focus.

📖 Read my full experience in the blog post [here](<blog_post_link>).

```

The total number of tokens used here is:

```python
len(encoder.encode(linkedin_prompt)) \
+ len(encoder.encode(human_message["content"])) \
+ len(encoder.encode(linkedin_post))
```

```text
1669
```

### Cost Accounting

Tabulating the total cost of tokens,
we have 3c per 1,000 tokens for prompts
and 6c per 1,000 token for generated texts.
We can do the math easily here:

```python
# Cost
prompt_encoding_lengths = (
    len(encoder.encode(linkedin_prompt)) \
    + len(encoder.encode(human_message["content"])) \
    + len(encoder.encode(summarization_prompt)) \
    + len(encoder.encode(human_message["content"]))
)

generated_encoding_lengths = (
    len(encoder.encode(linkedin_post)) + \
    len(encoder.encode(summary))
)

cost = (
    0.03 * prompt_encoding_lengths + 0.06 * generated_encoding_lengths
) / 1000

print(cost)
```

```python
0.11657999999999999
```

Or about 12c to perform this operation.

How much ROI do we get here?
Excluding benefits, equity, and more, a new Ph.D. grad data scientist
is paid about `$150,000` (give or take) per year in the biomedical industry in 2023.
Assuming about 250 days of work per year at an average of 8 hours per day,
we're talking about an hourly rate of `$75`/hr at that salary.
If it takes that person 10 minutes to cook up a summary and LinkedIn post
(which is about how long I take -
excluding figuring out what emojis to put in
because that's, for me, bloody time-consuming.),
then we're looking at `$12.5` worth of time put into crafting that post.
Looking at just the cold hard numbers,
**we're looking at a 100X cost improvement by using GPT-4 as a writing aid.**

## Implementation using LangChain's API

Now, let's do the same thing, except with the LangChain API. Here, we'll be using LangChain's Chain API.

### Summarization

First off, summarization:

```python
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)
from langchain.prompts import PromptTemplate

system_message_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        template=summarization_prompt,
    input_variables=[],
    ),
)
from langchain.chat_models import ChatOpenAI


chat = ChatOpenAI(model_name="gpt-4", temperature=0.0)

human_message_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template="Here is my post:\n\n {blog_post}?",
        input_variables=["blog_post"],
    )
)

chat_prompt_template = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
summary_chain = LLMChain(llm=chat, prompt=chat_prompt_template)
summary = summary_chain.run(blog_post=blog_text)
print(summary)
```

```text
I recently tried out the Arc browser 🌐, which reimagines the browser as a workspace to boost productivity! 🚀 After 24 hours of use, I'm loving its features: tabs that expire ⏳, spaces for organizing tabs 🗂️, rapid switching between tabbed and full-screen mode 🖥️, side-by-side view for multitasking 📑, and automatic developer mode for locally hosted sites 💻. Arc's focus on UI design helps us stay focused and organized in our digital lives. Curious to know more? Dive into my first impressions! 😃
```

According to tiktoken:

```text
len(encoder.encode(summary))
```

The generated text was 191 tokens.
```python
len(encoder.encode(system_message_prompt.format_messages()[0].content))
```

The system prompt was 237 tokens.

```python
len(encoder.encode(human_message_prompt.format_messages(blog_post=blog_text)[0].content))
```

The human message prompt was 1442.

We'll keep those numbers in mind when doing the final cost accounting.

### LinkedIn Post

Now, let's make the LinkedIn post.

```python
linkedin_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        template=linkedin_prompt,
    input_variables=[],
    ),
)

linkedin_blog_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template="Here is the blog post:\n\n{blog_post}",
        input_variables=["blog_post"],
    )
)

linkedin_chat_prompt_template = ChatPromptTemplate.from_messages([linkedin_system_prompt, linkedin_blog_prompt])

linkedin_chain = LLMChain(llm=chat, prompt=linkedin_chat_prompt_template)

linkedin_post = linkedin_chain.run(blog_post=blog_text)
print(linkedin_post)

```

```text
🎉 Just tried the new [Arc browser](https://arc.net/) and I'm loving it! 🧠

🕒 Arc's unique features like tabs that expire and spaces for different projects help me stay focused and organized. 📌

🚀 Check out my blog post for a detailed review and first impressions of this game-changing browser: [Arc Browser: First Impressions](<blog post link>) 🌐

👨‍💻 Are you ready to revolutionize your browsing experience? #ArcBrowser #Productivity #Tools

```

Doing an accounting of the tokens once again:

```text
len(encoder.encode(linkedin_post))
```

The generated LinkedIn post used 151 generated tokens.

```text
len(encoder.encode(linkedin_blog_prompt.format_messages(blog_post=blog_text)[0].content))
```

The blog post prompt itself used 1441 prompt tokens.

```text
len(encoder.encode(linkedin_system_prompt.format_messages()[0].content))
```

And the system prompt used 71 tokens.

### Cost Accounting

As usual, let's do the accounting of tokens.

```python
# Cost Accounting
generated_encodings_length = len(encoder.encode(linkedin_post)) + len(encoder.encode(summary))

prompt_lengths = (
    len(encoder.encode(human_message_prompt.format_messages(blog_post=blog_text)[0].content)) \
    + len(encoder.encode(system_message_prompt.format_messages()[0].content)) \
    + len(encoder.encode(linkedin_blog_prompt.format_messages(blog_post=blog_text)[0].content)) \
    + len(encoder.encode(linkedin_system_prompt.format_messages()[0].content))
)

cost = 0.03 * prompt_lengths + 0.06 * generated_encodings_length
print(cost / 1000)
```

```python
0.11648999999999998
```

As we can see, this also costs about 12c for the entire exercise.

## Implementation using LlamaIndex

The way LlamaIndex works is different from the previous two frameworks.
With OpenAI's and LangChain's APIs, we stuffed the entire document into the prompt for each task.
With LlamaIndex, we can embed and store the text beforehand
and then query it with a prompt for our LLM. Here is how it looks:

### Embed Text

To do this, we use the `GPTSimpleVectorIndex` provided by LlamaIndex:

```python
from llama_index import Document, GPTSimpleVectorIndex, LLMPredictor

# Index documents using GPT4
llm_predictor = LLMPredictor(llm=chat)
documents = [Document(blog_text)]
index = GPTSimpleVectorIndex(documents=documents, llm_predictor=llm_predictor)
```

Thanks to the built-in token accounting capabilities of LlamaIndex, we can see that building the index costed us 1637 tokens.

```text
INFO:llama_index.token_counter.token_counter:> [build_index_from_documents] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_documents] Total embedding token usage: 1637 tokens
```

### Summarization

Let's start by creating a summary of the blog post.

```python
response = index.query(summarization_prompt)
print(response.response)
```

```text
Discover the Arc browser, a game-changer that reimagines the browser as a workspace 🌐! With features like tabs that expire ⏳, spaces for grouping tabs 📁, rapid switching between modes ⚡, side-by-side view 👀, and automatic developer mode for locally hosted sites 🔧, Arc is designed to boost your productivity and focus 🚀. Dive into my 24-hour experience with this innovative browser and see how it fits my brain 🧠!
```

Not bad! The response looks pretty good, though I might edit it a bit further.

The token usage here is:

```text
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 2026 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 257 tokens
```

### LinkedIn Post Generation

Now, let's try generating a LinkedIn post the same way.

```python
response = index.query(linkedin_prompt)
print(response.response)
```

```text
🚀 Just tried the new Arc browser for 24 hours!
🌟 It reimagines the browser as a workspace, perfect for multitaskers.
⏰ Love the tabs that expire feature, keeping my workspace clutter-free.
🌈 Spaces help me group tabs by context, boosting focus and productivity.
🖥️ Rapid switching between tabbed and full-screen mode is a game-changer.
👩‍💻 Developer mode for locally hosted sites makes web development a breeze.
🔗 Check out my detailed review on my blog and see how Arc can transform your browsing experience!
```

Not bad, it followed my instructions as well.

Here's the token usage:

```text
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 1874 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 78 tokens
```

### Cost Accounting

LlamaIndex did not break down the difference in prompt tokens vs. generated text tokens for me
but split out embedding tokens.
In calculating the cost, we will make the following assumptions:

- the cost of embedding tokens to be [$0.0004 per 1000 tokens](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings),
- of the LLM token usage budget, the part used for prompting can be calculated by subtracting the number of tokens used to encode the output from the reported LLM token usage.

Crunching the numbers, we get:

```python
embedding_tokens = 1637 + 257 + 78

linkedin_llm_tokens = 1874
linkedin_generated_tokens = len(encoder.encode(response.response))

summary_llm_tokens = 2026
summary_generated_tokens = len(encoder.encode(summary_response.response))

llm_tokens_cost = (0.06 * (linkedin_generated_tokens + summary_generated_tokens) + 0.03 * (linkedin_llm_tokens - linkedin_generated_tokens) + 0.03 * (summary_llm_tokens - summary_generated_tokens)) / 1000

embedding_tokens_cost = embedding_tokens * 0.0004 / 1000

print(f"Cost: {llm_tokens_cost + embedding_tokens_cost}")
```

```text
Cost: 0.1243588
```

Also about 12c for this exercise.

## Generated Text Comparison

### Summarization

Here are the generated texts for summarization side-by-side:

#### OpenAI's Summarization

```text
I recently got my hands on the new [Arc browser](https://arc.net/) and I'm loving it! 🤩 Arc reimagines the browser as a workspace, helping us manage our chaotic tabs and multiple projects. Some cool features include tabs that expire ⏳, spaces for grouping tabs 🗂️, rapid switching between tabbed and full-screen mode 🖥️, side-by-side view for multitasking 📑, and automatic developer mode for locally hosted sites 🔧. Arc's focus on UI design is a game-changer for productivity and focus! Check out my first impressions and see if Arc could be your new favorite browser! 🚀
```

#### LangChain's Summarization

```text
I recently tried out the Arc browser 🌐, which reimagines the browser as a workspace to boost productivity! 🚀 After 24 hours of use, I'm loving its features: tabs that expire ⏳, spaces for organizing tabs 🗂️, rapid switching between tabbed and full-screen mode 🖥️, side-by-side view for multitasking 📑, and automatic developer mode for locally hosted sites 💻. Arc's focus on UI design helps us stay focused and organized in our digital lives. Curious to know more? Dive into my first impressions! 😃
```

#### LlamaIndex's Summarization

```text
Discover the Arc browser, a game-changer that reimagines the browser as a workspace 🌐! With features like tabs that expire ⏳, spaces for grouping tabs 📁, rapid switching between modes ⚡, side-by-side view 👀, and automatic developer mode for locally hosted sites 🔧, Arc is designed to boost your productivity and focus 🚀. Dive into my 24-hour experience with this innovative browser and see how it fits my brain 🧠!
```

#### Style verdict

Of the three, LlamaIndex's style is the furthest from my usual style,
though, in some instances, I might choose the style generated by LlamaIndex to change things up on my blog.

### LinkedIn Post Generation

#### OpenAI's Post

```text
🚀 Just tried the new [Arc browser](https://arc.net/) for 24 hours!

🧠 It's designed to fit the modern multitasker's brain.

⏳ Love the tabs that expire feature - goodbye clutter!

🌐 Spaces for grouping tabs - perfect for juggling multiple projects.

🔍 Rapid switching between tabbed and full-screen mode for better focus.

📏 Side-by-side view for efficient multitasking.

👨‍💻 Automatic developer mode for locally hosted sites - a developer's dream!

🌟 Overall, Arc is a game-changer for productivity and focus.

📖 Read my full experience in the blog post [here](<blog_post_link>).

```

#### LangChain's Post

```text
🎉 Just tried the new [Arc browser](https://arc.net/) and I'm loving it! 🧠

🕒 Arc's unique features like tabs that expire and spaces for different projects help me stay focused and organized. 📌

🚀 Check out my blog post for a detailed review and first impressions of this game-changing browser: [Arc Browser: First Impressions](<blog post link>) 🌐

👨‍💻 Are you ready to revolutionize your browsing experience? #ArcBrowser #Productivity #Tools
```

#### LlamaIndex's Post

```text
🚀 Just tried the new Arc browser for 24 hours!
🌟 It reimagines the browser as a workspace, perfect for multitaskers.
⏰ Love the tabs that expire feature, keeping my workspace clutter-free.
🌈 Spaces help me group tabs by context, boosting focus and productivity.
🖥️ Rapid switching between tabbed and full-screen mode is a game-changer.
👩‍💻 Developer mode for locally hosted sites makes web development a breeze.
🔗 Check out my detailed review on my blog and see how Arc can transform your browsing experience!
```

#### Style Verdict

Of the three, OpenAI's is furthest from how I usually write my LinkedIn posts,
but in fairness, I didn't instruct the model with examples provided.
If I were to choose, I would pick LlamaIndex's generated post.

## Developer Experience (DX)

For this simple use case, which would I go with? LlamaIndex, OpenAI's official API, or LangChain?

As a lazy programmer, I would go with LlamaIndex.
That's because I needed the fewest lines of code to reach my desired endpoints.
It is easy to remember the API as well - you only need to remember the pattern:

1. `Document` to wrap the text that we imported,
2. `GPTSimpleVectorIndex` (or more generically `<some>Index`), and
3. `LLMPredictor` to wrap around LangChain's LLMs.
4. `<Index>.query(prompt)`

The biggest reason why LlamaIndex is best suited to this use case is that
querying text is a relatively simple use case.
We only need to load the document in a query-able fashion.
Furthermore, as you can see from my code above,
using LlamaIndex resulted in the least boilerplate code.

That said, is LlamaIndex the right choice for every application?
Probably not.
As of March 2023, LangChain is geared towards much more complex (and autonomous) LLM use cases.
So the abstractions that the library creators put in the library may be geared
to design larger LLM applications rather than simple ones like we just did.
And OpenAI's API is officially supported,
which means it would likely have an official "blessing" in the long run.

I have a penchant/bias for more tightly-controlled LLM applications,
which means forgoing a chat interface in favour of a single-text-in-single-text-out interface.
Indeed, while I see the usefulness of chat-based interfaces for exploration,
I don't think it will become the dominant UI when embedding LLMs in applications.
Rather, I predict that we'll see UI/UX researchers designing, on a per-application basis,
whether to use a free-flowing chat UI or to use a more tightly controlled ad-lib-style interface,
or [even](https://twitter.com/thesephist/status/1587929014848540673)
[crazier](https://twitter.com/thesephist/status/1592241959489380354)
[interfaces](https://twitter.com/thesephist/status/1590545448066252800)!
The factor that should matter the most here is the ROI gained in human time.

Additionally, I predict that we will see data science teams use LLMs
to bang out dozens of little utility apps much faster than previously possible.
These utility apps will likely serve niche-specific but often-repeated use cases,
and may serve as the basis of larger applications that get developed.
For example, we'll probably see built apps that let users ad-lib a templated prompt.
We'll see things like LLMs being the role of data engineer
(e.g. [structuring data from unstructured text](https://ericmjl.github.io/blog/2023/2/5/building-a-gpt3-based-translation-app/))
and domain-specific idea generators prompted by domain experts or domain needs (as we saw here),

The short answer is that we'll see more customization to local contexts,
with highest ROI use cases being prioritized.

## Caveats to this analysis

There are some caveats here to what I've done that I'd like to point out.

Firstly, I've used the most straightforward implementations, stuffing the most text into the prompt.
Why? It is because I'm still exploring the libraries and their APIs and partly because so much development has happened quickly.
Others will be able to figure out more efficient ways of implementing what we did here with their favourite framework.

Secondly, this particular task is quite simple.
LangChain, on the other hand, can generate much more complex programs, as we can see from its documentation.
Critiquing LangChain's heavy abstractions would be unfair, as it's very likely designed for more complex autonomous applications.

## Conclusion

One application built three ways with three different libraries.
We have seen how the outputs can differ even with the same prompts and how the developer experience can vary between the three.
That said, I caution that these are early days.
Libraries evolve.
Their developers can introduce more overhead or reduce it.
It's probably too early to "pick a winner";
as far as I can tell, it's less a competition and more a collaboration between these library developers.
However, we can keep abreast of the latest developments and keep experimenting with the libraries on the side,
finding out what works and what doesn't and adapting along the way.

The near-term value proposition of GPT as a tool lies in its ability to automate low-risk, high-effort writing.
We saw through cost calculations that LLMs can represent a 100X ROI in time saved.
For us, as data scientists, that should be heartening!
Where in your day-to-day work can you find a similar 100X ROI?

# Static Sites and Apps On Your Own Dokku Server

**Summary:** In this essay,
I'm going to share with you how you can deploy
your own static sites and apps on a Dokku server.

## Introduction

You've worked on this awesome Streamlit app,
or a Panel dashboard,
or a Plotly Dash web frontend for your data science work,
and now you've decided to share the work.
Or you've built documentation for the project,
and you need to serve it up.
Except, if your company doesn't have a dedicated platform for apps, you're stuck!
That's because you've now got to share it from your laptop/workstation
and point your colleagues to there
(right... go ahead and email them a link to `http://10.16.213.24:8501` right now...)
and keep your computer running perpetually
to serve the app in order for them to interact with it.

Or, you copy/paste the docs into a separate hosted solution,
and now the docs are divorced from your code,
leading to documentation rot in the long-run
because it's too troublesome to maintain two things simultaneously.
That's much too fragile.
What you need is another hosting machine
that isolated from your development machine,
so that you can develop in peace
while the hosting machine reliably serves up the working,
stable version of your work.

The specific thing that you _really_ need is a "Platform as a Service".
There's a lot of commercial offerings,
but if you're "cheap" and don't mind learning some new concepts
to help you get around the web, then this essay is for you.
Here, I'm going to show you how to configure
and deploy Dokku as a personal PaaS solution
that you can use at work and for hobby projects.
I'm then going to show you how to deploy a static site
(which can be useful for hosting blogs and documentation),
and finally I'll show you how to deploy a Streamlit app,
which you can use to show off a front-end to your fancy modelling work.
Along the way, I hope to also point out the "generalizable" ideas
behind the steps listed here,
and give you a framework (at least, one useful one)
for building things on the web.

## But, but why?

### If you're part of a company...

Your organization might not be equipped
with modern PaaS tools that will enable you, a data scientist,
to move quickly from local prototype to share-able prototype.
If, however, you have access to bare metal cloud resources
(i.e. just gimme a Linux box!),
then as a hacker-type,
you might be able to stand up your own PaaS
and help demonstrate to your infrastructure team the value of having one.

### If you're doing this for your hobby projects...

You might be as cheap as I am,
but need a bit more beefy power
than the restrictions given to you on Heroku
(512MB RAM, 30 minute timeouts,
and limited number of records in databases),
_and_ you don't want to pay $7/month for each project.

Additionally, you might want a bit more control over your hosting options,
but you don't feel completely ready
to go fiddling with containers and networking
without a software stack to help out _just a bit_.

### More generally...

You might like the idea of containers,
but find it kind of troublesome to learn
_yet another thing that's not trivial to configure, execute and debug_ (i.e. Docker).
Dokku can be a bridge to get you there,
as it automates much of the workflow surrounding Docker containers.
It also comes with an API that both matches closely to Heroku
(which is famous for being very developer-friendly)
and also helps you handle proxy port mapping and domains easily.

Are you ready? Let's go!

## Pre-requisites

I'm assuming you know how to generate and use SSH keys
to remotely access another machine.
This is an incredibly useful thing to know how to do,
and so I'd recommend that you pick this skill up.
(As usual, DigitalOcean's community pages have
[a great tutorial][ssh-tutorial].)

[ssh-tutorial]: https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu

I am also assuming that you have access to a Linux box of some kind
with an IP address that you can expose to the "internet".
The "internet" in this case can mean the world wide web
if you're working on a personal project,
or your organization's "intranet"
if you're planning on only letting those in your organization
access the sites and apps that you will build.

I'm also assuming familiarity with `git`,
which I consider to be an indispensable tool in a data scientist's toolkit.

This last point is not an assumption, but an exhortation:
you should be building your data app prototype
in accordance to 12-factor app principles.
It'll make (most of) your Engineering colleagues delight in working with you.
(Yes, there are some esoteric types that don't subscribe to 12 factor app principles...)
If you've never heard of it, [go check it out here](https://12factor.net/).
It's a wonderful read that will change
how you build your data app prototypes for the better.
It will also make handing over the app to Engineering
much easier in the long-run,
improving your relationship with the Engineering team
that will take care of your app!

## Set up a Box in the Cloud (optional if you have one)

If you don't already have another computer that you have access to,
or if you're curious on how to get set up in the cloud,
then follow along these instructions.

To make things a bit more concrete,
I'm going to rent a server on DigitalOcean (DO).
If you don't have a DigitalOcean account,
feel free to use my [referral link][do_referral] to sign up
(and get free $100 credits that you can spend over 60 days)
if you haven't got a DigitalOcean account already.
(Disclaimer: I benefit too,
but your support helps me make more of this kind of content!)
Once you've signed up and logged into the DigitalOcean cloud dashboard,
you can now set up a new Droplet.

??? question "Droplets?"

    "Droplet" is nothing more than DO's fancy name for a cloud server,
    or basically a computer that they're running.

[do_referral]: https://m.do.co/c/2832a2124e66

To do so, click on the big green "Create" button,
set up a Droplet with the following settings:

1. Ubuntu operating system
2. "Standard" plan at $5/mo or $10/mo [^ram]
3. Additional options: "monitoring"
4. Authentication: you should use SSH keys (this is a pre-requisite for this essay).
5. Hostname: Give it something memorable.
6. Backups: Highly recommended. Give yourself peace of mind that you can rollback anytime.

[^ram]: I am paying for the $10/mo plan for the extra RAM seems to help.

Once you're done with that,
hit the big green "Create Droplet" button
right at the bottom of the screen!

Once your droplet is set up,
you can go ahead and click on the "Manage \> Droplets" left menu item,
and that will bring you to a place
where you can see all of your rented computers.

??? info "The Cloud"

    FYI, that's all the cloud is:
    renting someone else's computers.
    It turns out to be a pretty lucrative business!
    And because it's just someone else's computers,
    don't think of it as something magical.


## Setup Dokku on your Shiny Rented Machine

Let's now go ahead and set up Dokku on your shiny new droplet.

### Run the Dokku installation commands

Dokku installation on Ubuntu is quite easy;
the following instructions are taken from the [Dokku docs][dokku-docs].
SSH into your machine, then type the following:

[dokku-docs]: http://dokku.viewdocs.io/dokku/getting-started/installation/

```bash
wget https://raw.githubusercontent.com/dokku/dokku/v0.20.4/bootstrap.sh;
# CHECK FOR LATEST DOKKU VERSION!
# http://dokku.viewdocs.io/dokku/getting-started/installation/
sudo DOKKU_TAG=v0.20.4 bash bootstrap.sh
```

### Wrap up Dokku installation

If you're on an Ubuntu installation,
you'll want to navigate to your Linux box's IP address,
and finish up the installation instructions,
which involves letting your Dokku installation
know about your SSH public keys.
These keys are important,
as the are literally the _keys_
to letting you push your app to your Dokku box!

??? info "SSH Keys and Dokku"

    More pedantically, these SSH keys identify your machine
    as being "authorized" to push to the `git` server
    that is running on your Dokku machine.
    This is what allows you to `git push dokku master` later on!

For those of you who have CentOS or other flavours of Linux,
you will need to follow analogous instructions on the Dokku website.
I have had experience following the [CentOS instructions][centos] at work,
and had to modify the installation commands a little bit
to work with our internal proxies.

[centos]: http://dokku.viewdocs.io/dokku/getting-started/install/rpm/

### Test that Dokku is working

To test that your Dokku installation is working, type the following command:

```bash
dokku help
```

That should show the Dokku help menu,
and you'll know the installation has completed successfully!

### Optionally set proxies for Docker

Now, because Dokku builds upon Docker,
if you're behind a corporate proxy,
you might need to configure your Docker daemon proxies as well.
You'll then want to follow instructions
on the [Docker daemon documentation][docker_daemon].

[docker_daemon]: https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

Those steps will generally be the same as what's in the docs,
though the specifics will change (e.g. your proxy server address).


## Configure domain names

The allure of Heroku is that it gives your app a name:
`myapp.herokuapp.com`, or `myshinyapp.herokuapp.com` quite automagically.
With Dokku and a bit of extra legwork, we can replicate this facility.

We're going to set up your Dokku box
uch that its main domain will be `mydomain.com`,
and apps will get a subdomain `myapp.mydomain.com`.

### Register a domain name

Firstly, you'll need a domain name from a Domain Name Service (DNS) registrar.
Cloudflare seems to be doing all of the right things at the moment,
so [their domain name registration service][cloudflare]
is something I'm not hesitant to recommend (at least as of 2020).
For historical reasons, I'm currently using Google Domains.
At work, we have an internal service
that lets us register an internal domain name.
What matters most is that you have the ability
to assign a domain name that points to your Dokku machine's IP address.

[cloudflare]: https://www.cloudflare.com/products/registrar/

Go ahead and register a domain name that reflects who "you" are on the web.
For myself, I have a personal domain name that I use.
At work, I registered a name that reflects the research group that I work in.
Make sure that the name "points"/"forwards" to the IP address of your Dokku box.

### Enable subdomains!

To enable the ability to use subdomains like `myapp.mydomain.com` for each app,
you'll want to also configure the DNS settings.
On your domain registrar, look for the place
where you can customize "resource records".
On Google Domains, it's under "DNS \> Custom resource records".

There, you'll want to add an "A" record
(as opposed to other options that you might see,
like "CNAME", "AAAA", and others).
The "name" should be `*`, literally just an asterisk.
The IPv4 address should point to your Dokku machine.
This is all that is needed.

??? question "What is an 'A' record?"

    The most comprehensive explainer I've seen is
    at [dnsimple](https://support.dnsimple.com/articles/a-record/),
    but the long story short is that it is an "Address" record.
    Yes, "A" stands for "Address",
    and it is nothing more than a pointer that maps
    "string" address to IP address.


??? question "What then about the name `*`?"

    What we just did up there was to say,
    point everything `*.mydomain.com`
    to to the Dokku box IP address.
    How then do we get subdomains
    if we don't configure them with our DNS?
    Well, the secret here is that Dokku can help us with subdomains.
    Read on for how configuration of your Dokku box!

To test whether your domain name is setup correctly,
head over to the domain in your favourite browser.
At this point, you should see the default NGINX landing page,
as you have no apps deployed and no domains configured.

??? question "How do you pronounce 'NGINX'?"

    The official way is "engine-X".
    The wrong way is "en-jinx".
    Don't get it wrong!

??? question "And what is NGINX?"

    From [Wikipedia](https://en.wikipedia.org/wiki/Nginx):

    Nginx is a web server which can also be used as a reverse proxy,
    load balancer, mail proxy and HTTP cache.

    For our purposes, we treat it as a thing
    that routes URLs to containers.

## Deploy a test app

Heroku provides a "Python getting started" repository
that we will use to check that the installation is working correctly.
This one deploys reliably with all of the vanilla commands entered.
Leveraging this, I will also show you how to leverage your `*` A record
to put in nice subdomains!

### Clone the test app

Firstly, `git clone` Heroku's [`python-getting-started`][pgs] repository
to your laptop/local machine (i.e. not your Dokku box).

[pgs]: https://github.com/heroku/python-getting-started

Next, `cd` into the repository:

```bash
cd python-getting-started
```

After that, add your Dokku box as a `git` remote to the repository:

```bash
git remote add dokku dokku@your-domain-name:python-getting-started
```

Be sure to replace `your-domain-name` with your newfangled domain that you registered.

??? info "App name"

    The `python-getting-started` after the colon
    is the "app name" that you will see at the command line
    when interacting with Dokku later.

Now, push the app to your Dokku box!

```bash
git push dokku master
```

Unlike your usual pushes to GitHub, GitLab or Bitbucket,
you'll see a series of remote outputs being beamed back to your terminal.
What's happening here is the build of the app!
In particular, a Docker build is happening behind-the-scenes,
so your app is completely self-contained and containerized on the Dokku box!

If everything went well, the last output beamed back to you should look like:

```bash
=====> Application deployed:
       http://mydomain.com:10161
```

Wonderful! Now let's go back to Dokku and configure your app.

### Configure the app domain and ports

We're now going to configure Dokku to recognize
which subdomains should point to which apps.

Firstly, get familiar with the Dokku domains command:

```bash
# On your Dokku box
dokku domains:help
```

That should list out all of the Dokku `domains` sub-commands.

```bash
Usage: dokku domains[:COMMAND]

Manage domains used by the proxy

Additional commands:
    domains:add <app> <domain> [<domain> ...]       Add domains to app
    domains:add-global <domain> [<domain> ...]      Add global domain names
    domains:clear <app>                             Clear all domains for app
    domains:clear-global                            Clear global domain names
    domains:disable <app>                           Disable VHOST support
    domains:enable <app>                            Enable VHOST support
    domains:remove <app> <domain> [<domain> ...]    Remove domains from app
    domains:remove-global <domain> [<domain> ...]   Remove global domain names
    domains:report [<app>|--global] [<flag>]        Displays a domains report for one or more apps
    domains:set <app> <domain> [<domain> ...]       Set domains for app
    domains:set-global <domain> [<domain> ...]      Set global domain names
```

You can report domains used for the app, `python-getting-started`:

```bash
# On your Dokku box
dokku domains:report python-getting-started
```

The output should look something like this:

```bash
$ dokku domains:report python-getting-started
=====> python-getting-started domains information
       Domains app enabled:           false
       Domains app vhosts:
       Domains global enabled:        false
       Domains global vhosts:
```

This tells us that `python-getting-started`
has no domains configured for it.
We can now set it:

```bash
# On your Dokku box
dokku domains:set python-getting-started python-getting-started.mydomain.com
```

The output will look like this:

```bash
-----> Added python-getting-started.mydomain.com to python-getting-started
-----> Configuring python-getting-started.mydomain.com...(using built-in template)
-----> Creating http nginx.conf
       Reloading nginx
```

Now, you should be able to go to `http://python-getting-started.mydomain.com`,
and the page that gets loaded should be
the "Getting Started with Python on Heroku" landing page!

??? question "So, what magic happened here?"

    What's happening here is that NGINX resolving
    subdomains to particular containers,
    and mapping them to the appropriate container port
    that is being exposed.

If everything deployed correctly up till this point,
you're good to go with deploying a data app on your Dokku machine!

## Deploy your data app

Deploying the `python-getting-started` app should have given you:

1. the confidence that your Dokku installation is working correctly,
2. firsthand experience configuring Dokku,
3. a taste of the workflow for deploying an app.

Now, we're going to apply that to a Streamlit app.
I've chosen Streamlit because it's got the easiest programming model
amongst all of the Dashboard/app development frameworks that I've seen;
in fact, I was able to stand up an [explainer on the Beta distribution][beta]
in under 3 hours,
the bulk of which was spent on writing prose,
not figuring out how to program with Streamlit.

[beta]: https://minimal-streamlit.herokuapp.com/

### Build a streamlit app (skip if you already have an app)

If you don't have a Streamlit app,
here's one that you can use as a starter,
which simply displays some text and a button:

```python
# app.py

import streamlit as st

"""
# First Streamlit App!

This is a dummy streamlit app.
"""

finished = st.button("Click me!")
if finished:
    st.balloons()
```

Save it as `app.py` in your project directory.

Now, you can run the app with Streamlit:

```bash
# On your local machine
streamlit run app.py
```

You should see the following show up in your terminal:

```bash
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://<your_ip_address>:8501
```

You can go to the local URL and confirm that the app is running correctly,
and that it does exactly what's expected.

### Add project-specific configuration files for Dokku

Now, we need to add a few configuration files that Dokku will recognize.

#### `requirements.txt`

Firstly, make sure you have a `requirements.txt` file in the project root directory,
in which you specify all of the requirements for your app to run.

```text
# requirements.txt
streamlit==0.57.3  # pinning version numbers is good for apps.
# put more below as necessary, e.g.:
numpy==0.16
```

With a `requirements.txt` file,
Dokku (and Heroku) will automagically recognize that you have a Python app.
Dokku will then create a Docker container equipped with Python,
and install all of the dependencies in there.
Declarative configuration FTW!

#### `Procfile`

Next, you need a Procfile in the project root directory:

```text
# Procfile
web: streamlit run app.py
```

??? note "Procfile"

    A quick note: It is `Procfile`, with no file extensions.
    Don't save it as `Procfile.txt`,
    because that will not get recognized by Dokku/Heroku.
    To learn more, read about it on
    [Heroku](https://devcenter.heroku.com/articles/procfile).


The _general_ syntax in the Procfile is:

```text
<process_type>: <command>
```

The `command` is always a single line,
and tells Dokku/Heroku what commands to execute in order to run the app.
In our case, we simply execute the same command
that we used to run the app locally for development purposes.

??? note "More complex Procfile commands"

    You can have multiple bash commands in a single line,
    though if it gets complicated,
    you may want to extract the commands out
    into a separate bash script that you execute instead, e.g.:

    ```
    # dokku.sh
    pip install -e .
    export CONFIG_DIR="/path/to/config/files"
    streamlit run app.py
    ```

For the `process_type`, in the case of Dokku, is always "web".
Heroku, on the other hand, can handle other process types.
Since we're dealing with Dokku and not Heroku,
don't bother changing `process_type`.

### Configure `git` Remote with Dokku

Now, let's configure your Dokku remote.

```bash
# On your local machine
git remote add dokku dokku@mydomain.com:streamlit-app
```

Remember two points!

1. Firstly, change `mydomain.com` to your domain.
1. Secondly, you can use _any_ app name you want, it doesn't have to be `streamlit-app`.

A convention that has helped me is to have a 1:1 mapping
between app and project repository folder name.
It means one less thing to be confused about.

Once you're done configuring the remote, now push it up!

```bash
# On your local machine
git push dokku master
```

The same build commands will take place.
While they are taking place, go ahead and open a new Terminal,
and SSH into the Dokku box.
We're going to configure the new app on Dokku!

### Configure Dokku Subdomain

Let's start with the subdomain name first.
For this tutorial, I'm going to use the domain name `streamlit-app.mydomain.com`.
Let's configure the app `streamlit-app` with that domain name:

```bash
# On Dokku box
dokku domains:set streamlit-app streamlit-app.mydomain.com
```

### Configure Dokku port mapping

Next, we have to configure the port mapping that Dokku's proxy server will recognize.
By default, every container has the "hosting box" (i.e. the machine Dokku is running on)
port 80 mapped to "container box" (i.e. the container the _app_ is running on) port 5000.
You can see this with:

```bash
# On Dokku box
dokku proxy:report streamlit-app
```

That will give you something like:

```bash
=====> python-getting-started proxy information
       Proxy enabled:                 true
       Proxy port map:                http:80:5000
       Proxy type:                    nginx
```

Now, because `streamlit` is going to be run on port 8501 (in the container) by default,
we need to change the port mapping from `http:80:5000` to `http:80:8501`.
To do so:

```bash
# On Dokku box
dokku proxy:ports-set streamlit-app http:80:8501
```

Putting these two configurations together,
i.e. setting the subdomain and port mapping,
we have now told Dokku, "Each time you get a request from `http://streamlit-app.mydomain.com`,
forward it to port 8501 on the `streamlit-app` container."

### Test it out!

Well, we now can test it out.
Go ahead and head over to your app URL,
and see if the app works for you!

### Debugging

If things look like they're crashing, how do you debug?
Well, you always should know how to look at the logs:

```bash
dokku logs my_app_name -t
```

That will keep the logs updating in the terminal as you refresh the page.
Use the information in the logs to help you debug.
Also, see if you can reproduce the error in the logs locally.

Additionally, if you get `nginx` errors,
you can look at the `nginx` logs to help you debug
proxy errors as they show up:

```bash
dokku nginx:access-logs my_app_name -t
```

Look at the logs and dig through for anything
that might help you with your Google searches.
Follow this pattern, and soon enough,
you'll become an expert at debugging your web apps!

## Deploy a static site

Now that you've seen how to deploy an app
that's powered by a container behind-the-scenes,
let's now figure out how to deploy a static site
that is built upon every deploy.
It's essentially the same.
We have configuration files (in this case, slightly different ones)
that declare what kind of environment we need.
We basically treat the static site generator
as an "app" that generates the HTML pages
that we serve up freshly on each build.

For this example, I'm going to use [`mkdocs`][mkdocs],
as it is also easy to use to build sites,
and can be extended with some pretty awesome templates
(like [`mkdocs-material`][material])
for responsive docs generated from Markdown files.
If you've got another static site builder
(I have used [Lektor][lektor], [sphinx][sphinx], and [Nikola][nikola] before),
the places where we use `mkdocs` commands
can be easily replaced by the relevant ones for your situation.

[mkdocs]: https://www.mkdocs.org/
[material]: https://squidfunk.github.io/mkdocs-material/
[lektor]: https://www.getlektor.com/
[sphinx]: https://www.sphinx-doc.org/en/master/
[nikola]: https://getnikola.com/

### Build a static site (skip if you already have one)

If you don't already have a static site,
then feel free to use the following example.

In your project root directory,
create a `docs/` directory,
and then place a dummy `index.md` in there:

```md
<!-- index.md -->
# Index Page

Hello world!
```

Now, in the project root directory,
create a `mkdocs.yml` file,
in which you configure `mkdocs` to build the static site:

```yaml
# mkdocs.yml
site_name: Marshmallow Generator
```

This is a minimal `mkdocs` configuration.

Now, make sure you have mkdocs installed
in the Python environment that you're using.
It's available on PyPI:

```bash
# On your local machine
pip install -U mkdocs
```

Once installation has finished,
you can now command `mkdocs` to build the static site to view locally:

```bash
# On your local machine
mkdocs serve
```

If you can successfully view the static site on your local machine,
i.e. you see the contents of `index.md`
show up as a beautifully rendered HTML page,
you're good to move on!

### Add project-specific configuration files for Dokku

We're now going to add the necessary configuration files to work with Dokku.

Firstly, we have to add in a `.static` file in the project root directory.
This file tells Dokku that the site that is going to be built is a static site.
To do so in the terminal, you only have to `touch` the file at the command line:

```bash
# On your local machine
touch .static
```

Secondly, we have to add a `.buildpacks` file,
where we specify that we are using two "buildpacks":
one to provide the environment to run the commands that build the site,
and another to build the site and serve up the static site files.
In the case of our dummy `mkdocs` static sites, we need in `.buildpacks`:

```text
https://github.com/heroku/heroku-buildpack-python.git
https://github.com/dokku/buildpack-nginx.git
```

They have to go in that order, so that the first one is used for building, and the second one is used for serving the site.

??? question "What are 'buildpacks?"

    Once again, Heroku's docs have [the most comprehensive explanation](https://devcenter.heroku.com/articles/buildpacks),
    as they're the originators of the idea.
    The short answer is that they are pre-built and configured "base" environments
    that you can build off.
    It's like having an opinionated Dockerfile that you can extend,
    except we extend it using declared configuration files in the repository instead.


Thirdly, instead of a `Procfile`,
we add an `app.json` file that contains the command
for building the static site.

```json
{
  "scripts": {
    "dokku": {
      "predeploy": "cd /app/www && mkdocs build"
    }
  }
}
```

??? question "Deployment tasks"

    If you want to read more about this file,
    as well as the custom "deployment tasks" bit of Dokku,
    then check out the [docs pages here][deployment].)

    [deployment]: http://dokku.viewdocs.io/dokku/advanced-usage/deployment-tasks/

OK, we just created a bunch of files,
but I haven't explained how they're interacting with Dokku.
There's definitely some opinionated things that we'll have to unpack.

Firstly, the Dokku `buildpack-nginx` buildpack
makes the opinionated assumption that your repository
will be copied over into the Docker container's `/app/www` directory.
That is why we have the `cd /app/www` command.
Then, we follow it up with a `mkdocs build`,
which you can change depending on what static site generator you're using.

Secondly, the `predeploy` key declares to Dokku
to execute the commands in the value (i.e. `cd /app/www && mkdocs build`)
before starting up the `nginx` server that points to the static site files.

As you probably can grok by now, basically,
the static sites are being built upon every deploy.
This saves you from having to build the site locally and then pushing it up,
which is both in-line with how `git` is supposed to be used
(you only `git push` files that are generated by hand),
and is in-line with the continuous deployment philosophy.

Finally, we still need our `requirements.txt` file
to be populated with whatever is needed to build the docs locally:

```text
# requirements.txt
mkdocs==1.1
# put other dependencies below!
```

Now that we're done, let's configure our remotes once again.

### Configure `git` Remote with Dokku

As with the Streamlit app, go ahead and configure the `git` remote with Dokku:

```bash
# On your local machine
git remote add dokku dokku@mydomain.com:my-static-site
```

Now, push up to Dokku!

```bash
# On your local machine
git push dokku master
```

### Configure Dokku

As with the Streamlit app, let's now configure the domains:

```bash
# On your Dokku box
dokku domains:set my-static-site my-static-site.mydomain.com
```

Unlike the app, we don't have to configure ports,
because they will be mapped correctly by default.

Finally, we need to configure `nginx`
to point to the directory in which the `index.html` page is generated.
In the case of `mkdocs`,
the directory is in the `site/` directory in the project root directory.
We'll now configure it:

```bash
# On your Dokku box
dokku config:set my-static-site NGINX_ROOT='site'
```

???+ warning

    You'll want to change `site`
    to whatever the output directory is
    for the static site generator you use!

Alrighty, go ahead and visit your static site to confirm that it's running!

### Debugging

As with the Streamlit app above,
debugging is done in exactly the same way,
using the two commands:

```bash
# Inspect application logs
dokku logs my_app_name -t
# Inspect nginx logs
dokku nginx:access-logs my_app_name -t
```

## The Framework

I have a habit of categorizing things into a "framework"
to help me anchor how I debug things,
and I hope to share my framework for domains, apps, and Dokku with you.

Firstly, we organized our Dokku box + domain name
such that the Dokku box was referenced by the domain name,
while individual apps got subdomains.
We got subdomains for free by configuring a `*`
on the DNS provider's A records,
which forwarded all sub-domains to the Dokku box.

Secondly, we configured each app on the Dokku box
to resolve which subdomain points to it.
In this way, subdomains need not be set on our DNS provider.

Thirdly, we configured both static sites and dynamic data apps,
using a collection of configuration files.
For our data apps, it was primarily a `Procfile` and `requirements.txt`.
For our static sites, it was a `.buildpacks` file,
`app.json` file, and `requirements.txt`.
Each have their purpose, but together they tell Dokku
how to configure the environment in which apps are built.

## Cheatsheet of Commands

Here's a cheatsheet of commands we used in this essay,
to help you with getting set up.

### Domain Name Registration

- Register your domain.
- Add a custom resource record `*` pointing to your Dokku box's IP address

### Streamlit Commands

```bash
# Run streamlit app
streamlit run app.py
```

### Git commands

```bash
# Add dokku remote
git remote add dokku dokku@mydomain.com:streamlit-app

# Push master branch to Dokku box
git push dokku master
```

### Interacting with proxies

```bash
# View port forwarding for app
dokku proxy:report streamlit-app

# Set port forarding for app
dokku proxy:ports-set streamlit-app http:80:8501
```

The syntax for the ports is:

```bash
<protocol>:<host port>:<container port>
```

For port forwarding,
if you follow the general framework we're using here,
you should only have to configure the container port.

### Interacting with domains

```bash
# View domains for an app
dokku domains:report streamlit-app

# Set domains for an app
dokku domains:set streamlit-app streamlit-app.mydomain.com
```

Again, if you follow the framework we have used here,
then you should only need to configure `<app-url>.mydomain.com`

### Config Files

`Procfile` for apps

```text
web: streamlit run app.py
```

`mkdocs.yml` for MkDocs config

```yaml
# mkdocs.yml
site_name: Marshmallow Generator
```

Create `.static` for static sites:

```bash
touch .static
```

`.buildpacks` for static sites and multi-buildpack apps

```text
https://github.com/heroku/heroku-buildpack-python.git
https://github.com/dokku/buildpack-nginx.git
```

`app.json` for static sites:

```json
{
  "scripts": {
    "dokku": {
      "predeploy": "cd /app/www && mkdocs build"
    }
  }
}
```

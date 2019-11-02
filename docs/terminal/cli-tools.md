# Tools and Upgrades for your CLI

In this short essay,
I would like to introduce you
to a list of awesome command-line tools
that I have found on the internet.

Most of the tools listed here do one thing really well:
they add visual clarity to the text that we are looking at.
This is mostly done by colorizing the terminal
with syntax highlighting.

Without further ado, let's get started listing them.

## `exa`

[`exa`](https://the.exa.website/) is a favourite of mine,
because it is an almost drop-in replacement for `ls`,
except with saner defaults.
It also comes with a saner set of defaults for the `tree` command.

After installing, you can replace `ls` and `tree` with `exa` by aliasing:

```bash
alias ls='exa --long --git -a --header --group'
alias tree='exa --tree --level=2 --long -a --header --git'
```

## `tmux`

[`tmux`](https://github.com/tmux/tmux) is another daily driver of mine.
I use it to keep remote terminal sessions persistent,
and use it effectively as a workspace manager between projects.

## `nanorc`

If you're like me, and are accustomed to the `nano` text editor
rather than `vim` or `emacs`,
then [`nanorc`](https://github.com/scopatz/nanorc),
a set of syntax highlighting configurations
provided by [Anthony Scopatz](https://twitter.com/scopatz)
is an awesome addition to your `nano` toolkit.

(For what it's worth, I wrote this short essay in `nano`,
and `nanorc` played no small role in making the text readable!)

## `diff-so-fancy`

[`diff-so-fancy`](https://github.com/so-fancy/diff-so-fancy)
is a drop-in replacement for `diff`,
and makes it so much easier read diffs between two files.

After installation, you can easily replace `diff` with `diff-so-fancy` through aliasing:

```bash
alias diff="diff-so-fancy"
```

## `bat`

[`bat`](https://github.com/sharkdp/bat) is another one of those instant favourites.
I use `cat` and `less` often to look through files, but `bat` takes things to another level.
It is basically a mash-up between `cat` and `less`,
allowing you to scroll through your files in a `less`-like scrolling fashion,
while also providing syntax highlighting for the files you open.

At the same time, it'll let you concatenate two files together (just like `cat`)
and display them to the screen.

After installing, you can replace `cat` with `bat` by aliasing as well:

```bash
alias cat="bat"
```

## `fd`

[`fd`](https://github.com/sharkdp/fd)
is another tool that provides saner syntax than the default `find`.

After installing, you can replace `find` with `fd` by aliasing:

```bash
alias find="fd"
```

## `ripgrep`

[`ripgrep`](https://github.com/BurntSushi/ripgrep)
is a tool that will let you search directories recursively for a particular pattern.
This can help you quickly find text inside a file inside the file tree easily.

## References

[Vim From Scratch](https://www.vimfromscratch.com/articles/awesome-command-line-tools/)
introduced many of the tools shown here,
and I want to make sure that the author gets credit
for finding and sharing these awesome tools!

[James Weis](https://www.linkedin.com/in/jameswweis/) introduced me to `tmux`
while in grad school, and I've been hooked ever since.

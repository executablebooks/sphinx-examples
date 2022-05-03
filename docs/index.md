# `sphinx-examples`

A small sphinx extension to add "example snippets" that allow you to show off source markdown and the result of rendering it in Sphinx.

For example:

````{example} Showing off a card and note directive

```{card}
:class-header: bg-light
A note!
^^^
:::{note}
Here's a sample note!
:::
```

````

:::{warning}
This currently only works with MyST Markdown content, it will not work if you've written your documentation in reStructuredText.
:::


## Install

Install with pip:

```console
$ pip install sphinx-examples
```

## Use

The `{example}` directive allows you to show off some source markdown, and the result of rendering it.
It is meant to help you demonstrate functionality of a theme, extension, syntax, etc.
For example:

````{example} Using the example directive
```{example} Example title
Here's my **example**!
```
````

### Reverse source and result

You can reverse the order of `source` and `result` by using the `:reverse:` flag, like so:

````{example}
```{example} Reversed source and result
:reverse:
Here's my **example**!
```
````

You can also remove the parent container of the source/result blocks in case you wish to demonstrate something that would not work properly inside a container:

### Remove the container with simple mode

You can remove the Sphinx Design container entirely, which simply places the source / result next to one another.
This is useful if the container would prevent you from demonstrating some functionality:

````{example} No container so we can show off a margin
:no-container:

```{example}
:no-container:

:::{margin}
Here's my **margin content**!
:::

```
````

### Add your own class

You can add your own classes to examples as well.
For example:

````{example}
:no-container:

```{example} A full-width example
:class: full-width
:no-container:

:::{note}
A full-width note!
:::

```
````

```{toctree}
changelog
```

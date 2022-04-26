# `sphinx-demo`

A small sphinx extension to add "demo buttons" that allow you to show off source markdown and the result of rendering it in Sphinx.

For example:

```{example} Showing off a note directive

:::{note}
Here's a sample note!
:::
```


## Install

Install with pip:

```console
$ pip install sphinx-demo
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

You can reverse the order of `source` and `result` by using the `:reverse:` flag, like so:

````{example}
```{example} Reversed source and result
:reverse:
Here's my **example**!
```
````

You can also remove the parent container of the source/result blocks in case you wish to demonstrate something that would not work properly inside a container:


You can reverse the order of `source` and `result` by using the `:reverse:` flag, like so:

````{example}
:no-container:

```{example} No container so we can show off a margin
:no-container:
:reverse:

:::{margin}
Here's my **margin content**!
:::

```
````

You can add your own classes to examples as well.
For example:

````{example}
:no-container:

```{example} A full-width example
:class: full-width

:::{note}
A full-width note!
:::

```
````

```{toctree}
changelog
```

# Reference examples

The following examples show off the look and feel of this extension.
They also serve as an informal test-suite - none of them should result in problematic output or warnings.

As we discover edge-cases and bugs, add new examples below to confirm they work once fixed.

## `{card}` directive

````{example} Card directive with a header should be properly parsed.

```{card}
:class-header: bg-light
A note!
^^^
:::{note}
Here's a sample note!
:::
```

````

## Colon fence

````{example} Example with colon fence should not result in kwarg error

:::{note}
A note!
:::

````

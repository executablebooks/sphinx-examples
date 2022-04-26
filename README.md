# sphinx-demo

A small Sphinx extension to create examples of source markup and the result of rendering it in your documentation.
This is useful if you wish to demonstrate the functionality of a new directive or role in Sphinx.

## Installation

You can install `sphinx-demo` with `pip`:

```bash
pip install sphinx-demo
```

## Usage

See [the `sphinx-demo` documentation](https://sphinx-demo.readthedocs.io) for more information.

## Develop

To develop this extension, follow these steps:

1. **Clone the repository locally**

   ```console
   $ git clone https://github.com/executablebooks/sphinx-demo
   $ cd sphinx-demo
   ```
2. **Install pre-commit hooks**

   ```console
   $ pre-commit install
   ```
3. **Install development and documentation dependencies**

   ```console
   $ pip install -e .[sphinx]
   ```

The codebase for this package is in `src/sphinx_demo`.
Documentation is in `docs/`.

This package has no testing infrastructure, so be careful when using it!
If it becomes more complex or with more features, we may add more testing around it in the future.
For not it is packaged for convenience and re-use across EBP repositories.

"""A lightweight example directive to make it easy to demonstrate code / results."""
import os
from typing import List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

__version__ = "0.0.1"


TEMPLATE_GRID = """
::::::::::::::::::::::::{{grid}}
:gutter: 0
:margin: 0
:padding: 0
:class-container: sd-example

{content}

::::::::::::::::::::::::
"""

TEMPLATE_TITLE = """
:::::::::::::::::::::::{{grid-item}}
:columns: 12
:class: sd-example-title

{content}

:::::::::::::::::::::::
"""

TEMPLATE_SOURCE = """

:::::::::::::::::::::::{{grid-item-card}}
:columns: 12
:shadow: none
:class-header: bg-light py-1 fs-1
:class-card: sd-example-source

Source
^^^

``````````````````````````````markdown
{content}
``````````````````````````````

:::::::::::::::::::::::
"""

TEMPLATE_RESULT = """

:::::::::::::::::::::::{{grid-item-card}}
:columns: 12
:shadow: none
:class-header: bg-light py-1
:class-card: sd-example-result


Result
^^^

{content}


:::::::::::::::::::::::
"""


TEMPLATE_SIMPLE = """
**Source**

````````````````````````````markdown
{content}
````````````````````````````

**Result**

{content}
"""

TEMPLATE_SIMPLE_REVERSED = """
**Result**

{content}

**Source**

````````````````````````````markdown
{content}
````````````````````````````
"""


def st_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)


class ExampleDirective(SphinxDirective):
    """A directive to show source / result content blocks."""

    name = "example"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "class": directives.class_option,
        "reverse": directives.flag,
        "no-container": directives.flag,
    }

    def run(self) -> List[nodes.Node]:
        content_text = "\n".join(self.content)

        grid_items = []

        # Update our content and place it in a container
        container = nodes.container(classes=["sd-demo__container"])

        # Parse the template with Sphinx Design to create an output
        container = nodes.container()

        # Remove the container styling if requested
        if "no-container" in self.options:
            if "reverse" in self.options:
                simple_text = TEMPLATE_SIMPLE_REVERSED.format(content=content_text)
            else:
                simple_text = TEMPLATE_SIMPLE.format(content=content_text)
            self.state.nested_parse([simple_text], 0, container)
        else:
            # If we have a title, add it above the source code
            if self.arguments:
                grid_items.append(TEMPLATE_TITLE.format(content=self.arguments[0]))

            content_templates = [TEMPLATE_SOURCE, TEMPLATE_RESULT]
            if "reverse" in self.options:
                content_templates = content_templates[::-1]

            for template in content_templates:
                grid_items.append(template.format(content=content_text))

            # Use Sphinx Design to parse content
            grid_text = TEMPLATE_GRID.format(content="\n".join(grid_items))
            self.state.nested_parse([grid_text], 0, container)
            # Sphinx Design outputs a container too, so just use that
            container = container.children[0]

        # Add extra classes
        if self.options.get("class", []):
            container.attributes["classes"] += self.options.get("class", [])
        return [container]


# We connect this function to the step after the builder is initialized
def setup(app):
    # Activate Sphinx design
    app.setup_extension("sphinx_design")

    # Add our static path
    app.connect("builder-inited", st_static_path)
    app.add_css_file("styles/sphinx-demo.css")

    # Add directives
    app.add_directive("example", ExampleDirective)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

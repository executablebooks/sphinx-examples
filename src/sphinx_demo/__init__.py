"""A lightweight example directive to make it easy to demonstrate code / results."""
import os
from typing import List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

__version__ = "0.0.1"


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

        # Update our content and place it in a container
        extra_classes = self.options.get("class", [])
        output = nodes.container(classes=["sd-demo"] + extra_classes)
        container = nodes.container(classes=["sd-demo__container"])

        # If we have a title, add it above the source code
        if self.arguments:
            title_container = nodes.container(classes=["sd-demo__title"])
            title_container.append(nodes.paragraph(text=self.arguments[0]))
            output.append(title_container)

        # Create the literal container, add a literal version of the content to it
        literal_container = nodes.container(classes=["sd-demo__source"])
        literal_container.append(nodes.paragraph(text="Source"))
        literal_container.append(nodes.literal_block(text=content_text))
        container.append(literal_container)

        # Now render the content inside of a specific container
        rendered_container = nodes.container(classes=["sd-demo__result"])
        rendered_container.append(nodes.paragraph(text="Result"))
        self.state.nested_parse(self.content, 0, rendered_container)
        container.append(rendered_container)

        # Result should come first
        if "reverse" in self.options:
            container.children = container.children[::-1]

        # Remove the container styling if requested
        if "no-container" in self.options:
            container.attributes["classes"].append("sd-nostyle")

        output.append(container)
        return [output]


# We connect this function to the step after the builder is initialized
def setup(app):
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

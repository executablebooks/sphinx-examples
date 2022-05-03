# -- Project information -----------------------------------------------------

project = "Sphinx Examples"
copyright = "2022, Executable Books"
author = "Executable Books Community"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------
extensions = ["myst_parser", "sphinx_copybutton", "sphinx_examples"]
templates_path = []
master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
# html_theme = "sphinx_rtd_theme"
# html_theme = "furo"

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/sphinx-examples",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
}

myst_enable_extensions = ["colon_fence"]

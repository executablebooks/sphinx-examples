# -- Project information -----------------------------------------------------

project = "Sphinx Demo"
copyright = "2022, Executable Books"
author = "Executable Books Community"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------
extensions = ["myst_parser", "sphinx_demo"]
templates_path = ["_templates"]
master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/sphinx-demo",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
}

myst_enable_extensions = ["colon_fence"]


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "SphinxCollapseAdmonitionsdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "SphinxCollapseAdmonitions.tex",
        "Sphinx Collapse Admonitions Documentation",
        "Chris Holdgraf",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "SphinxCollapseAdmonitions",
        "Sphinx Collapse Admonitions Documentation",
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "SphinxCollapseAdmonitions",
        "Sphinx Collapse Admonitions Documentation",
        author,
        "SphinxCollapseAdmonitions",
        "One line description of project.",
        "Miscellaneous",
    )
]

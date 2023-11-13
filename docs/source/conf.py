# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_nefertiti


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme_path = [sphinx_nefertiti.get_html_theme_path()]
else:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../"))


# -- Project information -----------------------------------------------------

project = 'scorecardpipeline'
copyright = '2023, itlubber'
author = 'itlubber'

# The full version, including alpha/beta/rc tags
release = '0.1.26'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
]

myst_enable_extensions = [
    'amsmath',
    'attrs_block',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'tasklist',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "sphinx_rtd_theme"

html_theme = 'sphinx_nefertiti'
pygments_style = "pastie"
pygments_dark_style = "dracula"

html_theme_options = {
    "style": "indigo",
    "footer_links": ",".join([
        "itlubber|https://itlubber.art",
        "github|https://github.com/itlubber/scorecardpipeline",
        "examples|https://github.com/itlubber/scorecardpipeline/blob/main/examples/scorecard_samples.ipynb",
    ]),
    "show_powered_by": False,
    "project_name_font": "Nunito",
    "doc_headers_font": "Nunito",
    "documentation_font": "Nunito",
    "versions": [
        ("latest", "https://scorecardpipeline.readthedocs.io/zh/latest/"),
        ("v0.1.26", "https://scorecardpipeline.readthedocs.io/zh/v0.1.26/"),
    ],
    "repository_url": "https://github.com/itlubber/scorecardpipeline",
    "repository_name": "itlubber/scorecardpipeline",
    "current_version": f"v{release}",
    "show_colorset_choices": False,
}

htmlhelp_basename = "scorecardpipeline"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# 显示类的 __init__ 相关文档
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

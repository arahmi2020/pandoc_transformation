# Configuration file for the Sphinx documentation builder.

import os
import sys
from sphinx_needs import __version__
print ('sphinx-needs version: ' + str(__version__))
from sphinx_needs.api import add_dynamic_function

# -- Project information

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

project = 'Pandoc transformation for X-As-Code'
copyright = f'2024 - {date.year}, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.1.1'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx_needs',
    #'sphinx_immaterial',
]


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
#html_theme = 'sphinx_immaterial'

#html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'



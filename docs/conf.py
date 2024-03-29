# Configuration file for the Sphinx documentation builder.

# -- Project information
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

project = 'Masterchicken'
copyright = '2023, Masterchicken developers'
author = 'PythonChicken123'

release = '0.1'
version = '0.0.7'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'ext.headers',
    'ext.boilerplate',
    'ext.customversion',
    'ext.edit_on_github'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
pygments_style = 'sphinx'
modindex_common_prefix = ['masterchicken']
templates_path = ['_templates']

# -- Options for HTML output

html_theme = "pyramid"

# -- Options for EPUB output
epub_show_urls = 'footnote'

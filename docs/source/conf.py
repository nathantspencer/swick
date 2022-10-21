# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'swick'
copyright = '2022, Nathan T. Spencer'
author = 'Nathan T. Spencer'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_logo = '_static/logo_cropped.png'
html_css_files = ['custom_colors.css',]
html_theme_options = {
	"favicons": [
		{
				"rel": "icon",
				"sizes": "16x16",
				"href": "favicon-16x16.png",
		},
		{
				"rel": "icon",
				"sizes": "32x32",
				"href": "favicon-32x32.png",
		},
		{
				"rel": "apple-touch-icon",
				"sizes": "152x152",
				"href": "apple-touch-icon.png",
				"color": "#000000",
		}
	]
}

# -- Extension configuration -------------------------------------------------
extensions = ['sphinx.ext.autodoc']

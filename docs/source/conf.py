# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
from pathlib import Path
from django import setup

# Add broker_web package to path
package_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(package_dir))

# Set up the broker_web django application so that we can import
# views and models without raising
# django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.`
os.environ['DJANGO_SETTINGS_MODULE'] = 'broker_web.main.settings'
os.environ['SECRET_KEY'] = 'FAKE_KEY_FOR_BUILDING_DOCS'
setup()

# -- Project information -----------------------------------------------------

project = 'Broker-Web'
copyright = '2020, PGB Team'
author = 'PGB Team'

# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_copybutton'
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

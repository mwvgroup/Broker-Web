# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views."""

from pathlib import Path
from warnings import warn

from django.urls import path
from django.views.generic import TemplateView

app_name = 'getting_started'


def create_static_template_routes(path_list, namespace=app_name):
    """Create urls routes for a collection of file paths

    Routes to ``my_template.html`` from ``<app_name>:my-template``.

    Args:
        path_list (list): The file path for each template
        namespace  (str): The name of the application namespace

    Return:
        A list of url routes
    """

    routes, names, url_patterns = [], [], []
    for file_path in path_list:
        route = Path(file_path).stem
        name = route.replace('_', '-')
        view = TemplateView.as_view(template_name=file_path)

        url = path(route, view, name=name)
        url_patterns.append(url)

        routes.append(route)
        names.append(name)

    if len(routes) != len(set(routes)):
        warn(f'Routes for {namespace} are not unique')

    if len(names) != len(set(names)):
        warn(f'Reverse lookup names for {namespace} are not unique')

    return url_patterns


template_paths = [
    'getting_started/introduction.html',
    'getting_started/data_products_overview.html',
    'getting_started/technical_resources.html',
    'getting_started/data_access.html',
    'getting_started/broker_design.html'
]

urlpatterns = create_static_template_routes(template_paths, 'getting_started')

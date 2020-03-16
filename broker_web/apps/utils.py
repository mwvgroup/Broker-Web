# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""General utilities used across apps

Auto Generating URL Routes
--------------------------

This ``create_static_template_routes`` function automatically creates URL
routes for collections of static web templates (i.e., templates that only
require a TemplateView as a view). For example, instead of:

.. code-block:: python
   :linenos:

   view_1 = TemplateView.as_view(template_name='template_1.html')
   view_2 = TemplateView.as_view(template_name='template_2.html')
   view_3 = TemplateView.as_view(template_name='template_3.html')
   # etc.

   urlpatterns = [
       path('template_1', view_1, name='view-1'),
       path('template_2', view_1, name='view-2'),
       path('template_3', view_1, name='view-3'),
       # etc.
   ]

you can write:

.. code-block:: python
   :linenos:

   from apps.static_templates import create_static_template_routes

   template_paths = (
       'template_1',
       'template_2',
       'template_3',
       # etc.
   )

   urlpatterns = create_static_template_routes(template_paths)

If you wish to namespace the generated urls, simply add a name for the app of
your namespace:

.. code-block:: python
   :linenos:

   urlpatterns = create_static_template_routes(template_paths, 'my_app_name')

Paginating JSON Responses
-------------------------

The ``paginate_to_json`` function handles the generation of JSON responses to
HTTP requests for pagination of data.

Todo: Add a usage example for paginate_to_json

"""

from pathlib import Path
from warnings import warn

from django.http import JsonResponse
from django.urls import path
from django.views.generic import TemplateView


def create_static_template_routes(template_paths, app_name=None):
    """Create urls routes for a collection of file paths

    Args:
        template_paths (list[str]): The file path for each template
        app_name             (str): The name of the application namespace

    Return:
        A list of url routes
        The app_name if provided
    """

    routes, names, url_patterns = [], [], []
    for file_path in template_paths:
        route = Path(file_path).stem
        name = route.replace('_', '-')
        view = TemplateView.as_view(template_name=file_path)

        url = path(route, view, name=name)
        url_patterns.append(url)

        routes.append(route)
        names.append(name)

    if len(routes) != len(set(routes)):
        warn(f'Routes for {app_name} are not unique')

    if len(names) != len(set(names)):
        warn(f'Reverse lookup names for {app_name} are not unique')

    if app_name is None:
        return url_patterns

    else:
        return url_patterns, app_name


def paginate_to_json(request, data):
    """Paginate a list of dicts and return as a ``JsonResponse``

    For expected in/outputs of paginated data, see
    https://datatables.net/manual/server-side .

    Args:
        request (HttpRequest): Incoming HTTP request
        data           (list): The data to paginate
    """

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    draw = request.GET.get('draw', -1)

    paginated_alerts = data[start:start + length]

    response = {
        'draw': draw,
        'data': paginated_alerts,
        'recordsTotal': len(data),
        'recordsFiltered': len(paginated_alerts),
    }

    return JsonResponse(response)

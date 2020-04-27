# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views.

+--------------------+----------------------------+---------------------------+
| URL                | View                       | name                      |
+====================+============================+===========================+
|``/``               | ``RecentObjectsView``      | ``recent-objects``        |
+--------------------+----------------------------+---------------------------+
|``/<int:pk>``       | ``ObjectSummaryView``      | ``object-summary``        |
+--------------------+----------------------------+---------------------------+
|``json/``           | ``ObjectsJson``            | ``objects-json``          |
+--------------------+----------------------------+---------------------------+
"""

from django.urls import path

from . import views

app_name = 'objects'

urlpatterns = [
    path('', views.RecentObjectsView.as_view(), name='recent-objects'),
    path('<int:pk>', views.ObjectSummaryView.as_view(), name='object-summary'),
    path('json/', views.ObjectsJson.as_view(), name='objects-json')
]

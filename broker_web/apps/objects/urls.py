# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views.

+--------------------+----------------------------+---------------------------+
| URL                | View                       | name                      |
+====================+============================+===========================+
|``/``               | ``RecentObjectsView``      | ``recent-objects``        |
+--------------------+----------------------------+---------------------------+
|``/<str:pk>``       | ``ObjectSummaryView``      | ``object-summary``        |
+--------------------+----------------------------+---------------------------+
|``json/``           | ``ObjectsJsonView``        | ``objects-json``          |
+--------------------+----------------------------+---------------------------+
"""

from django.urls import path

from . import views

app_name = 'objects'

urlpatterns = [
    path('', views.RecentObjectsView.as_view(), name='recent-objects'),
    path('<str:pk>', views.ObjectSummaryView.as_view(), name='object-summary'),
    path('json/', views.ObjectsJsonView.as_view(), name='objects-json')
]

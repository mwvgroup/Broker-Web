# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views.

+-------------------------+----------------------------+---------------------------+
| URL                     | View                       | name                      |
+=========================+============================+===========================+
|``/``                    | ``RecentObjectsView``      | ``recent-objects``        |
+-------------------------+----------------------------+---------------------------+
|``/<str:pk>``            | ``ObjectSummaryView``      | ``object-summary``        |
+-------------------------+----------------------------+---------------------------+
|``json/``                | ``ObjectsJsonView``        | ``objects-json``          |
+-------------------------+----------------------------+---------------------------+
|``/singlejson/<str:pk>`` | ``RecentAlertsJsonView``   | ``single-object-json``    |
+-------------------------+----------------------------+---------------------------+
|``salt2/<str:pk>``       | ``Salt2FitsJsonView``      | ``salt2-fit-json``        |
+-------------------------+----------------------------+---------------------------+
"""

from django.urls import path

from . import views

app_name = 'objects'

urlpatterns = [
    path('', views.RecentObjectsView.as_view(), name='recent-objects'),
    path('<str:pk>', views.ObjectSummaryView.as_view(), name='object-summary'),
    path('json/', views.ObjectsJsonView.as_view(), name='objects-json'),
    path('singlejson/<str:pk>', views.RecentAlertsJsonView.as_view(), name='single-object-json'),
    path('salt2/<str:pk>', views.Salt2FitsJsonView.as_view(), name='salt2-fit-json')
]

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path

from . import views

app_name = 'objects'

urlpatterns = [
    path('objects/', views.ObjectsView.as_view(), name='recent-objects'),
    path('objects/<int:pk>', views.ObjectSummaryView.as_view(), name='object-summary'),
    path('objects/json/', views.ObjectsJson.as_view(), name='objects-json')
]

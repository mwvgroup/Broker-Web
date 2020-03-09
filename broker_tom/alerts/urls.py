# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path

from .views import AlertsView, AlertSummaryView

urlpatterns = [
    path('', AlertsView.as_view(), name='alerts'),
    path('<int:pk>', AlertSummaryView.as_view(), name='alert-summary'),
]

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path

from . import views

app_name = 'alerts'

urlpatterns = [
    path('alerts/', views.AlertsView.as_view(), name='recent-alerts'),
    path('alerts/<int:pk>', views.AlertSummaryView.as_view(), name='alert-summary'),
    path('alerts/json/', views.AlertsJson.as_view(), name='alerts-json'),
]

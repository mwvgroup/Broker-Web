# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views."""

from django.urls import path

from . import views

app_name = 'alerts'

urlpatterns = [
    path('', views.RecentAlertsView.as_view(), name='recent-alerts'),
    path('<int:pk>', views.AlertSummaryView.as_view(), name='alert-summary'),
    path('json/', views.AlertsJson.as_view(), name='alerts-json'),
]

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views."""

from django.urls import path

from .views import ProfileView, SubscriptionsView

app_name = 'subscriptions'

urlpatterns = [
    path('', SubscriptionsView.as_view(), name='subscriptions'),
    path('profile', ProfileView.as_view(), name='profile'),
]

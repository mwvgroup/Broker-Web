# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path

from .views import SubscriptionsView

app_name = 'subscriptions'

urlpatterns = [
    path('', SubscriptionsView.as_view(), name='subscriptions'),
]

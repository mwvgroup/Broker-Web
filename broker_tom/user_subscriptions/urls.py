# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path

from .views import ProfileView, SubscriptionsView

urlpatterns = [
    path('', ProfileView.as_view(), name='user'),
    path('subscriptions', SubscriptionsView.as_view(), name='edit-subscriptions')
]

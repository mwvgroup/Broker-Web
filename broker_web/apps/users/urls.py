# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path

from .views import ProfileView, SubscriptionsView, UserCreateView

app_name = 'users'

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('subscriptions', SubscriptionsView.as_view(), name='subscriptions'),
    path('signup', UserCreateView.as_view(), name='signup'),
]

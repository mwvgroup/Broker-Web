# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``urls`` module configures routes from URLs to views."""

from django.urls import path, re_path

from .views import ActivateAccount, SignUp, activation_sent_view

app_name = 'signup'

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('activation_sent', activation_sent_view, name='activation-sent'),
    re_path(r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            ActivateAccount.as_view(), name='activate'),
]

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import ActivateAccount, ProfileView, SignUp

app_name = 'users'

invalid_link_view = TemplateView.as_view(template_name='users/activation_link_sent.html')

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('signup', SignUp.as_view(), name='signup'),
    path('invalid_act_link', invalid_link_view, name='activation-sent'),
    re_path(r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', ActivateAccount.as_view(), name='activate'),
]

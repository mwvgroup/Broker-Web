# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class SubscriptionsView(PermissionRequiredMixin, View):
    """View that handles new subscriptions for users"""

    permission_required = 'user.is_authenticated'

    def get(self, request, *args, **kwargs):
        return render(request, 'subscriptions/subscriptions.html')

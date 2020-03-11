# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class ProfileView(PermissionRequiredMixin, View):
    """View for displaying a table of all recent alerts matching a query"""

    permission_required = 'user.is_authenticated'

    def get(self, request, *args, **kwargs):
        # Todo get pubsub messages
        timestamps = [123, 456]
        messages = ['a', 'b']
        context = {
            'pbsub_zip': zip(timestamps, messages)
        }

        return render(request, 'user_subscriptions/my_profile.html', context)


class SubscriptionsView(PermissionRequiredMixin, View):
    """View for displaying a table of all recent alerts matching a query"""

    permission_required = 'user.is_authenticated'

    def get(self, request, *args, **kwargs):
        return render(request, 'user_subscriptions/edit_subscriptions.html')

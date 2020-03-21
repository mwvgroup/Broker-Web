# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class SubscriptionsView(PermissionRequiredMixin, View):
    """View that handles new user subscriptions"""

    permission_required = 'user.is_authenticated'

    def get(self, request, *args, **kwargs):
        return render(request, 'subscriptions/subscriptions.html')


class ProfileView(PermissionRequiredMixin, View):
    """View that handles user profiles"""

    permission_required = 'user.is_active'

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        # Todo get pubsub messages
        timestamps = [123, 456]
        messages = ['a', 'b']
        context = {
            'pbsub_zip': zip(timestamps, messages)
        }

        return render(request, 'subscriptions/my_profile.html', context)

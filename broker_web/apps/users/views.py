# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from .forms import CustomUserCreationForm


class ProfileView(PermissionRequiredMixin, View):
    """View that handles user profiles"""

    permission_required = 'user.is_active'

    def get(self, request, *args, **kwargs):
        # Todo get pubsub messages
        timestamps = [123, 456]
        messages = ['a', 'b']
        context = {
            'pbsub_zip': zip(timestamps, messages)
        }

        return render(request, 'users/my_profile.html', context)


class SubscriptionsView(PermissionRequiredMixin, View):
    """View that handles new subscriptions for users"""

    permission_required = 'user.is_authenticated'

    def get(self, request, *args, **kwargs):
        return render(request, 'users/subscriptions.html')


class UserCreateView(CreateView):
    """View that handles ``CustomUser`` creation"""

    template_name = 'users/create_new_user.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

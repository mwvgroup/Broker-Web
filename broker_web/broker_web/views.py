# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    """View for the index page"""

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        context = {
            'online': False,
            'alerts_in_day': 0,
            'alerts_in_hour': 0
        }

        return render(request, 'broker_web/index.html', context)


class ContactView(View):
    """View for the index page"""

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        return render(request, 'broker_web/contact.html')

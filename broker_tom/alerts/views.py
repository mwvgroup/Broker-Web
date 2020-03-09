# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.shortcuts import render
from django.views.generic import View


class AlertsView(View):
    """View for displaying a table of all recent alerts matching a query"""

    def get(self, request, *args, **kwargs):
        # Todo get pubsub messages
        timestamps = [123, 456]
        messages = ['a', 'b']
        context = {
            'pbsub_zip': zip(timestamps, messages)
        }

        return render(request, 'alerts/alerts.html', context)


class AlertSummaryView(View):
    """View for displaying information about a single alert"""

    def get(self, request, *args, **kwargs):
        # Todo: Retrieve information about a single alert
        context = {
            'Alert Id': 1,
            'other alert data': 2
        }

        return render(request, 'alerts/alert_summary.html', context)

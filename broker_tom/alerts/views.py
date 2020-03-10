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

    def get_alert_data_for_id(self, alert_id, survey):
        """Retrieve alert data for a given alert ID"""
        alert_data = {
            'Alert Id': alert_id,
            'survey': survey.upper(),
            'some_field_1': 'some_value_1',
            'some_field_2': 'some_value_2'
        }

        return alert_data

    def get(self, request, *args, **kwargs):
        alert_id = kwargs['pk']
        survey = kwargs.get('survey', 'ztf')
        alert_data = self.get_alert_data_for_id(alert_id, survey)
        context = {'alert_data': alert_data, 'alert_id': alert_id, 'survey': survey}
        return render(request, 'alerts/alert_summary.html', context)

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    """View for the index page"""

    def get(self, request, *args, **kwargs):
        context = {
            'online': False,
            'alerts_in_day': 0,
            'alerts_in_hour': 0
        }

        return render(request, 'broker_tom/index.html', context)


class AlertsView(View):
    """View for displaying a table of all recent alerts matching a query"""

    def fetch_topic_list(self, **kwargs):
        return ['ztf_all', 'sne_ia', '91bg', 'cv']

    def fetch_pubsub_messages(self, **kwargs):
        surveys = ['ztf', 'ztf']
        alert_ids = [123, 234]
        object_ids = [345, 456]
        topics = ['ztf_all', 'ztf_all']
        timestamps = [1583959732, 1583959740]
        messages = ['a', 'b']
        return zip(surveys, alert_ids, object_ids, topics, timestamps, messages)

    def get(self, request, *args, **kwargs):

        context = {
            'message_zip': self.fetch_pubsub_messages(**kwargs),
            'topic_list': self.fetch_topic_list()
        }

        return render(request, 'broker_tom/alerts.html', context)


class AlertSummaryView(View):
    """View for displaying information about a single alert"""

    def get_alert_data_for_id(self, alert_id, survey):
        """Retrieve alert data for a given alert ID"""

        alert_data = {
            'alert_id': alert_id,
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
        return render(request, 'broker_tom/alert_summary.html', context)


class ObjectsView(View):
    """View for displaying a table of all recent objects matching a query"""

    def fetch_topic_list(self, **kwargs):
        return ['ztf_all', 'sne_ia', '91bg', 'cv']

    def fetch_objects(self, **kwargs):
        surveys = ['ztf', 'ztf']
        object_ids = [345, 456]
        alert_ids = [123, 234]
        timestamps = [1583959732, 1583959740]
        return zip(surveys, alert_ids, object_ids, timestamps)

    def get(self, request, *args, **kwargs):
        # Todo get pubsub messages

        context = {
            'pbsub_zip': self.fetch_objects(**kwargs),
            'topic_list': self.fetch_topic_list()
        }

        return render(request, 'broker_tom/objects.html', context)


class ObjectSummaryView(View):
    """View for displaying a table of all recent objects matching a query"""

    def get(self, request, *args, **kwargs):
        object_id = kwargs['pk']
        context = {'object_id': object_id}
        return render(request, 'broker_tom/object_summary.html', context)

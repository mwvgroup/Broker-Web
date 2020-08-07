# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.

.. autosummary::
   :nosignatures:

   broker_web.apps.alerts.views.AlertsJsonView
   broker_web.apps.alerts.views.AlertSummaryView
   broker_web.apps.alerts.views.RecentAlertsView
"""

import numpy as np
import os
from google.cloud import pubsub_v1
from django.shortcuts import render
from django.views.generic import View


from .forms import FilterAlertsForm
from ..utils import paginate_to_json


project_id = os.getenv('GOOGLE_CLOUD_PROJECT')


class AlertsJsonView(View):
    """Serves recent alerts as a paginated JSON response"""

    @staticmethod
    def fetch_alerts_as_dicts(request):
        """Returns a list of recent alerts messages as dicts

        Args:
            request (HttpRequest): Incoming HTTP request

        Return:
            A list of dictionaries representing
        """
        # Number of alerts to fetch from subscription
        max_alerts = 100
        
        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(project_id, subscription_name)

        response = subscriber.pull(subscription_path, max_messages=max_alerts)
        
        # Iterate through received messages and then acknowledge receipt
        ack_ids = []
        alert_ids, object_ids, timestamps = [], [], []

        for received_alert in response.received_messages:
            encoded = received_alert.message.data
            alert = encoded.decode('UTF-8')
            alert_ids.append(alert['candid'])
            object_ids.append(alert['objectId'])
            timestamps.append(alert['candidate']['jd'])
            
            ack_ids.append(received_message.ack_id)

        subscriber.acknowledge(subscription_path, ack_ids)
        
        # Still simulate some columns
        num_alerts = len(alert_ids)
        
        surveys = ['ztf' for _ in range(num_alerts)]
        topics = ['ztf_all' for _ in range(num_alerts)]
        messages = ['message' for _ in range(num_alerts)]


        keys = ["survey", "alert_id", "object_id", "topic", "timestamp", "message"]
        vals = zip(surveys, alert_ids, object_ids, topics, timestamps, messages)

        return [dict(zip(keys, val_set)) for val_set in vals]

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        alerts = self.fetch_alerts_as_dicts(request)
        return paginate_to_json(request, alerts)


class RecentAlertsView(View):
    """Provides a summary table of recently ingested alerts"""

    template = 'alerts/recent-alerts.html'

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        context = {'form': FilterAlertsForm()}
        return render(request, self.template, context)

    def post(self, request):  # Todo: Add filtering from form and update tests
        """Fill in the page's form with values from the POST request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        form = FilterAlertsForm(request.POST)
        return render(request, self.template, {'form': form})


class AlertSummaryView(View):
    """Displays information about a single alert"""

    template = 'alerts/alert_summary.html'

    @staticmethod
    def get_alert_data_for_id(alert_id, survey):
        """Retrieve alert data for a given alert ID

        Args:
            alert_id (int): Id of the alert to retrieve data for
            survey   (str): Parent survey of the alert

        Return:
            A dictionary of alert data
        """

        alert_data = {
            'alert_id': alert_id,
            'survey': survey.upper(),
            'some_field_1': 'some_value_1',
            'some_field_2': 'some_value_2'
        }

        return alert_data

    @staticmethod
    def get_value_added_data_for_id(alert_id, survey):
        """Retrieve value added data products for a given alert ID

        Args:
            alert_id (int): Id of the alert to retrieve data for
            survey   (str): Parent survey of the alert

        Return:
            A dictionary of value added data products
        """

        # Todo: This function can probably be broken into multiple
        # functions based on different data products. It depends
        # how the back / front end is designed
        return dict()

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        alert_id = kwargs['pk']
        survey = kwargs.get('survey', 'ztf')
        alert_data = self.get_alert_data_for_id(alert_id, survey)
        context = {'alert_data': alert_data, 'alert_id': alert_id, 'survey': survey}
        return render(request, self.template, context)

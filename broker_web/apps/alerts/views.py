# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.
"""

import numpy as np
from django.shortcuts import render
from django.views.generic import View

from .forms import FilterAlertsForm
from ..utils import paginate_to_json


class AlertsJson(View):
    """View for serving recent alerts as a paginated JSON response"""

    @staticmethod
    def fetch_alerts_as_dicts(request):
        """Returns a list of recent alerts messages as dicts

        Args:
            request (HttpRequest): Incoming HTTP request

        Return:
            A list of dictionaries representing
        """

        def random_int_arr(n):
            return np.round(1e12 * np.random.random(num_alerts))

        # Simulate placeholder data
        num_alerts = 100000
        surveys = ['ztf' for _ in range(num_alerts)]
        alert_ids = random_int_arr(num_alerts)
        object_ids = random_int_arr(num_alerts)
        topics = ['ztf_all' for _ in range(num_alerts)]
        timestamps = random_int_arr(num_alerts)
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
    """View for displaying a summary table of recent alerts"""

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
    """View for displaying information about a single alert"""

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

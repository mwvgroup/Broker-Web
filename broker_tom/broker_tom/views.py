# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .forms import FilterAlertsForm


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

        return render(request, 'broker_tom/index.html', context)


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

        # Get all available messages
        alerts = self.fetch_alerts_as_dicts(request)
        total = len(alerts)

        # Handle pagination
        # For expected in/outputs see https://datatables.net/manual/server-side
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        paginated_alerts = alerts[start:start + length]

        response = {
            'draw': int(request.GET.get('draw', -1)),
            'data': paginated_alerts,
            'recordsTotal': total,
            'recordsFiltered': len(paginated_alerts),
        }

        return JsonResponse(response)


class AlertsView(View):
    """View for displaying a summary table of recent alerts"""

    template = 'broker_tom/alerts.html'

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        context = {'form': FilterAlertsForm()}
        return render(request, self.template, context)

    def post(self, request):
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
        return render(request, 'broker_tom/alert_summary.html', context)


class ObjectsJson(View):
    """View for serving recent alerts as a paginated JSON response"""

    @staticmethod
    def fetch_objects_as_dicts(request):
        """Returns a list of recent alerts messages as dicts

        Args:
            request (HttpRequest): Incoming HTTP request

        Return:
            A list of dictionaries representing
        """

        def random_int_arr(n):
            return np.round(1e12 * np.random.random(num_alerts))

        num_alerts = 100000
        surveys = ['ztf' for _ in range(num_alerts)]
        object_ids = random_int_arr(num_alerts)
        recent_alert_ids = random_int_arr(num_alerts)
        recent_timestamps = random_int_arr(num_alerts)

        keys = ["survey", "object_id", "recent_alert_id", "recent_timestamp"]
        vals = zip(surveys, object_ids, recent_alert_ids, recent_timestamps)
        return [dict(zip(keys, val_set)) for val_set in vals]

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        # Get all available messages
        objects = self.fetch_objects_as_dicts(request)
        total = len(objects)

        # Handle pagination
        # For expected in/outputs see https://datatables.net/manual/server-side
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        paginated_alerts = objects[start:start + length]

        response = {
            'draw': int(request.GET.get('draw', -1)),
            'data': paginated_alerts,
            'recordsTotal': total,
            'recordsFiltered': len(paginated_alerts),
        }

        return JsonResponse(response)


class ObjectsView(View):
    """View for displaying a summary table of objects with recent alerts"""

    template = 'broker_tom/objects.html'

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        context = {'form': FilterAlertsForm()}
        return render(request, self.template, context)

    def post(self, request):
        """Fill in the page's form with values from the POST request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        form = FilterAlertsForm(request.POST)
        return render(request, self.template, {'form': form})


class ObjectSummaryView(View):
    """View for displaying a table of all recent objects matching a query"""

    @staticmethod
    def get_alerts_for_object(object_id):
        """Retrieve alert data for a given alert ID

        Args:
            object_id (int): Id of the object to retrieve alerts for

        Return:
            A dictionary of alert data
        """

        return dict()

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        object_id = kwargs['pk']
        recent_alerts = self.get_alerts_for_object(object_id)
        context = {'object_id': object_id, 'recent_alerts': recent_alerts}
        return render(request, 'broker_tom/object_summary.html', context)

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.
"""

import numpy as np
from django.shortcuts import render
from django.views.generic import View

from .forms import FilterObjectsForm
from ..utils import paginate_to_json


class ObjectsJson(View):
    """View for serving recently observed objects as a paginated JSON response"""

    @staticmethod
    def fetch_objects_as_dicts(request):
        """Returns a list of recent objects messages as dicts

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
        return paginate_to_json(request, objects)


class RecentObjectsView(View):
    """View for displaying a summary table of objects with recent alerts"""

    template = 'objects/recent_objects.html'

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        context = {'form': FilterObjectsForm()}
        return render(request, self.template, context)

    def post(self, request):
        """Fill in the page's form with values from the POST request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        form = FilterObjectsForm(request.POST)
        return render(request, self.template, {'form': form})


class ObjectSummaryView(View):
    """View for displaying a table of all recent objects matching a query"""

    template = 'objects/object_summary.html'

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
        return render(request, self.template, context)

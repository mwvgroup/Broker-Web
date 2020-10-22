# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.

.. autosummary::
   :nosignatures:

   broker_web.apps.objects.views.ObjectsJsonView
   broker_web.apps.objects.views.ObjectSummaryView
   broker_web.apps.objects.views.RecentObjectsView
"""

from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from google.cloud import bigquery

from .forms import FilterObjectsForm
from ..utils import paginate_to_json
from ..utils.templatetags.utility_tags import jd_to_readable_date

NUM_OBJECTS = 10_000
CLIENT = bigquery.Client()


class ObjectsJsonView(View):
    """View for serving recently observed objects as a paginated JSON response"""

    @staticmethod
    def fetch_objects_as_dicts(num_objects=NUM_OBJECTS):
        """Returns a list of recent alerts messages as dicts

        Args:
            num_objects     (int): Maximum number of alerts to return

        Return:
            A list of dictionaries representing
        """

        query = CLIENT.query(f"""
            SELECT 
                DISTINCT objectId as object_id, 
                publisher,
                CAST(candidate.candid AS STRING) recent_alert_id, 
                candidate.jd as pub_time,
                ARRAY_LENGTH( prv_candidates ) as num_alerts,
                ROUND(candidate.ra, 2) as ra, 
                ROUND(candidate.dec, 2) as dec
            FROM `{settings.ZTF_ALERTS_TABLE_NAME}`
            ORDER BY pub_time
            LIMIT {num_objects}
           """)

        output = []
        for row in query.result():
            row = dict(row)
            row['pub_time'] = jd_to_readable_date(row['pub_time'])
            output.append(row)

        return output

    def get(self, request):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        # Get all available messages
        objects = self.fetch_objects_as_dicts()
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


class RecentAlertsJsonView(View):
    """JSON rendering of recent alerts for a given object"""

    @staticmethod
    def fetch_recent_alerts(object_id):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        query = CLIENT.query(f"""
            SELECT 
                 publisher,
                 candidate.jd as pub_time,
                 CAST(candidate.candid AS STRING) as alert_id,
                 CASE candidate.fid WHEN 1 THEN 'g' WHEN 2 THEN 'R' WHEN 3 THEN 'i' END as filter,
                 ROUND(candidate.magpsf, 2) as magnitude
            FROM `{settings.ZTF_ALERTS_TABLE_NAME}`
            WHERE objectId="{object_id}"
        """)

        out_data = []
        for row in query.result():
            row_dict = dict(row)
            row_dict['jd'] = row_dict['pub_time']
            row_dict['pub_time'] = jd_to_readable_date(row_dict['pub_time'])
            out_data.append(row_dict)

        return out_data

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        # Get all available messages
        alerts = self.fetch_recent_alerts(kwargs['pk'])
        return paginate_to_json(request, alerts)


class ObjectSummaryView(View):
    """View for displaying a table of all recent objects matching a query"""

    template = 'objects/object_summary.html'

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        return render(request, self.template, {'object_id': kwargs['pk']})

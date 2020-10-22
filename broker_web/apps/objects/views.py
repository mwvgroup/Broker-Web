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
    def fetch_objects_as_dicts(request, num_objects=NUM_OBJECTS):
        """Returns a list of recent alerts messages as dicts

        Args:
            request (HttpRequest): Incoming HTTP request
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
            FROM `ardent-cycling-243415.ztf_alerts.alerts`
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
    def _get_alerts_for_ztf_object(object_id):
        """Retrieve an alert list for a ZTF object

        Args:
            object_id (int): Id of the object to retrieve alerts for

        Return:
            A dictionary of alert data
        """

        query = CLIENT.query(f"""
            SELECT 
                publisher, candid, candidate.jd as pub_time
            FROM `ardent-cycling-243415.ztf_alerts.alerts`
            WHERE objectId="{object_id}"
        """)

        return [[row['publisher'], row['candid'], jd_to_readable_date(row['pub_time'])] for row in query.result()]

    def get_alerts_for_object(self, object_id, survey):
        """Retrieve alert data for a given alert ID

        Args:
            object_id (int): Id of the object to retrieve alerts for
            survey   (str): Parent survey of the alert

        Return:
            A dictionary of alert data
        """

        if survey.lower() == 'ztf':
            return self._get_alerts_for_ztf_object(object_id)

        raise NotImplementedError(f'Database object queries not implemented for survey {survey}')

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing JsonResponse
        """

        object_id = kwargs['pk']
        recent_alerts = self.get_alerts_for_object(object_id, 'ztf')
        context = {'object_id': object_id, 'recent_alerts': recent_alerts}
        return render(request, self.template, context)

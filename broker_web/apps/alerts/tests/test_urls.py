# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase
from django.urls import resolve, reverse

from broker_web.apps.alerts.urls import app_name
from broker_web.apps.alerts import views


class TestUrlRouting(TestCase):
    """Test URLs are routed to the correct views"""

    app_name = app_name

    def assert_view_routed(self, name, view, args=None, is_class_view=True):
        """Assert reverse lookup of the given name equals the given view

        Args:
            name             (str): URL name
            view (class, callable): Class or function view
            args            (list): Optional arguments to use in reverse URL lookup
            is_class_view   (bool): Whether ``view`` is a class view
        """

        url = reverse(f'{self.app_name}:{name}', args=args)

        returned_view = resolve(url).func
        if is_class_view:
            returned_view = returned_view.view_class

        self.assertEqual(view, returned_view)

    def test_recent_alerts_routing(self):
        """Test 'recent-alerts' is routed to``AlertsView``"""

        self.assert_view_routed('recent-alerts', views.AlertsView)

    def test_alert_summary_routing(self):
        """Test 'alert-summary' is routed to``AlertSummaryView``"""

        dummy_alert_pk = '123'
        self.assert_view_routed(
            'alert-summary', views.AlertSummaryView, args=[dummy_alert_pk])

    def test_alerts_json_routing(self):
        """Test 'alerts-json' is routed to``AlertsJson``"""

        self.assert_view_routed('alerts-json', views.AlertsJson)

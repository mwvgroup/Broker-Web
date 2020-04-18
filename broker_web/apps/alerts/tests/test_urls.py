# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase

from broker_web.apps.alerts import urls, views
from broker_web.apps.base_tests import BaseURLRouting


class TestUrlRouting(TestCase, BaseURLRouting):
    """Test URLs are routed to the correct views"""

    app_name = urls.app_name

    def test_alerts_json_routing(self):
        """Test 'alerts-json' is routed to``AlertsJson``"""

        self.assert_view_routed('alerts-json', views.AlertsJson)

    def test_recent_alerts_routing(self):
        """Test 'recent-alerts' is routed to``RecentAlertsView``"""

        self.assert_view_routed('recent-alerts', views.RecentAlertsView)

    def test_alert_summary_routing(self):
        """Test 'alert-summary' is routed to``AlertSummaryView``"""

        dummy_alert_pk = '123'
        self.assert_view_routed(
            'alert-summary', views.AlertSummaryView, args=[dummy_alert_pk])

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.test import TestCase
from django.urls import reverse

from broker_web.apps.alerts import urls
from broker_web.apps.base_tests import ViewTests


class AlertsJsonView(TestCase, ViewTests):
    """Tests for the ``AlertsJson`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:alert-summary', args=['123'])
    template = 'alerts/alert_summary.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)


class RecentAlertsView(TestCase, ViewTests):
    """Tests for the ``RecentAlerts`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:recent-alerts')
    template = 'alerts/recent-alerts.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

    def test_post_200(self):
        """Test ``post`` method returns correct template with 200 status code"""

        self.assert_200_template('post', self.url, self.template)


class AlertSummaryView(TestCase, ViewTests):
    """Tests for the ``AlertSummary`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:alert-summary', args=['123'])
    template = 'alerts/alert_summary.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

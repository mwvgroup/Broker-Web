# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.http import JsonResponse
from django.test import Client, TestCase
from django.urls import reverse

from broker_web.apps.alerts import urls


class TestAlertsJson(TestCase):
    """Tests for the ``AlertsJson`` view"""

    url_name = f'{urls.app_name}:alerts-json'

    def setUp(self):
        self.client = Client()

    def test_get(self):
        """Test ``get`` method returns Json Response"""

        url = reverse(self.url_name)
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response, JsonResponse)


class TestRecentAlerts(TestCase):
    """Tests for the ``RecentAlerts`` view"""

    url_name = f'{urls.app_name}:recent-alerts'
    template = 'alerts/recent-alerts.html'

    def setUp(self):
        self.client = Client()

    def test_get(self):
        """Test ``get`` method returns correct template"""

        url = reverse(self.url_name)
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)

    def test_post(self):
        """Test ``post`` method returns correct template"""

        url = reverse(self.url_name)
        response = self.client.post(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)


class TestAlertSummary(TestCase):
    """Tests for the ``AlertSummary`` view"""

    url_name = f'{urls.app_name}:alert-summary'
    template = 'alerts/alert_summary.html'

    def setUp(self):
        self.client = Client()

    def test_get(self):
        """Test ``get`` method returns correct template and alert id"""

        dummy_alert_id = 123
        url = reverse(self.url_name, args=[dummy_alert_id])
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)

        returned_alert_id = response.context['alert_data']['alert_id']
        self.assertEqual(returned_alert_id, dummy_alert_id)

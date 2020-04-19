# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.test import Client, TestCase
from django.urls import reverse

from broker_web.apps.subscriptions import urls


class SubscriptionsView(TestCase):
    """Tests for the ``Subscriptions`` view"""

    url_name = f'{urls.app_name}:subscriptions'
    template = 'subscriptions/subscriptions.html'

    def test_get(self):
        """Test ``get`` method returns correct template with 200 status code"""

        url = reverse(self.url_name)
        response = Client().get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)


class ProfileView(TestCase):
    """Tests for the ``Profile`` view"""

    url_name = f'{urls.app_name}:profile'
    template = 'subscriptions/my_profile.html'

    def test_get(self):
        """Test ``get`` method returns correct template with 200 status code"""

        url = reverse(self.url_name)
        response = Client().get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)

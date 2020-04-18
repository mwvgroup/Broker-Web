# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.test import TestCase
from django.urls import reverse

from broker_web.apps.base_tests import ViewTests
from broker_web.apps.subscriptions import urls


class SubscriptionsView(TestCase, ViewTests):
    """Tests for the ``SignUp`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:subscriptions')
    template = 'subscriptions/subscriptions.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)


class ProfileView(TestCase, ViewTests):
    """Tests for the ``SignUp`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:profile')
    template = 'subscriptions/my_profile.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

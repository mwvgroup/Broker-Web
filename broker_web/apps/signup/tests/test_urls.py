# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase

from broker_web.apps.base_tests import BaseURLRouting
from broker_web.apps.signup import urls, views


class TestUrlRouting(TestCase, BaseURLRouting):
    """Test URLs are routed to the correct views"""

    app_name = urls.app_name

    def test_signup_routing(self):
        """Test 'signup' is routed to``SignUp``"""

        self.assert_view_routed('signup', views.SignUp)

    def test_activation_sent_routing(self):
        """Test 'activation-sent' is routed to``AlertSummaryView``"""

        self.assert_view_routed(
            'activation-sent', views.activation_sent_view, is_class_view=False)

    def test_activate_routing(self):
        """Test 'activate' is routed to``ActivateAccount``"""

        dummy_activation_key = 'AB/CD-EFGHIJKLMN/'
        self.assert_view_routed(
            'activate', views.ActivateAccount, args=[dummy_activation_key])

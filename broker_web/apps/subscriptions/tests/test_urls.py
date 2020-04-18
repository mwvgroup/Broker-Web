# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase

from broker_web.apps.base_tests import BaseURLRouting
from broker_web.apps.subscriptions import urls, views


class TestUrlRouting(TestCase, BaseURLRouting):
    """Test URLs are routed to the correct views"""

    app_name = urls.app_name

    def test_subscriptions_routing(self):
        """Test 'subscriptions' is routed to``SubscriptionsView``"""

        self.assert_view_routed('subscriptions', views.SubscriptionsView)

    def test_profile_routing(self):
        """Test 'profile' is routed to``ProfileView``"""

        self.assert_view_routed('profile', views.ProfileView)

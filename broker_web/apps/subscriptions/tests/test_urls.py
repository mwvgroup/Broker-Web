# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase
from django.urls import resolve, reverse

from broker_web.apps.subscriptions.urls import app_name
from broker_web.apps.subscriptions import views


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

    def test_subscriptions_routing(self):
        """Test 'subscriptions' is routed to``SubscriptionsView``"""

        self.assert_view_routed('subscriptions', views.SubscriptionsView)

    def test_profile_routing(self):
        """Test 'profile' is routed to``ProfileView``"""

        self.assert_view_routed('profile', views.ProfileView)

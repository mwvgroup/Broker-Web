# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from broker_web.apps.signup import urls
from broker_web.apps.signup import views


class TestUrlRouting(SimpleTestCase):
    """Test URLs are routed to the correct views"""

    app_name = urls.app_name

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

    def test_signup_routing(self):
        """Test 'signup' is routed to``SignUp``"""

        self.assert_view_routed('signup', views.SignUp)

    def test_activation_sent_routing(self):
        """Test 'activation-sent' is routed to``AlertSummaryView``"""

        self.assert_view_routed(
            'activation-sent', views.activation_sent_view, is_class_view=False)

    def test_activate_routing(self):
        """Test 'activate' is routed to``ActivateAccount``"""

        self.assert_view_routed('activate', views.ActivateAccount)

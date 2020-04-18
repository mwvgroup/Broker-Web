# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase
from django.urls import resolve, reverse

from broker_web.apps.contact import app_name
from broker_web.apps.contact import views


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

    def test_contact_routing(self):
        """Test 'contact' is routed to``ContactView``"""

        self.assert_view_routed('contact', views.ContactView)

    def test_contact_sent_routing(self):
        """Test 'contact-sent' is routed to``success_view``"""

        self.assert_view_routed(
            'contact-sent', views.success_view, is_class_view=False)

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase

from broker_web.apps.base_tests import BaseURLRouting
from broker_web.apps.contact import urls, views


class TestUrlRouting(TestCase, BaseURLRouting):
    """Test URLs are routed to the correct views"""

    app_name = urls.app_name

    def test_contact_routing(self):
        """Test 'contact' is routed to``ContactView``"""

        self.assert_view_routed('contact', views.ContactView)

    def test_contact_sent_routing(self):
        """Test 'contact-sent' is routed to``success_view``"""

        self.assert_view_routed(
            'contact-sent', views.success_view, is_class_view=False)

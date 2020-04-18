# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import TestCase

from broker_web.apps.base_tests import BaseURLRouting
from broker_web.apps.objects import urls, views


class TestUrlRouting(TestCase, BaseURLRouting):
    """Test URLs are routed to the correct views"""

    app_name = urls.app_name

    def test_objects_json_routing(self):
        """Test 'objects-json' is routed to``ObjectsJson``"""

        self.assert_view_routed('objects-json', views.ObjectsJson)

    def test_recent_objects_routing(self):
        """Test 'recent-objects' is routed to``RecentObjectsView``"""

        self.assert_view_routed('recent-objects', views.RecentObjectsView)

    def test_object_summary_routing(self):
        """Test 'object-summary' is routed to``ObjectSummaryView``"""

        dummy_object_pk = '123'
        self.assert_view_routed(
            'object-summary', views.ObjectSummaryView, args=[dummy_object_pk])

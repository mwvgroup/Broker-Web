# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``urls`` module."""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from broker_web.apps.objects import urls
from broker_web.apps.objects import views


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

    def test_recent_objects_routing(self):
        """Test 'recent-objects' is routed to``ObjectsView``"""

        self.assert_view_routed('recent-objects', views.ObjectsView)

    def test_object_summary_routing(self):
        """Test 'object-summary' is routed to``ObjectSummaryView``"""

        dummy_object_pk = '123'
        self.assert_view_routed(
            'object-summary', views.ObjectSummaryView, args=[dummy_object_pk])

    def test_objects_json_routing(self):
        """Test 'objects-json' is routed to``ObjectsJson``"""

        self.assert_view_routed('objects-json', views.ObjectsJson)

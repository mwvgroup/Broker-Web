# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.test import TestCase
from django.urls import reverse

from broker_web.apps.objects import urls
from broker_web.apps.base_tests import ViewTests


class ObjectsJsonView(TestCase, ViewTests):
    """Tests for the ``ObjectsJson`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:object-summary', args=['123'])
    template = 'objects/object_summary.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)


class RecentObjectsView(TestCase, ViewTests):
    """Tests for the ``RecentObjects`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:recent-objects')
    template = 'objects/recent_objects.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

    def test_post_200(self):
        """Test ``post`` method returns correct template with 200 status code"""

        self.assert_200_template('post', self.url, self.template)


class ObjectSummaryView(TestCase, ViewTests):
    """Tests for the ``ObjectSummary`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:object-summary', args=['123'])
    template = 'objects/object_summary.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``forms`` module."""

from django.test import TestCase

from broker_web.apps.alerts.forms import FilterAlertsForm


class TestFilterAlertsForm(TestCase):
    """Test the ``FilterAlertsForm`` validates correctly"""

    def test_empty_form(self):
        """Test that an empty form is valid"""

        form = FilterAlertsForm(data={})
        self.assertTrue(form.is_valid())

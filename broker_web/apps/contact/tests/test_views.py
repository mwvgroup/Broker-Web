# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.test import TestCase
from django.urls import reverse

from broker_web.apps.base_tests import ViewTests
from broker_web.apps.contact import urls


class ContactView(TestCase, ViewTests):
    """Tests for the ``Contact`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:contact')
    template = 'contact/contact_us.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

    def test_form_validation(self):
        self.fail()


class SuccessView(TestCase, ViewTests):
    """Tests for the ``success_view`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:contact-sent')
    template = 'contact/contact_sent.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

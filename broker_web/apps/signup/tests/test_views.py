# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``views`` module."""

from django.test import TestCase
from django.urls import reverse

from broker_web.apps.base_tests import ViewTests
from broker_web.apps.signup import urls


class SignUpView(TestCase, ViewTests):
    """Tests for the ``SignUp`` view"""

    app_name = urls.app_name
    url = reverse(f'{urls.app_name}:signup')
    template = 'signup/create_new_user.html'

    def test_get_200(self):
        """Test ``get`` method returns correct template with 200 status code"""

        self.assert_200_template('get', self.url, self.template)

    def test_form_validation(self):
        self.fail()


class ActivateAccountView(TestCase, ViewTests):
    app_name = urls.app_name

    def test_get_with_invalid_token(self):

        bad_signup_token = 'AB/CDE-FGHIJK'
        url = reverse(f'{urls.app_name}:activate', args=[bad_signup_token])
        self.assert_200_template('get', url, 'signup/invalid_activation_link.html')

    def test_get_with_valid_token(self):
        self.assert_200_template('get', url, 'signup/activation_success.html')

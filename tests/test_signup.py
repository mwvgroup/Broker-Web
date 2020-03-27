# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Tests for the ``signup`` application"""

import os
import sys
from pathlib import Path

from django import setup
from django.contrib.auth import get_user_model
from django.test import TestCase


def setUpModule():
    # Add broker_web package to path
    package_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(package_dir))

    # Set up the broker_web django application so that we can import
    # views and models without raising
    # django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.`
    os.environ['DJANGO_SETTINGS_MODULE'] = 'broker_web.main.settings'
    os.environ['SECRET_KEY'] = 'FAKE_KEY_FOR_BUILDING_DOCS'
    setup()


class UsersManagersTests(TestCase):
    """Test user creation"""

    def test_create_user(self):
        """Test creation of regular user has correct defaults"""

        UserModel = get_user_model()

        test_email = 'test@user.com'
        new_user = UserModel.objects.create_user(email=test_email, password='test')

        self.assertEqual(new_user.email, test_email, 'Email does not equal passed value.')
        self.assertFalse(new_user.is_active, 'User is set to active')
        self.assertFalse(new_user.is_staff, 'User is staff')
        self.assertFalse(new_user.is_superuser, 'User is superuser')

        with self.assertRaises(TypeError, msg='No error raised for missing email'):
            UserModel.objects.create_user()

        with self.assertRaises(TypeError, msg='No error raised for blank email'):
            UserModel.objects.create_user(email='')

    def test_create_superuser(self):
        """Test creation of a superuser has correct defaults"""

        UserModel = get_user_model()

        test_email = 'test@user.com'
        new_admin_user = UserModel.objects.create_superuser(test_email, 'foo')

        self.assertEqual(new_admin_user.email, test_email, 'Email does not equal passed value.')
        self.assertTrue(new_admin_user.is_active, 'User is not active')
        self.assertTrue(new_admin_user.is_staff, 'User is not staff')
        self.assertTrue(new_admin_user.is_superuser, 'User is not superuser')

        with self.assertRaises(TypeError, msg='No error raised for missing email'):
            UserModel.objects.create_superuser()

        with self.assertRaises(TypeError, msg='No error raised for blank email'):
            UserModel.objects.create_superuser(email='')

        with self.assertRaises(ValueError, msg='No error raised for is_superuser=False'):
            UserModel.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)

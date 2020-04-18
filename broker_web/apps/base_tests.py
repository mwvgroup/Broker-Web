# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Generic test classes"""

from django.test import Client
from django.urls import resolve, reverse


class BaseURLRouting:
    """Test URLs are routed to the correct views

    Setup:
       The ``app_name`` attribute must be set to reflect the name of the app
       being tested.
    """

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


class ViewTests:

    def assert_200_template(self, method, url, template):
        """Test for GET actions"""

        client = Client()
        response = getattr(client, method)(url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template)

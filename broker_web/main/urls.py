# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""URL routing for the main django application. URLS from each application
is routed to the following namespaces:

+-----------------------+-------------------+
| Application           | Namespace         |
+=======================+===================+
|``apps.contact``       | ``contact``       |
+-----------------------+-------------------+
|``apps.alerts``        | ``alerts``        |
+-----------------------+-------------------+
|``apps.objects``       | ``objects``       |
+-----------------------+-------------------+
|``apps.signup``        | ``signup``        |
+-----------------------+-------------------+
|``apps.subscriptions`` | ``subscriptions`` |
+-----------------------+-------------------+
"""

from django.contrib import admin
from django.urls import include
from django.urls import path

import broker_web.apps as apps
from .views import IndexView, why_pgb_view

getting_started_paths = (
    'getting_started/introduction.html',
    'getting_started/data_products_overview.html',
    'getting_started/technical_resources.html')

getting_started_urls = apps.utils.create_static_template_routes(
    getting_started_paths, 'getting-started')

# URLs for custom views
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('why_pgb', why_pgb_view, name='why-pgb'),
    path('contact/', include('broker_web.apps.contact.urls', namespace='contact')),
    path('alerts/', include('broker_web.apps.alerts.urls', namespace='alerts')),
    path('objects/', include('broker_web.apps.objects.urls', namespace='objects')),
    path('getting_started/', include(getting_started_urls, namespace='getting-started')),
    path('signup/', include('broker_web.apps.signup.urls', namespace='signup')),
    path('subscriptions/', include('broker_web.apps.subscriptions.urls', namespace='subscriptions')),
]

# Built in Django URL patterns
urlpatterns += [
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views

getting_started_paths = (
    'getting_started/introduction.html',
    'getting_started/data_products_overview.html',
    'getting_started/technical_resources.html')

getting_started_urls = apps.utils.create_static_template_routes(
    getting_started_paths, 'getting-started')

# URLs for custom views
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('', include('apps.alerts.urls', namespace='alerts')),
    path('', include('apps.objects.urls', namespace='objects')),
    path('getting_started/', include(getting_started_urls, namespace='getting-started')),
    path('users', include('apps.users.urls', namespace='users')),
]

# Built in Django URL patterns
urlpatterns += [
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

# Static URLs for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
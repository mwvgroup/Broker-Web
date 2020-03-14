# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

import apps
from . import views

# URLs for custom views
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('', include(apps.alerts.urls, namespace='alerts')),
    path('', include(apps.objects.urls, namespace='objects')),
    path('getting_started', include(apps.getting_started.urls, namespace='getting-started')),
    path('subscriptions', include(apps.user_subscriptions.urls, namespace='subscriptions')),
]

# Built in Django URL patterns
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

# Static URLs for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

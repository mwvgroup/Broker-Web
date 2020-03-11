# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from .views import IndexView

# URLs for custom views
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('alerts/', include('alerts.urls')),
    path('gettingstarted/', include('getting_started.urls')),
]

# Built in Django URL patterns
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

# Static URLs for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

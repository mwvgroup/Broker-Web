# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views

# URLs for custom views
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('alerts/', views.AlertsView.as_view(), name='alerts'),
    path('alerts/<int:pk>', views.AlertSummaryView.as_view(), name='alert-summary'),
    path('objects/', views.ObjectsView.as_view(), name='objects'),
    path('objects/<int:pk>', views.ObjectSummaryView.as_view(), name='object-summary'),
    path('gettingstarted/', include('getting_started.urls')),
    path('user/', include('user_subscriptions.urls')),
]

# URLS for json requests
urlpatterns += [
    path('alerts/json/', views.AlertsJson.as_view(), name='alerts_json'),
    path('objects/json/', views.ObjectsJson.as_view(), name='objects_json')
]


# Built in Django URL patterns
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

# Static URLs for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

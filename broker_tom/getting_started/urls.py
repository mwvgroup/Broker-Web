# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='getting_started/introduction.html'), name='getting-started'),
    path('technical_resources', TemplateView.as_view(template_name='getting_started/technical_resources.html'), name='technical-resources'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

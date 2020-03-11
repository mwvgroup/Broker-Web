# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django URL Configuration. Lists routes from URLs to views"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

getting_started_view = TemplateView.as_view(template_name='getting_started/introduction.html')
data_products_overview = TemplateView.as_view(template_name='getting_started/data_products_overview.html')
technical_resources_view = TemplateView.as_view(template_name='getting_started/technical_resources.html')

urlpatterns = [
    path('', getting_started_view, name='getting-started'),
    path('data_products_overview', data_products_overview, name='data-products-overview'),
    path('technical_resources', technical_resources_view, name='technical-resources'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

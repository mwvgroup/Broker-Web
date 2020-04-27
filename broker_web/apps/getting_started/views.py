# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.
"""

from django.views.generic import TemplateView

dir_name = 'getting_started/'

Introduction = TemplateView.as_view(
    template_name=dir_name + 'introduction.html')

DataProducts = TemplateView.as_view(
    template_name=dir_name + 'data_products.html')

TechnicalResources = TemplateView.as_view(
    template_name=dir_name + 'technical_resources.html')

DataAccess = TemplateView.as_view(
    template_name=dir_name + 'data_access.html')

BrokerDesign = TemplateView.as_view(
    template_name=dir_name + 'broker_design.html')

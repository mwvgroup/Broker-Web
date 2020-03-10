# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    """View for the index page"""

    def get(self, request, *args, **kwargs):
        context = {
            'online': False,
            'alerts_in_day': 0,
            'alerts_in_hour': 0
        }

        return render(request, 'broker_tom/index.html', context)

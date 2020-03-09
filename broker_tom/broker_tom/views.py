# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.shortcuts import render
from django.views.generic import View


class AlertsView(View):

    def get(self, request, *args, **kwargs):
        # Todo get pubsub messages
        timestamps = [1, 2]
        messages = ['a', 'b']
        context = {
            'pbsub_zip': zip(timestamps, messages)
        }

        return render(request, 'broker_tom/alerts.html', context)

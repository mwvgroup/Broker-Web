# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django app for serving data concerning recently observed astronomical
objects. The focus of this app is on the object itself, and not the
corresponding alerts.
"""

from . import forms, urls, views

# Todo-objects:
# - Add / use PubSub configuration to / from global settings
# - Populate the ObjectsJson view using PubSub messages
# - Use arguments from the filter results from to filter values in ObjectsJson
# - Move ``forms.topics`` into global settings

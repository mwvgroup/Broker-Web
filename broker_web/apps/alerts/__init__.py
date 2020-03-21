# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""django app for serving up data about recently observed LSST/ZTF alerts
published in a collection of configured PubSub topics.
"""

# Todo alerts:
# - Add / use PubSub configuration to / from global settings
# - Populate the AlertsJson view using PubSub messages
# - Use arguments from the filter results from to filter values in AlertsJson
# - Move ``forms.topics`` into global settings

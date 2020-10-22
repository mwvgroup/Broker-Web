# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``custom_tags`` module defines custom functions for use within Jinja
templates.

.. autosummary::
   :nosignatures:

   broker_web.apps.utils.templatetags.utility_tags.bin_to_utf8
   broker_web.apps.utils.templatetags.utility_tags.jd_to_readable_date
"""

from base64 import b64encode

from astropy.time import Time
from django import template

register = template.Library()


@register.filter
def bin_2_utf8(_bin):
    """Convert bytes data to UTF8

    Args:
        _bin (bytes): Bytes data

    Returns:
        A string in UTF-8 format
    """

    if _bin is not None:
        return b64encode(_bin).decode('utf-8')


@register.filter
def jd_to_readable_date(jd):
    """Convert a julian date to a human readable string

    Args:
        jd (float): Datetime value in julian format

    Returns:
        String in 'day mon year hour:min' format
    """

    return Time(jd, format='jd').strptime("%d %b %y %H:%M")

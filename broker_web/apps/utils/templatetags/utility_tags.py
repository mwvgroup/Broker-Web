# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``utility_tags`` module defines functions for casting between
different data types and formats.

.. autosummary::
   :nosignatures:

   broker_web.apps.utils.templatetags.utility_tags.bytes_to_64utf8
   broker_web.apps.utils.templatetags.utility_tags.jd_to_readable_date
"""

from base64 import b64encode

from astropy.time import Time
from django import template

register = template.Library()


@register.filter
def bytes_to_64utf8(bytes_data):
    """Convert bytes data to UTF8

    Args:
        bytes_data (bytes): Bytes data

    Returns:
        A string in UTF-8 format
    """

    if bytes_data is not None:
        return b64encode(bytes_data).decode('utf-8')


@register.filter
def jd_to_readable_date(jd):
    """Convert a julian date to a human readable string

    Args:
        jd (float): Datetime value in julian format

    Returns:
        String in 'day mon year hour:min' format
    """

    return Time(jd, format='jd').strftime("%d %b %Y - %H:%M:%S")

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views forms for data entry and query construction"""

from django import forms

topics = (
    'ztf_all',
    '91bg',
    'sne Ia',
    'CV'
)


class FilterAlertsForm(forms.Form):
    time_range = forms.DurationField(required=False, label='Publication time')
    min_ra = forms.FloatField(
        required=False,
        label='Min RA',
        widget=forms.TextInput()
    )

    max_ra = forms.FloatField(required=False, label='Max RA', widget=forms.TextInput())
    min_dec = forms.FloatField(required=False, label='Min Dec', widget=forms.TextInput())
    max_dec = forms.FloatField(required=False, label='Max Dec', widget=forms.TextInput())
    include_internal = forms.BooleanField(required=False, label='Include internal status messages')

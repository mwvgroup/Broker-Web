# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views forms for data entry and query construction"""

from django import forms


class ContactForm(forms.Form):
    """Form for sending a 'contact us' email"""

    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``forms`` module defines views forms for data entry and query
construction.
"""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

user_fields = 'email', 'first_name', 'last_name', 'country', 'university'


class CustomUserCreationForm(UserCreationForm):
    """Custom form for creating a new ``CustomUser``"""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = user_fields


class CustomUserChangeForm(UserChangeForm):
    """Custom form for modifying user data"""

    class Meta:
        model = CustomUser
        fields = user_fields

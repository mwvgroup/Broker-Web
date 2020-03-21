# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Custom app level interfaces for the Admin Panel"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Custom admin interface for user management"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Fields shown in the main summary page
    list_display = ('username', 'email', 'first_name', 'last_name', 'country', 'university')

    # Fields shown when editing a new user
    fieldsets = (
        ('User Data', {'fields': list_display}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    # Fields shown when creating a new user
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )

    search_fields = ('username', 'email', 'university')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)

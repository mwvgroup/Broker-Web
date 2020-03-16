# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Models for representing backend DB constructs"""

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model for authentication"""

    username = models.TextField(max_length=100, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    university = models.TextField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __repr__(self):
        return f'<User(username={self.username})>'

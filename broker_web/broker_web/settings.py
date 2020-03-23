# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Django settings

For more information on this file, see
https://api_docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://api_docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

# Add apps to python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read environment settings from BASE_DIR
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def gen_secret_key(length=50, chars=None):
    """Generate a secret key for Django

    Args:
        length (int): The length of the key
        chars  (str): Characters to use
    """

    import string
    from django.utils.crypto import get_random_string

    if chars is None:
        chars = string.ascii_lowercase + string.digits + string.punctuation

    return get_random_string(length, chars)


# SECURITY WARNING: Make sure the following settings are properly configured in production
###############################################################################
SECRET_KEY = env.str('SECRET_KEY', default=gen_secret_key())
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CONTACT_EMAILS = env.list('CONTACT_EMAILS', default=[])
###############################################################################

INSTALLED_APPS = [
    'django.contrib.admin',  # Django administration interface
    'django.contrib.auth',  # Core authentication framework and associated models
    'django.contrib.contenttypes',  # Allows permissions to be associated with models
    'django.contrib.sessions',  # Session framework for cookies handling
    'django.contrib.messages',  # Displays one-time notification messages
    'django.contrib.staticfiles',  # Renders paths to static files
    'django.contrib.sites',  # Handles multi-site hosting on multiple domains
    'django_extensions',  # Extends capability of django management commands
    'guardian',  # Extra authentication backend with per object permissions
    'bootstrap4',  # Front-end component library for building templates
    'crispy_forms',  # Makes forms look pretty
    'apps.alerts',  # Custom app for displaying alert information
    'apps.contact',  # Custom app for "contact Us" form
    'apps.objects',  # Custom app for displaying object information
    'apps.signup',  # Custom app for user creation / authentication
    'apps.subscriptions',  # Custom app for alert subscriptions
]

# App configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Site configuration
ROOT_URLCONF = 'broker_web.urls'
SITE_ID = 1  # For description, see https://stackoverflow.com/a/25468782/6466457
LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'signup.CustomUser'  # Use custom user model for authentication

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database connection settings
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Todo: configure to env: {'default': env.db('DATABASE_URL')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Authentication configuration
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATETIME_FORMAT = 'Y-m-d H:m:s'
DATE_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images, etc.)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

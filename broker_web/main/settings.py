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
import pymysql

# Set up environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pymysql.version_info = (1, 3, 13, "final", 0)  # https://stackoverflow.com/a/59591269
pymysql.install_as_MySQLdb()
env = environ.Env()

# Read environment settings from file only if we are not deployed to App Engine
if not os.getenv('GAE_APPLICATION', False):
    environ.Env.read_env(os.path.join(os.path.dirname(BASE_DIR), '.env'))

# SECURITY WARNING: Make sure the following settings are properly configured in production
###############################################################################
SECRET_KEY = env.str('SECRET_KEY')
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

    # Custom apps
    'broker_web.apps.alerts',  # Custom app for displaying alert information
    'broker_web.apps.contact',  # Custom app for "contact Us" form
    'broker_web.apps.objects',  # Custom app for displaying object information
    'broker_web.apps.signup',  # Custom app for user creation / authentication
    'broker_web.apps.subscriptions',  # Custom app for alert subscriptions
]

# App configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Site configuration
ROOT_URLCONF = 'broker_web.main.urls'
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
if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/ardent-cycling-243415:us-east1:broker-web',
            'USER': env.str('DB_USER'),
            'PASSWORD': env.str('DB_PASSWORD'),
            'NAME': 'web_backend',
        }
    }

elif os.getenv('GAE_REMOTE', None):
    # Running locally, but connect to Cloud SQL via the proxy.
    # To start the proxy see https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': env.str('DB_USER'),
            'PASSWORD': env.str('DB_PASSWORD'),
            'NAME': 'web_backend',
        }
    }

else:
    # Running locally against dummy db
    # mysql.server start
    # mysql -u root
    # > create database brokerweb;
    # > exit
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
STATIC_URL = 'https://storage.googleapis.com/broker-web-static/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

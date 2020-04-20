# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.
"""

import requests
from django.conf import settings
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View


# Todo: Replace AuthenticationForm with subclass that has a recaptcha component
# Todo: Can we inherit user validation?

def verify_recaptcha(request, *args, **kwargs):
    """Verify a recaptcha response

    Args:
        request (HttpRequest): Incoming HTTP request

    Returns:
        The recaptcha status as a bool
    """

    recaptcha_response = request.POST.get('g-recaptcha-response')
    post_data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }

    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    recaptcha_result = requests.post(verify_url, data=post_data)
    return recaptcha_result.json()['success']


class Login(View):
    """Custom login view that adds recaptcha verification"""

    template = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        form = AuthenticationForm()
        return render(request, "main/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        """Handle a POST request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect()

            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")

        recaptcha_valid = verify_recaptcha(requests)
        if not recaptcha_valid:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

        form = AuthenticationForm()
        return render(request, "main/login.html", {"form": form})

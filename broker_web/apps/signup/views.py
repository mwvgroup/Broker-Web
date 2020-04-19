# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.
"""

from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, View
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm
from .models import CustomUser
from .tokens import account_activation_token
from ..utils import send_email

activation_sent_view = TemplateView.as_view(template_name='signup/activation_link_sent.html')


class SignUp(CreateView):
    """View that handles ``CustomUser`` creation"""

    template_name = 'signup/create_new_user.html'
    form_class = CustomUserCreationForm

    # Todo: Include app name in reverse lookup in case app is namespaced differently
    success_url = reverse_lazy('signup:activation-sent')

    def form_valid(self, form):
        """Sends email confirmation for new user creation

        Called after form is validated

        Args:
            form (django.forms.Form): User creation form
        """

        # Create an inactive user
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = Site.objects.get_current()

        email_subject = 'Activate Your Account'
        message = render_to_string('signup/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        to_email = form.cleaned_data.get('email')
        response = send_email(
            from_address=settings.CONTACT_EMAIL,
            from_name='The PGB Team',
            to_address=to_email,
            to_name='',
            subject=email_subject,
            message=message
        )

        if response.status_code != 200:
            return HttpResponse('Invalid header found. Your message may ot have sent')

        # Parent class ``form_valid`` redirects to ``self.success_url``
        return super().form_valid(form)


class ActivateAccount(View):
    """View that account verification"""

    def get(self, request, uidb64, token):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request
            uidb64          (str): Base 64 encoded user id

        Returns:
            Outgoing HTTPResponse
        """

        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)

        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'signup/activation_success.html')

        else:
            return render(request, 'signup/invalid_activation_link.html')

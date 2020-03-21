# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, View

from .forms import CustomUserCreationForm
from .models import CustomUser

account_activation_token = PasswordResetTokenGenerator()


class SignUp(CreateView):
    """View that handles ``CustomUser`` creation"""

    template_name = 'users/create_new_user.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('activation-sent')

    def form_valid(self, form):
        """Sends email confirmation for new user creation

        Called after form is validated

        Args:
            form (django.forms.Form): User creation form
        """

        super().form_valid(form)

        # Create an inactive user
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        email_subject = 'Activate Your Account'
        message = render_to_string('users/activate_account.html', {
            'user': user,
            'domain': 'domain',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()

        # Parent class ``form_valid`` redirects to ``self.success_url``
        return super().form_valid(form)


class ActivateAccount(View):
    """View that account verification"""

    def get(self, request, uidb64, token):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

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
            return render(request, 'users/activation_success.html')

        else:
            return render(request, 'users/invalid_activation_link.html')


class ProfileView(PermissionRequiredMixin, View):
    """View that handles user profiles"""

    permission_required = 'user.is_active'

    def get(self, request, *args, **kwargs):
        """Handle an incoming HTTP request

        Args:
            request (HttpRequest): Incoming HTTP request

        Returns:
            Outgoing HTTPResponse
        """

        # Todo get pubsub messages
        timestamps = [123, 456]
        messages = ['a', 'b']
        context = {
            'pbsub_zip': zip(timestamps, messages)
        }

        return render(request, 'users/my_profile.html', context)

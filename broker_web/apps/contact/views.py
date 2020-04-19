# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""The ``views`` module defines ``View`` objects for converting web requests
into rendered responses.
"""

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm
from ..utils import send_email

success_view = TemplateView.as_view(template_name='contact/contact_sent.html')


class ContactView(FormView):
    """View for submitting an email to the website maintainers"""

    template_name = "contact/contact_us.html"
    form_class = ContactForm
    # Todo: Include app name in reverse lookup in case app is namespaced differently
    success_url = reverse_lazy('contact:contact-sent')

    def form_valid(self, form):
        """Send contents of email form and redirect to success url

        Called after form is validated

        Args:
            form (django.forms.Form): User creation form
        """

        subject = form.cleaned_data['subject']
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']

        response = send_email(
            from_address='pgalertbroker@gmail.com',
            from_name=name + ':' + email,
            to_address=settings.CONTACT_EMAIL,
            to_name='PGB Team',
            subject=subject,
            message=message)

        if response.status_code != 200:
            return HttpResponse('Invalid header found. Your message may ot have sent')

        return super().form_valid(form)

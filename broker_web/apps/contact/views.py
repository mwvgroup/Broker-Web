# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Defines views for converting a Web requests into a Web responses"""

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.conf import settings
from .forms import ContactForm

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
        message = form.cleaned_data['message']

        try:
            send_mail(subject, message, email, settings.CONTACT_EMAILS)

        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return super().form_valid(form)
from django.test import Client, TestCase
from django.urls import reverse

from broker_web.apps.alerts.urls import app_name


class AlertsView(TestCase):
    app_name = app_name

    def setUp(self):
        self.client = Client()
        self.url = reverse(f'{self.app_name}:alerts')
        self.template = 'alerts/alert_summary.html'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)

    def test_post(self):
        pass

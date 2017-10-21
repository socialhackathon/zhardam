from django.urls import reverse
from rest_framework.test import APITestCase as TestCase


class ResponseTestCase(TestCase):
    def test_success(self):
        response = self.client.get(reverse('quizes:get-scenario'))
        self.assertEqual(200, response.status_code)

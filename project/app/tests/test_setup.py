from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.get_urls = reverse('all_urls')
        self.create_urls = reverse('create_link')
        self.valid_url = {
            'original_url': "https://www.google.com/"
        }
        self.invalid_url = {
            'invalid_url': "www.google.com"
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

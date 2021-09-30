from rest_framework.test import APITestCase
from django.urls import reverse

# This class is responsible for creating test class by inheriting APITestCase 
class TestSetUp(APITestCase):
    
    # This method is resposible to set all the variables before executing any TestCases. This SetUp method gets called before execution of each TestCase.
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

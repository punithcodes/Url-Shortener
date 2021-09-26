from .test_setup import TestSetUp
import pdb


class TestViews(TestSetUp):

    def test_get_all_urls(self):
        res = self.client.get(self.get_urls)
        self.assertEqual(res.status_code, 200)

    def test_no_shortlink_without_originallink(self):
        res = self.client.post(self.create_urls)
        self.assertEqual(res.status_code, 400)

    def test_create_shortlink_with_originallink(self):
        res = self.client.post(self.create_urls, self.valid_url, format="json")
        self.assertEqual(res.status_code, 201)

    def test_invalid_originallink(self):
        res = self.client.post(self.create_urls, self.invalid_url, format="json")
        self.assertEqual(res.status_code, 400)


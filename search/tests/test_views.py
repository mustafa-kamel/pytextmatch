from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_search_accepts_only_get(self):
        response = self.client.get(reverse('search:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_search_rejects_post(self):
        response = self.client.post(reverse('search:index'))
        self.assertEqual(response.status_code, 405)
        self.assertTemplateNotUsed(response, 'index.html')
        self.assertTemplateNotUsed(response, 'results.html')

    def test_results_accepts_only_post_empty_body(self):
        response = self.client.post(reverse('search:results'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue('message' in response.context)

    def test_results_accepts_only_post_has_body(self):
        response = self.client.post(
            reverse('search:results'), {'query': 'finde me'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'results.html')
        self.assertTrue('result' in response.context)

    def test_results_rejects_get(self):
        response = self.client.get(reverse('search:results'))
        self.assertEqual(response.status_code, 405)
        self.assertTemplateNotUsed(response, 'index.html')
        self.assertTemplateNotUsed(response, 'results.html')

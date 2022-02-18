from django.test import SimpleTestCase
from django.urls import reverse, resolve

from search.views import search, results


class TestUrls(SimpleTestCase):

    def test_search_url(self):
        self.assertEqual(resolve(reverse('search:index')).func, search)

    def test_results_url(self):
        self.assertEqual(resolve(reverse('search:results')).func, results)

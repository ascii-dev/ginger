from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from ginger.tests.mocks.arxiv_articles import mock_articles_with_query, sample_arxiv_article


class SingleAuthorTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()

    @patch("articles.views.all_articles.arxiv.query", mock_articles_with_query)
    def test_get_single_author_page_succeeds(self):
        """
        Tests that we can successfully get the single author page to display
        """
        response = self.client.get(reverse('single_author', kwargs={'author': sample_arxiv_article['author']}))
        self.assertTemplateUsed('authors/single.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, sample_arxiv_article['author'], html=True)
        self.assertContains(response, sample_arxiv_article['title'], html=True)

from unittest.mock import patch
from django.urls import reverse
from django.test import Client, TestCase

from articles.tests.mocks.arxiv_articles import sample_arxiv_article, mock_arxiv_articles


class AllArticlesTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()

    @patch("articles.views.all_articles.arxiv.query", mock_arxiv_articles)
    def test_get_all_articles_page_succeeds(self):
        """
        Tests that we can successfully get the all articles page to display
        :return:
        """
        response = self.client.get(reverse('all_articles'))
        self.assertTemplateUsed('articles/all.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About', html=True)
        self.assertContains(response, sample_arxiv_article['title'], html=True)

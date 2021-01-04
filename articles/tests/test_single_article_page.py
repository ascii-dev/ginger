from unittest.mock import patch
from django.urls import reverse
from django.test import Client, TestCase

from articles.tests.mocks.arxiv_articles import (
    sample_arxiv_article,
    mock_article_with_id_list,
)


class SingleArticleTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()

    @patch("articles.views.all_articles.arxiv.query", mock_article_with_id_list)
    def test_get_all_articles_page_succeeds(self):
        """
        Tests that we can successfully get the a articles page to display
        """
        response = self.client.get(reverse('single_article', args=[sample_arxiv_article['split_id']]))
        self.assertTemplateUsed('articles/single.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, sample_arxiv_article['authors'][0], html=True)
        self.assertContains(response, sample_arxiv_article['arxiv_comment'], html=True)
        self.assertContains(response, sample_arxiv_article['title'], html=True)

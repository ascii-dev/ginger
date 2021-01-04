from unittest.mock import patch
from django.urls import reverse
from django.test import Client, TestCase


class SignupTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()

    def test_get_signup_page_succeeds(self):
        """
        Tests that we can successfully get the signup page to display
        :return:
        """
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create account', html=True)

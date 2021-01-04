from django.urls import reverse
from django.test import Client, TestCase


class LoginTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()

    def test_get_login_page_succeeds(self):
        """
        Tests that we can successfully get the login page to display
        """
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login', html=True)

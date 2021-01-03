from django.urls import reverse
from django.test import Client, TestCase


class GetSignupTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()

    def test_get_login_page_succeeds(self):
        """
        Tests that we can successfully get the login page to display
        :return:
        """
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed('registration/signup.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create account', html=True)

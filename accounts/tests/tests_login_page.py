from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client, TestCase


class GetLoginTests(TestCase):
    def setUp(self) -> None:
        """
        Sets up data needed for successful test runs
        """
        self.client = Client()
        self.user = get_user_model().objects.create(
            username='some_user',
            email='some_user@user.com',
            password='password123')

    def test_get_login_page_succeeds(self):
        """
        Tests that we can successfully get the login page to display
        """
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login', html=True)

    def test_login_action_succeeds(self):
        """
        Tests that the process of logging in is successful
        """
        response = self.client.post('login', {
            'username': self.user.username,
            'password': self.user.password})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Log out' in response.content)

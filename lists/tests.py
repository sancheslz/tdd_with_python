from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
        self.assertIn('To-Do lists', response.content.decode('utf-8'))

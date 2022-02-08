import baker as baker
from django.test import TestCase
from django.http import response
from django.urls.base import reverse

from .models import Watch
from django.contrib.auth.models import User

# Create your tests here.

class WatchViewTest(TestCase):
    def test_suggestion_view_with_no_suggestion(self):

        self.user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.get(reverse('blog:suggestionWatch'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['sugg_watch'], [])


from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from core.models import Newsletter

class NewsletterAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.newsletter = Newsletter.objects.create(email='test@example.com')

    def test_delete_newsletter(self):
        csrf_token = self.client.cookies['csrftoken'].value
        response = self.client.delete(
            f'/api/v1/newsletters/{self.newsletter.id}/',
            HTTP_X_CSRFTOKEN=csrf_token
        )
        self.assertEqual(response.status_code, 204)

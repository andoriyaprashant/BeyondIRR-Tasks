from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword")
        self.login_url = reverse('login') 
        self.protected_url = reverse('protected')  

    def test_login_success(self):
        data = {"email": "test@example.com", "password": "testpassword"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_failure(self):
        data = {"email": "wrong@example.com", "password": "wrongpassword"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_protected_view(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "This is a protected view only accessible to authenticated users."})

    def test_protected_view_without_token(self):
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


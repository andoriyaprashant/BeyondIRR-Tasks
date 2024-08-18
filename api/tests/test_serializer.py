from django.test import TestCase
from api.models import User
from api.serializer import UserSerializer, LoginSerializer

class UserSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword", arn_number="1234567890")

    def test_user_serializer(self):
        serializer = UserSerializer(self.user)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['email', 'arn_number', 'is_verified']))
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['arn_number'], self.user.arn_number)
        self.assertFalse(data['is_verified'])

class LoginSerializerTest(TestCase):

    def test_login_serializer(self):
        serializer = LoginSerializer(data={"email": "test@example.com", "password": "testpassword"})
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['email'], "test@example.com")

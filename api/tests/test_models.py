from django.test import TestCase
from api.models import User

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword", arn_number="1234567890")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertEqual(self.user.arn_number, "1234567890")

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.email)

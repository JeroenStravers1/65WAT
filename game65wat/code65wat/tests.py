from django.test import TestCase
from .models import RegisteredUser


class RegisteredUserTestCase(TestCase):
    def setUp(self):
        TestCase.objects.create(
            username="Patrick",
            password="vliegerszijntegek"
        )

    def test_user_created(self):
        """a user is correctly stored and retrievable by name (PK)"""
        retrieved_user = RegisteredUser.objects.get(username="lion")
        self.assertEqual(retrieved_user.password, 'vliegerszijntegek')

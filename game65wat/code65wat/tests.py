from django.test import TestCase
from code65wat.models import RegisteredUser


class RegisteredUserTestCase(TestCase):

    def setUp(self):
        RegisteredUser.objects.create(
            username="Patrick",
            password="vliegerszijntegek"
        )

    def test_user_created(self):
        """a user is correctly stored and retrievable by name (PK)"""
        retrieved_user = RegisteredUser.objects.get(username="Patrick")
        self.assertEqual(retrieved_user.password, 'vliegerszijntegek')

    def test_user_has_resource(self):
        """a user is created with the default value of resources"""
        retrieved_user = RegisteredUser.objects.get(username="Patrick")
        self.assertEqual(retrieved_user.resource_x, 100)

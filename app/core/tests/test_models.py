from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Leírás:  """
    def test_create_user_with_email_succesful(self, ):
        """ Leírás: Test creating a new user with an email is successful """
        email = 'test@tes.hu'
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self, ):
        """ Leírás: Test the email for a new user is normalized """
        email = "test@TEst.Te"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self, ):
        """ Leírás: Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self, ):
        """ Leírás: Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@teszt.hu',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

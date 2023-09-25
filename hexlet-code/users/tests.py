from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class UserCreateTestCase(TransactionTestCase):
    def test_registration(self):
        response = self.client.post(
            reverse("users:create"),
            {"first_name": "some",
             "last_name": "name",
             "username": "some_name",
             "email": "some@email.com",
             "password1": "string123",
             "password2": "string123"}
        )
        self.assertEqual(response.status_code, 301)
        assert User.objects.get(username="some_name")


class UserDeleteTestCase(TransactionTestCase):
    def setUp(self):
        User.objects.create_user(
            username="foo",
            email="foo@bar.com",
            password="string123",
        )

    def test_user_delete(self):
        response = self.client.post(reverse("users:delete", args=[1]))
        self.assertEqual(response.status_code, 302)


class UserUpdateTestCase(TransactionTestCase):
    def setUp(self):
        User.objects.create_user(
            username="foo",
            email="foo@bar.com",
            password="string123",
        )

    def test_user_update(self):
        response = self.client.post(reverse("users:update", args=[1]),
                                    {"first_name": "foo",
                                     "last_name": "bar",
                                     "username": "foobar",
                                     "email": "bar@foo.com",
                                     })
        self.assertEqual(response.status_code, 302)

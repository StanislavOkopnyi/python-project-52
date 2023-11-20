from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client

from .models import Task
from statuses.models import Status

User = get_user_model()


class TaskListTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test",
            password="string123",
        )
        status = Status.objects.create(name="test")
        Task.objects.create(
            name="foo",
            author=user,
            performer=user,
            status=status,
            text="test",
        )

    def test_list(self):
         response = self.client.get(
            reverse("tasks:list"))
         self.assertEqual(response.status_code, 200)




class TaskCreateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="string123",
        )
        self.status = Status.objects.create(name="test")

    def test_create(self):
        response = self.client.post(
            reverse("tasks:create"),
            {"name": "some",
             "author": self.user,
             "performer": self.user,
             "status": self.status,
             "text": "test",}
        )
        self.assertEqual(response.status_code, 302)


class TaskDeleteTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test",
            password="string123",
        )
        self.another_user = User.objects.create_user(
            username="test2",
            password="string123",
        )
        status = Status.objects.create(name="test")
        Task.objects.create(
            name="foo",
            author=user,
            performer=user,
            status=status,
            text="test",
        )

    def test_delete(self):
        response = self.client.post(reverse("tasks:delete", args=[1]))
        self.assertEqual(response.status_code, 302)

    def task_delete_by_another_user(self):
        client = Client()
        client.force_login(self.another_user)
        response = client.post(reverse("tasks:delete", args=[1]))
        self.assertEqual(response.status_code, 403)


class TaskesUpdateTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test",
            password="string123",
        )
        status = Status.objects.create(name="test")
        Task.objects.create(
            name="foo",
            author=user,
            performer=user,
            status=status,
            text="test",
        )

    def test_user_update(self):
        response = self.client.post(reverse("tasks:update", args=[1]),
                                    {"name": "bar"})
        self.assertEqual(response.status_code, 302)

# Create your tests here.

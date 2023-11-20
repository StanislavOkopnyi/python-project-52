from django.test import TestCase
from django.urls import reverse
from .models import Status


class StatusListView(TestCase):
    def setUp(self):
        Status.objects.create(name="foo")
        Status.objects.create(name="bar")
        Status.objects.create(name="xyz")

    def test_list(self):
        response = self.client.get(reverse("statuses:list"))
        self.assertEqual(response.status_code, 200)



class StatusCreateTestCase(TestCase):
    def test_create(self):
        response = self.client.post(
            reverse("statuses:create"),
            {"name": "some"}
        )
        self.assertEqual(response.status_code, 302)


class StatusDeleteTestCase(TestCase):
    def setUp(self):
        Status.objects.create(name="foo")

    def test_delete(self):
        response = self.client.post(reverse("statuses:delete", args=[1]))
        self.assertEqual(response.status_code, 302)


class StatusesUpdateTestCase(TestCase):
    def setUp(self):
        Status.objects.create(
            name="foo",
        )

    def test_user_update(self):
        response = self.client.post(reverse("statuses:update", args=[1]),
                                    {"name": "bar"})
        self.assertEqual(response.status_code, 302)

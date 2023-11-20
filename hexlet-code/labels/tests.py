from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Label

User = get_user_model()


class LabelListView(TestCase):
    def setUp(self):
        Label.objects.create(name="foo")
        Label.objects.create(name="bar")
        Label.objects.create(name="xyz")

    def test_list(self):
        response = self.client.get(reverse("labels:list"))
        self.assertEqual(response.status_code, 200)



class LabelCreateTestCase(TestCase):

    def test_create(self):
        response = self.client.post(
            reverse("labels:create"),
            {"name": "some"}
        )
        self.assertEqual(response.status_code, 302)


class LabelDeleteTestCase(TestCase):
    def setUp(self):
        Label.objects.create(name="foo")

    def test_delete(self):
        response = self.client.post(reverse("labels:delete", args=[1]))
        self.assertEqual(response.status_code, 302)


class LabelesUpdateTestCase(TestCase):
    def setUp(self):
        Label.objects.create(name="foo")

    def test_user_update(self):
        response = self.client.post(reverse("labels:update", args=[1]),
                                    {"name": "bar"})
        self.assertEqual(response.status_code, 302)


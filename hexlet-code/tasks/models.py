from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from statuses.models import Status
from labels.models import Label

User = get_user_model()


class Task(models.Model):

    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="created_tasks")
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    performer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="todo_tasks")
    labels = models.ManyToManyField(Label)
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

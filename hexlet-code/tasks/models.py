from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from statuses.models import Status
from labels.models import Label

User = get_user_model()


class Task(models.Model):

    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="created_tasks", verbose_name=_("author"))
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, verbose_name=_("status"))
    performer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="todo_tasks", verbose_name=_("performer"))
    labels = models.ManyToManyField(Label, verbose_name=_("labels"))
    name = models.CharField(max_length=255, verbose_name=_("name"))
    text = models.TextField(verbose_name=_("text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

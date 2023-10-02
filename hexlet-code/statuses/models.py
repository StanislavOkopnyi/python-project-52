from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("name"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))

    class Meta:
        verbose_name = _("status")
        verbose_name_plural = _("statuses")

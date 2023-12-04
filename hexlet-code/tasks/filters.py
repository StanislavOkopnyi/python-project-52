from django.forms import Form
import django_filters

from .models import Task

class TaskFilterForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        form = TaskFilterForm
        fields = ("status", "performer", "labels")

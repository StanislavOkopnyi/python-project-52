from django.forms import ModelForm, ModelMultipleChoiceField

from .models import Task


class TaskCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = Task
        exclude = ["author"]

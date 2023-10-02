from django.forms import ModelForm

from .models import Status


class StatusCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = Status
        fields = "__all__"


class StatusUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = Status
        fields = ["name", ]

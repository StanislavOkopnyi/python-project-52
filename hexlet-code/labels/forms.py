from django.forms import ModelForm

from .models import Label


class LabelCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = Label
        fields = ["name", ]


class LabelUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = Label
        fields = ["name", ]

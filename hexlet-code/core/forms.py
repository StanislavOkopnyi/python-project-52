from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm


class AuthenticationForm(DjangoAuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

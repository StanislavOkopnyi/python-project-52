from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class UserUpdateForm(UserChangeForm):
    password = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control py-2'

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ["first_name", "last_name", "username", "email"]

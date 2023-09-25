from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout

from .forms import AuthenticationForm


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(DjangoLoginView):
    form_class = AuthenticationForm
    template_name = "login.html"


class LogoutView(DjangoLogoutView):
    http_method_names = ["get", "options"]

    def get(self, request):
        """Logout may be done via GET."""
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import redirect, reverse, render
from django.forms.models import model_to_dict

from .forms import UserCreateForm, UserUpdateForm


User = get_user_model()


class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "users/index.html"


class UserCreateView(TemplateView):
    template_name = "users/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserCreateForm
        return context

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"), permanent=True)
        return render(request, self.template_name, context={"form": form})


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "users/update.html"

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        form = UserUpdateForm(model_to_dict(user))
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse("users:list"), permanent=True)
        return render(request, self.template_name, context={"form": form})


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "users/delete.html"

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(reverse("users:list"), permanent=True)

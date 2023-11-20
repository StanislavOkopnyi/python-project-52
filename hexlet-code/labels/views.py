from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from .forms import LabelCreateForm, LabelUpdateForm
from .models import Label


class LabelListView(ListView):
    model = Label
    context_object_name = "labels"
    template_name = "labels/index.html"


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "labels/create.html"
    form_class = LabelCreateForm
    success_url = reverse_lazy('labels:list')
    success_message = _("Label was created successfully")


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = LabelUpdateForm
    template_name = "labels/update.html"
    success_url = reverse_lazy('labels:list')
    success_message = _("Label was updated successfully")
    model = Label


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy('labels:list')
    success_message = _("Label was deleted successfully")

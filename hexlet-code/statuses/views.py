from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from .forms import StatusCreateForm, StatusUpdateForm
from .models import Status


class StatusListView(ListView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/index.html"


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "statuses/create.html"
    form_class = StatusCreateForm
    success_url = reverse_lazy('statuses:list')
    success_message = _("Status was created successfully")


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = StatusUpdateForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy('statuses:list')
    success_message = _("Status was updated successfully")
    model = Status


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "statuses/delete.html"
    success_url = reverse_lazy('statuses:list')
    success_message = _("Status was deleted successfully")

from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from .filters import TaskFilter
from .forms import TaskCreateForm, TaskUpdateForm
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        filter = TaskFilter(self.request.GET, queryset=Task.objects.all())
        data["filter"] = filter
        return data


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task.html"


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "tasks/create.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks:list')
    success_message = _("Task was created successfully")


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = TaskUpdateForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy('tasks:list')
    success_message = _("Task was updated successfully")
    model = Task


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy('tasks:list')
    success_message = _("Task was deleted successfully")

    def test_func(self):
        return self.request.user == self.get_object().author

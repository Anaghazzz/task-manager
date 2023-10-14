from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TaskApp
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = TaskApp
    template_name = 'task/list.html'
    context_object_name = 'tasks'
    ordering = ['due_date']

class TaskDetailView(DetailView):
    model = TaskApp
    template_name = 'task/detail.html'

class TaskCreateView(CreateView):
    model = TaskApp
    template_name = 'task/form.html'
    fields = ['title', 'description', 'due_date', 'priority']
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = TaskApp
    template_name = 'task/form.html'
    fields = ['title', 'description', 'due_date', 'priority']
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = TaskApp
    template_name = 'task/confirm_delete.html'
    success_url = reverse_lazy('task-list')
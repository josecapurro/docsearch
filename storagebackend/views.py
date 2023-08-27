from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
import django_tables2 as tables
from django_tables2.config import RequestConfig
from django.conf import settings
from .models import StorageBackend
from .tables import StorageBackendTable
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

__all__ = (
        'StorageBackendListView',
        'StorageBackendCreateView',
        'StorageBackendUpdateView',
        'StorageBackendDelete',
        )

class StorageBackendListView(LoginRequiredMixin, ListView):
    model = StorageBackend.objects.all()
    template_name = 'list.html'
    table = StorageBackendTable(model)

    def get(self, request):
        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table, 'model': self.model, })

class StorageBackendCreateView(LoginRequiredMixin, CreateView):
    model = StorageBackend
    template_name = 'new.html'
    fields = ['name', 'description', 'kind', 'url', 'active']
    success_url = reverse_lazy('storagebackend')

class StorageBackendUpdateView(LoginRequiredMixin, UpdateView):
    model = StorageBackend
    template_name = 'update.html'
    fields = ['name', 'description', 'kind', 'url', 'active']
    success_url = reverse_lazy('storagebackend')

class StorageBackendDeleteView(LoginRequiredMixin, DeleteView):
    model = StorageBackend
    template_name = 'delete.html'
    success_url = reverse_lazy('storagebackend')

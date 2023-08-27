from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
import django_tables2 as tables
from django_tables2.config import RequestConfig
from django.conf import settings
from .models import SearchBackend
from .tables import SearchBackendTable
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

__all__ = (
        'SearchBackendListView',
        'SearchBackendCreateView',
        )

class SearchBackendListView(LoginRequiredMixin, ListView):
    model = SearchBackend.objects.all()
    template_name = 'list.html'
    table = SearchBackendTable(model)

    def get(self, request):
        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table, 'model': self.model, })

class SearchBackendCreateView(LoginRequiredMixin, CreateView):
    model = SearchBackend
    template_name = 'new.html'
    fields = ['name', 'description', 'host', 'port', 'user', 'password', 'active']
    success_url = reverse_lazy('searchbackend')

class SearchBackendUpdateView(LoginRequiredMixin, UpdateView):
    model = SearchBackend
    template_name = 'update.html'
    fields = ['name', 'description', 'host', 'port', 'user', 'password', 'active']
    success_url = reverse_lazy('searchbackend')

class SearchBackendDeleteView(LoginRequiredMixin, DeleteView):
    model = SearchBackend
    template_name = 'delete.html'
    success_url = reverse_lazy('searchbackend')

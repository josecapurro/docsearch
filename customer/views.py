from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
import django_tables2 as tables
from django_tables2.config import RequestConfig
from django.conf import settings
from .models import Customer
from .tables import CustomerTable
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

__all__ = (
        'CustomerListView',
        'CustomerCreateView',
        'CustomerUpdateView',
        'CustomerDeleteView',
        )

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer.objects.all()
    template_name = 'list.html'
    table = CustomerTable(model)

    def get(self, request):
        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table, 'model': self.model, })

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'new.html'
    fields = ['name',
            'description',
            'storagebackend',
            'storagebackend_user',
            'storagebackend_password',
            'searchbackend',
            'active']
    success_url = reverse_lazy('customer')

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'update.html'
    fields = ['name',
            'description',
            'storagebackend',
            'storagebackend_user',
            'storagebackend_password',
            'searchbackend',
            'active']
    success_url = reverse_lazy('customer')

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'delete.html'
    success_url = reverse_lazy('customer')

from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
import django_tables2 as tables
from django_tables2.config import RequestConfig
from django.conf import settings
from .models import Account
from .tables import AccountTable
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

__all__ = (
        'AccountListView',
        'AccountCreateView',
        'AccountUpdateView',
        'AccountDeleteView',
        'AccountLoginView',
        'AccountLogoutView',
        )

class AccountListView(LoginRequiredMixin, ListView):
    model = Account.objects.all()
    template_name = 'list.html'
    table = AccountTable(model)

    def get(self, request):
        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table, 'model': self.model, })

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = 'new.html'
    fields = ['user', 'customer', 'active']
    success_url = reverse_lazy('account')

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'update.html'
    fields = ['user', 'customer', 'active']
    success_url = reverse_lazy('account')

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'delete.html'
    success_url = reverse_lazy('account')

class AccountLoginView(LoginView):
    template_name = 'login.html'

class AccountLogoutView(LogoutView):
    template_name = 'logout.html'

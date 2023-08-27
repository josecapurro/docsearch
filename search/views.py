from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import View
import django_tables2 as tables
from django_tables2.config import RequestConfig
from django.conf import settings
from .tables import SearchTable
from utils.utils import docsearch as Search
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

__all__ = (
        'SearchView',
        )


class SearchView(LoginRequiredMixin, View):
    data = Search()
    template_name = 'search.html'
    table = SearchTable(data)

    def get(self, request):
        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table, 'data': self.data, })

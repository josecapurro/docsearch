from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import FormView
from django_tables2.config import RequestConfig
from django.conf import settings
from .tables import SearchTable
from .forms import UploadFileForm
from utils.utils import docsearch as Search
from utils.utils import file_upload as Upload
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
import django_tables2 as tables

# Create your views here.

__all__ = (
        'SearchView',
        'SearchUploadView',
        )


class SearchView(LoginRequiredMixin, View):
    data = Search()
    template_name = 'search.html'
    table = SearchTable(data)

    def get(self, request):
        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table, 'data': self.data, })

class SearchUploadView(LoginRequiredMixin, View):
    form_class = UploadFileForm
    success_url = reverse_lazy('search')
    template_name = 'upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            Upload(request.FILES["file"])
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

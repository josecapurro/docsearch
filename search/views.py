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

    def get(self, request):
        template_name = 'search.html'
        #RequestConfig(request).configure(self.table)
        #return render(request, self.template_name, {'table': self.table, 'data': self.data, })
        return render(request, template_name)

    def post(self, request):
        data = Search()
        table = SearchTable(data)
        template_name = 'search_result.html'
        success_url = reverse_lazy('search')
        RequestConfig(request).configure(table)
        return render(request, template_name, {'table': table, 'data': data, })

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

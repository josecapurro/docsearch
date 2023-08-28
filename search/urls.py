from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import SearchView, SearchUploadView

_patterns = [
        path('', SearchView.as_view(), name='search'),
        path('upload', SearchUploadView.as_view(), name='upload'),
        ]

urlpatterns = [
        path('', include(_patterns)),
        ]

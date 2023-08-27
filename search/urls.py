from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import SearchView

_patterns = [
        path('', SearchView.as_view(), name='search'),
        ]

urlpatterns = [
        path('', include(_patterns)),
        ]

from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import SearchBackendListView, SearchBackendCreateView, SearchBackendUpdateView, SearchBackendDeleteView

_patterns = [
        path('', SearchBackendListView.as_view(), name='searchbackend'),
        path('new', SearchBackendCreateView.as_view(), name='new'),
        path('edit/<int:pk>', SearchBackendUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>', SearchBackendDeleteView.as_view(), name='delete'),
        ]

urlpatterns = [
        path('', include(_patterns)),
        ]

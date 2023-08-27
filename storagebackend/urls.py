from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import StorageBackendListView, StorageBackendCreateView, StorageBackendUpdateView, StorageBackendDeleteView

_patterns = [
        path('', StorageBackendListView.as_view(), name='storagebackend'),
        path('new', StorageBackendCreateView.as_view(), name='new'),
        path('edit/<int:pk>', StorageBackendUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>', StorageBackendDeleteView.as_view(), name='delete'),
        ]

urlpatterns = [
        path('', include(_patterns)),
        ]

from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

_patterns = [
        path('', CustomerListView.as_view(), name='customer'),
        path('new', CustomerCreateView.as_view(), name='new'),
        path('edit/<int:pk>', CustomerUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>', CustomerDeleteView.as_view(), name='delete'),
        ]

urlpatterns = [
        path('', include(_patterns)),
        ]

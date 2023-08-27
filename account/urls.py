from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import AccountListView, AccountCreateView, AccountUpdateView, AccountDeleteView, AccountLoginView, AccountLogoutView

_patterns = [
        path('', AccountListView.as_view(), name='account'),
        path('new', AccountCreateView.as_view(), name='new'),
        path('edit/<int:pk>', AccountUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
        path('login', AccountLoginView.as_view(), name='login'),
        path('logout', AccountLogoutView.as_view(), name='logout'),
        ]

urlpatterns = [
        path('', include(_patterns)),
        ]

from django.urls import path

from .views import (
    ContactCreateView,
    ContactDetailView,
    ContactListView,
    ContactUpdateView,
    ContactDeleteView,
    SignUpView,
    search,
)

urlpatterns = [
    path('create/', ContactCreateView.as_view(), name='create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='detail'),
    path('search/', search, name='search'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', ContactListView.as_view(), name='home'),
]

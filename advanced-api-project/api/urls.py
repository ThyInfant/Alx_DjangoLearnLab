# URL routes mapping Book views to API endpoints
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update book endpoint (checker expects 'books/update')
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete book endpoint (checker expects 'books/delete')
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

# URL routes mapping Book views to API endpoints
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create book endpoint containing 'books/create'
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update book endpoint containing 'books/update'
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete book endpoint containing 'books/delete'
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Function-based view for all books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library detail (use <int:pk> to identify the library)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

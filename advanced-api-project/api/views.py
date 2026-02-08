# DRF generic views with filtering, searching, and ordering for Book model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework

# List all books with advanced query capabilities
# filters.OrderingFilter allows clients to specify the ordering of results using query parameters
# filters.SearchFilter enables text search on specified fields using the 'search' query parameter
# "DetailView", "CreateView", "UpdateView", "DeleteView" are used for retrieving, creating, updating, and deleting individual book instances respectively
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering by specific fields
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author']

    # Enable text search on title and author's name
    search_fields = ['title', 'author__name']

    # Allow ordering by selected fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

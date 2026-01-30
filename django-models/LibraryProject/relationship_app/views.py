from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.urls import reverse_lazy
from .models import Book, Library


# ------------------------
# Book List View
# ------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ------------------------
# Library Detail View
# ------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ------------------------
# User Registration View (Class-Based)
# ------------------------
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'  # your signup template
    success_url = reverse_lazy('login')  # redirect to login after successful signup

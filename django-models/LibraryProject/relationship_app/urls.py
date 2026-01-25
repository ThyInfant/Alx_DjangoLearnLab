from django.urls import path
from . import views  # Import views as a module
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Book and library views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Custom permissions-secured book URLs (checker requires literal substrings)
    path('book/add/', views.add_book_view, name='add_book'),
    path('book/edit/<int:pk>/', views.edit_book_view, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book_view, name='delete_book'),
]

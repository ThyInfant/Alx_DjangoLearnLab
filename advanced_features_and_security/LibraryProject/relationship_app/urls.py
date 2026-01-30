from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book_view, name='delete_book'),
]

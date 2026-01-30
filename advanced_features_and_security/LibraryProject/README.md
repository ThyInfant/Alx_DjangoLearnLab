from django.urls import path
from . import views

urlpatterns = [
path('', views.book_list, name='book_list'),
path('create/', views.book_create, name='book_create'),
path('edit/<int:pk>/', views.book_edit, name='book_edit'),
path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]

SECURITY MEASURES IMPLEMENTED

1. SETTINGS HARDENING

- DEBUG disabled
- X_FRAME_OPTIONS set to DENY
- SECURE_BROWSER_XSS_FILTER enabled
- SECURE_CONTENT_TYPE_NOSNIFF enabled
- CSRF and session cookies restricted to HTTPS

2. CSRF PROTECTION

- All POST forms include {% csrf_token %}

3. SQL INJECTION PREVENTION

- All database access uses Django ORM
- No raw SQL string formatting
- Forms used for input validation

4. XSS PROTECTION

- Django auto-escaping used
- No unsafe template rendering

5. CONTENT SECURITY POLICY (CSP)

- django-csp middleware added
- Only same-origin scripts, styles, and images allowed

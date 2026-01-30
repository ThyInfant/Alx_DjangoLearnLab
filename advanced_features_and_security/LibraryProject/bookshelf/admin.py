from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
  model = CustomUser

  fieldsets = UserAdmin.fieldsets + (
    ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
  )

  add_fieldsets = UserAdmin.add_fieldsets + (
    ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
  )

  list_display = ('username', 'email', 'date_of_birth', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'published_date')
  list_filter = ('published_date', 'author')
  search_fields = ('title', 'author')

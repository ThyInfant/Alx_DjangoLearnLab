from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    ExampleForm is used to demonstrate secure form handling.
    It ensures user input is validated and protected against
    malicious data such as SQL injection or script injection.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

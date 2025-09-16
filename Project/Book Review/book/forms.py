from book.models import Book
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import RegexValidator



class BookForm(ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'Book Title'})
    )
    author = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'Author Name'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'Book Description', 'rows': 4})
    )
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'type': 'date'})
    )
    isbn = forms.CharField(
        max_length=13,
        validators=[RegexValidator(regex='^\d{10}(\d{3})?$', message='ISBN must be 10 or 13 digits')],
        widget=forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'ISBN Number'})
    )
    pages = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'Number of Pages'})
    )
    cover_image = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'Cover Image URL'})
    )
    language = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'border rounded px-3 py-2 w-full', 'placeholder': 'Language'})
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date', 'isbn', 'pages', 'cover_image', 'language']

        def clean_published_date(self):
            publised__date = self.cleaned_data.get('published_date')
            if publised__date > timezone.now().date():
                raise ValidationError("Published date cannot be in the future.")
            return publised__date
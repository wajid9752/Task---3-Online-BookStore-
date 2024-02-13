from django import forms
from .models import Book, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

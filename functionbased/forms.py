from django import forms
from classbased.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['order', 'title', 'author', 'price','slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
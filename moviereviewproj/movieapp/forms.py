from django import forms
from .models import Movie, Genre, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'
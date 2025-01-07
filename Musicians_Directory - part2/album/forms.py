from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            
            'title': 'Album Title',
            'artist': 'Artist Name',
            'release_date': 'Release Date',
            'rating': 'Rating',
        }
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
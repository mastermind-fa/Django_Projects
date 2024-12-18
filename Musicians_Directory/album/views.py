from django.shortcuts import render, redirect
from . import forms
from .models import Album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('add_album')
    else:
        form = forms.AlbumForm
    return render(request, 'album_form.html', {'form': form})


def edit(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save(commit=True)
            return redirect('homepage')
    else:
        form = forms.AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def delete(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('homepage')

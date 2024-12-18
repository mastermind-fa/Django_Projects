from django.shortcuts import render, redirect
from album.models import Album

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {'data': albums})
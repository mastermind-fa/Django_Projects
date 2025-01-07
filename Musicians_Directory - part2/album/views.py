from django.shortcuts import render, redirect
from . import forms
from .models import Album
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
# def add_album(request):
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('add_album')
#     else:
#         form = forms.AlbumForm
#     return render(request, 'album_form.html', {'form': form})


class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def edit(request, album_id):
#     album = Album.objects.get(id=album_id)
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('homepage')
#     else:
#         form = forms.AlbumForm(instance=album)
#     return render(request, 'album_form.html', {'form': form})


class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    
    
# def delete(request, album_id):
#     album = Album.objects.get(id=album_id)
#     album.delete()
#     return redirect('homepage')

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
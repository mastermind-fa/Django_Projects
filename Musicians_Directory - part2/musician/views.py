from django.shortcuts import render, redirect 
from . import forms
from .models import Musician
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
# def add_musician(request):
#     if request.method == 'POST':
#         form = forms.MusicianForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('add_musician')
#     else:
#         form = forms.MusicianForm()
#     return render(request, 'musician_form.html' , {'form': form})

class AddMusicianCreateView(CreateView):
    model = Musician
    form_class = forms.MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
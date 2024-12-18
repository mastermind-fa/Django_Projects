from django.shortcuts import render, redirect 
from . import forms

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('add_musician')
    else:
        form = forms.MusicianForm()
    return render(request, 'musician_form.html' , {'form': form})
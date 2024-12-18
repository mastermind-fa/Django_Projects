from django.shortcuts import render, redirect
from . import forms

def models(request):
    form = forms.myModelForm()
    return render(request, 'model.html', {'form': form})

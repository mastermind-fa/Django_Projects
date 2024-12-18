from django.shortcuts import render, redirect
from .forms import exampleForm

# Create your views here.
def forms(request):
    if request.method == 'POST':
        form = exampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('formpage')
    else:
        form = exampleForm()
    return render(request, 'form.html', {'form': form})

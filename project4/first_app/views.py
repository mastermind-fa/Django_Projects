from django.shortcuts import render
from first_app.forms import StudentForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        std = StudentForm(request.POST)
        if std.is_valid():
            std.save()
            print(std.cleaned_data)
            
    else:
        std = StudentForm()
    return render(request, 'first_app/home.html', {'form': std} )

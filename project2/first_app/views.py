from django.shortcuts import render
from . forms import contactForm,studentData,PasswordValidationProject

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        selected = request.POST.get('select')
        print('Form submitted')
        print(request.POST)
        return render(request, 'first_app/about.html', {'name': name, 'email': email, 'selected': selected})
    else:
        return render(request, 'first_app/about.html')
    #return render(request, 'first_app/about.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        print('Form submitted')
        print(request.POST)
        return render(request, 'first_app/form.html', {'name': name, 'email': email})
    return render(request, 'first_app/form.html')

def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    
        return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'first_app/django_form.html', {'form': form})

def studentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = studentData()
    return render(request, 'first_app/django_form.html', {'form': form})

def passwordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = PasswordValidationProject()
    return render(request, 'first_app/django_form.html', {'form': form})
    
    

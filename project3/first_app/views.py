from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
# def model_form(request):
#     return render(request,'first_app/model_form.html')
def home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request,'first_app/model_form.html', {'data':student})
def delete_student(request, roll):
    std = models.Student.objects.get(pk=roll).delete()
    student = models.Student.objects.all()
    print(student)
    # return render(request,'first_app/model_form.html', {'data':student})
    return redirect('home')
    

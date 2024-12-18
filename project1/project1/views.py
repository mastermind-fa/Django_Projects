from django.http import HttpResponse
from django.shortcuts import render
# def contact(request):
#     return HttpResponse('Contact page')

def home(request):
    return HttpResponse('Home page')

# def about(request):
#     return render(request,'app1/index.html')

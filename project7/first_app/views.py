from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse


def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'farhana')
    response.set_cookie('name', 'alam', expires=datetime.now() + timedelta(days=1))
    return response 

def get_cookie(request):
    name = request.COOKIES['name']
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {'name': 'farhana', 'age': 25, 'city': 'Dhaka'}
    request.session.update(data)
    return render(request, 'home.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'guest')
        request.session.modified = True
    
        return render(request, 'get_session.html', {'name': name})
    else:
        return HttpResponse('Session not found')
        

def delete_session(request):
    request.session.flush()
    
    return render(request, 'del.html')
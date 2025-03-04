from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            
            form.save(commit=True)
            print(form.cleaned_data)
    else:       
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST, request=request)
            if form.is_valid():
                name = form.cleaned_data.get('username')
                userpass = form.cleaned_data.get('password')
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in succesfully')
                    return redirect('profile')
    
            
            
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
       return redirect('profile') 
        
def profile(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account update successfully')
                
                form.save(commit=True)
                print(form.cleaned_data)
        else:       
            form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup') 

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

def password_reset(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'password_reset.html', {'form': form})
    else:
        redirect('login')

def password_reset2(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'password_reset2.html', {'form': form})
    else:
        redirect('login')
        
def change_user_data(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account update successfully')
                
                form.save(commit=True)
                print(form.cleaned_data)
        else:       
            form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')

def index(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('login')
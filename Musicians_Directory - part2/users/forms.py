from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'
        
class RegistrationForm(UserCreationForm):
        
    
    class Meta:
        model = User
        fields = [
            'username',
            
            
            'password1',
            'password2'
        ]
        
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'username',
            
        ]
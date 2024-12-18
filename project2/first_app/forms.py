from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label='Your Name', initial="Farhana", help_text="You must have to have a name", max_length=100, required=False)
    email = forms.EmailField(label='Your Email', max_length=100)
    age = forms.IntegerField(label='Your Age')
    weight = forms.FloatField(label='Your Weight')
    balance = forms.DecimalField(label='Your Balance')
    check = forms.BooleanField(label='Check this box')
    birthday = forms.DateField(label='Your Birthday', widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(label='Your Appointment', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    url = forms.URLField(label='Your URL')
    CHOICES = [('S', 'small'), ('M', 'medium'), ('L', 'large')]
    size = forms.ChoiceField(label='Size', choices=CHOICES, widget=forms.RadioSelect)
    choose = [('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('mush', 'Mushrooms')]
    pizza = forms.MultipleChoiceField(label='Pizza', choices=choose, widget=forms.CheckboxSelectMultiple)
    file = forms.FileField(label='File', required=False)
    
    
    
    
    
    # Add this line to the file
    
    
    
class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10, message='Name has to be less than 10 characters')])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Email has to be gmail.com')])
    age =forms.IntegerField(widget=forms.NumberInput, validators=[validators.MinValueValidator(18,message="age must be 18"), validators.MaxValueValidator(30, message="age must be less than 30")])
    file = forms.FileField(widget=forms.FileInput, validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'], message='File must be pdf or docx')], required=False)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name has to be more than 10 characters')
    #     return valname
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not 'gmail.com' in email:
    #         raise forms.ValidationError('Email has to be gmail.com')
    #     return email
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name has to be more than 10 characters')
    #         return valname
    #     if not 'gmail.com' in email:
    #         raise forms.ValidationError('Email has to be gmail.com')
    #         return email
# Compare this snippet from first_app/forms.py:

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password does not match')
        return cleaned_data
        
        
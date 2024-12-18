from django import forms
from . import models
class myModelForm(forms.ModelForm):
    class Meta:
        model = models.myModel
        fields = '__all__'
        labels = {
            'name': 'Name',
            'age': 'Age',
            'check_field': 'Check',
            'date_field': 'Date Field',
            'datetime_field': 'Datetime Field',
            'email': 'Email',
        }
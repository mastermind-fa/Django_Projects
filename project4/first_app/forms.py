from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {'roll': 'Roll No', 'name': 'Name', 'address': 'Address'}
        widgets = {
            'name' : forms.TextInput(),
            'roll' : forms.NumberInput(),
        }
        help_texts = {
            'roll': 'Enter your roll number',
            'name': 'Enter your name',
            'address': 'Enter your address',
        }
        error_messages = {
            'name': {
                'required': 'Name field is required'
            }
        }
    
print(StudentForm.Meta.widgets)
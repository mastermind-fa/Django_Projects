from django.urls import path
from . import views

urlpatterns = [
    
    #path('model/',views.model_form,name='model_form'),
    path('',views.home,name='home'),
    path('delete/<int:roll>/',views.delete_student,name='delete_student'),
]
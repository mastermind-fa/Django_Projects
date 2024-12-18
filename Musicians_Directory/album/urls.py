from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    
    path('edit/<int:album_id>/', views.edit, name='edit'),
    path('delete/<int:album_id>/', views.delete, name='delete'),
]

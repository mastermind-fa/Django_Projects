from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddAlbumCreateView.as_view(), name='add_album'),
    
    path('edit/<int:album_id>/', views.EditAlbumView.as_view(), name='edit'),
    path('delete/<int:album_id>/', views.DeleteAlbumView.as_view(), name='delete'),
]

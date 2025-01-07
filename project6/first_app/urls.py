from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset2/', views.password_reset2, name='password_reset2'),
    path('change_user_data/', views.change_user_data, name='change_user_data'),
]

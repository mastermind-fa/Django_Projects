from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('brand/<slug:brand_slug>/', views.home, name='brand_wise_post'),
    
    path('buy/<int:pk>/', views.buy_car, name='buy-car'),
]

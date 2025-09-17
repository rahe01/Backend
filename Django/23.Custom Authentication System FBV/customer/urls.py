
from django.urls import path 
from . import views

urlpatterns = [
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('password-change/', views.password_change, name='password_change'),
 
]


from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('register/' , views.register , name='register'),
    path('login/' , views.login , name='login'),
    path('password_reset/' , views.password_reset , name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/' , views.password_reset_confirm , name='password_reset_confirm'),
]

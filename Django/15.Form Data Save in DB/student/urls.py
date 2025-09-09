
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home),
    path('regi/' , views.regi),
    path('success/' , views.reg_success)
    
]


from django.urls import path 
from . import views
urlpatterns = [
   path('' , views.home , name='home'),
   path('regi/' , views.regi, name='registation'),
   path('login/' , views.login)
]

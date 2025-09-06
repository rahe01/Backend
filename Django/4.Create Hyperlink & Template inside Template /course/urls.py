from django.urls import path  
from . import views

urlpatterns = [
    path('django/' , views.django , name='dj' ),
    path('python/', views.pythonn , name='py')
   

]
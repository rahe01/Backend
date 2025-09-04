from django.urls import path

from . import views 


urlpatterns = [
    path('' , views.home),
    path('django' , views.learn_django)
    
]

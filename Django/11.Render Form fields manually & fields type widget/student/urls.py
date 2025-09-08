
from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.home, name='home'),
    path('regi/' , views.regi),
    path('form/' , views.form)
]

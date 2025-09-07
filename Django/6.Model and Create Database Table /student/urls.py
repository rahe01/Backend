
from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.home, name='home'),
    path('all/', views.student_data, name='students'),
     path('single/', views.single_student_data, name='student')
]

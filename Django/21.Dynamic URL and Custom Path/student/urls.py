from django.urls import path , register_converter
from . import views
from student.converters import  FourDigitYearConverter

register_converter(FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('', views.home , name='home'),
    # path('profile/<int:id>' , views.profile , name='profile'),
    # path('profile/<slug:title>' , views.profile , name='profile'),
    # path('profile/<str:title>' , views.profile , name='profile')
     path('profile/<yyyy:year>' , views.profile , name='profile'),

]

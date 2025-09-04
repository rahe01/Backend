from django.urls import path

from . import views 


urlpatterns = [
    path('' , views.home),
    path('app1/' , views.myapp1 )
]

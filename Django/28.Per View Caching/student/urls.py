from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('result/',  cache_page(20)(views.result), name='result'),
]
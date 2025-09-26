from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set/' , views.set_cookie, name='set_cookie'),
    path('get/' , views.get_cookie, name='get_cookie'),
    path('delete/' , views.delete_cookie, name='delete_cookie'),
    path('setsigned/' , views.set_signed_cookie, name='set_signed_cookie'),
    path('getsigned/' , views.get_signed_cookie, name='get_signed_cookie'),

]
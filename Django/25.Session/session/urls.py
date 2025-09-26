from django.urls import path
from . import views

urlpatterns = [
    path('set/' , views.setsession, name='setsession'),
    path('get/' , views.getsession, name='getsession'),
    path('del/' , views.delsession, name='delsession'),
    path('flush/' , views.flushsession, name='flushsession'),
    path('inview/' , views.sessionmethodview, name='sessionmethodview'),
    path('clear/' , views.sessionclear, name='sessionclear'),
    path('intemplate/' , views.sessionmethodintemplate, name='sessionmethodintemplate'),
    path
]
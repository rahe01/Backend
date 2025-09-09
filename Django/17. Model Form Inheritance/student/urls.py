
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home),
    path('regi/' , views.student_form_view),
    path('tregi/' ,views.teacher_form_view)
    

]

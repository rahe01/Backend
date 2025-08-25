from django.urls import path
from .import views


urlpatterns = [
    path('',views.home),
    path('about/' , views.about),
    path('hire/' , views.hire),
    path('project/' , views.project),
    path('testimonial/' , views.testimonial),
    

]
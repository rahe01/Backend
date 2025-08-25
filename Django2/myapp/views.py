from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls page.")

def hire(request):

    return render(request, 'hire.html')
def about(request):

    return render(request, 'about.html')

def project(request):

    return render(request, 'projects.html')

def testimonial(request):

    return render(request, 'testimonial.html')
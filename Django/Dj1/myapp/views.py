from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return HttpResponse("Hello")

def myapp1(request):

    return HttpResponse("My app 1")
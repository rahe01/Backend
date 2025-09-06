from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def django(req):

    return render(req, 'course/django.html' , {'name':'rahe'})


def pythonn(req):

    return render(req, 'course/python.html')
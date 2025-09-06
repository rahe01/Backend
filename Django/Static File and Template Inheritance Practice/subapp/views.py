from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def subhome(req):

    return HttpResponse("Hello world from sub app")


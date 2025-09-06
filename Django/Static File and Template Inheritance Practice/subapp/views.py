from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def subhome(req):

    return render(req, 'sub1.html')


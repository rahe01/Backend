from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from student.forms import Registation , FormField



def home(req):
    
    return HttpResponse("This is home page")



def regi(req):

    fm = Registation(auto_id=True)

    return render(req, 'regi.html' , {'form':fm})


def form(req):

    fm = FormField()

    return render(req , 'form.html' , {'form':fm})


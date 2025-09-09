from django.shortcuts import render
from django.http import HttpResponse
from student.forms import Registation
from django.http import HttpResponseRedirect
from student.models import Profile


# Create your views here.


def home(req):

    return HttpResponse("Home page")



def regi(req):

    if req.method == 'POST':
        # print(req.POST['name'])
        # print(req.POST['email'])
        # print(req.POST['password'])
        form = Registation(req.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            c_p= form.cleaned_data['confirm_pass']
            pr =Profile(name= name,email= email,password = password)
            pr.save()

            print(name)
            print(email)
            print(password)
            print(c_p)
            return HttpResponseRedirect('/success/')

    else :
        form = Registation()

    return render(req, 'student/regi.html' , {'form':form})




def reg_success(req):

    return render(req, 'student/success.html')

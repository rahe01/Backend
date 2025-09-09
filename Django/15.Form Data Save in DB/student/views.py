from django.shortcuts import render
from django.http import HttpResponse
from student.forms import Registation
from django.http import HttpResponseRedirect
from student.models import UserProfile


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

            # save data in Db
            # user =UserProfile(name = name, email= email, password = password)
            # user.save()

             # update data in Db
            user =UserProfile(id=1,name = name, email= email, password = password)
            user.save()

             # delete data in Db
            user =UserProfile(id=1)
            user.delete()

           
            return HttpResponseRedirect('/regi/')

    else :
        form = Registation()

    return render(req, 'student/regi.html' , {'form':form})




def reg_success(req):

    return render(req, 'student/success.html')

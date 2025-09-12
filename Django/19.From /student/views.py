from django.shortcuts import render , redirect
from django.http import HttpResponse
from student.forms import ProfileForm
# Create your views here.
from student.models import Profile


def home(req):
    candidate = Profile.objects.all()

    if req.method == 'POST':
        form = ProfileForm(req.POST , req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors) 

    else:
     form = ProfileForm()

    return render(req , 'home.html',{'form':form , 'candidate': candidate})




def candi_detail(req , pk):
   
   candi = Profile.objects.get(pk=pk)
   
   return render(req, 'candidate.html' , {'candi':candi})
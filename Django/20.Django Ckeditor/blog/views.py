from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import CreatePostForm
# Create your views here.



def home(req):

    form = CreatePostForm()



    return render(req, 'home.html' , {'form':form})

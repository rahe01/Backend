from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'account/home.html')



def register(req):
    return render(req, 'account/register.html')


def login(req):
    return render(req, 'account/login.html')


def password_reset(req):
    return render(req, 'account/password_reset.html')
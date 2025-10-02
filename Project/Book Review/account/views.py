from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request, 'account/signup.html')

def signin(request):
    return render(request, 'account/signin.html')
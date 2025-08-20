from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls page.")



def profile(request):
    return HttpResponse("Hello, Profile")


def about(request):

    return render(request, 'about.html')
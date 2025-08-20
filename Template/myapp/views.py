from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls page.")

def about(request):

    data = {
        'title': 'Welcome to Django templates context feature',
        'word' : 'hello World',
        'sentence' : 'The quick brown fox jumps over the lazy dog',
        'number' : 123454545.56,
        'my_list' : [1,2,3,4,5,6]
    }
    return render(request, 'about.html', data)
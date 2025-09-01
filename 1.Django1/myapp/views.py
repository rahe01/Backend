from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime , timedelta

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls page.")

def about(request):

    data = {
        'title': 'Welcome to Django templates context feature',
        'word' : 'hello World',
        'sentence' : 'The quick brown fox jumps over the lazy dog',
        'number' : 123454545.56,
        'my_list' : [1,2,3,4,5,6],
        'my_date' : datetime.now(),
        'my_string' : 'alert("Hello world")',
        'my_html' : '<h1> rahe </h1>',
        'my_var' : None,
        'is_bangla': None,
        'my_dict' :[{'name':'Rahe' , 'age' : 20},
                    
                    {'name':'Moon' , 'age' : 18}
                    ]
    }
    
    return render(request, 'about.html', data)



def profile(request):
    
    data = {
        'user' : {'is_authenticated': True, 'username': 'rahe'},
        'title': 'Working with template tags',
        'products': [
            {'name': 'Laptop', 'price': 1000},
            {'name': 'Smartphone', 'price': 500},
            {'name': 'Tablet', 'price': 300},
            {'name': 'Laptop', 'price': 1000},
            {'name': 'Smartphone', 'price': 500},
          
        ],
    }
    
    return render(request , 'profile.html' , data)
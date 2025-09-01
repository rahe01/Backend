from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):

    data ={
        "name" : "Rahat Ahmed",
        "title": "django Filter's",
        "Product": [
            {"name" : "apple" , "price" : 5000} 
        ],
        "fruits": ["apple" ,"banana" , "orange"  ],
        "price": [10,23,34,5,6,56]

    }










    return render(request, 'home.html' , data)


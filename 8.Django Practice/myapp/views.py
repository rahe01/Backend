from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):

    data ={
        "name" : "Rahat Ahmed",
        "title": "django <i> Filter's </i>",
        "Product": [
            {"name" : "apple" , "price" : 5000} 
        ],
        "fruits": ["apple" ,"banana" , "orange"  ],
        "price": [10,23,34,5,6,56],
        "des":None,
        'cars': [
      {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
      {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
      {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
      {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
    ],
    "total":10,
    'heading': 'Hello &lt;i>my&lt;/i> World!',

    }










    return render(request, 'home.html' , data)


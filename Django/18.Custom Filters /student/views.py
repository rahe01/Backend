from django.shortcuts import render

# Create your views here.

def home(req):

    context = {
        'data': 'Hello I am django developer. I am also creationg backend '
    }

    return render(req, 'home.html' , context)
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return HttpResponse("Hello")




# Example-1.1: Variable

"""def learn_django(req):
    return render(req, 'django.html' , context={'name':'Rahe'})"""




# Example-1.2: Variable

def learn_django(req):

    name ='Django'
    duration ='$mounth'
    seats = 10

    course={
        'name' :name,
        'duration': duration,
        'seats': seats
    }




    return render(req, 'django.html' , course)








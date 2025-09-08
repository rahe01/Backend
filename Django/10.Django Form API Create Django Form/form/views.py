from django.shortcuts import render
from django.http import HttpResponse

from form.forms import Registation , Login

# Create your views here.




def home(req):

    return HttpResponse("Hello          dfdfdsf")




def regi(req):
    # fm = Registation()

    fm = Registation(field_order=['email', 'city'])

    return render(req, 'regi.html' , {'form': fm})



def login(req):
   # fm = Login(auto_id='rahe_%s')
   # fm = Login(auto_id=True)
   # fm = Login(auto_id=False) #level Remove

    # fm = Login(label_suffix='')

    # fm = Login(initial={'email' :'rahe@gmail.com'})
    fm = Login()

    return render(req, 'login.html' , {'form': fm})






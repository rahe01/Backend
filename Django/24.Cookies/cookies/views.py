from django.shortcuts import render
from datetime import datetime, timedelta , timezone
# Create your views here.

def home(request):
    return render(request, 'cookies/base.html')


def set_cookie(request):
    response = render(request, 'cookies/setcookies.html')
    # response.set_cookie('payid', 'pyyyyyyyyyy' , max_age=3600)
    response.set_cookie('payid', 'pyyyyyyyyyy' , expires=datetime.now(timezone.utc) + timedelta(days=2))
    return response

def get_cookie(request):
    # pay_id = request.COOKIES['payid']
    pay_id = request.COOKIES.get('payid', 'No Pay ID')
    response = render(request, 'cookies/getcookies.html' , {'payid': pay_id})
    return response

def delete_cookie(request):

    response = render(request, 'cookies/delcookies.html')
    response.delete_cookie('payid')
    return response


def set_signed_cookie(request):
    response = render(request, 'cookies/setsignedcookie.html')
    response.set_signed_cookie('token' , 'sdfghjkl' , salt='tk')
    return response

def get_signed_cookie(request):
    token = request.get_signed_cookie('token' , default='no token' , salt='tk')
    response = render(request, 'cookies/getsignedcookie.html' , {'pay_id': token})
    return response
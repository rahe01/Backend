from django.shortcuts import render

from django.contrib import messages


def home(req):
    # messages.add_message(req, messages.SUCCESS, 'Your account has been created')

    messages.success(req, 'This is success')
    
    messages.set_level(req , messages.DEBUG)
    messages.debug(req,'thisjisdfsdf')

    return render(req, 'home.html')


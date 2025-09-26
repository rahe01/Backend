from django.shortcuts import render

# Create your views here.


def setsession(request):
    request.session['name'] = 'Rahe'
    request.session['age'] = '25'
    # request.session.set_expiry(10)  # Session will expire in 10 seconds
    request.session.set_expiry(0)  # Session will expire when the browser is closed
    return render(request, 'session/setsession.html')


def getsession(request):
    name = request.session.get('name', 'Guest')
    age = request.session.get('age', 'Unknown')
    return render(request, 'session/getsession.html', {'name': name,'age': age})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    if 'age' in request.session:
         del request.session['age']
    
    return render(request, 'session/delsession.html')


def flushsession(request):
    request.session.flush()
    return render(request, 'session/flushsession.html')

def sessionmethodview(request):
    keys = request.session.keys()
    print(keys)
    items = request.session.items()
    print(items)
    lname = request.session.setdefault('lname', 'Guest')
    print(lname)

    session_cookie_age = request.session.get_expiry_age()
    print(session_cookie_age)
    session_cookie_expiry = request.session.get_expiry_date()
    print(session_cookie_expiry)


   
   
    
    return render(request, 'session/sessionmethodsinview.html')

def sessionclear(request):
    request.session.clear_expired()
    return render(request, 'session/sessionclear.html')


def sessionmethodintemplate(request):
    keys = request.session.keys()
    items = request.session.items()
   

    return render(request, 'session/sessionmethodsintemplate.html' , {
        'keys': keys,
        'items': items,})


def settestcookie(request):
    request.session.set_test_cookie()
   

  
    return render(request, 'session/settestcookie.html')

def gettestcookie(request):
    print(request.session.test_cookie_worked())
    
    return render(request, 'session/gettestcookie.html')
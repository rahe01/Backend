from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Rahe'
    request.session['roll'] = 'fddffd'
    return render(request, 'setsession.html')

def getsession(request):
    name = request.session.get('name')
    roll = request.session.get('roll')
    return render(request, 'getsession.html', {'name': name, 'roll': roll})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')
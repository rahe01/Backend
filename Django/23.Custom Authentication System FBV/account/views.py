from django.shortcuts import render , redirect
from account.forms import RegistationForm
from django.contrib import messages

# Create your views here.


def home(req):
    return render(req, 'account/home.html')

def login(req):
    if req.method == 'POST':
        return redirect('home')
    return render(req, 'account/login.html')




def register(req):
    if req.method == 'POST':
        form = RegistationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            messages.success(req, 'Your account has been created successfully. Please check your email to activate your account.')
            return redirect('login')
    else:
        form = RegistationForm()
    return render(req, 'account/register.html' , {'form':form})



def password_reset(req):
    return render(req, 'account/password_reset.html')


def password_reset_confirm(req, uidb64, token):
    return render(req, 'account/password_reset_confirm.html')
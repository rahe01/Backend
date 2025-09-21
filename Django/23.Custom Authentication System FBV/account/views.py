from django.shortcuts import render , redirect
from account.forms import RegistationForm , PasswordResetForm
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import force_str , force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from account.utils import send_activation_email
from account.models import User
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.


def home(req):
    return render(req, 'account/home.html')

def login(req):
    if req.user.is_authenticated:
        if req.user.is_seller:
            return redirect('seller_dashboard')
        elif req.user.is_customer:
            return redirect('customer_dashboard')
        else:
           
            return redirect('home')
        
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        if not email or not password:
            messages.error(req, 'Please provide both email and password.')
            return redirect('login')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(req, 'Invalid email or password.')
            return redirect('login')
        if not user.is_active:
            messages.error(req, 'Your account is inactive. Please activate your account via the link sent to your email.')
            return redirect('login')
        
        user = authenticate(req, email=email, password=password)
        if user is not None:
            auth_login(req, user)
            if user.is_seller:
                return redirect('seller_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            else:
                return redirect('home')
    return render(req, 'account/login.html')




def register(req):
    if req.method == 'POST':
        form = RegistationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            if form.cleaned_data['role'] == 'seller':
                user.is_seller = True
                user.is_customer = False
            else:
                user.is_customer = True
                user.is_seller = False

            
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
            activation_link = f'{settings.SITE_URL}{activation_link}'

            send_activation_email(user.email, activation_link)
            messages.success(req, "Registration successful! Please check your email to activate your account.")
            return redirect('login')  # <-- ei line add korbe
    else:
        form = RegistationForm()
    return render(req, 'account/register.html', {'form': form})


def account_activate(req, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.get(pk=uid)
        if user.is_active:
            messages.warning(req, 'Your account is already activated. Please login.')
            return redirect('login')
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(req, 'Your account has been activated successfully. You can now login.')
            return redirect('login')
        else:
            messages.error(req, 'The activation link is invalid or has expired.')
            return redirect('register')
 
    except(TypeError , ValueError, OverflowError, User.DoesNotExist):
            messages.error(req, 'The activation link is invalid or has expired.')
            return redirect('register')
    







def password_reset(req):
    if req.method == 'POST':
        form = PasswordResetForm(req.POST)
        if form.is_vailid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email=email).first()
            if user:
                 uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                 token = default_token_generator.make_token(user)
                 reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                 activation_link = f'{settings.SITE_URL}{reset_url}'

                 send_activation_email(user.email, activation_link)


    else:
        form = PasswordResetForm()
    return render(req, 'account/password_reset.html', {'form':form})


def password_reset_confirm(req, uidb64, token):
    return render(req, 'account/password_reset_confirm.html')
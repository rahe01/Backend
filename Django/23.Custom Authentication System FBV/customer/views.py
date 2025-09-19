from django.shortcuts import render , redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout
from core.decorators import login_and_role_required

login_and_role_required("customer")
def customer_dashboard(request):
    return render(request, 'customer/dashboard.html')



login_and_role_required("customer")
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, 'Password changed')
            return redirect('login')  # <-- return add korte hobe

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'customer/password_change.html', {'form': form})  # form context e pathano valo
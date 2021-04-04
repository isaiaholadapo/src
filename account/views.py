from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import random

from account.forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.

def home_view(request):
    return render(request, 'account\home.html')

def about_view(request):
    return render(request, 'account\about.html')

def service_view(request):
    return render(request, 'account\service.html')

def contact_view(request):
    return render(request, 'account\contact.html')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password = raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    context = {}
    user =  request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)



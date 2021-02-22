from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import random

from account.forms import RegistrationForm, AccountAuthenticationForm
from account.models import AccountDetails

# Create your views here.

def randomNum():
    return int(random.uniform(1000000000, 9999999999))

def home_view(request):
    try:
        user = request.user
        if user.is_authenticated:
            active_user = AccountDetails.objects.get(user_name = user)
    except:
        active_user = AccountDetails()
        active_user.account_number = randomNum()
        active_user.account_type = 'savings'
        active_user.balance = 0
        active_user.user_name = request.user
        active_user.save()
    return render(request, 'account/home.html', {})

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
    return redirect('home')

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

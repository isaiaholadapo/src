from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import  random

from transaction.models import Deposit, AccountDetails
from transaction.forms import DepositForm
from transaction import  forms
from . import models

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
    return render(request, 'transaction/home.html', {"active_user": active_user})


def deposit_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:  
        if request.method == "POST":
            form = forms.DepositForm(request.POST)
            if form.is_valid():
                form.save()
                actii_user = models.AccountDetails.objects.get(user_name = request.user)
                acti_user = models.Deposit.objects.filter(dep_user_name = request.user).last()
                depositor_account_number = acti_user.dep_account
                temp = acti_user
                
                #act_user = models.Status.objects.get(account_number = depositor_account_number)
                act_user_amout = acti_user.amount
                actii_user.balance = actii_user.balance + act_user_amout

                actii_user.save()
                #temp.delete()

                return redirect('home')
    else:
        return redirect('login')

    return render(request, 'transaction/deposit.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import  random
from django.contrib import  messages
from datetime import datetime


from transaction.models import Deposit, AccountDetail, Withdraw, Transfer
from transaction.forms import DepositForm, WithdrawForm, TransferForm
from transaction import  forms
from . import models

# Create your views here.

def randomNum():
    return int(random.uniform(1000000000, 9999999999))

def home_view(request):
    user = request.user
    if user.is_authenticated:
        try:            
            active_user = AccountDetail.objects.get(user_name = user)
        except:
            active_user = AccountDetail()
            active_user.account_number = randomNum()
            active_user.account_type = 'savings'
            active_user.balance = 0
            active_user.user_name = request.user
            active_user.save()
    else:
        return redirect('login')
    return render(request, 'transaction/home.html', {"active_user": active_user})


def deposit_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:  
        if request.method == "POST":
            form = forms.DepositForm(request.POST)
            if form.is_valid():
                form.save()
                actii_user = models.AccountDetail.objects.get(user_name = request.user)
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
            form = forms.DepositForm()
    else:
        return redirect('login')

    return render(request, 'transaction/deposit.html', context)

def withdraw_view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = forms.WithdrawForm(request.POST)
            if form.is_valid():
                form.save()
                withdrawal_user = models.Withdraw.objects.filter(withdraw_username = request.user).last()
                withdrawal_account = withdrawal_user.withdraw_account
                withdrawal_amount = withdrawal_user.withdraw_amount
                temp = withdrawal_user
                withdrawal_user = models.AccountDetail.objects.get(user_name = request.user)
                wbal = withdrawal_user.balance
                if withdrawal_amount < 5000:
                    temp.delete()
                    messages.error(request, "You can't withdraw amount less than 5,000")
                    return redirect('withdraw')
                elif withdrawal_amount > 50000:
                    temp.delete()
                    messages.error(request, "You can't withdraw amount more than 50,000")
                    return redirect('withdraw')
                elif wbal > withdrawal_amount:
                    withdrawal_user.balance = withdrawal_user.balance - withdrawal_amount
                    withdrawal_user.save()
                    return redirect('home')
                else:
                    temp.delete()
                    messages.error(request, "You don't have enough Money.")
                    return redirect('withdraw')
            else:
                form = forms.WithdrawForm()
    else:
        return redirect('login')
    
    return render(request, 'transaction/withdraw.html', {})


def transfer_view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = forms.TransferForm(request.POST)
            if form.is_valid():
                form.save()
                sender = models.Transfer.objects.filter(sender_username = request.user).last()
                receiver_account_no = sender.receiver_account
                transfer_amount = sender.amount
                temp = sender

                receiver_account = models.AccountDetail.objects.get(account_number = receiver_account_no)
                sender = models.AccountDetail.objects.get(user_name = request.user)
                if sender.balance > transfer_amount:
                    sender.balance = sender.balance - transfer_amount
                    receiver_account.balance = receiver_account.balance + transfer_amount

                    sender.save()
                    receiver_account.save()
                    return redirect('home')
                else:
                    temp.delete()
                    
                    messages.error(request, "You don't have enough Money.")
                    return redirect('transfer')                    
        else:
            form = forms.TransferForm()
    else:
        return redirect('login')
    return render(request, 'transaction/transfer.html', {"form": form})

def transaction_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    deposit = models.Deposit.objects.all()
    withdraw = models.Withdraw.objects.all()
    transfer = models.Transfer.objects.all()
    context = {"depositi": deposit, "withdraw": withdraw, "transfer": transfer}
    return render(request, 'transaction/transaction.html', context = context )

def interest_view(self):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    int_user = models.AccountDetail.objects.get(user_name = request.user)
    int_user.balance = int_user.balance * (1/ 0.01)
    int_user.save()
    return render(request, 'transaction/interest.html', {"int_user": int_user})
    

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator

from transaction.models import Deposit, AccountDetail, Withdraw, Transfer
from transaction.forms import DepositForm, WithdrawForm, TransferForm
from transaction import forms
from . import models

# Create your views here.


def randomNum():
    return int(random.uniform(1000000000, 9999999999))


def account_view(request):
    user = request.user
    if user.is_authenticated:
        try:
            active_user = AccountDetail.objects.get(user_name=user)
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
                actii_user = models.AccountDetail.objects.get(
                    user_name=request.user)
                acti_user = models.Deposit.objects.filter(
                    dep_user_name=request.user).last()
                depositor_account_number = acti_user.dep_account
                temp = acti_user

                # act_user = models.Status.objects.get(account_number = depositor_account_number)
                act_user_amout = acti_user.amount
                actii_user.balance = actii_user.balance + act_user_amout

                actii_user.save()
                # temp.delete()
                messages.success(request, "deposited successfully")
                return redirect('deposit-history')
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
                withdrawal_user = models.Withdraw.objects.filter(
                    withdraw_username=request.user).last()
                withdrawal_account = withdrawal_user.withdraw_account
                withdrawal_amount = withdrawal_user.withdraw_amount
                temp = withdrawal_user
                withdrawal_user = models.AccountDetail.objects.get(
                    user_name=request.user)
                wbal = withdrawal_user.balance
                if withdrawal_amount < 5000:
                    temp.delete()
                    messages.error(
                        request, "You can't withdraw amount less than 5,000")
                    return redirect('withdraw')
                elif withdrawal_amount > 50000:
                    temp.delete()
                    messages.error(
                        request, "You can't withdraw amount more than 50,000")
                    return redirect('withdraw')
                elif wbal > withdrawal_amount:
                    withdrawal_user.balance = withdrawal_user.balance - withdrawal_amount
                    withdrawal_user.save()
                    messages.success(request, "Withdrawal successful")
                    return redirect('withdraw-history')
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
                sender = models.Transfer.objects.filter(
                    sender_username=request.user).last()
                receiver_account_no = sender.receiver_account
                transfer_amount = sender.amount
                temp = sender

                receiver_account = models.AccountDetail.objects.get(
                    account_number=receiver_account_no)
                sender = models.AccountDetail.objects.get(
                    user_name=request.user)
                if sender.balance > transfer_amount:
                    sender.balance = sender.balance - transfer_amount
                    receiver_account.balance = receiver_account.balance + transfer_amount

                    sender.save()
                    receiver_account.save()
                    messages.success(request, "Transaction successful")
                    return redirect('transfer-history')
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
    deposit = models.Deposit.objects.all().order_by('date').reverse()
    deposit_paginator = Paginator(deposit, 5)
    page_num = request.GET.get('page')
    page = deposit_paginator.get_page(page_num)
    context = {
        "depositi": deposit,
        "page": page,
        "count": deposit_paginator.count,

    }
    return render(request, 'transaction/transaction.html', context=context)


def withdraw_history_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Withdraw.objects.raw('select id,withdraw_amount,date from transaction_withdraw where date between "'+fromdate+'" and "'+todate+'"')
        searchresult_paginator = Paginator(searchresult, 5)
        page_num = request.GET.get('page')
        page = searchresult_paginator.get_page(page_num)
        
        contexti = {
            'searchresult': searchresult,
            'page' : page,
            'count': searchresult_paginator.count,
        }
        
        return render(request, 'transaction/withdraw_history.html', contexti)
    else:
        withdraw = Withdraw.objects.all().order_by('date').reverse()
        withdraw_paginator = Paginator(withdraw, 5)
        page_num = request.GET.get('page')
        page = withdraw_paginator.get_page(page_num)
        
        contexti = {
            'withdrawal': withdraw,
            'page' : page,
            'count': withdraw_paginator.count,
        }
        return render(request, 'transaction/withdraw_history.html', contexti)

def deposit_history_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Deposit.objects.raw('select id,amount,date from transaction_deposit where date between "'+fromdate+'" and "'+todate+'"')
        searchresult_paginator = Paginator(searchresult, 5)
        page_num = request.GET.get('page')
        page = searchresult_paginator.get_page(page_num)
        context = {
            "searchresult" : searchresult,
            "page": page,
            "count": searchresult_paginator.count,
        }
        return render(request, 'transaction/deposit_history.html', context)
    else:
        deposit = Deposit.objects.all().order_by('date').reverse()
        deposit_paginator = Paginator(deposit, 5)
        page_num = request.GET.get('page')
        page = deposit_paginator.get_page(page_num)
        context = {
            "deposit" : deposit,
            "page": page,
            "count": deposit_paginator.count,
        }
        return render(request, 'transaction/deposit_history.html', context)

def transfer_history_view(request):
    user =  request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        fromdate = request.POST.get("fromdate")
        todate = request.POST.get("todate")
        searchresult = Transfer.objects.raw('select id,amount,date from transaction_transfer where date between "'+fromdate+'" and "'+todate+'"')
        transfer_paginator = Paginator(searchresult, 5)
        page_num = request.GET.get('page')
        page = transfer_paginator.get_page(page_num)
        context = {
            "searchresult": searchresult,
            "page" : page,
            "count": transfer_paginator.count,
        }
        return render(request, 'transaction/transfer_history.html', context)
    else:
        transfer = Transfer.objects.all().order_by('date').reverse()
        transfer_paginator = Paginator(transfer, 5)
        page_num = request.GET.get('page')
        page = transfer_paginator.get_page(page_num)
        context = {
            "transfer": transfer,
            "page" : page,
            "count": transfer.count,
        }

        return render(request, 'transaction/transfer_history.html', context)



def deposit_search_view(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Deposit.objects.raw('select id,amount,date from transaction_deposit where date between "'+fromdate+'" and "'+todate+'"')
        return render(request, 'transaction/searchdate.html', {"ssdata": searchresult})
    else:
        deposit_date = Deposit.objects.all()
        return render(request, 'transaction/searchdate.html', {"ssdata": deposit_date})

def interest_view(self):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    int_user = models.AccountDetail.objects.get(user_name = request.user)
    int_user.balance = int_user.balance * (1/ 0.01)
    int_user.save()
    return render(request, 'transaction/home.html', {"int_user": int_user})
    

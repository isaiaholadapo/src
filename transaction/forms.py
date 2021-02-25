from django import forms
from . import models
from transaction.models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = models.Deposit
        fields = [ 'amount', 'dep_user_name', 'dep_account']

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = models.Withdraw
        fields = ['withdraw_amount', 'withdraw_account', 'withdraw_username']

class TransferForm(forms.ModelForm):
    class Meta: 
        model = models.Transfer
        fields = ['sender_username', 'amount', 'receiver_account']


from django import forms
from . import models
from transaction.models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = models.Deposit
        fields = [ 'amount', 'dep_user_name', 'dep_account']


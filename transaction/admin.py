from django.contrib import admin

from transaction.models import Deposit, AccountDetails, Withdraw
# Register your models here.

admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(AccountDetails)
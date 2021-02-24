from django.contrib import admin

from transaction.models import Deposit, AccountDetails
# Register your models here.

admin.site.register(Deposit)
admin.site.register(AccountDetails)
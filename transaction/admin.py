from django.contrib import admin

from transaction.models import Deposit, AccountDetails, Withdraw, Transfer
# Register your models here.

class DepositAdmin(admin.ModelAdmin):
    list_display = [ 'amount', 'dep_user_name', 'dep_account', 'date',]

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['withdraw_username', 'withdraw_account', 'withdraw_amount', 'date',]

class TransferAdmin(admin.ModelAdmin):
    list_display = ['sender_username', 'receiver_account', 'amount', 'date',]

admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(AccountDetails)
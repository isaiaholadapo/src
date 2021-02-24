from django.db import models

# Create your models here.

account_choices = (
    ('savings', 'SAVINGS'),
    ('current', 'CURRENT'),
)

class AccountDetails(models.Model):
	account_number              = models.IntegerField()
	balance                     = models.IntegerField()
	account_type                = models.CharField(max_length = 8, choices = account_choices, default = 'savings')
	user_name                   = models.CharField(max_length =  50)

	def __str__(self):
		return self.user_name

class Deposit(models.Model):
    amount						= models.IntegerField()
    dep_account					= models.IntegerField(default = 0)
    dep_user_name				= models.CharField(max_length =  50, default = None)

class Withdraw(models.Model):
	withdraw_amount				= models.IntegerField()
	withdraw_account			= models.IntegerField()
	withdraw_username			= models.CharField(max_length = 50, default = None)

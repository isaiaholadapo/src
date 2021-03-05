from django.db import models
from datetime import datetime

# Create your models here.

account_choices = (
    ('savings', 'SAVINGS'),
    ('current', 'CURRENT'),
)

class AccountDetail(models.Model):
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
	date						= models.DateTimeField(blank=True, null=True, auto_now_add=True)

	def __str__(self):
		return self.dep_user_name

class Withdraw(models.Model):
	withdraw_amount				= models.IntegerField()
	withdraw_account			= models.IntegerField()
	withdraw_username			= models.CharField(max_length = 50, default = None)
	date						= models.DateTimeField(auto_now_add=True, blank = True)
	def __str__(self):
		return self.withdraw_username

class Transfer(models.Model):
	sender_username				= models.CharField(max_length = 50, default = None)
	receiver_account			= models.IntegerField()
	amount						= models.IntegerField()
	date 						= models.DateTimeField(auto_now_add=True, blank = True)
	def __str__(self):
		return self.sender_username

class Interest(models.Model):
	today_interest				= models.IntegerField()
	interest_username			= models.IntegerField()
	interest_account			= models.IntegerField()
	date 						= models.DateTimeField(auto_now_add=True, blank = True)



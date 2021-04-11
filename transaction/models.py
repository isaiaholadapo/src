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
	email 						= models.EmailField(verbose_name="email", max_length=60, unique=True)

	def __str__(self):
		return self.email

class Deposit(models.Model):
	amount						= models.IntegerField()
	dep_account					= models.IntegerField(default = 0)
	date						= models.DateTimeField(blank=True, null=True, auto_now_add=True)
	dep_email					= models.EmailField(verbose_name="email", max_length=60)

	def __str__(self):
		return self.dep_email

class Withdraw(models.Model):
	withdraw_amount				= models.IntegerField()
	withdraw_account			= models.IntegerField()
	email						= models.EmailField(verbose_name="email", max_length=60)
	date						= models.DateTimeField(auto_now_add=True, blank = True)
	def __str__(self):
		return self.email

class Transfer(models.Model):
	email						= models.EmailField(verbose_name="email", max_length=60)
	receiver_account			= models.IntegerField()
	amount						= models.IntegerField()
	date 						= models.DateTimeField(auto_now_add=True, blank = True)
	def __str__(self):
		return self.email

class History(models.Model):
	transaction					= models.ForeignKey(Transfer, default=11, on_delete = models.SET_DEFAULT)
	date						= models.DateTimeField(auto_now_add=True, blank = True)


class Interest(models.Model):
	today_interest				= models.IntegerField()
	email						= models.EmailField(verbose_name="email", max_length=60)
	interest_account			= models.IntegerField()
	date 						= models.DateTimeField(auto_now_add=True, blank = True)



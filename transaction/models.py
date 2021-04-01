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
	email						= models.EmailField(verbose_name="email", max_length=60, unique=True)

	def __str__(self):
		return self.email

class Withdraw(models.Model):
	withdraw_amount				= models.IntegerField()
	withdraw_account			= models.IntegerField()
	email						= models.EmailField(verbose_name="email", max_length=60, unique=True)
	date						= models.DateTimeField(auto_now_add=True, blank = True)
	def __str__(self):
		return self.email

class Transfer(models.Model):
	email						= models.EmailField(verbose_name="email", max_length=60, unique=True)
	receiver_account			= models.IntegerField()
	amount						= models.IntegerField()
	date 						= models.DateTimeField(auto_now_add=True, blank = True)
	def __str__(self):
		return self.email

class Interest(models.Model):
	today_interest				= models.IntegerField()
	email						= models.EmailField(verbose_name="email", max_length=60, unique=True)
	interest_account			= models.IntegerField()
	date 						= models.DateTimeField(auto_now_add=True, blank = True)



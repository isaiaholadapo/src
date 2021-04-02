from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


account_choices = (
    ('savings', 'SAVINGS'),
    ('current', 'CURRENT'),
	('deposit', 'DEPOSIT'),
	('dom', 'DOM'),

)
class MyAccountManager(BaseUserManager):
	def create_user(self, email,  password=None):
		if not email:
			raise ValueError('Users must have an email address')


		user = self.model(
			email=self.normalize_email(email),

		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email,  password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			
			
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name 				= models.CharField(max_length=255)
	last_name 				= models.CharField(max_length=255)
	phone_number 			= models.CharField(max_length=255)
	address		 			= models.CharField(max_length=255)
	address22	 			= models.CharField(max_length=255)
	city		 			= models.CharField(max_length=255)
	state		 			= models.CharField(max_length=255)
	postal_code	 			= models.CharField(max_length=255)
	bvn			 			= models.CharField(max_length=255)
	account_type 			= models.CharField(max_length=15, choices = account_choices, default = 'savings')
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	#REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
	if created:
		Token.objects.create(user = instance)
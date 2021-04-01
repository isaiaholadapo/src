# Generated by Django 3.1.7 on 2021-03-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('account_type', models.CharField(choices=[('savings', 'SAVINGS'), ('current', 'CURRENT')], default='savings', max_length=8)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('dep_account', models.IntegerField(default=0)),
                ('dep_user_name', models.CharField(default=None, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_interest', models.IntegerField()),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('interest_account', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('receiver_account', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw_amount', models.IntegerField()),
                ('withdraw_account', models.IntegerField()),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

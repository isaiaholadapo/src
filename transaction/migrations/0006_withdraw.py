# Generated by Django 3.1.7 on 2021-02-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_accountdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw_amount', models.IntegerField()),
                ('withdraw_account', models.IntegerField()),
                ('withdraw_username', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]

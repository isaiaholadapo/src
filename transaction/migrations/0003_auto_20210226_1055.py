# Generated by Django 3.1.7 on 2021-02-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetails',
            name='period',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='rate',
            field=models.IntegerField(default=0.01),
        ),
    ]

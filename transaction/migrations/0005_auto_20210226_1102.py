# Generated by Django 3.1.7 on 2021-02-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20210226_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='rate',
            field=models.FloatField(default=0.1),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20210408_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='dep_email',
            field=models.EmailField(max_length=60, verbose_name='email'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-30 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Moneys', '0008_customeraccounthistory_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraccount',
            name='currency',
        ),
    ]

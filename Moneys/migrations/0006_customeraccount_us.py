# Generated by Django 3.2.4 on 2021-06-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moneys', '0005_alter_customeraccounthistory_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccount',
            name='us',
            field=models.CharField(default='00', max_length=255),
        ),
    ]

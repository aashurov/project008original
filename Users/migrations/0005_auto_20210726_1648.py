# Generated by Django 3.2.4 on 2021-07-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_usermodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.TextField(default='Name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.TextField(default='Familiya'),
        ),
    ]
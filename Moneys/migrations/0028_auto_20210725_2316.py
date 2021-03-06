# Generated by Django 3.2.4 on 2021-07-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moneys', '0027_auto_20210725_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customeraccount',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customeraccounthistory',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customeraccounthistory',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customerexpenses',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customerexpenses',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customerexpenseshistory',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customerexpenseshistory',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]

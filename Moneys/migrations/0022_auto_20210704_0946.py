# Generated by Django 3.2.4 on 2021-07-04 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Moneys', '0021_customeraccounthistory_expenseshistory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraccounthistory',
            name='expenseshistory_id',
        ),
        migrations.AddField(
            model_name='customerexpenseshistory',
            name='customeraccounthistory_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='accounthistory_id', to='Moneys.customeraccounthistory'),
        ),
    ]

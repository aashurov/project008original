# Generated by Django 3.2.4 on 2021-07-04 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Moneys', '0020_auto_20210704_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccounthistory',
            name='expenseshistory_id',
            field=models.ForeignKey(blank=True, default='00', on_delete=django.db.models.deletion.CASCADE, related_name='expenseshistory_id', to='Moneys.customerexpenseshistory'),
        ),
    ]
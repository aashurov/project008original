# Generated by Django 3.2.4 on 2021-07-04 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_remove_service_price'),
        ('Moneys', '0017_alter_customerexpenseshistory_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccounthistory',
            name='service',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='service', to='Services.service'),
        ),
        migrations.AlterField(
            model_name='customerexpenseshistory',
            name='service',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='servicea', to='Services.service'),
        ),
    ]

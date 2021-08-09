# Generated by Django 3.2.4 on 2021-07-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'За Перевозку'), ('2', 'За Товар'), ('3', 'За Перевод'), ('4', 'Возврат')], max_length=255, null=True, verbose_name='Role')),
                ('price', models.FloatField(default='00', max_length=255)),
            ],
        ),
    ]
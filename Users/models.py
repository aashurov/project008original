from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator

# Create your models here.


class UserModel(AbstractUser):
    CHOICES = (
        ('Manager', 'Manager'),
        ('Senior', 'Senior'),
        ('Middle', 'Middle'),
        ('Junior', 'Junior'),
        ('Courier', 'Courier'),
        ('Customer', 'Customer'),
    )

    role = models.CharField('Role', max_length=100, choices=CHOICES, default=6)
    address = models.CharField('Address', max_length=255, null=True, blank=True)
    first_name = models.TextField(default='Name', null=True, blank=True)
    last_name = models.TextField(default='Familiya', null=True, blank=True)
    description = models.TextField(default='00', blank=True)
    # phone = models.CharField('Phone', max_length=255, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    def __str__(self):
        return self.username
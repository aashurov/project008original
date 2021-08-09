from django.db import models

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255, default='00')

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    name = models.CharField(max_length=255, default='00')

    def __str__(self):
        return str(self.name)
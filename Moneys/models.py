from django.db import models
from django.conf import settings
from Services.models import Plan, Service
# Create your models here.


class CommonModel(models.Model):
    usd = models.FloatField(max_length=255, default='00', blank=True)
    rub = models.FloatField(max_length=255, default='00', blank=True)
    description = models.TextField(default='00', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class CustomerAccount(CommonModel):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='customeraccount')

    def __str__(self):
        return self.customer


class CustomerAccountHistory(CommonModel):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customeraccounthistory')
    courier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courier_add')
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff_add_one')
    currency = models.CharField(max_length=255, default='00', blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,  default='1', blank=True, related_name='service')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, blank=True, default='1', related_name='plane')


    def __str__(self):
        return self.customer


class CustomerExpenses(CommonModel):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customerexpenses')

    def __str__(self):
        return self.customer


class CustomerExpensesHistory(CommonModel):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customerexpenseshistory')
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff_add_two')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE,  blank=True, default='1', related_name='plan')
    service = models.ForeignKey(Service, on_delete=models.CASCADE,   default='1', blank=True, related_name='servicea')
    # customeraccounthistory = models.ForeignKey(CustomerAccountHistory, blank=False, default='1', on_delete=models.CASCADE, related_name='accounthistory_id')
    customeraccounthistory = models.ForeignKey(CustomerAccountHistory, blank=True, null=True, on_delete=models.CASCADE, related_name='accounthistory_id')
    currency = models.CharField(max_length=255, default='00', blank=True)

    def __str__(self):
        return self.customer
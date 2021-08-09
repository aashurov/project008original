from django.contrib import admin
from .models import CustomerAccount, CustomerAccountHistory, CustomerExpenses, CustomerExpensesHistory
# Register your models here.

admin.site.register(CustomerAccount)
admin.site.register(CustomerAccountHistory)
admin.site.register(CustomerExpenses)
admin.site.register(CustomerExpensesHistory)


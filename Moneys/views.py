from rest_framework import viewsets
from .serializers import CustomerAccountSerializer, CustomerAccountHistorySerializerRead, CustomerExpensesSerializer, CustomerExpensesHistorySerializer
# from .models import CustomerAccount, CustomerAccountHistory, CustomerExpenses, CustomerExpensesHistory
# Create your views here.
from .moneys import *
#
# class CustomerAccountViewSet(viewsets.ModelViewSet):
#     queryset = CustomerAccount.objects.all().order_by('-created_at')
#     serializer_class = CustomerAccountSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(staff=self.request.user)
#
#     def perform_update(self, serializer):
#         serializer.save(staff=self.request.user)
#
#
class CustomerAccountHistoryViewSet(viewsets.ModelViewSet):
    queryset = CustomerAccountHistory.objects.all().order_by('-created_at')
    serializer_class = CustomerAccountHistorySerializerRead

    def perform_create(self, serializer):
        # serializer.save(currency='rub', usd=0, staff=self.request.user)
        serializer.save(staff=self.request.user)

    def perform_update(self, serializer):
        serializer.save(staff=self.request.user)

#
# class CustomerExpensesViewSet(viewsets.ModelViewSet):
#     queryset = CustomerExpenses.objects.all().order_by('-created_at')
#     serializer_class = CustomerExpensesSerializer
#
#
# class CustomerExpensesHistoryViewSet(viewsets.ModelViewSet):
#     queryset = CustomerExpensesHistory.objects.all().order_by('-created_at')
#     serializer_class = CustomerExpensesHistorySerializer
#
#     def perform_create(self, serializer):
#         serializer.save(staff=self.request.user)



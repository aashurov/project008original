from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from .models import *
from Moneys.pagination import StandardResultsSetPagination
from Moneys.models import CustomerAccount, CustomerExpenses


@api_view(['GET', 'POST'])
def usersall(request):
    if request.method == 'GET':
        users = UserModel.objects.all().order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserModelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = UserModelSerializer(data=request.data)
        customeraccount = CustomerAccount()
        customerexpenses = CustomerExpenses()

        if serializer.is_valid():
            if request.data['username'] and request.data['role']:
                obj = serializer.save()
                customeraccount.usd = 0
                customeraccount.rub = 0
                customeraccount.customer_id = obj.id
                customeraccount.save()

                customerexpenses.usd = 0
                customerexpenses.rub = 0
                customerexpenses.customer_id = obj.id
                customerexpenses.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

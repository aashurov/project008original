from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from .pagination import StandardResultsSetPagination

@api_view(['GET'])
def customeraccounts(request):
    if request.method == 'GET':
        customeraccount = CustomerAccount.objects.filter(customer__role='Customer').order_by('id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customeraccount, request)
        serializer = CustomerAccountSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def customeraccount(request, pk):
    if request.method == 'GET':
        customeraccount = CustomerAccount.objects.filter(customer_id=pk)
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customeraccount, request)
        serializer = CustomerAccountSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET', 'POST'])
def customeraccounthistory(request):
    if request.method == 'GET':
        customeraccounthistory = CustomerAccountHistory.objects.all().order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customeraccounthistory, request)
        serializer = CustomerAccountHistorySerializerRead(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerAccountHistorySerializerWrite(data=request.data)
        customeraccount = CustomerAccount.objects.get(customer_id=request.data['customer'])
        if serializer.is_valid():
            if request.data['rub'] == 0.0 or request.data['rub'] is None or request.data['rub'] == '':
                obj = serializer.save(currency='usd', rub=0, staff=request.user)
                customeraccount.usd = customeraccount.usd + request.data['usd']
                customeraccount.save()
                if request.data['service'] == 2:
                    customeraccount.usd = customeraccount.usd - request.data['usd']
                    customeraccount.save()
                    customerexpenseshistory = CustomerExpensesHistory()
                    customerexpenseshistory.usd = request.data['usd']
                    customerexpenseshistory.staff = request.user
                    customerexpenseshistory.service_id = request.data['service']
                    customerexpenseshistory.customer_id = request.data['customer']
                    customerexpenseshistory.plan_id = request.data['plan']
                    customerexpenseshistory.customeraccounthistory_id = obj.id
                    customerexpenseshistory.save()
                    customerexpenses = CustomerExpenses.objects.get(customer_id=request.data['customer'])
                    customerexpenses.usd = customerexpenses.usd + request.data['usd']
                    customerexpenses.save()
                return Response(serializer.data)
            if request.data['usd']== 0.0 or request.data['usd'] is None or request.data['usd']=='':
                obj = serializer.save(currency='rub', usd=0, staff=request.user)
                customeraccount.rub = customeraccount.rub + request.data['rub']
                customeraccount.save()
                if request.data['service'] == 2:
                    customeraccount.rub = customeraccount.rub - request.data['rub']
                    customeraccount.save()
                    customerexpenseshistory = CustomerExpensesHistory()
                    customerexpenseshistory.rub = request.data['rub']
                    customerexpenseshistory.staff = request.user
                    customerexpenseshistory.service_id = request.data['service']
                    customerexpenseshistory.customer_id = request.data['customer']
                    customerexpenseshistory.plan_id = request.data['plan']
                    customerexpenseshistory.customeraccounthistory_id = obj.id
                    customerexpenseshistory.save()
                    customerexpenses = CustomerExpenses.objects.get(customer_id=request.data['customer'])
                    customerexpenses.rub = customerexpenses.rub + request.data['rub']
                    customerexpenses.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def customeraccounthistoryy(request, pk):
    if request.method == 'GET':
        customeraccounthistory = CustomerAccountHistory.objects.filter(customer_id=pk).order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customeraccounthistory, request)
        serializer = CustomerAccountHistorySerializerRead(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def customerexpenseshistoryy(request, pk):
    if request.method == 'GET':
        customerexpenseshistory = CustomerExpensesHistory.objects.filter(customer_id=pk).exclude(service_id=2).order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customerexpenseshistory, request)
        serializer = CustomerExpensesHistorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def customerexpenseshistoryyy(request, pk):
    if request.method == 'GET':
        customerexpenseshistory = CustomerExpensesHistory.objects.filter(customer_id=pk).filter(service_id=2).order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customerexpenseshistory, request)
        serializer = CustomerExpensesHistorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def customeraccounthistory_detail(request, pk):
    try:
        customeraccounthistory = CustomerAccountHistory.objects.get(pk=pk)
        customeraccount = CustomerAccount.objects.get(customer_id=customeraccounthistory.customer_id)
    except CustomerAccountHistory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerAccountHistorySerializerRead(customeraccounthistory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print('Putga kirdi')
        serializer = CustomerAccountHistorySerializerWrite(customeraccounthistory, data=request.data)
        if serializer.is_valid():
            if request.data['rub'] == 0.0:
                customeraccount.usd = customeraccount.usd - customeraccounthistory.usd + request.data['usd']
                customeraccount.save()
                obj = serializer.save(currency='usd', rub=0, staff=request.user)
                if customeraccounthistory.service == 2:
                    customerexpenseshistory = CustomerExpensesHistory.objects.get(customeraccounthistory_id=obj.id)
                    customerexpenseshistory.usd = request.data['usd']
                    customerexpenseshistory.staff = request.user
                    customerexpenseshistory.service_id = request.data['service']
                    customerexpenseshistory.customer_id = request.data['customer']
                    customerexpenseshistory.plan_id = request.data['plan']
                    customerexpenseshistory.customeraccounthistory_id = obj.id
                    customerexpenseshistory.save()
                    customerexpenses = CustomerExpenses.objects.get(customer_id=request.data['customer'])
                    customerexpenses.usd = customerexpenses.usd - customerexpenses.usd + request.data['usd']
                    customerexpenses.save()

            if request.data['usd'] == 0.0:
                customeraccount.rub = customeraccount.rub - customeraccounthistory.rub + request.data['rub']
                customeraccount.save()
                obj = serializer.save(currency='rub', usd=0, staff=request.user)
                if customeraccounthistory.service == 2:
                    customerexpenseshistory = CustomerExpensesHistory.objects.get(customeraccounthistory_id=obj.id)
                    customerexpenseshistory.rub = request.data['rub']
                    customerexpenseshistory.staff = request.user
                    customerexpenseshistory.service_id = request.data['service']
                    customerexpenseshistory.customer_id = request.data['customer']
                    customerexpenseshistory.plan_id = request.data['plan']
                    customerexpenseshistory.customeraccounthistory_id = obj.id
                    customerexpenseshistory.save()
                    customerexpenses = CustomerExpenses.objects.get(customer_id=request.data['customer'])
                    customerexpenses.rub = customerexpenses.rub - customerexpenses.rub + request.data['rub']
                    customerexpenses.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if customeraccounthistory.service_id == 2:
            customerexpenseshistory = CustomerExpensesHistory.objects.get(customeraccounthistory_id=customeraccounthistory.id)
            customerexpenses = CustomerExpenses.objects.get(customer_id=customerexpenseshistory.customer_id)
            if customeraccounthistory.currency == 'rub':
                customerexpenses.rub = customerexpenses.rub - customerexpenseshistory.rub
                customerexpenses.save()
            customerexpenses.usd = customerexpenses.usd - customerexpenseshistory.usd
            customerexpenses.save()
            customerexpenseshistory.delete()
        elif customeraccounthistory.service_id == 1:
            if customeraccounthistory.currency == 'rub':
                customeraccount.rub = customeraccount.rub - customeraccounthistory.rub
                customeraccount.save()
            customeraccount.usd = customeraccount.usd - customeraccounthistory.usd
            customeraccount.save()
        customeraccounthistory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def customerexpenseshistory(request):
    if request.method == 'GET':
        customerexpenseshistory = CustomerExpensesHistory.objects.all().order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customerexpenseshistory, request)
        serializer = CustomerExpensesHistorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        # serializer = CustomerExpensesHistorySerializer(customerexpenseshistory, many=True)
        # return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerExpensesHistorySerializerWrite(data=request.data)
        customerexpenses = CustomerExpenses.objects.get(customer_id=request.data['customer'])
        customeraccount = CustomerAccount.objects.get(customer_id=request.data['customer'])
        if serializer.is_valid():
            if request.data['rub'] == 0.0:
                serializer.save(currency='usd', rub=0, staff=request.user)
                customerexpenses.usd = customerexpenses.usd + request.data['usd']
                customeraccount.usd = customeraccount.usd - request.data['usd']
                customeraccount.save()
                customerexpenses.save()
                return Response(serializer.data)
            serializer.save(currency='rub', usd=0, staff=request.user)
            customerexpenses.rub = customerexpenses.rub + request.data['rub']
            customeraccount.rub = customeraccount.rub - request.data['rub']
            customeraccount.save()
            customerexpenses.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customerexpenseshistory_detail(request, pk):

    try:
        customerexpenseshistory = CustomerExpensesHistory.objects.get(pk=pk)
        customeraccount = CustomerAccount.objects.get(customer_id=customerexpenseshistory.customer_id)
        customerexpenses = CustomerExpenses.objects.get(customer_id=customerexpenseshistory.customer_id)
    except CustomerExpensesHistory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerExpensesHistorySerializer(customerexpenseshistory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerExpensesHistorySerializer(customerexpenseshistory, data=request.data)
        if serializer.is_valid():
            if request.data['rub'] == 0.0:
                customeraccount.usd = customeraccount.usd + customerexpenseshistory.usd - request.data['usd']
                customeraccount.save()
                customerexpenses.usd = customerexpenses.usd - customerexpenseshistory.usd + request.data['usd']
                customerexpenses.save()
                serializer.save(currency='usd', rub=0, staff=request.user)
            if request.data['usd'] == 0.0:
                customeraccount.rub = customeraccount.rub + customerexpenseshistory.rub - request.data['rub']
                customeraccount.save()
                customerexpenses.rub = customerexpenses.rub - customerexpenseshistory.rub + request.data['rub']
                customerexpenses.save()
                serializer.save(currency='rub', usd=0, staff=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if customerexpenseshistory.currency == 'rub':
            customeraccount.rub = customeraccount.rub + customerexpenseshistory.rub
            customeraccount.save()
            customerexpenses.rub = customerexpenses.rub - customerexpenseshistory.rub
            customerexpenses.save()
        customeraccount.usd = customeraccount.usd + customerexpenseshistory.usd
        customeraccount.save()
        customerexpenses.usd = customerexpenses.usd - customerexpenseshistory.usd
        customerexpenses.save()
        customerexpenseshistory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def customerexpenses(request, pk):
    if request.method == 'GET':
        customerexpenses = CustomerExpenses.objects.filter(customer_id=pk)
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customerexpenses, request)
        serializer = CustomerExpensesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def customerexpenseslist(request):
    if request.method == 'GET':
        customerexpenses = CustomerExpenses.objects.filter(customer__role='Customer').order_by('-id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(customerexpenses, request)
        serializer = CustomerExpensesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
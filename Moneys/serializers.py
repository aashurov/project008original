from rest_framework import serializers
from .models import CustomerAccount, CustomerAccountHistory, CustomerExpenses, CustomerExpensesHistory
from Users.serializers import UserModelSerializer
from Services.serializers import ServiceSerializer, PlanSerializer


class CustomerAccountSerializer(serializers.ModelSerializer):
    customer = UserModelSerializer(read_only=True)

    class Meta:
        model = CustomerAccount
        fields = '__all__'


class CustomerAccountHistorySerializerRead(serializers.ModelSerializer):
    # staff = serializers.StringRelatedField()
    staff = UserModelSerializer(read_only=True)
    customer = UserModelSerializer(read_only=True)
    # customer = serializers.StringRelatedField()
    courier = UserModelSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = CustomerAccountHistory
        fields = '__all__'
        # extra_kwargs = {
        #     'rub': {'required': False},
        # }

class CustomerAccountHistorySerializerWrite(serializers.ModelSerializer):
    staff = serializers.StringRelatedField()

    class Meta:
        model = CustomerAccountHistory
        fields = '__all__'


class CustomerExpensesSerializer(serializers.ModelSerializer):
    customer = UserModelSerializer(read_only=True)

    class Meta:
        model = CustomerExpenses
        fields = '__all__'


class CustomerExpensesHistorySerializer(serializers.ModelSerializer):
    # staff = serializers.StringRelatedField()
    staff = UserModelSerializer(read_only=True)
    customer = UserModelSerializer(read_only=True)
    # customer = serializers.StringRelatedField()
    # courier = UserModelSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = CustomerExpensesHistory
        fields = '__all__'


class CustomerExpensesHistorySerializerWrite(serializers.ModelSerializer):
    staff = serializers.StringRelatedField()

    class Meta:
        model = CustomerExpensesHistory
        fields = '__all__'
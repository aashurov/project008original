from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password


class UserModelSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserModelSerializer, self).create(validated_data)

    # def get_is_active(self, obj):
    #     is_active = obj.is_active
    #     is_active = 1
    #     return is_active

    def get_is_active(self, obj):
        return getattr(obj, 'is_active', 1)
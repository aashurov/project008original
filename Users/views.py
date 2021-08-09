from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel
from .serializers import UserModelSerializer
from Moneys.pagination import StandardResultsSetPagination
from .users import *
# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all().order_by('-id')
    serializer_class = UserModelSerializer
    pagination_class = StandardResultsSetPagination


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(role='Manager')
    serializer_class = UserModelSerializer


class SeniorViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(role='Senior')
    serializer_class = UserModelSerializer


class MiddleViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(role='Middle')
    serializer_class = UserModelSerializer


class JuniorViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(role='Junior')
    serializer_class = UserModelSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(role='Courier')
    serializer_class = UserModelSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(role='Customer')
    serializer_class = UserModelSerializer
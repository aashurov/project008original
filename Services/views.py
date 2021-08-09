from rest_framework import viewsets
from .serializers import PlanSerializer, ServiceSerializer
from .models import Plan, Service
# Create your views here.


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, ServiceViewSet


router_plans = DefaultRouter()
router_plans.register('plans', PlanViewSet)

router_services = DefaultRouter()
router_services.register('services', ServiceViewSet)

urlpatterns = [
    path('', include(router_plans.urls)),
    path('', include(router_services.urls)),

]
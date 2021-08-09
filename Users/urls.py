from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .users import usersall
#
router_users = DefaultRouter()
router_users.register('users', UsersViewSet)

router_manager = DefaultRouter()
router_manager.register('manager', ManagerViewSet)

router_senior = DefaultRouter()
router_senior.register('senior', SeniorViewSet)

router_middle = DefaultRouter()
router_middle.register('middle', MiddleViewSet)

router_junior = DefaultRouter()
router_junior.register('junior', JuniorViewSet)

router_customer = DefaultRouter()
router_customer.register('customers', CustomerViewSet)

router_courier = DefaultRouter()
router_courier.register('couriers', CourierViewSet)

urlpatterns = [
    path('usersall/', usersall, name='usersall'),
    path('', include(router_users.urls)),
    path('', include(router_manager.urls)),
    path('', include(router_senior.urls)),
    path('', include(router_middle.urls)),
    path('', include(router_junior.urls)),
    path('', include(router_customer.urls)),
    path('', include(router_courier.urls)),

]
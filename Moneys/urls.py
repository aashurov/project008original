from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import customeraccounthistory, customeraccounthistory_detail
from .views import CustomerAccountHistoryViewSet
# CustomerAccountViewSet, CustomerExpensesViewSet, CustomerExpensesHistoryViewSet
from .views import *

# router_customeraccount = DefaultRouter()
# router_customeraccount.register('customeraccount', CustomerAccountViewSet)
#
router_customeraccounthistory = DefaultRouter()
router_customeraccounthistory.register('customeraccounthistoryyy', CustomerAccountHistoryViewSet)
#
# router_customerexpenses = DefaultRouter()
# router_customerexpenses.register('customerexpenses', CustomerExpensesViewSet)
#
# router_customerexpenseshistory = DefaultRouter()
# router_customerexpenseshistory.register('customerexpenseshistory', CustomerExpensesHistoryViewSet)

urlpatterns = [
    # path('', include(router_customeraccount.urls)),
    path('', include(router_customeraccounthistory.urls)),
    # path('', include(router_customerexpenses.urls)),
    # path('', include(router_customerexpenseshistory.urls)),
    path('customeraccounts/', customeraccounts, name='customeraccounts'),
    path('customeraccount/<int:pk>/', customeraccount, name='customeraccount'),
    path('customeraccounthistory/', customeraccounthistory, name='customeraccounthistory'),
    path('customeraccounthistoryy/<int:pk>/', customeraccounthistoryy, name='customeraccounthistoryy'),
    path('customerexpenseshistoryy/<int:pk>/', customerexpenseshistoryy, name='customerexpenseshistoryy'),
    path('customerexpenseshistoryyy/<int:pk>/', customerexpenseshistoryyy, name='customerexpenseshistoryyy'),
    path('customeraccounthistory/<int:pk>/', customeraccounthistory_detail, name='customeraccounthistory_detail'),
    path('customerexpenseshistory/', customerexpenseshistory, name='customerexpenseshistory'),
    path('customerexpenseshistory/<int:pk>', customerexpenseshistory_detail, name='customerexpenseshistory_detail'),
    path('customerexpenses/<int:pk>', customerexpenses, name='customerexpenses'),
    path('customerexpenseslist/', customerexpenseslist, name='customerexpenseslist'),

]